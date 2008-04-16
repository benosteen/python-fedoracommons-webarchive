from cStringIO import StringIO

import string, os, uuid

from xml import xpath

from xml.dom import minidom
from xml.dom import Node

from xml.dom.ext import PrettyPrint
                        
# Mods metadata creation and maintenance module.

# Typical usage:
# >>>  from archive.lib.mods import *
# >>>  m = Mods()
# >>>  params = {}
# >>>  corporate_params = {}
# >>>  params['nametype'] = 'personal'
# >>>  params['givenname'] = 'Benjamin'
# >>>  params['familyname'] = "O'Steen"
# >>>  params['termofaddress'] = 'Mr'
# >>>  params['displayform'] = "Benjamin O'Steen"
# >>>  params['roles'] = ['System Administrator', 'Archive developer']
# >>>  params['affiliation'] = {'System Administrator':'Archive developer','email':'benjamin.osteen@ouls.ox.ac.uk','website':'http://ora.ouls.ox.ac.uk'}
# >>>  m.addName(params)
# >>>  m.addName(params)
# >>>  m.addName(params)
# >>>  m.deleteName(2)
# >>>  m.addName(params)
# >>>  corporate_params['nametype'] = 'corporate'
# >>>  corporate_params['displayform'] = "Maysubdivide.org"
# >>>  corporate_params['roles'] = ['Funding Organisation']
# >>>  corporate_params['affiliation'] = {'email':'benjamin.osteen@ouls.ox.ac.uk','website':'http://www.maysubdivide.org'}
# >>>  m.updateName(2,corporate_params)
# >>>  m.updateName('3', corporate_params)
# >>>  print m.toString()

# If this module is to be able to automatically pull submitter's details from
# the fedora repository, it will need to be passed an instance of the client, either
# on init:

# >>>  fclient = fedoraClient('http://localhost:8080/fedora')
# >>>  m = Mods(fedoraClient = fclient)

# or during:

# >>>  m = Mods()
# >>> . ....... etc.
# >>>  fclient = fedoraClient('http://localhost:8080/fedora')
# >>>  m.fedoraClient = fclient
# >>>  m.addAuthor('person:2')


NS = {}
NS['mods'] = u'http://www.loc.gov/mods/v3'
NS['etd'] = u'http://www.ndltd.org/standards/metadata/etdms/1.0/'

allowed_affiliations = ['email',
                        'website',
                        'institution',
                        'faculty',
                        'researchgroup',
                        'pid',
                        'college',
                        'funding',
                        'grantnumber',
                        'depiction']  # As stolen from foaf...


