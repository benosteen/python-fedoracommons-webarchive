# Details #


NB - 'archive-host' is the IP/name of the server running the app and lication'pid' stands for the object's id

Browse URLs

  * http://archive-host:5000/browse will show a set of facetable fields, each with a max of 10 groupings, sorted with the more populated groups first
  * http://archive-host:5000/browse/field_name -> can be any of the faceted fields as listed at the top of controllers/browse.py
  * http://archive-host:5000/browse/field_name/query -> For example, to browse the list of items which have a date of 2008, visit http://archive-host:5000/browse/date/2008

Resource URLs

  * http://archive-host:5000/objects will redirect to the search
  * http://archive-host:5000/objects/pid or
  * http://archive-host:5000/objects/pid/show will take them to the HTML splash page for the 'pid' record
  * Related to this is http://archive-host:5000/objects/pid/format -> show an HTML list of the possible export formats (?xml=true for machinable version)
  * E.g http://archive-host:5000/objects/pid/format/mods -> Spits out the MODS record
  * http://archive-host:5000/objects/pid/datastreams -> Show Html list of attachments for download
  * http://archive-host:5000/objects/pid/datastream?xml=true -> Show xml list of attachments for download (shows all possible resources, not just those for 'human' download.)
  * http://archive-host:5000/objects/pid/datastreams/datastream -> Start a download for the given datastream e.g. IMAGE01

Relationships and properties for objects - RDF

  * http://archive-host:5000/objects/pid/relationships -> show as HTML the relationships attached to this item
  * http://archive-host:5000/objects/pid/relationships?format=n3 -> show the relationships attached to this item in rdf-n3 format for example)

OAI-ORE Resource Maps for objects -

  * http://archive-host:5000/objects/pid/aggregation -> The URI-A for the object pid.

> An HTTP GET on this URL will undergo content negotiation - Based on what mimetype responses the request header 'Accept' contains, you will be redirected to either the splash page for the item, or to a serialisation of the requisite resource map.

  * http://archive-host:5000/objects/pid/aggregation.xml -> RDF/XML serialisation for the URI-R for object pid.
  * http://archive-host:5000/objects/pid/aggregation.nt -> RDF/n-triples serialisation for the URI-R for object pid.
  * http://archive-host:5000/objects/pid/aggregation.n3 -> RDF/N3 serialisation for the URI-R for object pid.
  * http://archive-host:5000/objects/pid/aggregation.turtle -> RDF/Turtle serialisation for the URI-R for object pid.
  * http://archive-host:5000/objects/pid/aggregation.atom -> Atom serialisation for the URI-R for object pid.

info:fedora/XXX:XXX resolver -

  * http://archive-host:5000/resolve/[Fedora URI] -> Dereference a Fedora URI of the form info:fedora/pid. A HTTP GET on this URL will result in producing the HTML human readable record page for the item.
  * On a side note, a HTTP GET on a Fedora URI with the datastream ID - info:fedora/pid/datastream will result in initiating the download for that datastream.

Resource URLs and accessing past versions

Note that including the date after the pid will reference a revision of the pid at the date asked for:

  * http://archive-host:5000/objects/pid -> Most current version
  * http://archive-host:5000/objects/pid/20050303/datastreams/MODS

Note that I don't think I'll be able to easily version the range of things I'd like to show on the relationships pages. For the rest, the internal mechnism that Fedora uses to store the revisions of the items fits the pattern I have used above, so this functionality is more a case of exposing and using it, than coding it myself.
Search URLs to top

  * The basic search is available from any page that is not the detailed search or results page from the box at the top of the screen. The syntax for this is http://archive-host:5000/search/basic?rows=number_of_rows&truncate=number_of_characters_to_truncate_at&q=Query - NB I prefered to make the full search the OpenSearch endpoint.
  * Site exposes a detailed search service that aims to be OpenSearch Compliant (eventually). Currently, it works well enough. Firefox 2, and Flock should automatically detect the search engine and offer it as an installable plugin. OpenSearch doc is at http://archive-host:5000/search/opensearch
  * http://archive-host:5000/search is the address of the actual search service. This includes faceted searching and control over sort and detail returned from the search.
  * All search results pages include a link on the page, the URL of which will recreate the search as the user has entered it. For example, searching on 'economics' and showing groupings by 'Publisher' can be recreated by the url: http://archive-host:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default
  * By adding the parameter of 'format=atom', the search results will be relayed out as an Atom feed of sorts (facet filtering is still applied but the facet browse terms aren't included). E.g. http://archive-host:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default&format=atom Also, the feed for a given search has been added to the search result page metadata, meaning that this feed should be automatically discovered by the browser.