from fedoraClient30 import FedoraClient as FedoraClient30

from solrfeeder import DCSolrFeeder

repo = FedoraClient30(server='http://localhost:8080/fedora', username='fedoraAdmin', password='asdfadsf', version="3.0")

r = repo.ri

query = """select $object from <#ri> where $object <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <info:fedora/fedora-system:def/model#FedoraObject>"""

# Scan up to the first 100,000 objects
csv = r.getTuples(query, format='csv', limit='100000').split('\n')[1:-1]

sf = DCSolrFeeder(fedora_url='http://localhost:8080/fedora', 
                                 fedora_version="3.0",
                                 solr_url='localhost:8080',
                                 solr_username='',
                                 solr_password='')

csv = [x.split('/')[1] for x in csv]

for pid in csv:
    sf.solr.delete(pid)
    repo.deleteObject(pid)
    
sf.commit()
