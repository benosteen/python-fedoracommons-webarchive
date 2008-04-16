import rdflib
from rdflib.Graph import ConjunctiveGraph as cg
from rdflib import Namespace, Literal
from rdflib import URIRef

class term_list():
    def get_all_search_fields(self):
        return ['id', 'title', 'contributor', 'coverage', 'creator', 'date', 'description', 'format', 'identifier', 'language', 'publisher', 'relation', 'rights', 'source', 'subject', 'type','automatic_terms', 'f_date','f_creator', 'f_format','f_subject','f_type','f_automatic_terms']

    def get_search_field_dictionary(self):
        field_names = {
                'id':'Fedora id',
                'contributor':'Contributor',
                'coverage':'Coverage',
                'creator':'Creator',
                'date':'Date',
                'description':'Description',
                'format':'Format',
                'identifier':'Identifier',
                'language':'Language',
                'publisher':'Publisher',
                'relation':'Relation',
                'rights':'Rights',
                'source':'Source',
                'subject':'Subject',
                'title':'Title',
                'type':'Type',
                'f_contributor':'Contributer',
                'f_coverage':'Coverage',
                'f_creator':'Creator',
                'f_date':'Date',
                'f_description':'Description',
                'f_format':'Format',
                'f_identifier':'Identifier',
                'f_language':'Language',
                'f_publisher':'Publisher',
                'f_relation':'Relation',
                'f_rights':'Rights',
                'f_source':'Source',
                'f_subject':'Subject',
                'f_title':'Title',
                'f_type':'Type',
                'f_automatic_terms':'Automatically derived terms',
                'f_date':'Date'}
        return field_names
        
    def get_fedora_ontology(self):
        rel = Namespace("info:fedora/fedora-system:def/relations-external#")
        view = Namespace("info:fedora/fedora-system:def/view#")
        rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
        sioc = Namespace(u"http://rdfs.org/sioc/ns#")
        dct = Namespace(u"http://purl.org/dc/terms/")
        
        forward_ontology = {'Member of collection %s':rel['isMemberOfCollection'],
                    'Part of item %s':rel['isPartOf'],
                    'Annotation of item %s':rel['isAnnotationOf'],
                    'Modified on %s':view['lastModifiedDate'],
                    'Related item %s':rdfs['seeAlso'],
                    "Trackback of %s":sioc['reply_of'],
                    'Linked/Cited by: %s':dct['isReferencedBy'],
                    'Has a resource map %s':rdfs['isDefinedBy']
                    }
        back_ontology = {'has %s as a member of its collection':rel['isMemberOfCollection'],
                    'has %s as part of itself':rel['isPartOf'],
                    'Trackback: %s':sioc['reply_of'],
                    'has %s as an annotation of itself':rel['isAnnotationOf']
                    }
        return (forward_ontology, back_ontology)
