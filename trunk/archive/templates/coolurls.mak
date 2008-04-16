# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Information - Tools for researchers and developers</title>
  <style>
    div#tools_wrapper {
        margin:1em;
    }
    div#tools_wrapper div {
       margin: 1em 2em;
       border: 1px solid #ededed;
    }    
    div#tools_wrapper ul li {
        list-style-type: disc;
        margin-left: 2em;
    }    
    div#tools_wrapper ul li ul li {
        list-style-type: square;
        margin-left: 2em;
    }
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="tools_wrapper">

<h1> <a name="top">A walkthrough of the URL structures</h1>
<ul>
<li><a href="#browse">Browse URLs</a></li>
<li><a href="#resource">Resource URLs</a>
<ul><li><a href="#versions"> and versions</a></li></ul>
</li>
<li><a href="#search">Search URLs</a></li>
</ul>
<div class="subheading"><em>NB - '<em>pid</em>' stands for the object's id</em></div>
<a name="browse"></a>
<div id="browse">
<div class="subheading"> Browse URLs <a href="#top">to top</a></div>
<ul>
<li><a href="http://localhost:5000/browse">http://localhost:5000/browse</a> will show a set of facetable fields, each with a max of 10 groupings, sorted with the more populated groups first</li>

<li>http://localhost:5000/browse/field_name -> can be <a href="http://localhost:5000/browse/keyphrase">keyphrase</a>, <a href="http://localhost:5000/browse/collection">collection</a>, <a href="http://localhost:5000/browse/subject">subject</a>, <a href="http://localhost:5000/browse/date">date</a>, <a href="http://localhost:5000/browse/faculty">faculty</a></li>

