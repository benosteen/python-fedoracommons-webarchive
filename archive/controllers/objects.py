# -*- coding: utf-8 -*-
import logging

from archive.lib.base import *
from archive.lib.resource_map import resource_map

from archive.lib.download_app import temporaryFileApp
from archive.lib.search_term import term_list

from archive.lib.dc import DC

import simplejson
from bisect import bisect_left

import urllib2
from urllib2 import quote, unquote

import rdflib
from rdflib import Namespace, Literal, URIRef

from elementtree import ElementTree as ET

import os

import mimetypes

from archive.lib.mimeTypes import *

log = logging.getLogger(__name__)

class ObjectsController(BaseController):
    def index(self, id = None, date = None):
        if not id and request.params.get('id',None):
            h.redirect_to(controller='/objects', id=request.params.get('id',None))
            
        if not id:
            h.redirect_to(controller='/search', action='index')

        if not g.f.ri.doesPIDExist(id):
            new_id = g.f.ri.resolveTinyPid(id)
            if new_id:
                h.redirect_to(id=new_id)

        if g.f.ri.doesPIDExist(id) and not date:
            # Set basic variables
            c.resource_map_url = "%sobjects/%s/aggregation.xml" % (g.root, id)
            
            #ReM header
            response.headers['Link'] = "<%s>; rel=resource-map" % c.resource_map_url
            
            # Pingback header
            response.headers['X-Pingback'] = "%spingback" % g.root
            
            c.id = id
            c.title = g.f.ri.getDCTitle(id)
            
            
            # For inline images
            inline_object = request.params.get('inline',None)
            if inline_object and g.f.ri.doesPIDExist(inline_object):
                c.inline_object = inline_object

            # Content model
            c.content_type = g.f.ri.getContentType(id)
            c.model = g.cm.get_model(c.content_type)
            
            # Sort out download list
            c.download_list = []
            c.image_list = []
            c.dsid_list = g.f.listDatastreams(id, format='python')
            for dsid in c.dsid_list:
                # Filter for valid download targets
                if dsid not in c.model['metadata_formats'] and dsid not in c.model['admin_datastreams']:
                    c.download_list.append(c.dsid_list[dsid])
                if dsid in c.model['inline_images']:
                    c.image_list.append(c.dsid_list[dsid])
            
            # Get ordered lists for collections:
            if c.model['ordered_relations']:
                c.relations = {}
                for relationship in c.model['ordered_relations']:
                    if c.model['model_id'] == u"type:book":
                        c.relations[relationship] = g.f.ri.getOrderedRelations(c.id, relationship, numerical=True)
                    else:
                        c.relations[relationship] = g.f.ri.getOrderedRelations(c.id, relationship)
            
            # RDF things
            if c.model['rdf_graph']:
                c.f_ontol, c.b_ontol = term_list().get_fedora_ontology()
                c.fedora_uri = URIRef('info:fedora/%s' % id)
                if c.model['rdf_graph'] == "forward":
                    # Only get the triples that 'pid' is a subject of
                    c.graph = g.f.ri.getTriplesGraph(id)
                else:
                    # Get the triples that 'pid' is a subject OR object of
                    c.graph = g.f.ri.getWalkGraph(id)
                c.rdfs = Namespace("http://www.w3.org/2001/01/rdf-schema#")
                c.rdf  = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
                c.ore  = Namespace("http://www.openarchives.org/ore/terms/")
                c.rel = Namespace("info:fedora/fedora-system:def/relations-external#")
                c.sioc = Namespace(u"http://rdfs.org/sioc/ns#")
                
                c.graph.add((URIRef("info:fedora/%s" % (id)),c.rdfs['isDefinedBy'] ,URIRef(c.resource_map_url)))
                c.graph.add((URIRef(c.resource_map_url), c.rdf['type'], c.ore['resourceMap']))
                
                # Get trackbacks
                if c.model['trackbacks']:
                    # Get all trackbacks
                    c.trackbacks = {}
                    for s,p,o in g.f.ri.getWalkGraph(id).triples((None, c.sioc['reply_of'], c.fedora_uri)):
                        sub_pid = s.split('/')[1]
                        dc = DC(FedoraClient=g.f)
                        dc.setDOM(pid=sub_pid)
                        c.trackbacks[sub_pid] = dc.listFields()

            # Get search terms
            if c.model['search_terms']:
                ns, objid = c.id.split(':')
                solr_params = {'start': 0, 'rows': 1, 'fl': 'title, subtitle, description, abstract, person_name, editor, reviewer, principal_investigator, supervisor, funder, publisher, copyright_holder, institution, faculty, researchGroup, oxfordCollege, funding, website, rightsOwnership, ThirdPartyCopyright, subject, keyphrase, genre, typeofresource, identifier, grantNumber, host, volume, issue, pages, edition, status, review_status, version, peer_reviewed, issue_date, creation_date, modified_date, copyright_date, thesis_type, thesis_level, collection, content_type', 'wt': 'json', 'q':'id:%s\:%s' % (ns, objid)}
                json_response = g.search.search(**solr_params)
                search = simplejson.loads(json_response)
                            
                c.search_terms = search['response'].get('docs',None)[0]
                c.field_list = term_list().get_search_field_dictionary()
                c.all_fields = term_list().get_all_search_fields()
                
            # NOTE Collection browse - special non-general functionality
            if c.model['model_id']=='type:collection':
                start = request.params.get('start', 0)
                
                try:
                    c.start = int(start)
                    if c.start < 0:
                        c.start = 0
                except ValueError:
                    c.start = 0

                c.rows = 10
                solr_params = {'start': start, 'rows': c.rows, 'fl': 'title, subtitle, abstract, person_name, publisher, subject, keyphrase, host, volume, issue, pages, copyright_date, thesis_type, thesis_level, id', 'wt': 'json', 'q':'collection:"%s:%s"' % (ns, objid)}
                json_response = g.search.search(**solr_params)
                collection_search = simplejson.loads(json_response)
                c.docs = collection_search['response'].get('docs',None)
                numFound = collection_search['response'].get('numFound',None)
                
                c.numFound = 0
                c.permissible_offsets = []
                
                c.pages_to_show = 8
                
                try:
                    c.numFound = int(numFound)
                    if numFound > c.rows:
                        full_offsets = [x*c.rows for x in xrange(c.numFound/c.rows+1)]
                        if len(full_offsets)>c.pages_to_show-1:
                            if c.start>0 and c.start<c.numFound:
                                location = bisect_left(full_offsets, c.start)
                                if location<c.pages_to_show-1:
                                    c.permissible_offsets = full_offsets[:c.pages_to_show]
                                elif location+c.pages_to_show>=len(full_offsets)-1:
                                    c.permissible_offsets = [full_offsets[0], '...'] 
                                    c.permissible_offsets.extend(full_offsets[-c.pages_to_show:])
                                else:
                                    c.permissible_offsets = [full_offsets[0], '...']                            
                                    c.permissible_offsets.extend(full_offsets[location-c.pages_to_show/2:location+c.pages_to_show/2])
                            else:
                                c.permissible_offsets = full_offsets[:c.pages_to_show]
                        else:
                            c.permissible_offsets = full_offsets
                except ValueError:
                    pass

                
            # Get XML metadata for page template to use
            c.metadata = {}
            for dsid in c.model['metadata_for_page']:
                raw_metadata_stream = g.f.getDatastream(id, dsid)
                metadata_stream = raw_metadata_stream
                
                if metadata_stream and not (isinstance(metadata_stream, int) or metadata_stream.startswith('no path in db registry for [') or metadata_stream.startswith('[DefaulAccess] No datastream could be returned')):
                    tree_list = ET.fromstring(metadata_stream)
                    c.metadata[dsid] = tree_list

            # Load inline text from datastreams
            c.inline_text = {}
            for dsid in c.model['inline_text']:
                try:
                    text_stream = g.f.getDatastream(id, dsid).decode('utf-8')
                    if not (isinstance(text_stream, int) or text_stream.startswith('no path in db registry for [') or text_stream.startswith('[DefaulAccess] No datastream could be returned')):
                        c.inline_text[dsid] = text_stream
                except:
                    pass
            
            return render(c.model['mako_template'])
