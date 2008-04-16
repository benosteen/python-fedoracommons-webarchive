from StringIO import StringIO

from xml.dom import minidom, Node
from xml import xpath
from xml.dom.ext import PrettyPrint

class DC(object):
    dc_template = u"""<?xml version="1.0" encoding="UTF-8"?><oai_dc:dc xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/"></oai_dc:dc>"""

    def __init__(self, FedoraClient = None):
        self.doc = None
        self.ctx = None
        self.fedoraClient = FedoraClient
        self.pid = None
        self.setDOM(DC.dc_template)

    def setDOM(self, XMLstring='', pid=None):
        if pid==None:
            if XMLstring == '':
                self.doc = minidom.parseString(DC.dc_template)
            else:
                self.doc = minidom.parseString(XMLstring)
        else:
            self.pid = pid
            if self.fedoraClient != None:
                dc_text = self.fedoraClient.getDatastream(self.pid, 'DC')
                if not (isinstance(dc_text, int) or dc_text.startswith('no path in db registry for [') or dc_text.startswith('[DefaulAccess] No datastream could be returned')):
                    self.doc = minidom.parseString(dc_text)
                else:
                    self.doc = minidom.parseString(DC.dc_template)
            else:
                self.doc = minidom.parseString(DC.dc_template)
                
        self.ctx = xpath.CreateContext(self.doc)
        self.ctx.setNamespaces({u'DC':"info:fedora/fedora-system:def/DC#",
                                u'dc':"http://purl.org/dc/elements/1.1/",
                                u'oai_dc':"http://www.openarchives.org/OAI/2.0/oai_dc/"
                                })
        
        # TODO: Adapt this for multiple Mods records in a given collection XML
        self.basenode = self.doc.documentElement
        
    def addField(self, field, value):
        response = False
        
        field = field.lower()
        
        # Split the dc: or oai_dc: namespace from the field name, if it exists
        split_field = field.split(':')
        
        if len(split_field)>1:
            field = ''.join(split_field[1:])
        
        if field != None and self.basenode != None:
            node = self.doc.createElementNS("http://purl.org/dc/elements/1.1/", 'dc:'+field)
            node.appendChild(self.doc.createTextNode(value))
            self.basenode.appendChild(node)
            response = True
        return response
        
    def addFieldList(self, list_of_tuples):
        for name_value_pair in list_of_tuples:
            self.addField(name_value_pair[0], name_value_pair[1])

    def listFields(self):
        if self.doc != None:
            field_list = {}
            for node in self.doc.documentElement.childNodes:
                nodename, nodevalue = None, None
                if node.nodeType == Node.ELEMENT_NODE:
                    nodename = node.nodeName
                    if node.firstChild.nodeType == Node.TEXT_NODE:
                        nodevalue = node.firstChild.nodeValue
                    else:
                        nodevalue = node.firstChild
                        
                    if field_list.get(nodename, None):
                        if isinstance(field_list.get(nodename), list):
                            tmp_list = field_list.get(nodename)
                            tmp_list.append(nodevalue)
                            field_list[nodename] = tmp_list
                    else:
                        field_list[nodename] = [nodevalue]
            return field_list
        else:
            return None
        
    def store(self, store='/tmp/'):
        if self.pid != None and self.fedoraClient != None: 
            dsContent = self.toString()
            response = self.fedoraClient.putString(self.pid, 'DC', dsContent.encode('utf-8'), params={'dsLabel':'Dublin Core Record'})
            return response
        return False

    def removeField(self, field):
        response = False
        dc_nodes = xpath.Evaluate("//dc:"+field, context=self.ctx)
        if dc_nodes != None:
            # remove the last hit
            last_node = dc_nodes[-1]
            last_node.parentNode.removeChild(last_node)
            response = True
        return response

    def toString(self):
        return self.doc.toxml()
        
        
    def toFileObj(self):
        strIO = StringIO()
        strIO.write(self.doc.toxml())
        return strIO

