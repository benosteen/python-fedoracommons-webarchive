# -*- coding: utf-8 -*-
import logging

from archive.lib.base import *

from urllib2 import urlparse, quote, unquote

from archive.lib.search_term import term_list
from archive.lib.solrjson import *

from math import sqrt

import simplejson

from bisect import bisect_left

log = logging.getLogger(__name__)

class BrowseController(BaseController):

    def __before__(self):
        c.field_names = term_list().get_search_field_dictionary()
        browse_fields = [
                'f_creator',
                'f_date',
                'f_format',
                'f_subject',
                'f_type',
                'f_automatic_terms']
        c.browsable = dict([(x,x) for x in browse_fields])
        
        c.rev_browsable = {}
        for key in c.browsable:
            c.rev_browsable[c.browsable[key]] = key
        
        # set some defaults
        self.solr_params = {}
        self.solr_params['q'] = "*:*"
        self.solr_params['wt'] = 'json'
        self.solr_params['fl'] = 'id'
        self.solr_params['rows'] = 1
        self.solr_params['start'] = 0
        self.solr_params['facet'] = 'true'
        self.solr_params['facet.mincount'] = 1

    def index(self):
        # subject, keyphrase, faculty, copyright_date
        
        c.quote = quote
        
        self.solr_params['facet.limit'] = 10
        self.solr_params['facet.field'] = [c.browsable[x] for x in c.browsable]
        
        json_response = g.search.search(**self.solr_params)
        
        if not json_response:
            # FAIL - do something here:
            session['message'] = 'Sorry, the search service is not functional.'
            session.save()
            h.redirect_to(controller='/browse', action='index')
        
        search = simplejson.loads(json_response)
                
        numFound = search['response'].get('numFound',None)
        
        c.numFound = 0
        
        try:
            c.numFound = int(numFound)
        except ValueError:
            pass

        c.returned_facets = {}
        for facet in search['facet_counts']['facet_fields']:       
            facet_list = search['facet_counts']['facet_fields'][facet]
            keys = facet_list[::2]
            values = facet_list[1::2]
            c.returned_facets[facet] = []
            for index in range(len(keys)):
                c.returned_facets[facet].append((keys[index].encode('utf-8'),values[index]))

        return render('browse_root')
        
    def field(self, field=None, item=None, part=None):

        if not field:
            h.redirect_to(controller='/browse', action='index')
        
        c.facet = field.encode('utf-8')
        
        if part:
            # Check to see if it is 'special' (field has '/' in it)
            if field in c.browsable:
                # Try the following as new_field = '/'.join([field, item])
                item = u'/'.join([item, part])

        if not item:
            # List of browsable fields
            view = request.params.get('view', None)

            if field in c.browsable:
                self.solr_params['facet.limit'] = 1000
                self.solr_params['facet.field'] = [c.browsable[field]]
                
                json_response = g.search.search(**self.solr_params)
                
                if not json_response:
                    # FAIL - do something here:
                    session['message'] = 'Sorry, the search service is not functional.'
                    session.save()
                    h.redirect_to(controller='/browse', action='index')
                
                search = simplejson.loads(json_response)
                numFound = search['response'].get('numFound',None)
                c.numFound = 0
                try:
                    c.numFound = int(numFound)
                except ValueError:
                    pass

                c.returned_facets = {}
                for facet in search['facet_counts']['facet_fields']:       
                    facet_list = search['facet_counts']['facet_fields'][facet]
                    keys = facet_list[::2]
                    
                    # Strip leading whitespace
                    stripped_lookup_dict = dict([(x.lstrip().lower(),x) for x in keys])
                    stripped_keys = stripped_lookup_dict.keys()
                    
                    # Alphabetise the keys *in place*
                    stripped_keys.sort()
                    
                    values = facet_list[1::2]
                    
                    # Get the biggest value as the marker
                    top_value = max([float(x) for x in values])
                                        
                    c.returned_facets[facet] = []
                    facet_list = {}
                    for index in range(len(keys)):
                        if view and view=='cloud':
                            facet_list[keys[index]] = int( ((float(values[index]))/top_value)*10.0 )
                        elif view and view=='cloud_small':
                            if float(values[index]) > top_value/6.0:
                                facet_list[keys[index]] = int( ((float(values[index]))/top_value)*10.0 )
                        else:
                            facet_list[keys[index]] = values[index]
                    for key in stripped_keys:
                        if facet_list.get(stripped_lookup_dict[key], None) != None:
                            c.returned_facets[facet].append((stripped_lookup_dict[key].encode('utf-8'), facet_list[stripped_lookup_dict[key]]))
                if view and view in ['cloud', 'cloud_small']:
                    return render('browse_cloud')
                return render('browse_field')
            else:
                session['message'] = 'Sorry, that field is not available for browsing.'
                session.save()
                h.redirect_to(controller='/browse', action='index')
        elif item and field:
            c.item = item.encode('utf-8')
            c.rows = 50
            c.truncate = 100
            if field in c.browsable:
                self.solr_params['q'] = "%s:\"%s\"" % (c.browsable[field], item.encode('utf-8'))
                self.solr_params['wt'] = 'json'
                self.solr_params['fl'] = 'title, person_name, volume, issue, pages, host,copyright_date, thesis_type,id'
                self.solr_params['rows'] = c.rows
                self.solr_params['start'] = 0
                
                start = request.params.get('start', None)
                if start:
                    try:
                        self.solr_params['start'] = int(start)
                        if self.solr_params['start'] < 0:
                            self.solr_params['start'] = 0
                    except ValueError:
                        pass
                        
                c.start = self.solr_params['start']
                
                json_response = g.search.search(**self.solr_params)
                
                if not json_response:
                    # FAIL - do something here:
                    session['message'] = 'Sorry, the search service is not functional.'
                    session.save()
                    h.redirect_to(controller='/browse', action='index')
                if request.params.get('format', None):
                    format = request.params.get('format', None)
                    if format == 'atom':
                        atom_gen = Solrjson(response=json_response)
                        atom_gen.create_atom(title="ORA Search: <em>%s</em>" % self.solr_params['q'], link="http://ora.ouls.ox.ac.uk", author="Oxford University Research Archive", url_prefix="http://archive.sers.ox.ac.uk/objects/display/")
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

                return render('browse_facet')
            else:
                session['message'] = 'Sorry, that field is not available for browsing.'
                session.save()
                h.redirect_to(controller='/browse', action='index')
       
