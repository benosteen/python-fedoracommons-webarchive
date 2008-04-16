import simplejson
import elementtree.ElementTree as ET

from datetime import datetime

from search_term import term_list

from uuid import uuid4

class Solrjson(object):
    """Takes the 'json' output from a Solr search service and reformats it into an 
       OpenSearch compatible feed without having to alter the Solr service"""
    def __init__(self, response=None):
        self.atom = None
        self.term_list = term_list().get_search_field_dictionary()
        if response:
            self._parse_response(response=response)

    def _parse_response(self, response=None):
        if response:
            self.response = response
        try:
            self.parsed_results = simplejson.loads(self.response)
            self.loaded = True
        except:
            self.loaded = False

    def create_atom(self, **params):
        if self.loaded:
            if self.atom:
                # Atom feed already in cache
                pass
                return True
            else:
                self.atom = Opensearch_atom()
                numFound = self.parsed_results['response'].get('numFound',None)
                search_params = self.parsed_results['responseHeader'].get('params',None)
                
                query = search_params.get('q',None)
                if query:
                    query = query.strip()

                start = search_params.get('start',None)
                if start and isinstance(start,list):
                    start = start[-1]

                rows = search_params.get('rows',None)
                
                self.atom.set_feed_properties(totalResults=numFound, startIndex=start, itemsPerPage=rows, Query=query, **params)
                
                docs = self.parsed_results['response'].get('docs',None)
                
                for doc in docs:
                    entry_params = {}
                    content = ["<table>"]
                    if 'score' in doc:
                        score = doc.pop('score')
                    if 'title' in doc:
                        title_field = doc.pop('title')
                        if isinstance(title_field, list):
                            entry_params['title'] = ";".join(title_field)
                        else:
                            entry_params['title'] = "%s" % title_field
                    if 'fullname' in doc:
                        entry_params['author'] = doc['person_name']
                    if 'timestamp' in doc:
                        entry_params['updated'] = doc.pop('timestamp')
                    if 'id' in doc:
                        if params.get('url_prefix', None):
                            entry_params['link'] = "%s%s" % (params.get('url_prefix', None), doc['id'])
                        else:
                            entry_params['link'] = doc['id']
                    
                    for field in doc:
                        if isinstance(doc[field], list):
                            content.append('<tr><td><span style="font-weight:bold;">%s</span>: %s</td></tr>' % (self.term_list[field]," ; ".join(doc[field])))
                        elif not isinstance(doc[field],str) and not isinstance(doc[field],float) and len(doc[field]) > 300:
                            content.append('<tr><td><span style="font-weight:bold;">%s</span>: %s ... [truncated at 300 characters in length]</td></tr>' % (self.term_list[field],doc[field][:300]))
                        else:
                            content.append('<tr><td><span style="font-weight:bold;">%s</span>: %s</td></tr>' % (self.term_list[field],doc[field]))
                    content.append("</table>")
                    
                    entry_params['content'] = u"\r\n".join(content)
                    entry_params['content_type'] = 'html'
                    entry_params['content_mode'] = 'escaped'
                    self.atom.add_entry(**entry_params)
                
                return True
        else:
            return False

    def get_atom(self):
        if self.atom:
            return self.atom.tostring()
        else:
            return False

class Opensearch_atom(object):
    def __init__(self):
        self.root = ET.Element('feed')
        self.root.set('version', '0.3')
        self.root.set('xml:lang', 'en')
        self.root.set('xmlns', 'http://www.w3.org/2005/Atom')
        self.root.set('xmlns:opensearch', 'http://a9.com/-/spec/opensearch/1.1/')

    def set_feed_properties(self, **params):
        # Basic Search Parameters
        if params.get('title', None):
            title = ET.SubElement(self.root, "title")
            title.set('type','text/html')
            title.set('mode','escaped')
            title.text = "%s" % (params.get('title', None))
        if params.get('link', None):
            link = ET.SubElement(self.root, "link")
            link.set('href', "%s" % (params.get('link', None)))
        if params.get('updated',None):
            updated = ET.SubElement(self.root, "updated")
            updated.text = "%s" % (params.get('updated', None))
        else:
            updated = ET.SubElement(self.root, "updated")
            updated.text = "%sZ" % (datetime.now().isoformat())
        if params.get('author',None):
            author = ET.SubElement(self.root, "author")
            name = ET.SubElement(author, "name")
            name.text = "%s" % (params.get('author', None))
        
        uid = ET.SubElement(self.root, "id")
        uid.text = uuid4().urn

        # Opensearch parameters
        for prop in params:
            if prop in ['totalResults', 'startIndex','itemsPerPage']:
                node = ET.SubElement(self.root, "opensearch:%s" % (prop))
                node.text = "%s" % (params.get(prop, None))
       
        if params.get('Query', None):
            query = ET.SubElement(self.root, "opensearch:Query")
            query.set('searchTerms', "%s" % (params.get('Query', None)))
            if params.get('role', None):
                query.set('role',"%s" % (params.get('role', None)))
            if params.get('startPage', None):
                query.set('startPage',"%s" % (params.get('startPage', None)))

        
    def add_entry(self, **params):
        entry = ET.SubElement(self.root, "entry")
        if params.get('title', None):
            title = ET.SubElement(entry, "title")
            title.set('type','text/html')
            title.set('mode','escaped')
            title.text = "%s" % (params.get('title', None))
        if params.get('link', None):
            link = ET.SubElement(entry, "link")
            link.set('type','text/html')
            link.set('href', "%s" % (params.get('link', None)))
        if params.get('updated',None):
            updated = ET.SubElement(entry, "updated")
            updated.text = "%s" % (params.get('updated', None))
            modified = ET.SubElement(entry, "modified")
            modified.text = "%s" % (params.get('updated', None))
            issued = ET.SubElement(entry, "issued")
            issued.text = "%s" % (params.get('updated', None))
        else:
            time = datetime.now().isoformat()
            updated = ET.SubElement(entry, "updated")
            updated.text = "%sZ" % (time)
            modified = ET.SubElement(entry, "modified")
            modified.text = "%sZ" % (time)
            issued = ET.SubElement(entry, "issued")
            issued.text = "%sZ" % (time)
        if params.get('author',None):
            authors = params.get('author', None)
            if isinstance(authors, list):
                author = ET.SubElement(entry, "author")
                node = ET.SubElement(author, "name")
                node.text = "%s" % (authors[0])
            else:
                author = ET.SubElement(entry, "author")
                node = ET.SubElement(author, "name")
                node.text = "%s" % (authors)
        if params.get('content', None):
            content = ET.SubElement(entry, "content")
            if params.get('content_mode', None):
                content.set('mode',params.get('content_mode', None))
            else:
                content.set('mode','escaped')
            if params.get('content_type', None):
                content.set('type',params.get('content_type', None))
            else:
                content.set('type','text/plain')

            
            content.text = "%s" % (params.get('content', None))
        
        # TODO: replace these with the uuid pids when the time is right
        uid = ET.SubElement(entry, "id")
        uid.text = uuid4().urn
    
    def tostring(self):
        return ET.tostring(self.root)
