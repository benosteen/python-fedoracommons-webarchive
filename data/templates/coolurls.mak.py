from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1207130040.205857
_template_filename='/home/ben/Desktop/archive/archive/templates/coolurls.mak'
_template_uri='/coolurls.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['header', 'footer', 'head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.mak', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 22
        context.write(u'\n')
        # SOURCE LINE 24
        context.write(u'\n')
        # SOURCE LINE 26
        context.write(u'\n<div id="tools_wrapper">\n\n<h1> <a name="top">A walkthrough of the URL structures</h1>\n<ul>\n<li><a href="#browse">Browse URLs</a></li>\n<li><a href="#resource">Resource URLs</a>\n<ul><li><a href="#versions"> and versions</a></li></ul>\n</li>\n<li><a href="#search">Search URLs</a></li>\n</ul>\n<div class="subheading"><em>NB - \'<em>pid</em>\' stands for the object\'s id</em></div>\n<a name="browse"></a>\n<div id="browse">\n<div class="subheading"> Browse URLs <a href="#top">to top</a></div>\n<ul>\n<li><a href="http://localhost:5000/browse">http://localhost:5000/browse</a> will show a set of facetable fields, each with a max of 10 groupings, sorted with the more populated groups first</li>\n\n<li>http://localhost:5000/browse/field_name -> can be <a href="http://localhost:5000/browse/keyphrase">keyphrase</a>, <a href="http://localhost:5000/browse/collection">collection</a>, <a href="http://localhost:5000/browse/subject">subject</a>, <a href="http://localhost:5000/browse/date">date</a>, <a href="http://localhost:5000/browse/faculty">faculty</a></li>\n\n<li>http://localhost:5000/browse/field_name/query -> For example, to browse the list of items which have a copyright date of 2008, visit <a href="http://localhost:5000/browse/date/2008">http://localhost:5000/browse/date/2008</a></li>\n</ul>\n</div><a name="resource"></a>\n<div id="objects">\n<div class="subheading"> Resource URLs <a href="#top">to top</a></div> \n<ul>\n<li><a href="http://localhost:5000/objects">http://localhost:5000/objects</a> will redirect to the search\n<li><a href="http://localhost:5000/objects/pid">http://localhost:5000/objects/<em>pid</em></a>     or\n<li><a href="http://localhost:5000/objects/pid/show">http://localhost:5000/objects/<em>pid</em>/show</a>   will take them to the HTML splash page for the \'pid\' record\n<li>Related to this is <a href="http://localhost:5000/objects/pid/format">http://localhost:5000/objects/<em>pid</em>/format</a>    -> show an HTML list of the possible export formats (?xml=true for machinable version)</li>\n<li>E.g\t<a href="http://localhost:5000/objects/pid/format/mods">http://localhost:5000/objects/<em>pid</em>/format/<em>mods</em></a>   -> Spits out the MODS record </li>\n<li><a href="http://localhost:5000/objects/pid/datastreams">http://localhost:5000/objects/<em>pid</em>/datastreams</a>   -> Show Html list of attachments for download</li>\n<li><a href="http://localhost:5000/objects/pid/datastreams?xml=true">http://localhost:5000/objects/<em>pid</em>/datastream?xml=true</a>   -> Show xml list of attachments for download (shows all possible resources, not just those for \'human\' download.)</li>\n<li><a href="http://localhost:5000/objects/pid/datastreams/IMAGE01">http://localhost:5000/objects/<em>pid</em>/datastreams/datastream</a> -> Start a download for the given datastream e.g. IMAGE01</li>\n</ul>\n<a name="rdf"></a>\n<div class="subheading"> Relationships and properties for objects - RDF <a href="#top">to top</a></div>\n<ul>\n<li><a href="http://localhost:5000/objects/pid/relationships">http://localhost:5000/objects/<em>pid</em>/relationships</a>   -> show as HTML the relationships attached to this item</li>\n<li><a href="http://localhost:5000/objects/pid/relationships?format=n3">http://localhost:5000/objects/<em>pid</em>/relationships?format=n3</a>   -> show the relationships attached to this item in rdf-n3 format for example)</li>\n</ul>\n<a name="ore"></a>\n<div class="subheading"> OAI-ORE Resource Maps for objects  - <a href="#top">to top</a></div>\n<ul>\n<li><a href="http://localhost:5000/objects/pid/rem">http://localhost:5000/objects/<em>pid</em>/rem</a> -> Get an RDF/XML serialisation of the OAI-ORE resource map. </li>\n</ul>\n<a name="resolver"></a>\n<div class="subheading"> info:fedora/XXX:XXX resolver - <a href="#top">to top</a></div>\n<ul>\n<li><a href="http://localhost:5000/resolve/info:fedora/pid">http://localhost:5000/resolve/[Fedora URI]</a> -> Dereference a Fedora URI of the form info:fedora/pid. A HTTP GET on this URL will result in producing the HTML human readable record page for the item. </li>\n<li>On a side note, a HTTP GET on a Fedora URI with the datastream ID - <a href="http://localhost:5000/resolve/info:fedora/pid/datastream">info:fedora/pid/datastream</a> will result in initiating the download for that datastream.</li>\n</ul>\n<a name="versions"></a>\n<div class="subheading"> Resource URLs and accessing past versions <a href="#top">to top</a></div>\n<p>Note that including the date after the <em>pid</em> will reference a revision of the <em>pid</em> at the date asked for:</p>\n<ul>\n<li><a href="http://localhost:5000/objects/pid">http://localhost:5000/objects/<em>pid</em></a>   -> Most current version</li>\n<li><a href="http://localhost:5000/objects/pid/2008">http://localhost:5000/objects/<em>pid</em>/2008</a>   -> Version from 2008 (2008-01-01 by default)</li>\n<li><a href="http://localhost:5000/objects/pid/20050303">http://localhost:5000/objects/<em>pid</em>/20050303</a>  -> Version from 2005-03-03 (and the day after is 2005-03-04)</li>\n<li><a href="http://localhost:5000/objects/pid/20050303/datastreams">http://localhost:5000/objects/<em>pid</em>/20050303/datastreams</a>\n<li><a href="http://localhost:5000/objects/pid/20050303/datastreams/MODS">http://localhost:5000/objects/<em>pid</em>/20050303/datastreams/MODS</a>\n</ul>\n<p>Note that I don\'t think I\'ll be able to easily version the range of things I\'d like to show on the relationships pages. For the rest, the internal mechnism that Fedora uses to store the revisions of the items fits the pattern I have used above, so this functionality is more a case of exposing and using it, than coding it myself.</p>\n</div> <a name="search"></a>\n<div id="search">\n<div class="subheading">Search URLs <a href="#top">to top</a></div>\n<ul>\n<li> The basic search is available from any page that is not the detailed search or results page from the box at the top of the screen. The syntax for this is <a href="http://localhost:5000/search/basic?rows=5&truncate=450&q=test">http://localhost:5000/search/basic?rows=<em>number_of_rows</em>&truncate=<em>number_of_characters_to_truncate_at</em>&q=<em>Query</em></a> - NB I prefered to make the full search the OpenSearch endpoint.</li>\n<li> Site exposes a detailed search service that aims to be OpenSearch Compliant (eventually). Currently, it works well enough. Firefox 2, and Flock should automatically detect the search engine and offer it as an installable plugin. OpenSearch doc is at <a href="http://localhost:5000/search/opensearch">http://localhost:5000/search/opensearch</a></li>\n<li><a href="http://localhost:5000/search">http://localhost:5000/search</a> is the address of the actual search service. This includes faceted searching and control over sort and detail returned from the search.</li>\n<li>All search results pages include a link on the page, the URL of which will recreate the search as the user has entered it. For example, searching on \'economics\' and showing groupings by \'Publisher\' can be recreated by the url: <a href="http://localhost:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default">http://localhost:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default</a></li>\n<li>By adding the parameter of \'format=atom\', the search results will be relayed out as an Atom feed of sorts (facet filtering is still applied but the facet browse terms aren\'t included). E.g. <a href="http://localhost:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default&format=atom">http://localhost:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default&format=atom</a>  Also, the feed for a given search has been added to the search result page metadata, meaning that this feed should be automatically discovered by the browser.</li>\n</ul>\n<div class="subheading">Convenience Search URLs <a href="#top">to top</a></div>\n<ul>\n<li>')
        # SOURCE LINE 101
        context.write(filters.decode.utf8(h.link_to( h.url_for(controller='person', q='bishop') )))
        context.write(u'</li>\n</ul>\n</div>\n\n\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 23
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 25
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 3
        context.write(u'\n  <title> Information - Tools for researchers and developers</title>\n  <style>\n    div#tools_wrapper {\n        margin:1em;\n    }\n    div#tools_wrapper div {\n       margin: 1em 2em;\n       border: 1px solid #ededed;\n    }    \n    div#tools_wrapper ul li {\n        list-style-type: disc;\n        margin-left: 2em;\n    }    \n    div#tools_wrapper ul li ul li {\n        list-style-type: square;\n        margin-left: 2em;\n    }\n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


