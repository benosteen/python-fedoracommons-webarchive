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
<ul>
% if facet=="collection":
% for result,value in c.returned_facets[facet]:
% if result:
<li><span class="label">${h.link_to(g.f.ri.getDCTitle(result), h.url(controller='/browse', action='field', field=c.rev_browsable[facet], item=result.decode('utf-8')))} - (${value})</li>
% endif
% endfor
% else:
% for result,value in c.returned_facets[facet]:
% if result:
<li><span class="label">${h.link_to(result, h.url(controller='/browse', action='field', field=c.rev_browsable[facet], item=result.decode('utf-8')))} - (${value})</li>
% endif
% endfor
% endif
</ul>
</div>
% endfor
</div>
</div>
% endif
