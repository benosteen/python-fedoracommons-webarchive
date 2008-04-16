# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Browse - Search through the </title>
  <style>
    div#browse {
       margin: 1em 2em;
    }
    div#facet_container {
        margin-left: 3em;
        border: 1px solid #cdcdcd;
        background-color: #efefef;
        float: left;
    }
    
    div#facet_container h1 {
        padding-left: 3em;
    }
    
    div#facet_container div {
        margin: 0 auto;
        width: 100%;
    }
    
    div#facet_container div div {
        width: 90%;
        float:left;
        padding: 1em;
    }
    #cloud a.tag0 { font-size: 0.7em; font-weight: 100; }
    #cloud a.tag1 { font-size: 0.8em; font-weight: 200; }
    #cloud a.tag2 { font-size: 0.9em; font-weight: 300; }
    #cloud a.tag3 { font-size: 1.0em; font-weight: 400; }
    #cloud a.tag4 { font-size: 1.2em; font-weight: 500; }
    #cloud a.tag5 { font-size: 1.4em; font-weight: 600; }
    #cloud a.tag6 { font-size: 1.6em; font-weight: 700; }
    #cloud a.tag7 { font-size: 1.8em; font-weight: 800; }
    #cloud a.tag8 { font-size: 2.2em; font-weight: 900; }
    #cloud a.tag9 { font-size: 2.5em; font-weight: 900; }
    #cloud a.tag10 { font-size: 2.7em; font-weight: 1000; }
    #cloud { padding: 2px; line-height: 3em; text-align: center; }
    #cloud a { padding: 0px; }
    #cloud { margin: 0; }
    #cloud li { display: inline; }
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="browse">
<h1> Browse: (${h.link_to('as cloud, largest populations only', h.url_for(view='cloud_small') )}) (${h.link_to('as cloud, all members', h.url_for(view='cloud') )}) (${h.link_to('as alphabetical list', h.url_for(view='list') )})</h1>
<div class="subheading"> ${h.link_to('Back to top-level Browse page.', h.url_for(controller="/browse"))}</div>
</div>
% if c.returned_facets:
<div id="facet_container">
<div id="facet_box_container">
% for facet in c.returned_facets:
<div id="${facet}">
<strong>${c.field_names[facet]}</strong>
<ul id="cloud">
% if facet=="collection":
% for result,value in c.returned_facets[facet]:
% if result:
<li><a href="${h.url_for(controller='/browse', action='field', field=c.rev_browsable[facet], item=result.decode('utf-8'))}" class="${"tag%s" % (value)}">${g.f.ri.getDCTitle(result)}</a></li>
% endif
% endfor
% else:
% for result,value in c.returned_facets[facet]:
% if result:
<li><a href="${h.url_for(controller='/browse', action='field', field=c.rev_browsable[facet], item=result.decode('utf-8'))}" class="${"tag%s" % (value)}">${result}</a></li>
% endif
% endfor
% endif
</ul>
</div>
% endfor
</div>
</div>
% endif
