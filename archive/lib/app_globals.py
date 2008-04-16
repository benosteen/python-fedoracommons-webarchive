"""The application's Globals object"""
from pylons import config

from risearch import *
from legacy import *

from cmodel_mapper import cmodel_mapper

from fedoraClient30 import FedoraClient
from archive.lib.solr import *

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application
    """

    def __init__(self):
        """One instance of Globals is created during application
        initialization and is available during requests via the 'g'
        variable
        """
        
        self.root = "http://localhost:5000/"
        
        # Initialise fedora client
        self.f = FedoraClient(server="http://localhost:8080/fedora", username='fedoraAdmin', password='PUTYOURPASSWORDHERE', version="3.0", use_UUID=True)
        # See lib/cmodel_mapper for the purposes of the following data structures
        self.cm = cmodel_mapper()
        self.cm.add_model(u"type:basic", ["DC"], ["REDIF", "MARC21"], ["RELS-EXT", "DC", "EVENT", "DROID"], 'type.basic')
        self.cm.add_model(u'type:article', ["MODS"], ["DC", "MARC21"], ["RELS-EXT", "MODS", "MARC21", "DROID", "EVENT"], 'type.journal_article')
        self.cm.add_model(u'type:thesis', ["MODS"], ["DC", "MARC21"], ["RELS-EXT", "DC", "MARC21", "DROID", "EVENT"], 'type.thesis')
        self.cm.add_model(u'type:conference', ["MODS"], ["DC", "MARC21"], ["RELS-EXT", "DC", "MARC21", "DROID", "EVENT"], 'type.conference')
        self.cm.add_model(u'type:conferenceitem', ["MODS"], ["DC", "MARC21"], ["RELS-EXT", "DC", "MARC21", "DROID", "EVENT"], 'type.conferenceitem')
        self.cm.add_model(u'type:general', ["MODS"], ["DC", "MARC21"], ["RELS-EXT", "DC", "MARC21", "DROID", "EVENT"], 'type.general')
        self.cm.add_model(u'type:working', ["MODS"], ["DC", "MARC21"], ["RELS-EXT", "DC", "MARC21","DROID", "EVENT"], 'type.working_paper')
        self.cm.add_model(u'type:collection',  ["DC"], ["MARC21"], ["RELS-EXT", "DC", "MARC21"], 'type.collection', inline_images="BRANDING", rdf_graph="forward")
        self.cm.add_model(u'type:documentation', ["DC"], [], ["RELS-EXT", "DC", "TEXT", "EVENT"], 'type.documentation', inline_text=["TEXT"])
        self.cm.add_model(u'type:image', ["DC","EXIF"], [], ["RELS-EXT", "DC", "METS", "EVENT"], 'type.image', inline_images=["IMAGE"])
        self.cm.add_model(u'type:imagecollection', ["DC"], [], ["RELS-EXT", "EVENT", "DC", "METS"], 'type.imagecollection', inline_images="THUMBNAIL", ordered_relations=["isPartOf"])
        self.cm.add_model(u'type:book', ["MODS"], ["DC", "MARC21"], ["RELS-EXT", "EVENT", "DC", "METS"], 'type.book', inline_images="IMAGE", ordered_relations=["isPartOf"], rdf_graph="forward")
        self.cm.add_model(u'type:trackback', ["DC"], [], ["RELS-EXT", "EVENT", "DC", "REMOTE_ADDR"], 'type.trackback', search_terms=False)
        self.cm.add_model(u'type:repository', ["DC", "REPOSITORY"], [], ["RELS-EXT", "EVENT", "REPOSITORY", "TEXT", "DC", "REPOSITORY"], 'type.repository', search_terms=False, inline_text=["TEXT"])
        self.cm.add_model(u'type:resource', ["DC"], [], ["RELS-EXT", "TEXT", "EVENT", "DC", "TEXT"], 'type.resource', search_terms=False, inline_text=["TEXT"])
        
        
        # Initialise risearch client
        self.r = self.f.ri
        
        # Solr search
        self.search = SolrConnection(host='localhost:8080', persistent=True)

        m = type_mapping()
        self.types = m.getDictionary()
        
        # Directory for 'temporary' store.
        self.permanent_store = '/tmp/'
        pass
