from cStringIO import StringIO

from xml.dom import minidom
from xml import xpath
from xml.dom.ext import PrettyPrint

NS = {}
NS['rdf'] = u'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
NS['rel'] = u'info:fedora/fedora-system:def/relations-external#'
NS['rdfs']= u"http://www.w3.org/2000/01/rdf-schema#"
NS['sioc']= u"http://rdfs.org/sioc/ns#"
NS['dcterms']= u"http://purl.org/dc/terms/"
NS['person'] = u'http://ora.ouls.ox.ac.uk/person-properties#'

class Rels_Ext(object):
    
    rdf_template = u"""<?xml version="1.0" encoding="UTF-8"?>
  <rdf:RDF xmlns:rel="info:fedora/fedora-system:def/relations-external#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns:sioc="http://rdfs.org/sioc/ns#">
    <rdf:Description>
    </rdf:Description>
  </rdf:RDF>"""
  
    def __init__(self, FedoraClient=None):
        self.fedoraClient = FedoraClient
        self.pid = None
        self.setDOM(Rels_Ext.rdf_template)

    def setDOM(self, XMLstring, pid=None):
        if pid==None:
            if XMLstring == '':
                self.rdf = minidom.parseString(Rels_Ext.rdf_template)
            else:
                self.rdf = minidom.parseString(XMLstring)
        else:
            self.pid = pid
            if self.fedoraClient != None:
                rdf_xml = self.fedoraClient.getDatastream(self.pid, 'RELS-EXT')
                if not (isinstance(rdf_xml, int) or rdf_xml.startswith('no path in db registry for [') or rdf_xml.startswith('[DefaulAccess] No datastream could be returned')):
                    self.rdf = minidom.parseString(rdf_xml)

        self.ctx_rdf = xpath.CreateContext(self.rdf)
        self.ctx_rdf.setNamespaces({u'rel':NS['rel'],
                                    u'rdfs':NS['rdfs'],
                                    u'rdf':NS['rdf'],
                                    u'sioc':NS['sioc'],
                                    u'dcterms':NS['dcterms']
                                    })

    def store(self, store='/tmp/'):
        if self.pid != None and self.fedoraClient != None:
            dsContent = self.toString()
            response = self.fedoraClient.putString(self.pid, 'RELS-EXT', dsContent.encode('utf-8'), params={'dsLabel':'Relationships'} )
            return response

    def setPID(self, pid):
        response = False
        
        self.pid = pid
        
        rels_ext_nodes = xpath.Evaluate("//rdf:RDF/rdf:Description", context=self.ctx_rdf)
        
        if rels_ext_nodes != None:
            for node in rels_ext_nodes:
                node.setAttribute('rdf:about', 'info:fedora/'+pid)
                response = True
        return response

    def listProperty(self, namespace_prefix, predicate):
        response = []
        namespace = NS.get(namespace_prefix.lower(), None)
        
        if namespace != None:
            rels_ext_nodes = xpath.Evaluate("//rdf:RDF/rdf:Description/"+namespace_prefix+':'+predicate, context=self.ctx_rdf)
            if rels_ext_nodes != None:
                for node in rels_ext_nodes:
                    object_pid = node.getAttribute('rdf:resource')
                    parsed_fedora_uri = object_pid.split('/')
                    if parsed_fedora_uri[0] == 'info:fedora':
                        object_pid = parsed_fedora_uri[1]
                    response.append(object_pid)
        return response

    def setProperty(self, namespace_prefix, predicate, object_ref):
        response = False
        namespace = NS.get(namespace_prefix.lower(), None)
        
        if namespace != None:
            rels_ext_nodes = xpath.Evaluate("//rdf:RDF/rdf:Description/"+namespace_prefix+':'+predicate, context=self.ctx_rdf)
            if rels_ext_nodes != None:
                for node in rels_ext_nodes:
                    if not response:
                        if object_ref.startswith('http://'):
                            node.setAttributeNS(NS['rdf'],'rdf:resource', object_ref)
                            response = True
                        else:
                            node.setAttributeNS(NS['rdf'],'rdf:resource', 'info:fedora/'+object_ref)
                            response = True
        return response

    def addProperty(self, namespace_prefix, predicate, object_ref):
        response = False
        namespace = NS.get(namespace_prefix.lower(), None)
        
        if namespace != None:
            # Make sure the namespace is declared:
            self.rdf.documentElement.setAttribute('xmlns:%s' % (namespace_prefix.lower()), namespace)
            rels_ext_nodes = xpath.Evaluate("//rdf:RDF/rdf:Description", context=self.ctx_rdf)
            if rels_ext_nodes != None:
                for node in rels_ext_nodes:
                    owner_node = self.rdf.createElementNS(namespace, namespace_prefix+':'+predicate)
                    if object_ref.startswith('http://'):
                        owner_node.setAttributeNS(NS['rdf'],'rdf:resource', object_ref)
                        response = True
                    else:
                        owner_node.setAttributeNS(NS['rdf'],'rdf:resource', 'info:fedora/'+object_ref)
                        response = True
                    node.appendChild(owner_node)
                    response = True
        return response

    def changeProperty(self, namespace_prefix, predicate, previous_subject, new_subject):
        response = False
        namespace = NS.get(namespace_prefix.lower(), None)
        
        if namespace != None:
            rels_ext_nodes = xpath.Evaluate("//rdf:RDF/rdf:Description", context=self.ctx_rdf)
            if rels_ext_nodes != None:
                # Should only be one node, but I feel better iterating through the nodes
                # rather than pulling it out by index (ie nodes[0])
                # This is just in case there is a bad parsing of the RDF, or the wrong datastream is
                # parsed or present in the 'RELS-EXT' dsid. If this is the case response will stay False
                for node in rels_ext_nodes:
                    for link in node.childNodes:
                        if link.nodeName == namespace_prefix+':'+predicate and link.getAttribute('rdf:resource') == 'info:fedora/'+previous_subject:
                                link.setAttribute('rdf:resource', 'info:fedora/'+new_subject)
                                response = True
        return response

    def removeProperty(self, namespace_prefix, predicate, object_ref):
        response = False
        rels_ext_nodes = xpath.Evaluate("//rdf:RDF/rdf:Description", context=self.ctx_rdf)
        if rels_ext_nodes != None:
            # Should only be one node, but I feel better iterating through the nodes
            # rather than pulling it out by index (ie nodes[0])
            # This is just in case there is a bad parsing of the RDF, or the wrong datastream is
            # parsed or present in the 'RELS-EXT' dsid. If this is the case response will stay False
            for node in rels_ext_nodes:
                for link in node.childNodes:
                    if link.nodeName == namespace_prefix+':'+predicate:
                        uri_ref = ""
                        if object_ref.startswith('http://'):
                            uri_ref = object_ref
                        else:
                            uri_ref = 'info:fedora/%s' % (object_ref)
                        
                        if link.getAttribute('rdf:resource') == uri_ref:
                            link.parentNode.removeChild(link)
                            response = True
        return response


    def toString(self):
        return self.rdf.toxml()
        
        
    def toFileObj(self):
        strIO = StringIO()
        strIO.write(self.rdf.toxml())
        return strIO

