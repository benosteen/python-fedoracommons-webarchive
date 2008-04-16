#PoC code to index items in Solr from Fedora repository
from fedoraClient30 import FedoraClient
from filter import Filter
from solr import SolrException, SolrConnection

from urllib2 import urlparse, quote, unquote

from elementtree import ElementTree as ET

from term_extraction import Term_extraction

FEDORA_DEFAULT_URL='http://localhost:8080/fedora'
FEDORA_VERSION="3.0"
SOLR_DEFAULT_URL='localhost:8080'
SOLR_BASE = '/solr'

# Log facility
import logging
import logging.config

logging.config.fileConfig("logging.conf")

#create logger
logger = logging.getLogger("solr")

# NOTE: Uncomment the next import line to let the BasicSolrFeeder use XSLT transforms
# Commented out by default, as this constitutes a further dependancy that
# may not be required.

#from Ft.Xml.Xslt import Transform

from xml.dom import minidom, Node

class DCSolrFeeder(object):
    def __init__(self, fedora_url=None, fedora_version=None, solr_url=None, solr_base=SOLR_BASE, solr_username=None, solr_password=None):
        if not fedora_url:
            # Use some defaults if None are passed:
            self.fedoraClient = FedoraClient(FEDORA_DEFAULT_URL, version=FEDORA_VERSION)
        else:
            self.fedoraClient = FedoraClient(fedora_url, version=fedora_version)
        
        if not solr_url:
            self.solr = SolrConnection(host=SOLR_DEFAULT_URL, solrBase=solr_base, username=solr_username, password=solr_password, persistent=True)
        else:
            self.solr = SolrConnection(host=solr_url, solrBase=solr_base, username=solr_username, password=solr_password, persistent=True)
            
        self.filter_tool = Filter()
        
        # Use Yahoo's term extractor
        self.t = Term_extraction()
    
    def commit(self):
        self.solr.commit()
    def add_pid(self, pid, commit=True, debug=False):
        # Testing if fedoraClient and solr exist as objects (in lieu of a better fast test):
        if self.fedoraClient and self.solr:
            dc_text = self.fedoraClient.getDatastream(pid, 'DC')
            
            dc_tree = ET.fromstring(dc_text)
            dc_fields = []
            full_text = []
            for element in dc_tree.getchildren():
                elementtext = element.text
                            
                elementtext = elementtext.replace("&", "&amp;")
                elementtext = elementtext.replace("<", "&lt;")
                elementtext = elementtext.replace("]]>", "]]&gt;")
                
                dc_fields.append(u'<field name="%s">%s</field>' % (element.tag.split('}')[-1], elementtext))
                full_text.append(element.text)

            #Term Extraction
            auto_term_list = []
            termlist = self.t.get_term_list(u"\n".join(full_text))
            for gen_term in termlist:
                auto_term_list.append(u'<field name="automatic_terms">%s</field>' % (gen_term))     

            if dc_fields:
                logger.info("Attempting to add pid: %s to Solr" % (pid))
                
                text_to_add = [u'<add><doc>']
                text_to_add.append(u'<field name="id">%s</field>' % (pid))
                if dc_fields: text_to_add.append(u"".join(dc_fields))
                if auto_term_list: text_to_add.append(u"".join(auto_term_list))
                text_to_add.append(u'</doc></add>')
                
                if debug:
                    logger.debug(u"".join(text_to_add).encode('UTF-8'))
                
                self.solr.doUpdateXML(u"".join(text_to_add).encode('UTF-8'))
                
            else:
                logger.error("FAIL: %s - Error getting object and/or datastreams from Fedora" % (pid))
                return False

            if commit: 
                self.solr.commit()
                
            return True
        else:
            logger.error("FAIL: self.fedoraClient = None or self.solr = None in the add_pid function")
            return False

