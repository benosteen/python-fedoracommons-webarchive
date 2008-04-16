# -*- coding: utf-8 -*-
import logging

from archive.lib.base import *
from archive.lib.rels_ext import Rels_Ext as rels
from archive.lib.dc import DC

from archive.lib.linkback_helper import *

import httplib
from urllib2 import urlparse, quote

log = logging.getLogger('linkback')

FAIL = """<?xml version="1.0" encoding="utf-8"?>
    <response>
        <error>1</error>
        <message>%s</message>
    </response>"""
    
SUCCESS = """<?xml version="1.0" encoding="utf-8"?>
    <response>
        <error>0</error>
    </response>"""

class TrackbackController(BaseController):

    def index(self, id=None):
        if not id:
            abort(404)
        
        ip_address = request.environ['REMOTE_ADDR']
        log.info('IP address %s attempting trackback' % ip_address)
#  In two minds on whether or not I should 'turn this on'
#  There are blogs hosted by the same server from which
#  the trackbacks are issued.

        if session.get('trackbacked', None):
            for ip, tracked_pid in session['trackbacked']:
                if ip == ip_address and tracked_pid == id:
                    c.xml = FAIL % "Trackback Failed"
                    response.headers['Content-Type'] = 'application/xml'
                    return render('xml')

            session['trackbacked'].append((ip_address, id))
        else:
            session['trackbacked'] = [(ip_address, id)]
            session.save()
        
        url = request.params.get('url', None)
        
        if not url:
            log.info('Trackback Failed: No url included in trackback - %s' % ip_address)
            c.xml = FAIL % "Trackback Failed: No url included in trackback"
            response.headers['Content-Type'] = 'application/xml'
            return render('xml')
        
        # Test URL
        (scheme, netloc, path, query, fragment) = urlparse.urlsplit(url)
        conn = httplib.HTTPConnection(netloc)
        # permalinks only, so only considering host/path
        conn.request("GET", path)
        test_response = conn.getresponse()
        if int(test_response.status) != 200:
            log.info("Trackback Failed: URL doesn't resolve - %s %s" % (url, ip_address))
            c.xml = FAIL % "Trackback Failed: URL doesn't resolve"
            response.headers['Content-Type'] = 'application/xml'
            return render('xml')
            
        contains_link = False
        
        htmlheaders = dict(test_response.getheaders())
        # Test to make sure it's a HTML page
        if htmlheaders.get('content-type','').startswith('text/html'):
            htmlcontent = test_response.read()
            l = LocationHTMLParser()
            l.feed(htmlcontent)
            
            target_url = "%sobjects/%s" % (g.root, id)
            (discard, targ_host, targ_path, discard, discard) = urlparse.urlsplit(target_url)
            
            quoted_target_url = quote("%sobjects/%s" % (g.root, id))
            (discard, discard, quoted_path, discard, discard) = urlparse.urlsplit(quoted_target_url)
            
            for test_url in l.get_links():
                (discard, host, path, discard, discard) = urlparse.urlsplit(test_url)
                if host == targ_host and (path.startswith(targ_path) or path.startswith(quoted_path)):
                    log.info("URL %s contains link for %s" % (url, id))
                    contains_link = True
        else:
            log.info("Trackback Failed: URL doesn't link to a HTML page - %s" % (id))
            c.xml = FAIL % "Trackback Failed: URL doesn't contain a link to a page of type text/html"
            response.headers['Content-Type'] = 'application/xml'
            return render('xml')
            

        if not contains_link:
            log.info("Trackback Failed: URL doesn't contain a link to the requested item - %s" % (id))
            c.xml = FAIL % "Trackback Failed: URL doesn't contain a link to the requested item"
            response.headers['Content-Type'] = 'application/xml'
            return render('xml')
        
        
        query = "select $url from <#ri> where $object <http://rdfs.org/sioc/ns#reply_of> <info:fedora/%s> and $object <dc:relation> $url" % (id)
        does_trackback_exist = g.f.ri.getTuples(query, format="csv").split('\n')
        
        if url in does_trackback_exist:
            # ie there is a hit
            log.info("Trackback Failed: Trackback has already been added - %s %s" % (url, ip_address))
            c.xml = FAIL % "Trackback Failed: Trackback has already been added"
            response.headers['Content-Type'] = 'application/xml'
            return render('xml')
        
        title = request.params.get('title', None)
        if not title:
            log.info("Trackback Failed: No title included - %s %s" % (url, ip_address))
            c.xml = FAIL % "Trackback Failed: No title included; This is a mandatory field for this site"
            response.headers['Content-Type'] = 'application/xml'
            return render('xml')
        
        excerpt = request.params.get('excerpt', None)
        blog_name = request.params.get('blog_name', None)
        
        if g.f.ri.doesPIDExist(id):
            pids = g.f.create_UUID_Object(label=title)
            log.info("Trackback object spawned - %s" % pids['pid'])
        
            dc = DC(FedoraClient=g.f)
            dc.setDOM(pid=pids['pid'])
            if excerpt:
                dc.addField('abstract', excerpt)
            if blog_name:
                dc.addField('creator', blog_name)
            
            dc.addField('relation', url)
            
            dc.store()
            
            log.info("Trackback DC stored - %s" % pids['pid'])
            
            rdf_ds = rels(FedoraClient=g.f)
            rdf_ds.setPID(pid=pids['pid'])
            rdf_ds.addProperty('rel', u'isMemberOf', 'type:trackback')
            rdf_ds.addProperty('sioc', u'reply_of', id)
            rdf_ds.store()
            
            log.info("Trackback RDF stored - %s" % pids['pid'])
            
            g.f.putString(pids['pid'], 'REMOTE_ADDR', ip_address, fake_filename="ip_address.txt")
            
            log.info("Trackback stored - %s" % pids['pid'])
            
            c.xml = SUCCESS
            response.headers['Content-Type'] = 'application/xml'
            return render('xml')
        
        abort(404)
