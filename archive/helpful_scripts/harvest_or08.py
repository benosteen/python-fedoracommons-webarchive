from fedoraClient30 import FedoraClient as FedoraClient30

from uuid import uuid4

import urllib, urllib2

import os

from rels_ext import Rels_Ext as Relsext

import rdflib
from rdflib.Graph import ConjunctiveGraph as cg
from rdflib import Namespace, Literal
from rdflib import URIRef

from datetime import datetime

from elementtree import ElementTree as ET

from solrfeeder import DCSolrFeeder

import pickle

repo = FedoraClient30(server='http://localhost:8080/fedora', username='fedoraAdmin', password='asdfadsf', version="3.0", use_UUID=True)

sf = DCSolrFeeder(fedora_url='http://localhost:8080/fedora', 
                                 fedora_version="3.0",
                                 solr_url='localhost:8080',
                                 solr_username='',
                                 solr_password='')

def add_resource_map(resource_map_url, copy_by="Val"):
    print "Adding ReM at %s" % resource_map_url
    rdf  = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    ore  = Namespace("http://www.openarchives.org/ore/terms/")
    dc  = Namespace("http://purl.org/dc/elements/1.1/")
    dcterms  = Namespace("http://purl.org/dc/terms/")
    owl  = Namespace("http://www.w3.org/2002/07/owl#")
    rdfs = Namespace("http://www.w3.org/2001/01/rdf-schema#")
    bindings = { u"rdf": rdf, u"rdfs": rdfs, u"dc": dc, u"dcterms": dcterms, u'owl':owl, u'ore':ore }
    g = cg()
    g.parse(resource_map_url)
    for s,p,o in g.triples((None, ore['describes'], None)):
        # o is the URI for the aggregation
        pids = repo.createNewObject(label=resource_map_url, namespace="uuid")
        relsext = Relsext(FedoraClient=repo)
        relsext.setPID(pids['pid'])
        relsext.addProperty('rel', u'isMemberOf', 'type:basic')
        relsext.addProperty('rel', u'isMemberOfCollection', 'repository:or08')
        relsext.store()
        fileno = 01
        for ap,sp,so in g.triples((o, ore['aggregates'], None)):
            # triples test for oai_dc
            oai_dc = False
            for q,w,e in g.triples((so, dcterms['conformsTo'], Literal('http://www.openarchives.org/OAI/2.0/oai_dc/'))):
                oai_dc=True
            if oai_dc:
                repo.putString(pids['pid'], 'DC', urllib2.urlopen(so).read())
            elif copy_by=="ref":
                print "Creating %s dsid - via Copy By Reference" % ("Item%s" % fileno)
                info = repo.putString(pids['pid'], "Item%s" % fileno, None, params={'controlGroup':'R', 'dsLocation':so, 'dsLabel':so})
                fileno = fileno + 1
                print info
            else:
                filename = "%s.%s" % (uuid4().urn[9:], so.split('.')[-1])
                print "Adding %s (tmp filename: /tmp/%s" % (so, filename)
                filepath = os.path.join('/tmp/', filename)
                file_handle = open(filepath, 'w')
                file_handle.write(urllib2.urlopen(so).read())
                file_handle.close()
                print "Creating %s dsid" % ("Item%s" % fileno)
                info = repo.putFile(pids['pid'], "Item%s" % fileno, filepath, params={'dsLabel':so})
                fileno = fileno + 1
                print "Reponse: %s" % info
                try:
                    os.remove(filepath)
                except OSError:
                    # Tried to remove file... oh well.
                    pass
    return pids



url = "http://pubs.or08.ecs.soton.ac.uk/cgi/export_all?format=ResMapUrls"

list = urllib.urlopen(url).read()

urls = list.split('\n')

for rem_url in urls:
    if rem_url.startswith('http://'):
        pids = add_resource_map(rem_url)
        sf.add_pid(pids['pid'], commit=False)
    
sf.commit()