class BasicSolrFeeder(object):
    def __init__(self, fedora_url=None, fedora_version=None, solr_url=None, solr_base=SOLR_BASE, solr_username=None, solr_password=None):
        if not fedora_url:
            # Use some defaults if None are passed:
            self.fedoraClient = FedoraClient(FEDORA_DEFAULT_URL, version=FEDORA_VERSION)
        else:
            self.fedoraClient = FedoraClient(fedora_url, version=fedora_version)
        
        if not solr_url:
            self.solr = SolrConnection(host=SOLR_DEFAULT_URL, solrBase=solr_base, username=solr_username, password=solr_password, persistent=True)
        else:
            self.solr = SolrConnection(host=solr_url, solrBase=solr_base, username=solr_username, password=solr_password, persistent=True)
            
        self.filter_tool = Filter()
        
        # Use Yahoo's term extractor
        self.t = Term_extraction()
    
    def commit(self):
        self.solr.commit()

    def add_pid(self, pid, commit=True, debug=False):
        # Testing if fedoraClient and solr exist as objects (in lieu of a better fast test):
        if self.fedoraClient and self.solr:
            
            # TODO pid regex assertion
            
            
            # Not needed as the content type is now encoded in the RELS-EXT
            # Get content_type
            #logger.info("Attempting to discover content_type")
            #content_type = self.fedoraClient.getContentModel(pid)
            
            #logger.info(content_type)
            
            # Getting Metadata: (Mods or DC if no Mods)
            logger.info("Attempting to get MODS from pid: %s" % (pid))
            mods_text = self.fedoraClient.getDatastream(pid, 'MODS')
        
            solr_text = False
            if not (isinstance(mods_text, int) or mods_text.startswith('no path in db registry for [') or mods_text.startswith('[DefaulAccess] No datastream could be returned')):
                logger.info("Transforming MODS to Solr fields")
                solr_text = Transform(mods_text, 'xsl/mods2solr.xsl', params={'pid':pid}).decode('UTF-8')
            else:
                # Fall back on DC
                logger.info("Attempting to get DC from pid: %s as MODS was not downloadable or not present" % (pid))
                dc_text = self.fedoraClient.getDatastream(pid, 'DC')
                
                if debug:
                    logger.debug(dc_text)
                    
                if not (isinstance(dc_text, int) or dc_text.startswith('no path in db registry for [') or dc_text.startswith('[DefaulAccess] No datastream could be returned')):
                    logger.info("Transforming DC to Solr fields")
                    solr_text = Transform(dc_text, 'xsl/dc2solr.xsl', params={'pid':pid}).decode('UTF-8')
                
                if debug:
                    logger.debug(solr_text)

            # TODO: Get the RELS-EXT information out
            logger.info("Attempting to get RELS-EXT from pid: %s" % (pid))
            rels_text = self.fedoraClient.getDatastream(pid, 'RELS-EXT')
            
            collections_text = False
            if not (isinstance(rels_text, int) or rels_text.startswith('no path in db registry for [') or rels_text.startswith('[DefaulAccess] No datastream could be returned')):
                logger.info("Transforming RELS-EXT to Solr fields collection and content_type")
                collections_text = Transform(rels_text, 'xsl/relsext2solr.xsl', params={'pid':pid}).decode('UTF-8')

            # Get Full-text datastream, if possible
            logger.info("Getting text extraction datastream for pid: %s" % (pid))
            full_text = self.fedoraClient.getDatastream(pid, 'FULLTEXT')

            full_text_field = False
            auto_term_list = []
            
            contains_full_text = u'<field name="contains_full_text">false</field>'
            if not (isinstance(full_text, int) or full_text.startswith('no path in db registry for [') or full_text.startswith('[DefaulAccess] No datastream could be returned')):
                logger.info("Creating full_text and contains_full_text fields")
                # TODO: employ harsher XML filtering for bad/special characters. Should really be done soon
                full_text = full_text.decode('latin1')
                full_text = self.filter_tool.filter_non_XML_text(full_text)
                full_text = self.filter_tool.xmlEntityEncode(full_text)
                
                #Term Extraction
                logger.info("Attempting Term extraction")
                termlist = self.t.get_term_list(full_text.encode('utf-8'))
                for gen_term in termlist:
                    auto_term_list.append(u'<field name="automatic_terms">%s</field>' % (gen_term))
                
                contains_full_text = u'<field name="contains_full_text">true</field>'
                full_text_field = u'<field name="full_text">%s</field>' % (full_text)     

            if solr_text:
                logger.info("Attempting to add pid: %s to Solr" % (pid))
                
                text_to_add = [u'<add><doc>']
                text_to_add.append(solr_text)
                if collections_text: text_to_add.append(collections_text)
                if auto_term_list: text_to_add.append(u"".join(auto_term_list))
                if contains_full_text: text_to_add.append(contains_full_text)
                if full_text_field: text_to_add.append(full_text_field)
                text_to_add.append(u'</doc></add>')
                
                if debug:
                    logger.debug(u"".join(text_to_add).encode('UTF-8'))
                
                self.solr.doUpdateXML(u"".join(text_to_add).encode('UTF-8'))
                
            else:
                logger.error("FAIL: %s - Error getting object and/or datastreams from Fedora" % (pid))
                return False

            if commit: 
                self.solr.commit()
                
            return True
        else:
            logger.error("FAIL: self.fedoraClient = None or self.solr = None in the add_pid function")
            return False
