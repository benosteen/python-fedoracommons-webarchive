from fedoraClient30 import FedoraClient as FedoraClient30

import getopt, sys

from datetime import datetime, timedelta

from solrfeeder import DCSolrFeeder

def main():
    try:
        # Using getopt to make it easier to forgive bad dates
        opts, args = getopt.getopt(sys.argv[1:], "")
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err)
        sys.exit(2)

    from_date = ''
    if not args:
        now = datetime.now()
        twentyfour_hours = timedelta(days=100)
        then = now - twentyfour_hours
        from_date = then.isoformat().split('.')[0]
    else:
        from_date = args[0]

    repo = FedoraClient30(server='http://localhost:8080/fedora', username='fedoraAdmin', password='asdfadsf', version="3.0")

    r = repo.ri

    query = """select $object from <#ri>
            where $object  <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <info:fedora/fedora-system:def/model#FedoraObject>
            and $object <info:fedora/fedora-system:def/view#lastModifiedDate> $date
            and $date <http://mulgara.org/mulgara#after> '%s'^^<http://www.w3.org/2001/XMLSchema#dateTime> in <#xsd>""" % (from_date)

    # Scan up to the first 100,000 objects
    csv = r.getTuples(query, format='csv', limit='100000')
    if isinstance(csv, tuple):
        
        print "There was an error with the query %s\nDate must be in the format YYYY-MM-DDTHH:MM:SS.MILZ\nServer reply was %s"% (query, csv)
    else:
        csv = csv.split('\n')[1:-1]

        sf = DCSolrFeeder(fedora_url='http://localhost:8080/fedora', 
                                        fedora_version="3.0",
                                        solr_url='localhost:8080',
                                        solr_username='',
                                        solr_password='')

        csv = [x.split('/')[1] for x in csv]

        for pid in csv:
            sf.add_pid(pid, commit=False)

        sf.commit()

if __name__ == "__main__":
    main()