#        if date:
#            return "show %s from date %s" % (id, date)
        h.redirect_to(controller='/search', action='index')
        
    def format(self, id = None, format=None, date = None):    
        if not id:
            h.redirect_to(controller='/search', action='index')
        if g.f.ri.doesPIDExist(id):
            c.resource_map_url = "%sobjects/%s/rem" % (g.root, id)
            c.id = id
            c.title = g.f.ri.getDCTitle(id)
            c.content_type = g.f.ri.getContentType(id)
            c.model = g.cm.get_model(c.content_type)
            
            if not date and not format:
                if request.params.get('xml', None):
                    h.redirect_to(controller='/unapi', id=id)
                else:
                    #Assume html list format
                    return render('format_list.mak')
            elif format:
                return "Show %s in format '%s'" % (id, format)
            elif date:
                return "Show format list available for %s  from date %s" % (id, date)
            elif date and format:
                return "Show %s in format '%s' from date %s" % (id, format, date)
            
        
        return "Show format list available for %s" % (id)

    def datastreams(self, id = None, date = None):
        if g.f.ri.doesPIDExist(id):
            # Pingback header
            response.headers['X-Pingback'] = "%spingback" % g.root
            
            c.resource_map_url = "%sobjects/%s/rem" % (g.root, id)
            if request.params.get('xml', None):
                response.headers['Content-Type'] = 'application/xml'
                return g.f.listDatastreams(id)
                
            if date:
                return "Show datastreams for %s from date %s %s" % (id, date, xml_format)
            
            c.pid = id
            c.objectProfile = g.f.getObjectProfile(id, format='python')
            c.datastream_list = g.f.listDatastreams(id, format='python')
            
            return render('datastream_list')
        else:
            abort(404, 'No such object')

    def download(self, id = None, dsid=None, date = None):
        if g.f.ri.doesPIDExist(id):
            if id and dsid:
                # Pingback header
                response.headers['X-Pingback'] = "%spingback" % g.root
                
                datastreams = g.f.listDatastreams(id, format='python')
                
                if dsid in datastreams:
                    mimetype = datastreams[dsid]['mimetype']
                    if date:
                        geturl = g.f.getDatastreamUrl(id, dsid, date=date)
                    else:
                        geturl = g.f.getDatastreamUrl(id, dsid)
                        
                    namespace, id_number = id.split(':')
                
                    winname = datastreams[dsid]['winname']
                    filename = os.path.join('/tmp/', winname)
                    file_handle = open(filename, 'w')
                    file_handle.write(urllib2.urlopen(geturl).read())
                    file_handle.close()
                    
                    response.headers['Content-Type'] = mimetype
                    response.headers['Content-Disposition'] = 'attachment; filename="'+ winname +'"'
                    
                    fapp = temporaryFileApp(filename)
                    return fapp(request.environ, self.start_response)
        
            if date:
                return "Download datastream %s/%s from date %s" % (id, dsid, date)
        else:
            abort(404, 'No such object')

    def relationships(self, id = None, date = None):
        format = request.params.get('format', None)
        if id and g.f.ri.doesPIDExist(id):
            # Pingback header
            response.headers['X-Pingback'] = "%spingback" % g.root
            
            c.resource_map_url = "%sobjects/%s/aggregation.xml" % (g.root, id)
            c.id = id
            c.title = g.f.ri.getDCTitle(id)
            if format == 'htmllite':
                graph = g.f.ri.getTriplesGraph(id)
            else:
                graph = g.f.ri.getWalkGraph(id)
            rdfs = Namespace("http://www.w3.org/2001/01/rdf-schema#")
            rdf  = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
            ore  = Namespace("http://www.openarchives.org/ore/terms/")
            
            graph.add((URIRef("info:fedora/%s" % (id)),rdfs['isDefinedBy'] ,URIRef(c.resource_map_url)))
            graph.add((URIRef(c.resource_map_url), rdf['type'], ore['resourceMap']))
            
            if not format or format=='htmllite':
                # Human readable list
                c.graph = graph
                c.f_ontol, c.b_ontol = term_list().get_fedora_ontology()
                c.fedora_uri = URIRef('info:fedora/%s' % id)
                    
                return render('relationships')
            else:
                if format=='html':
                    c.graph = graph
                    c.f_ontol, c.b_ontol = term_list().get_fedora_ontology()
                    c.fedora_uri = URIRef('info:fedora/%s' % id)
                    
                    return render('full_relationships')
                    
                if format not in ['xml','turtle','n3','nt']:
                    format = 'xml'
                    
                if format == 'xml':
                    response.headers['Content-Type'] = 'application/rdf+xml'
                elif format == 'n3':
                    response.headers['Content-Type'] = 'text/rdf+n3'
                else:
                    response.headers['Content-Type'] = 'text/plain'

                return graph.serialize(format=format)
                
    def resource_map(self, id = None, format=None):
        if g.f.ri.doesPIDExist(id):
            # Set basic variables
            c.resource_map_url = "%sobjects/%s/aggregation.xml" % (g.root, id)
            
            #ReM header
            response.headers['Link'] = "<%s>; rel=resource-map" % c.resource_map_url
            # Pingback header
            response.headers['X-Pingback'] = "%spingback" % g.root
            
            content_type = g.f.ri.getContentType(id)
            model = g.cm.get_model(content_type)
            
            # Allow 'hacking' - .rdf => .xml format
            if format == "rdf":
                h.redirect_to(format='xml')
            
            # Content Negotiation
            if not format:
                if request.headers.get('Accept', None):
                    acceptable_response_types = request.headers['Accept'].split(',')
                    # Check for rdf/xml
                    if 'application/rdf+xml' in acceptable_response_types:
                        redirect_to(format='xml', _code=303)
                    elif 'application/atom+xml' in acceptable_response_types:
                        redirect_to(format='atom', _code=303)
                    elif 'application/rdf+nt' in acceptable_response_types or 'text/rdf+nt' in acceptable_response_types:
                        redirect_to(format='nt', _code=303)
                    elif 'text/rdf+n3' in acceptable_response_types:
                        redirect_to(format='n3', _code=303)
                    elif 'application/rdf+turtle' in acceptable_response_types:
                        redirect_to(format='turtle', _code=303)
                    else:
                        # Assume human agent at this point
                        h.redirect_to(controller='/objects', action="index", id=id)   
                else:
                    # No "Accept:" header - assume to be automated agent - rdf/xml a good default though?
                    h.redirect_to(format='xml', _code=303)
            elif format in ['xml', 'nt', 'turtle','n3', 'atom']:
                rmap = resource_map("%sobjects/" % (g.root))
                mod_date = g.f.ri.getLastModifiedDate(id)
                rmap.create_graph("%s" % (id), format=format, map_params={'dc:creator':'Oxford University Research Archive ReM generator', 'dcterms:modified':mod_date})
                
                dc = g.f.getDatastream(id,'DC')
                dc_tree = ET.fromstring(dc)
                
                # Add metadata to aggregation
                rmap.addMetadata(dc_tree)
                
                ds_list = g.f.listDatastreams(id, format='python')
                date_mod_dict = g.f.ri.getDSIDModifiedDates(id)
                for dsid in date_mod_dict:
                    if dsid in ds_list:
                        ds_list[dsid]['modified'] = date_mod_dict[dsid]

                url_dsid_list = dict([("%sobjects/%s/datastreams/%s" % (g.root, quote(id), dsid), ds_list[dsid]) for dsid in ds_list])
                
                rmap.add_aggregates_from_list(url_dsid_list)
                
                if len(model['metadata_for_page']) == 1:
                    # Assume other metadata's are crosswalked versions
                    for dsid in model['metadata_formats']:
                        if dsid in ds_list:
                            rmap.g.add((URIRef("%sobjects/%s/datastreams/%s" % (g.root, quote(id), model['metadata_for_page'][0])), rmap.dcterms['hasFormat'] , URIRef("%sobjects/%s/datastreams/%s" % (g.root, quote(id), dsid)) ))
                
                relationships = g.f.ri.getWalkGraph(id)
                ore  = Namespace("http://www.openarchives.org/ore/terms/")
                rel = Namespace("info:fedora/fedora-system:def/relations-external#")
                # Add 'isPartOf' aggregate maps :)
                
                surrogate_parts = {}
                for s,p,o in relationships.triples((None, rel['isPartOf'], URIRef('info:fedora/%s' % id))):
                    pid_is_part_of = s.split('/')[-1]
                    literals = {}
                    urirefs = {}
                    literals['dc:title'] = g.f.ri.getDCTitle(pid_is_part_of).decode('UTF-8')
                    urirefs['rdf:type'] = ore['Aggregation']
                    rmap.addAggregate("%sobjects/%s/aggregation" % (g.root, pid_is_part_of), literals=literals, urirefs=urirefs, passed_uri="info:fedora/%s" % pid_is_part_of)
                
                # Add generated 'datastreams'
                rmap.addAggregate("%sobjects/%s/relationships?format=xml" % (g.root, id), literals={'dc:title':'RDF graph of the triples that this object is either the subject or object of', 'dc:format':'application/rdf+xml','dcterms:modified':mod_date}, passed_uri="info:fedora/%s/gen_relationships" % id)
                
                if format == 'xml':
                    response.headers['Content-Type'] = 'application/rdf+xml'
                    response.headers['Content-Disposition'] = 'inline; filename="%s_resource_map.rdf.xml"' % "_".join(id.split(':'))
                elif format == 'nt':
                    response.headers['Content-Type'] = 'application/rdf+nt'
                    response.headers['Content-Disposition'] = 'inline; filename="%s_resource_map.nt.txt"' % "_".join(id.split(':'))
                elif format == 'atom':
                    response.headers['Content-Type'] = 'application/atom+xml'
                    response.headers['Content-Disposition'] = 'inline; filename="%s_resource_map.xml"' % "_".join(id.split(':'))
                elif format == 'n3':
                    response.headers['Content-Type'] = 'text/rdf+n3'
                    response.headers['Content-Disposition'] = 'inline; filename="%s_resource_map.n3.txt"' % "_".join(id.split(':'))
                elif format == 'turtle':
                    response.headers['Content-Type'] = 'application/rdf+turtle'
                    response.headers['Content-Disposition'] = 'inline; filename="%s_resource_map.turtle.txt"' % "_".join(id.split(':'))
                else:
                    response.headers['Content-Type'] = 'text/plain'
                    
                return rmap.toString(format=format)
            else:
                abort(404, 'No such object')

    def redirect(self, id=None):
        # Legacy support
        pid = request.params.get('pid', None) or id
        if not pid:
            h.redirect_to(controller='/search', action='index')
        
        guessed_pid = g.f.resolve_Non_UUID_pid(pid) or pid

        if guessed_pid and g.f.ri.doesPIDExist(pid):
            session['message'] = 'Please update your bookmark to <a href="%s">this page</a>, as it is using the older form of link' % (h.url_for(controller='/objects', id=guessed_pid))
            session.save()
            h.redirect_to(controller='/objects', id=guessed_pid)
        else:
            abort(404, 'No such object')
        
    def handle(self, id):
        # Legacy support
        session.save()
        handle_pid = id
        if not handle_pid.startswith('uuid') or not handle_pid.startswith('uuid'):
            # True legacy handle
            pid = "ora:%s" % handle_pid
        else:
            pid = ":".join(handle_pid.split('_'))
            
        if not pid:
            h.redirect_to(controller='/search', action='index')
        
        guessed_pid = g.f.resolve_Non_UUID_pid(pid)
        if guessed_pid:
            h.redirect_to(controller='/objects', id=guessed_pid)
        else:
            abort(404, 'No such object')
        
