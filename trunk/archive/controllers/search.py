# -*- coding: utf-8 -*-
import logging

from archive.lib.base import *

from archive.lib.solrjson import *

from archive.lib.search_term import term_list

import simplejson

from bisect import bisect_left

log = logging.getLogger(__name__)

class SearchController(BaseController):

    def __before__(self):
        c.all_fields = term_list().get_all_search_fields()

        c.field_names = term_list().get_search_field_dictionary()
        c.facetable_fields = ['f_date','f_creator', 'f_format', 'f_subject', 'f_type', 'f_automatic_terms']
        c.views = {'Default':['id', 'title', 'creator', 'date', 'subject', 'type'],'Verbose':['id', 'title', 'contributor', 'coverage', 'creator', 'date', 'description', 'format', 'identifier', 'language', 'publisher', 'relation', 'rights', 'source', 'subject', 'type','automatic_terms']}
        c.sort_options = {'score desc':'Relevance',  'date desc':'Date (Latest to oldest)','date asc':'Date (Oldest to Latest)'}

    def index(self):
        c.truncate = 450
        c.rows = 5
        # Hide the basic search
        c.hide_basic_search = True
        return render('search_form')
        

    def opensearch(self):
        response.headers['Content-Type'] = 'application/xml'
        return render('opensearch')
        
    def _basic_search(self, query):
        start = request.params.get('start', None)
        format = request.params.get('format', None)
        
        if start:
            try:
                c.start = int(start)
                if c.start < 0:
                    c.start = 0
            except ValueError:
                pass
                
    
        c.q = query
        
        c.truncate = 450
        c.rows = 5
        c.start = 0
        
        if start:
            try:
                c.start = int(start)
                if c.start < 0:
                    c.start = 0
            except ValueError:
                pass

        
        if not c.q:
            h.redirect_to(controller='/search', action='index')
            
        c.view = "Default"
        c.chosen_fields = ['id','score']
        
        c.search = {}
        
        c.search['q'] = c.q
        
        for field in c.views[c.view]:
            c.chosen_fields.append(field)
        
        c.search['rows'] = c.rows
        c.search['truncate'] = c.truncate
        c.search['start'] = c.start
        
        solr_params = {}
        
        solr_params['q'] = c.q
        solr_params['wt'] = 'json'
        solr_params['fl'] = ','.join(c.chosen_fields)
        solr_params['rows'] = c.rows
        solr_params['start'] = c.start
        
        json_response = g.search.search(**solr_params)
        
        if not json_response:
            # FAIL - do something here:
            c.message = 'Sorry, either that search "%s" resulted in no matches, or the search service is not functional.' % c.q
            h.redirect_to(controller='/search', action='index')

        
        if request.params.get('format', None):
            if format == 'atom':
                atom_gen = Solrjson(response=json_response)
                atom_gen.create_atom(title="ORA Search: <em>%s</em>" % c.q, link="http://ora.ouls.ox.ac.uk", author="Oxford University Research Archive", url_prefix="http://archive.sers.ox.ac.uk/objects/")
                response.headers['Content-Type'] = 'application/atom+xml'
                c.atom = atom_gen.get_atom()
                return render('atom_results')

        
        search = simplejson.loads(json_response)
                
        numFound = search['response'].get('numFound',None)
        
        c.numFound = 0
        c.permissible_offsets = []
        
        c.pages_to_show = 6
        
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

        c.docs = search['response'].get('docs',None)
        
        return render('basic_search_form')
        
        
    def redirect(self):
        # Legacy support
        session['message'] = 'Please update your bookmark to <a href="%s">this page</a>, as it is using the older form of the search link' % (h.url_for(controller='/search', action='basic', q=request.params.get('q0', None)))
        session.save()
        h.redirect_to(controller='/search', action='basic', q=request.params.get('q0', None))
    
    def person(self, id):
        c.q = request.params.get('q', id)
        
        if c.q:
            c.q = "creator:%s" % c.q
            
        return self._basic_search(c.q)

    def title(self, id):        
        c.q = request.params.get('q', id)
        
        if c.q:
            c.q = "title:%s" % c.q
            
        return self._basic_search(c.q)
        
    def faculty(self, id):        
        c.q = request.params.get('q', id)
        
        if c.q:
            c.q = "faculty:%s" % c.q
            
        return self._basic_search(c.q)

    def collection(self, id):        
        c.q = request.params.get('q', id)
        
        if c.q:
            c.q = "collection:%s" % c.q
            
        return self._basic_search(c.q)
        
    def date(self, id):        
        c.q = request.params.get('q', id)
        
        if c.q:
            c.q = "copyright_date:%s" % c.q
            
        return self._basic_search(c.q)
        
    def subject(self, id):        
        c.q = request.params.get('q', id)
        
        if c.q:
            c.q = "subject:%s" % c.q
            
        return self._basic_search(c.q)

    
    def basic(self, q=None):
        if not q:
            q = request.params.get('q', None)
        
        return self._basic_search(q)
        
    def detailed(self):
        
        c.q = request.params.get('q', None)
        
        if not c.q:
            h.redirect_to(controller='/search', action='index')
        
        # Search controls
        truncate = request.params.get('truncate', None)
        start = request.params.get('start', None)
        rows = request.params.get('rows', None)
        sort = request.params.get('sort', None)
        
        c.fulltext = False
        if request.params.get('fulltext', None):
            c.fulltext = "true"
        
        c.view = request.params.get('view', 'Default')
        
        c.sort = 'score desc'
        
        # Lock down the sort parameter.
        if sort and sort in c.sort_options:
            c.sort = sort
        
        c.sort_text = c.sort_options[c.sort]
        
        if c.view not in c.views:
            c.view = 'Default'
        
        c.chosen_fields = ['id','score', 'timestamp']
        c.fields_to_facet = []
        c.facet_limit = 10
        c.chosen_facets = {}
        
        query_filter = ""
        
        #Setup to capture all the url parameters needed to regenerate this search
        c.search = {}
        
        for field in c.all_fields:
            if request.params.get(field, None):
                c.chosen_fields.append(field)
                c.search[field] = 'true'
            if request.params.get("facet"+field, None) and field in c.facetable_fields:
                c.fields_to_facet.append(field)
                c.search["facet"+field] = 'true'
            if request.params.get("filter"+field, None):
                c.chosen_facets[field] = request.params.get("filter"+field, None)
                c.search["filter"+field] = request.params.get("filter"+field, None)
                query_filter += " AND %s:\"%s\"" % (field, c.chosen_facets[field])
        
        
        
        for field in c.views[c.view]:
            if field not in c.chosen_fields:
                c.chosen_fields.append(field)

        c.truncate = 450
        c.start = 0
        c.rows = 5
        
        # Parse/Validate search controls
        if truncate:
            try:
                c.truncate = int(truncate)
                if c.truncate < 10:
                    c.truncate = 10
                if c.truncate > 1000:
                    c.truncate = 1000
            except ValueError:
                pass
                
        if start:
            try:
                c.start = int(start)
                if c.start < 0:
                    c.start = 0
            except ValueError:
                pass

        if rows:
            try:
                c.rows = int(rows)
                if c.rows < 5:
                    c.rows = 5
            except ValueError:
                pass
        
        
            
        c.search['rows'] = c.rows
        c.search['truncate'] = c.truncate
        c.search['start'] = c.start
        c.search['sort'] = c.sort
        c.search['q'] = c.q
        c.search['view'] = c.view
        if c.fulltext:
            c.search['fulltext'] = c.fulltext
        
        search_params_for_url = []
        for search_url_param in c.search:
            search_params_for_url.append("%s=%s" % (search_url_param, c.search[search_url_param]))

        search_params_for_url.append('filter%s=%s')

        c.add_facet = "%ssearch/detailed?%s" % (g.root, "&amp;".join(search_params_for_url))
        
        solr_params = {}
        
        if c.fulltext:
            solr_params['q'] = "( %s OR full_text:%s ) %s" % (c.q, c.q, query_filter)
        else:
            solr_params['q'] = c.q+query_filter
        solr_params['wt'] = 'json'
        solr_params['fl'] = ','.join(c.chosen_fields)
        solr_params['rows'] = c.rows
        solr_params['start'] = c.start
        if c.sort:
            solr_params['sort'] = c.sort
                
        if c.fields_to_facet:
            solr_params['facet'] = 'true'
            solr_params['facet.limit'] = c.facet_limit
            solr_params['facet.mincount'] = 1
            solr_params['facet.field'] = []
            for facet in c.fields_to_facet:
                solr_params['facet.field'].append(facet)
        
        json_response = g.search.search(**solr_params)
        
        if not json_response:
            # FAIL - do something here:
            c.message = 'Sorry, either that search "%s" resulted in no matches, or the search service is not functional.' % c.q
            h.redirect_to(controller='/search', action='index')
        
        
        if request.params.get('format', None):
            format = request.params.get('format', None)
            if format == 'atom':
                atom_gen = Solrjson(response=json_response)
                atom_gen.create_atom(title="ORA Search: <em>%s</em>" % c.q, link="http://ora.ouls.ox.ac.uk", author="Oxford University Research Archive", url_prefix="http://archive.sers.ox.ac.uk/objects/")
                response.headers['Content-Type'] = 'application/atom+xml'
                c.atom = atom_gen.get_atom()
                return render('atom_results')
                
                
        search = simplejson.loads(json_response)
                
        numFound = search['response'].get('numFound',None)
        
        c.numFound = 0
        c.permissible_offsets = []
        
        c.pages_to_show = 6
        
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

        c.docs = search['response'].get('docs',None)
        
        # Hide the basic search
        c.hide_basic_search = True
        
        if c.fields_to_facet:
            c.returned_facets = {}
            for facet in search['facet_counts']['facet_fields']:       
                facet_list = search['facet_counts']['facet_fields'][facet]
                keys = facet_list[::2]
                values = facet_list[1::2]
                c.returned_facets[facet] = []
                for index in range(len(keys)):
                    c.returned_facets[facet].append((keys[index].encode('utf-8'),values[index]))
        return render('search_form')