<li>http://localhost:5000/browse/field_name/query -> For example, to browse the list of items which have a copyright date of 2008, visit <a href="http://localhost:5000/browse/date/2008">http://localhost:5000/browse/date/2008</a></li>
</ul>
</div><a name="resource"></a>
<div id="objects">
<div class="subheading"> Resource URLs <a href="#top">to top</a></div> 
<ul>
<li><a href="http://localhost:5000/objects">http://localhost:5000/objects</a> will redirect to the search
<li><a href="http://localhost:5000/objects/pid">http://localhost:5000/objects/<em>pid</em></a>     or
<li><a href="http://localhost:5000/objects/pid/show">http://localhost:5000/objects/<em>pid</em>/show</a>   will take them to the HTML splash page for the 'pid' record
<li>Related to this is <a href="http://localhost:5000/objects/pid/format">http://localhost:5000/objects/<em>pid</em>/format</a>    -> show an HTML list of the possible export formats (?xml=true for machinable version)</li>
<li>E.g	<a href="http://localhost:5000/objects/pid/format/mods">http://localhost:5000/objects/<em>pid</em>/format/<em>mods</em></a>   -> Spits out the MODS record </li>
<li><a href="http://localhost:5000/objects/pid/datastreams">http://localhost:5000/objects/<em>pid</em>/datastreams</a>   -> Show Html list of attachments for download</li>
<li><a href="http://localhost:5000/objects/pid/datastreams?xml=true">http://localhost:5000/objects/<em>pid</em>/datastream?xml=true</a>   -> Show xml list of attachments for download (shows all possible resources, not just those for 'human' download.)</li>
<li><a href="http://localhost:5000/objects/pid/datastreams/IMAGE01">http://localhost:5000/objects/<em>pid</em>/datastreams/datastream</a> -> Start a download for the given datastream e.g. IMAGE01</li>
</ul>
<a name="rdf"></a>
<div class="subheading"> Relationships and properties for objects - RDF <a href="#top">to top</a></div>
<ul>
<li><a href="http://localhost:5000/objects/pid/relationships">http://localhost:5000/objects/<em>pid</em>/relationships</a>   -> show as HTML the relationships attached to this item</li>
<li><a href="http://localhost:5000/objects/pid/relationships?format=n3">http://localhost:5000/objects/<em>pid</em>/relationships?format=n3</a>   -> show the relationships attached to this item in rdf-n3 format for example)</li>
</ul>
<a name="ore"></a>
<div class="subheading"> OAI-ORE Resource Maps for objects  - <a href="#top">to top</a></div>
<ul>
<li><a href="http://localhost:5000/objects/pid/rem">http://localhost:5000/objects/<em>pid</em>/rem</a> -> Get an RDF/XML serialisation of the OAI-ORE resource map. </li>
</ul>
<a name="resolver"></a>
<div class="subheading"> info:fedora/XXX:XXX resolver - <a href="#top">to top</a></div>
<ul>
<li><a href="http://localhost:5000/resolve/info:fedora/pid">http://localhost:5000/resolve/[Fedora URI]</a> -> Dereference a Fedora URI of the form info:fedora/pid. A HTTP GET on this URL will result in producing the HTML human readable record page for the item. </li>
<li>On a side note, a HTTP GET on a Fedora URI with the datastream ID - <a href="http://localhost:5000/resolve/info:fedora/pid/datastream">info:fedora/pid/datastream</a> will result in initiating the download for that datastream.</li>
</ul>
<a name="versions"></a>
<div class="subheading"> Resource URLs and accessing past versions <a href="#top">to top</a></div>
<p>Note that including the date after the <em>pid</em> will reference a revision of the <em>pid</em> at the date asked for:</p>
<ul>
<li><a href="http://localhost:5000/objects/pid">http://localhost:5000/objects/<em>pid</em></a>   -> Most current version</li>
<li><a href="http://localhost:5000/objects/pid/2008">http://localhost:5000/objects/<em>pid</em>/2008</a>   -> Version from 2008 (2008-01-01 by default)</li>
<li><a href="http://localhost:5000/objects/pid/20050303">http://localhost:5000/objects/<em>pid</em>/20050303</a>  -> Version from 2005-03-03 (and the day after is 2005-03-04)</li>
<li><a href="http://localhost:5000/objects/pid/20050303/datastreams">http://localhost:5000/objects/<em>pid</em>/20050303/datastreams</a>
<li><a href="http://localhost:5000/objects/pid/20050303/datastreams/MODS">http://localhost:5000/objects/<em>pid</em>/20050303/datastreams/MODS</a>
</ul>
<p>Note that I don't think I'll be able to easily version the range of things I'd like to show on the relationships pages. For the rest, the internal mechnism that Fedora uses to store the revisions of the items fits the pattern I have used above, so this functionality is more a case of exposing and using it, than coding it myself.</p>
</div> <a name="search"></a>
<div id="search">
<div class="subheading">Search URLs <a href="#top">to top</a></div>
<ul>
<li> The basic search is available from any page that is not the detailed search or results page from the box at the top of the screen. The syntax for this is <a href="http://localhost:5000/search/basic?rows=5&truncate=450&q=test">http://localhost:5000/search/basic?rows=<em>number_of_rows</em>&truncate=<em>number_of_characters_to_truncate_at</em>&q=<em>Query</em></a> - NB I prefered to make the full search the OpenSearch endpoint.</li>
<li> Site exposes a detailed search service that aims to be OpenSearch Compliant (eventually). Currently, it works well enough. Firefox 2, and Flock should automatically detect the search engine and offer it as an installable plugin. OpenSearch doc is at <a href="http://localhost:5000/search/opensearch">http://localhost:5000/search/opensearch</a></li>
<li><a href="http://localhost:5000/search">http://localhost:5000/search</a> is the address of the actual search service. This includes faceted searching and control over sort and detail returned from the search.</li>
<li>All search results pages include a link on the page, the URL of which will recreate the search as the user has entered it. For example, searching on 'economics' and showing groupings by 'Publisher' can be recreated by the url: <a href="http://localhost:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default">http://localhost:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default</a></li>
<li>By adding the parameter of 'format=atom', the search results will be relayed out as an Atom feed of sorts (facet filtering is still applied but the facet browse terms aren't included). E.g. <a href="http://localhost:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default&format=atom">http://localhost:5000/search/detailed?sort=copyright_date+asc&rows=5&truncate=450&facetfaculty=true&q=economics&view=Default&format=atom</a>  Also, the feed for a given search has been added to the search result page metadata, meaning that this feed should be automatically discovered by the browser.</li>
</ul>
<div class="subheading">Convenience Search URLs <a href="#top">to top</a></div>
<ul>
<li>${h.link_to( h.url_for(controller='person', q='bishop') )}</li>
</ul>
</div>


</div>
