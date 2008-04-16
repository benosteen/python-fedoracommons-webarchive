import logging

from archive.lib.base import *

log = logging.getLogger(__name__)

class AllResourceMapsController(BaseController):

    def index(self):
        query = """select $object from <#ri> where $object <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <info:fedora/fedora-system:def/model#FedoraObject>"""

        # Scan up to the first 100,000 objects
        csv = g.f.ri.getTuples(query, format='csv', limit='100000').split('\n')[1:-1]
        
        c.csv = [x.split('/')[1] for x in csv]
        
        return render('resource_map_list')
        
    def collection(self, id=None):
        if not id:
            h.redirect_to(action="index")

        if g.f.ri.doesPIDExist(id):
            query = """select $object from <#ri> where $object <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <info:fedora/fedora-system:def/model#FedoraObject> and $object <info:fedora/fedora-system:def/relations-external#isMemberOfCollection> <info:fedora/%s>""" % (id)

            # Scan up to the first 100,000 objects
            csv = g.f.ri.getTuples(query, format='csv', limit='100000').split('\n')[1:-1]
            
            c.csv = [x.split('/')[1] for x in csv]
            
            return render('resource_map_list')
            
