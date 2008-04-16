from fedoraClient30 import FedoraClient as FedoraClient30

from solrfeeder import BasicSolrFeeder

import pickle

repo = FedoraClient30(server='http://archive.sers.ox.ac.uk:8080/fedora', username='fedoraAdmin', password='eiteis4D', version="3.0")

pids_file = open('deleteThese.pkl', "rb")
pids_to_scan = pickle.load(pids_file)


sf = BasicSolrFeeder(fedora_url='http://archive.sers.ox.ac.uk:8080/fedora', 
                                 fedora_version="3.0",
                                 solr_url='archive.sers.ox.ac.uk:8080',
                                 solr_username='',
                                 solr_password='')

for pid in pids_to_scan:
    sf.add_pid(pid, commit=False)
    
sf.commit()
