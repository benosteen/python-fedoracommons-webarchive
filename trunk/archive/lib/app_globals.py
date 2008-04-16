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
        self.cm.add_model(u"type:basic", ["DC"], ["DC", "REDIF", "EVENT", "DROID"], ["RELS-EXT", "DC", "MARC21"], 'type.basic')
        self.cm.add_model(u'type:article', ["MODS"], ["MODS", "DROID", "EVENT"], ["RELS-EXT", "DC", "MARC21"], 'type.journal_article')
        self.cm.add_model(u'type:thesis', ["MODS"], ["MODS", "DROID", "EVENT"], ["RELS-EXT", "DC", "MARC21"], 'type.thesis')
        self.cm.add_model(u'type:conference', ["MODS"], ["MODS", "DROID", "EVENT"], ["RELS-EXT", "DC", "MARC21"], 'type.conference')
        self.cm.add_model(u'type:conferenceitem', ["MODS"], ["MODS", "DROID", "EVENT"], ["RELS-EXT", "DC", "MARC21"], 'type.conferenceitem')
        self.cm.add_model(u'type:general', ["MODS"], ["MODS", "DROID", "EVENT"], ["RELS-EXT", "DC", "MARC21"], 'type.general')
        self.cm.add_model(u'type:working', ["MODS"], ["MODS","DROID", "EVENT"], ["RELS-EXT", "DC", "MARC21"], 'type.working_paper')
        self.cm.add_model(u'type:collection',  ["DC"], ["DC", "DROID", "EVENT"], ["RELS-EXT", "DC", "MARC21"], 'type.collection', inline_images="BRANDING", rdf_graph="forward")
        self.cm.add_model(u'type:documentation', ["DC"], ["DC", "TEXT", "EVENT"], ["RELS-EXT", "DC"], 'type.documentation', inline_text=["TEXT"])
        self.cm.add_model(u'type:image', ["DC","EXIF"], ["DC", "EVENT"], ["RELS-EXT", "DC", "METS"], 'type.image', inline_images=["IMAGE"])
        self.cm.add_model(u'type:imagecollection', ["DC"], ["DC", "EVENT"], ["RELS-EXT", "DC", "METS"], 'type.imagecollection', inline_images="THUMBNAIL", ordered_relations=["isPartOf"])
        self.cm.add_model(u'type:book', ["MODS"], ["MODS", "EVENT"], ["RELS-EXT", "EVENT", "DC", "METS"], 'type.book', inline_images="IMAGE", ordered_relations=["isPartOf"], rdf_graph="forward")
        self.cm.add_model(u'type:trackback', ["DC"], ["DC"], ["RELS-EXT", "EVENT", "DC", "REMOTE_ADDR"], 'type.trackback', search_terms=False)
        self.cm.add_model(u'type:repository', ["DC", "REPOSITORY"], ["DC", "EVENT", "REPOSITORY", "TEXT"], ["RELS-EXT", "DC", "REPOSITORY"], 'type.repository', search_terms=False, inline_text=["TEXT"])
        self.cm.add_model(u'type:resource', ["DC"], ["DC", "TEXT"], ["RELS-EXT", "EVENT", "DC", "TEXT"], 'type.resource', search_terms=False, inline_text=["TEXT"])
        
        
        # Initialise risearch client
        self.r = self.f.ri
        
        # Solr search
        self.search = SolrConnection(host='localhost:8080', persistent=True)

        m = type_mapping()
        self.types = m.getDictionary()
        
        # Directory for 'temporary' store.
        self.permanent_store = '/tmp/'
        pass
