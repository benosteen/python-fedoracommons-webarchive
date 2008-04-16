import rdflib
from rdflib.Graph import ConjunctiveGraph as cg
from rdflib import Namespace, Literal
from rdflib import URIRef

from elementtree import ElementTree as ET

from urllib2 import quote, unquote

from datetime import datetime

RMAP_TYPES = {'xml':'application/rdf+xml','nt':'application/rdf+nt','turtle':'application/rdf+turtle','atom':'application/atom+xml'}

RDF2ATOM={'dcterms:modified':'updated'}

"""
RDF2ATOM={'dcterms:rightsHolder':'',
          'dc:creator':'',
          'dcterms:modified':'updated', 
          'dc:rights':''}
"""

class resource_map():
    """ Example usage:
ore = resource_map('http://archive.sers.ox.ac.uk:5000/objects/')
ore.create_graph('uuid:5aafb3a5-9c5c-4bae-abc9-568f2df81c84', map_params={'dc:creator':'AgentX', 'dcterms:modified':'2008-03-13'})
ore.addAggregate("http://host/file.pdf", literals={'dc:format':'application/pdf'})
ore.addAggregate("http://host/file.bib", literals={'dc:format':'text/x-bibtex'})
ore.toString()
        
<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:dcterms="http://purl.org/dc/terms/"
   xmlns:ore="http://www.openarchives.org/ore/terms/"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
>
  <rdf:Description rdf:about="http://host/file.pdf">
    <dc:format>application/pdf</dc:format>
  </rdf:Description>
  <rdf:Description rdf:about="http://archive.sers.ox.ac.uk:5000/objects/uuid:5aafb3a5-9c5c-4bae-abc9-568f2df81c84/aggregation.xml">
    <ore:describes rdf:resource="http://archive.sers.ox.ac.uk:5000/objects/uuid:5aafb3a5-9c5c-4bae-abc9-568f2df81c84/aggregation"/>
    <dc:creator>AgentX</dc:creator>
    <rdf:type rdf:resource="http://www.openarchives.org/ore/terms/ResourceMap"/>
    <dcterms:created>2008-04-05T06:23:38.001738</dcterms:created>
    <dc:rights>http://creativecommons.org/licenses/by-nc-sa/2.0/uk/</dc:rights>
    <dcterms:modified>2008-03-13</dcterms:modified>
    <dcterms:rightsHolder>The University of Oxford</dcterms:rightsHolder>
  </rdf:Description>
  <rdf:Description rdf:about="http://host/file.bib">
    <dc:format>text/x-bibtex</dc:format>
  </rdf:Description>
  <rdf:Description rdf:about="http://archive.sers.ox.ac.uk:5000/objects/uuid:5aafb3a5-9c5c-4bae-abc9-568f2df81c84/aggregation">
    <ore:aggregates rdf:resource="http://host/file.bib"/>
    <ore:aggregates rdf:resource="http://host/file.pdf"/>
    <rdf:type rdf:resource="http://www.openarchives.org/ore/terms/Aggregation"/>
  </rdf:Description>
</rdf:RDF>

        """
    def __init__(self, url_base):
        self.rdf  = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
        self.ore  = Namespace("http://www.openarchives.org/ore/terms/")
        self.dc  = Namespace("http://purl.org/dc/elements/1.1/")
        self.dcterms  = Namespace("http://purl.org/dc/terms/")
        self.owl  = Namespace("http://www.w3.org/2002/07/owl#")
        self.rdfs = Namespace("http://www.w3.org/2001/01/rdf-schema#")
        # For convience later, when defining URIs for the objects
        self.base =  Namespace(url_base)
        
        self.bindings = { u"rdf": self.rdf, u"rdfs": self.rdfs, u"dc": self.dc, u"dcterms": self.dcterms, u'owl':self.owl, u'ore':self.ore }

    def create_graph(self, id, format="xml", map_params={}):
        """ Call this with the id and the map properties to create the initial graph and atom serialisation. id is such that the URI url_base+id+'/aggregation.*format*' will result in the URI for the map. *format* is rdf,nt or n3 in this case"""
        
        self.id = id
        self.format = format
        if format=="atom":
            # Start the Atom feed
            self.feed = ET.Element('feed')
            self.feed.set('xmlns', 'http://www.w3.org/2005/Atom')
            self.URIR_quoted_id = self.base["%s/aggregation.%s" % (quote(self.id), format)]
            link = ET.SubElement(self.feed, 'link')
            link.set('href',"%s" % self.URIR_quoted_id)
            link.set('rel','self')
            link.set('type','application/atom+xml')
            icon = ET.SubElement(self.feed, 'icon')
            icon.text = "http://www.openarchives.org/ore/logos/ore_icon.png"
        
            category = ET.SubElement(self.feed, 'category')
            category.set('scheme', "http://www.openarchives.org/ore/terms/")
            category.set('term', "http://www.openarchives.org/ore/terms/Aggregation")
            category.set('label', "Aggregation")
        
        # Get the creation date
        time_now = datetime.now().isoformat()
        
        self.URIR = self.base["%s/aggregation.%s" % (self.id, format)]
        
        other_serialiation_types = [x for x in RMAP_TYPES if x != format]
        
        other_URIRs = []
        if format=="atom":
            self.URIA_quoted_id = self.base["%s/aggregation" % (quote(self.id))]
            atom_id = ET.SubElement(self.feed, 'id')
            atom_id.text = "%s" % self.URIA_quoted_id
            for serialisation_type in other_serialiation_types:
                other_URI_quoted_id = self.base["%s/aggregation.%s" % (quote(self.id), serialisation_type)]
                link = ET.SubElement(self.feed, 'link')
                link.set('href',"%s" % other_URI_quoted_id)
                link.set('rel','alternate')
                link.set('type',RMAP_TYPES[serialisation_type])
        else:
            for serialisation_type in other_serialiation_types:
                other_URI = self.base["%s/aggregation.%s" % (self.id, serialisation_type)]
                other_URIRs.append(other_URI)
        
        self.URIA = self.base["%s/aggregation" % (self.id)]
        
        self.g = cg(identifier=self.URIR)
        for prefix in self.bindings:
            self.g.bind(prefix, self.bindings[prefix])
            
        self.g.add((self.URIR, self.rdf['type'], self.ore['ResourceMap']))
        self.g.add((self.URIR, self.ore['describes'], self.URIA))
        
        # Creation date
        self.g.add((self.URIR, self.dcterms['created'], Literal(time_now)))
        
        # Defaults
        default_triples = {}
        default_triples['dcterms:rightsHolder'] = "The University of Oxford"
        default_triples['dc:creator'] = "Python Resource Map Generator"
        default_triples['dcterms:modified'] = time_now
        default_triples['dc:rights'] = 'http://creativecommons.org/licenses/by-nc-sa/2.0/uk/'
        
        if format=='atom':
            for term in default_triples:
                namespace, prop = term.split(':')
                if term in map_params:
                    param_to_add = map_params.pop(term)
                    # Atom X-walk
                    if term in RDF2ATOM:
                        element = ET.SubElement(self.feed, RDF2ATOM[term])
                        element.text = param_to_add
                else:
                    # Atom X-walk
                    if term in RDF2ATOM:
                        element = ET.SubElement(self.feed, RDF2ATOM[term])
                        element.text = default_triples[term]
        else:
            for term in default_triples:
                namespace, prop = term.split(':')
                if term in map_params:
                    param_to_add = map_params.pop(term)
                    self.g.add((self.URIR, self.bindings[namespace][prop], Literal(param_to_add)))
                else:
                    self.g.add((self.URIR, self.bindings[namespace][prop], Literal(default_triples[term])))
        
        # Now add any misc triples (only <URI> <URI> 'Literal' though)
        for term in map_params:
            namespace, prop = term.split(':')
            if namespace in self.bindings:
                self.g.add((self.URIR, self.bindings[namespace][prop], Literal(map_params[term])))

        self.g.add((self.URIA, self.rdf['type'],  self.ore['Aggregation']))
        
        self.g.add((self.URIA, self.ore['isDescribedBy'], self.URIR))
        
        for other_URIR in other_URIRs:
            self.g.add((self.URIA, self.ore['isDescribedBy'], other_URIR))
        
    def addAggregate(self, uri, literals={}, urirefs={}, passed_uri=None):
        """ uri is a uri for the resource. The literals dictionary is simple:
        X.addAggregate(self, a_uri, literals={'dc:format':'application/pdf'})
        -> must be in the form 'namespace:property':'Literal value', and namespace must be in the bindings
        """
        if not self.URIR:
            return "Error - You must create a map first"
            
        self.g.add((self.URIA, self.ore['aggregates'], URIRef(uri)))
        
        if self.format=='atom':
            entry = ET.SubElement(self.feed, 'entry')
            entry_id = ET.SubElement(entry, 'id')
            entry_id.text = "%s" % (passed_uri)
     	    entry_link = ET.SubElement(entry, 'link')
            entry_link.set('href', uri)
            entry_link.set('rel', 'alternate')
            if 'dc:title' in literals:
                entry_title = ET.SubElement(entry, 'title')
                entry_title.text = literals['dc:title']
            if 'dc:format' in literals:
                entry_link.set('type', literals['dc:format'])
            
            if 'dcterms:modified' in literals:
                entry_updated = ET.SubElement(entry, 'updated')
                entry_updated.text = literals['dcterms:modified']
        
            if urirefs.get('rdf:type', None) == self.ore['Aggregation']:
                entry_category = ET.SubElement(entry, 'category')
                entry_category.set('scheme', "http://www.openarchives.org/ore/terms/")
                entry_category.set('term', "http://www.openarchives.org/ore/terms/Aggregation")
                entry_category.set('label', "Aggregation")
        
        for term in literals:
            namespace, prop = term.split(':')
            if namespace in self.bindings:
                self.g.add((URIRef(uri), self.bindings[namespace][prop], Literal(literals[term])))
                
        for term in urirefs:
            namespace, prop = term.split(':')
            if namespace in self.bindings:
                self.g.add((URIRef(uri), self.bindings[namespace][prop], urirefs[term]))
        
    def add_aggregates_from_list(self, ds_list):
        for dsid in ds_list:
            literals = {}
            urirefs = {}
            if ds_list[dsid]['label']:
                literals['dc:title'] = ds_list[dsid]['label']
            if ds_list[dsid]['modified']:
                literals['dcterms:modified'] = ds_list[dsid]['modified']
            literals['dc:format'] = ds_list[dsid]['mimetype']
            if dsid.endswith("DC"):
                urirefs['dcterms:conformsTo'] = URIRef('http://www.openarchives.org/OAI/2.0/oai_dc/')
            
            self.addAggregate(dsid, literals=literals, urirefs=urirefs, passed_uri="info:fedora/%s/%s" % (self.id, ds_list[dsid]['dsid']))
            
    def addMetadata(self, et_tree):
        for element in et_tree.getchildren():
            if element.text:
                dc_field = element.tag.split('}')[-1]
                text = element.text
                
                # RDF graph
                self.g.add((self.URIA, self.bindings['dc'][dc_field], Literal(text)))
                if self.format == "atom":
                    # Atom feed specific things here
                    if dc_field == 'title':
                        title = ET.SubElement(self.feed, 'title')
                        title.text = text
                    elif dc_field == 'creator':
                        author = ET.SubElement(self.feed, 'author')
                        name = ET.SubElement(author, 'name')
                        name.text = text
                
        
    def toString(self, format='xml'):
        if format not in ['xml','turtle','n3','nt']:
            if format == "atom":
                return ET.tostring(self.feed)
            else:
                format='xml'
        return self.g.serialize(format=format)
