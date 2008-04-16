from risearch import Risearch

r = Risearch()

dontcount_query = """select $object from <#ri> where $object <info:fedora/fedora-system:def/relations-external#isMemberOf> <info:fedora/type:image> or $object <info:fedora/fedora-system:def/relations-external#isMemberOf> <info:fedora/type:imagecollection>"""

query = """select $object from <#ri> where $object <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <info:fedora/fedora-system:def/model#FedoraObject>"""

total = r.getTuples(query, lang='itql', format='count', limit='100000', offset='0')
dontcount_item_number = r.getTuples(dontcount_query, lang='itql', format='count', limit='100000', offset='0')

print int(total)-int(dontcount_item_number)