class Mods(object):
    
    mods_template = u"""<mods:modsCollection xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:etd="http://www.ndltd.org/standards/metadata/etdms/1.0/" xmlns:mods='http://www.loc.gov/mods/v3'
 xsi:schemaLocation="http://www.loc.gov/mods/v3 http://ora.ouls.ox.ac.uk/access/mods-3.2-oxford.xsd  http://www.ndltd.org/standards/metadata/etdms/1.0/ http://www.ndltd.org/standards/metadata/etdms/1.0/etdms.xsd">
  <mods:mods version="3.2">
  </mods:mods>
</mods:modsCollection>"""
  
    def __init__(self, FedoraClient=None):
        self.setDOM(Mods.mods_template)
        self.fedoraClient = FedoraClient
        self.pid = None
                                    
    def setDOM(self, XMLstring, pid=None):
        if pid==None:
            if XMLstring == '':
                self.mods = minidom.parseString(Mods.mods_template)
            else:
                self.mods = minidom.parseString(XMLstring)
        else:
            self.pid = pid
            if self.fedoraClient != None:
                mods_text = self.fedoraClient.getDatastream(self.pid, 'MODS')
                if not (isinstance(mods_text, int) or mods_text.startswith('no path in db registry for [') or mods_text.startswith('[DefaulAccess] No datastream could be returned')):
                    self.mods = minidom.parseString(mods_text)
                else:
                    self.mods = minidom.parseString(Mods.mods_template)    
            else:
                self.mods = minidom.parseString(Mods.mods_template)    
                
        self.ctx_mods = xpath.CreateContext(self.mods)
        self.ctx_mods.setNamespaces({u'mods':NS['mods'],
                                     u'etd':NS['etd']
                                    })
        # add the first <mods:mods> instance to a handle called basenode
        # TODO: Adapt this for multiple Mods records in a given collection XML
        self.basenode = xpath.Evaluate("//mods:mods", context=self.ctx_mods)[0]

    def makeModsNode(self, nodename):
        return self.mods.createElementNS(NS['mods'], nodename)

    def makeModsLeaf(self, nodename, text, attribs={}):
        node = self.makeModsNode(nodename)
        node.appendChild(self.mods.createTextNode(text))
        for attrib in attribs.keys():
            node.setAttribute(attrib, attribs[attrib])
        
        return node
        
    def store(self, store='/tmp/'):
        if self.pid != None and self.fedoraClient != None:
            dsContent = self.toString()
            response = self.fedoraClient.putString(self.pid, 'MODS', dsContent.encode('utf-8'), params={'dsLabel':'MODS v3.2 Metadata'})
            return response
        return False


    # Section: name and namePart creation section
    # Description: Contains the functions needed to add, remove, and update name
    #               elements in the MODS dom.

    def addAuthor(self, authorpid):
        # First, make sure this has access to a fedora client instance:
        if self.fedoraClient == None:
            return False
        
        # First check to see if the author is already in this record:
        # isAuthorInRecord = self.isAuthor(authorpid)
        isAuthorInRecord = False
        
        # If not, then get the author's MOD profile and append that fragment
        if isAuthorInRecord != True:
            # Test to see if the fragment exists
            if self.fedoraClient.doesDatastreamExist(authorpid, 'MODS'):
                # Get fragment and the mods document root and append the
                # fragment to the root.
                fragment_mods = Mods()
                fragment_text = self.fedoraClient.getDatastream(authorpid, 'MODS')
                
                fragment_mods.setDOM(fragment_text)
                
                author_node_tree = fragment_mods._getNameNodeByID('1').cloneNode(1)
                
                name_id = str(self.getNextNameID())
                
                author_node_tree.setAttribute('ID', name_id)
                
                if author_node_tree != False:
                    self.basenode.appendChild(author_node_tree)
                    return True
                else:
                    return False
                
            # bail if no fragment
        return False
        
    def createNameNode(self, params):
        # Check for minimal necessary details:
        # In this case, displayName, familyName, email
        
        # Create Name node
        namenode = self.mods.createElementNS(NS['mods'], 'mods:name')
        
        # Check for what type of name this is (personal - a person, or
        # corporate - a company/publisher/department/etc
        # Don't set a type if this is unknown
        if params.get('nametype',None) != None:
            namenode.setAttribute('type', params['nametype'])
        
        # Given or first name
        if params.get('given',None) != None:
            namePart = self.makeModsLeaf('mods:namePart', params['given'], {'type':'given'})
            namenode.appendChild(namePart)
        # Family name
        if params.get('family',None) != None:
            namePart = self.makeModsLeaf('mods:namePart', params['family'], {'type':'family'})
            namenode.appendChild(namePart)
        # Term of address (Dr, Ms, etc.)
        if params.get('termsofaddress',None) != None:
            namePart = self.makeModsLeaf('mods:namePart', params['termsofaddress'], {'type':'termsOfAddress'})
            namenode.appendChild(namePart)
        
        # displayForm: Useful for non personal or DC-style names
        if params.get('displayform',None) != None:
            namePart = self.makeModsLeaf('mods:displayForm', params['displayform'])
            namenode.appendChild(namePart)
        
        # Description: No idea what to use this for yet, but it's in MODS 3.2...
        if params.get('description',None) != None:
            namePart = self.makeModsLeaf('mods:description', params['description'])
            namenode.appendChild(namePart)
        
        # Roles: Expect a dict entry 'roles' which links to a list
        if params.get('roles',None) != None:
            role = self.mods.createElementNS(NS['mods'], 'mods:role')
            # If supplied with a string, add a single attribute. Or, if it is
            # a list, process the list:
            if isinstance(params['roles'], list):
                for role_name in params['roles']:
                    roleTerm = self.makeModsLeaf('mods:roleTerm', role_name, {'type':'text'})
                    role.appendChild(roleTerm)
            elif isinstance(params['roles'], str):
                roleTerm = self.makeModsLeaf('mods:roleTerm', params['roles'], {'type':'text'})
                role.appendChild(roleTerm)
            namenode.appendChild(role)
        
        # Affiliations: process much like the roles previously
        if params.get('affiliation',None) != None:
            # If supplied with a tuple, add a single role. 
            # If it is a dictionary, process it:
            affiliations = params['affiliation']
            if isinstance(affiliations, dict):
                for affiliation_type in affiliations.keys():
                    # Make sure the affiliation is part of the allowed list:
                    if allowed_affiliations.__contains__(affiliation_type.lower()):
                        affiliation = self.makeModsLeaf('mods:affiliation', 
                                                        affiliations[affiliation_type], 
                                                        {'type':affiliation_type})
                        namenode.appendChild(affiliation)
            elif isinstance(affiliations, tuple):
                affiliation_type, affiliation_value = affiliations
                # Make sure the affiliation is part of the allowed list:
                if allowed_affiliations.__contains__(affiliation_type.lower()):
                    affiliation = self.makeModsLeaf('mods:affiliation', 
                                                    affiliation_value, 
                                                    {'type':affiliation_type})
                    namenode.appendChild(affiliation)

        return namenode
    
    def addName(self, params):
        name_node = self.createNameNode(params)

        name_id = str(self.getNextNameID())
        name_node.setAttribute('ID', name_id)

        if name_node != False:
            self.basenode.appendChild(name_node)
            return True
        else:
            return False
    
    def updateName(self, node_id, params):
        name_node = self.createNameNode(params)
        previous_node = self._getNameNodeByID(node_id)
        
        # Set the name ID to be the same as the one it replaces:
        name_node.setAttribute('ID', node_id)
        
        if name_node != False and previous_node != None:
            self.basenode.replaceChild(name_node, previous_node)
            return True
        else:
            return False

    def deleteName(self, node_id):
        name_node = self._getNameNodeByID(node_id)
        if name_node != False:
            name_node.parentNode.removeChild(name_node)
            return True
        else:
            return False
    
    # Shouldn't be needed outside of the module
    def _getNameNodeByID(self, node_id):
        if node_id != None:
            if isinstance(node_id, int):
                node_id = str(node_id)
            node = xpath.Evaluate("//mods:name[@ID="+node_id+"]", context=self.ctx_mods)
            if node != []:
                # return first match
                return node[0]
        return None
        
    def nameToHash(self, ID):
        name_node = self._getNameNodeByID(ID)
        if name_node == None:
            return {}
        else:
            namehash = {}
            # Sort out the nameParts first: (family, given, termsofaddress)
            nameParts = name_node.getElementsByTagName('mods:namePart')
            for namePart in nameParts:
                text = ''
                for node in namePart.childNodes:
                    if node.nodeType == Node.TEXT_NODE:
                        text += node.nodeValue
                
                namehash[namePart.getAttribute('type').lower()] = text
            
            # displayForm(s) next:
            displayForms = name_node.getElementsByTagName('mods:displayForm')
            for displayForm in displayForms:
                text = ''
                for node in displayForm.childNodes:
                    if node.nodeType == Node.TEXT_NODE:
                        text += node.nodeValue
                
                # Only keep the last one...
                namehash['displayform'] = text
            
            # Affiliations now:
            affiliations = name_node.getElementsByTagName('mods:affiliation')
            for affiliation in affiliations:
                text = ''
                for node in affiliation.childNodes:
                    if node.nodeType == Node.TEXT_NODE:
                        text += node.nodeValue
                
                namehash[affiliation.getAttribute('type').lower()] = text
                
            return namehash

    def getNextNameID(self):
        nodes = xpath.Evaluate("//mods:name", context=self.ctx_mods)
        if len(nodes) != 0:
            ID_list = []
            for node in nodes:
                string_ID = node.getAttribute('ID')
                ID_list.append(string.atoi(string_ID))
            ID_list.sort()
            # return a number, one more than the last list value (i.e. the highest value)
            return ID_list[-1]+1
        else:
            return 1

    # Section: TitleInfo setting and getting
    # Description: Used to set and retrieve the current title and subtitle elements
    #               NB It will always attempt to place this section at the top of a MODS record.


    # Shouldn't be needed outside of the module            
    def _getTitleInfoNode(self):
        nodes = xpath.Evaluate("//mods:titleInfo", context=self.ctx_mods)
        if len(nodes) != 0:
            # NOTE: return the first hit, as more than one titleinfo section
            # is not to be used in the Oxford Research archive. If this is
            # no longer the case, this should obviously be restructured, perhaps
            # similarly to the way that names are handled
            return nodes[0]
        else:
            return None
            
    def _createTitleInfoNode(self):
        # Create an empty 'titleInfo' node
        # Abstracted just in case we start to use ID's on these fields
                
        titleinfo_node = self.mods.createElementNS(NS['mods'], 'mods:titleInfo')
        return titleinfo_node

    def setTitleInfo(self, titles=[], subtitles=[]):
        # TODO: decide whether it remains a good choice to be an atomic remove -> update process
        #       or if it is time to add more flexibility/iterative updating.
            
        # Only start doing something, if there is a title
        if len(titles) != 0:
            # Get a new titleInfo node to work on:
            titleinfo_node = self._createTitleInfoNode()
            
            # Add the titles to the fresh, new node:
            for title in titles:
                title_node = self.makeModsLeaf('mods:title', title)
                titleinfo_node.appendChild(title_node)
                
            # Same for the subtitles now:
            for subtitle in subtitles:
                subtitle_node = self.makeModsLeaf('mods:subTitle', subtitle)
                titleinfo_node.appendChild(subtitle_node)            
                
            # Try to get the current node
            old_titleinfo_node = self._getTitleInfoNode()
            
            if old_titleinfo_node == None:
                # No titleInfo node exists. Add the titleInfo node to the top of the DOM:
                self.basenode.insertBefore(titleinfo_node, self.basenode.firstChild)
                return True
            else: 
                self.basenode.replaceChild(titleinfo_node, old_titleinfo_node)
                return True
        else:
            return False
            
    # Section: Add/Modify and remove Identifiers
    # Aim: to abstract away the difference between adding or modifying identifiers
    #       Each type of identifier should only appear once, and if this is not the case
    #       then there is a problem elsewhere, as we should avoid one-to-many identifiers.
    #       If one-to-many links need to be expressed, then relatedItem should be used.
    
    def addIdentifier(self, id_type, id_value):
        # Basic checks:
        if id_type != None and id_type != '' and id_value != None and id_value != '':
            # Types should always be lowercase, to make XPath navigation less problematic:
            id_type = id_type.lower()
            
            # Make up the id node:
            id_node = self.makeModsLeaf('mods:identifier', id_value, {'type':id_type})
            
            # Only change the top level identifiers. Try to get the relevant node:
            nodes = xpath.Evaluate("/mods:modsCollection/mods:mods/mods:identifier[@type='"+id_type+"']", context=self.ctx_mods)
            
            if len(nodes) == 1:
                self.basenode.replaceChild(id_node, nodes[0])
                return True
            elif len(nodes) == 0:
                self.basenode.appendChild(id_node)
                return True
            else:
                # Argh, more than one id value for a given type
                return False
        else:
            # None or '' was entered for either the type or the value:
            return False
    
    def removeIdentifier(self, id_type):
        # Basic checks:
        if id_type != None and id_type != '':
            # Types should always be lowercase, to make XPath navigation less problematic:
            id_type = id_type.lower()
            
            # Only look for the top level identifiers. 
            # Try to get the relevant node:
            nodes = xpath.Evaluate("/mods:modsCollection/mods:mods/mods:identifier[@type='"+id_type+"']", context=self.ctx_mods)
            
            if len(nodes) == 0:
                # No id of that type
                return False
            else:
                # Remove the first 'hit'
                self.basenode.removeChild(nodes[0])
                return True
        else:
            # None or '' was entered for the type:
            return False


    def toString(self):
        return self.mods.toxml()
        
        
    def toFileObj(self):
        strIO = StringIO()
        strIO.write(self.mods.toxml())
        return strIO

