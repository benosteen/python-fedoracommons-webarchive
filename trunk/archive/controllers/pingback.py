import logging

from archive.lib.base import *

from archive.lib.rels_ext import Rels_Ext as rels

import xmlrpclib

import httplib
from urllib2 import urlparse, quote, unquote

from archive.lib.linkback_helper import *

log = logging.getLogger('linkback')

SUCCESS = """<?xml version="1.0"?>
<methodResponse>
   <params>
      <param>
         <value><string>%s</string></value>
         </param>
      </params>
   </methodResponse>"""
   
FAIL = """<?xml version="1.0"?>
<methodResponse>
   <fault>
      <value>
         <struct>
            <member>
               <name>faultCode</name>
               <value><int>%s</int></value>
            </member>
         </struct>
      </value>
   </fault>
</methodResponse>"""

class PingbackController(BaseController):

    def index(self):
        if request.environ.get('wsgi.input', None):
            xmlrpc = request.environ['wsgi.input'].read()
            parsed_params, method = xmlrpclib.loads(xmlrpc)
            
            ip_address = request.environ['REMOTE_ADDR']
            log.info('IP address %s attempting pingback' % ip_address)
            
            log.info("Params: %s  - Method: %s" % (parsed_params, method))
            if method == 'pingback.ping' and len(parsed_params)==2:
                url, target_url = parsed_params
                (scheme, netloc, path, query, fragment) = urlparse.urlsplit(url)
                conn = httplib.HTTPConnection(netloc)
                # permalinks only, so only considering host/path
                conn.request("GET", path)
                test_response = conn.getresponse()
                if int(test_response.status) != 200:
                    # Doesn't exist
                    c.xml = FAIL % "16"
                    response.headers['Content-Type'] = 'text/xml'
                    return render('xml')
                    
                htmlheaders = dict(test_response.getheaders())
                # Test to make sure it's a HTML page
                if htmlheaders.get('content-type','').startswith('text/html'):
                    htmlcontent = test_response.read()
                    l = LocationHTMLParser()
                    l.feed(htmlcontent)
                    if target_url in l.get_links():
                        (scheme, netloc, path, query, fragment) = urlparse.urlsplit(unquote(target_url))
                        (root_scheme, root_netloc, discard, discard, discard) = urlparse.urlsplit(g.root)
                        if netloc == root_netloc:
                            parts = path.split('/')
                            if len(parts)>=3 and parts[1]=='objects':
                                pid = parts[2]
                                if g.f.ri.doesPIDExist(pid):
                                    r = rels(FedoraClient=g.f)
                                    r.setDOM('', pid=pid)
                                    if url not in r.listProperty('dcterms','isReferencedBy'):
                                        r.addProperty('dcterms','isReferencedBy', url)
                                        r.store()
                                        log.info("URL %s  linked to object %s" % (url, pid))
                                    else:
                                        # pingback already registered
                                        c.xml = FAIL % "48"
                                        response.headers['Content-Type'] = 'text/xml'
                                        return render('xml')
                                        
                                    c.xml = SUCCESS % "Pingback Success"
                                    response.headers['Content-Type'] = 'text/xml'
                                    return render('xml')
                    else:
                        # url doesn't link back
                        # Doesn't exist
                        c.xml = FAIL % "17"
                        response.headers['Content-Type'] = 'text/xml'
                        return render('xml')
                        
            # Catchall failure
            c.xml = FAIL % "0"
            response.headers['Content-Type'] = 'text/xml'
            return render('xml')
