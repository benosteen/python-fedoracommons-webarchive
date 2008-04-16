# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Browse - Search through the archive</title>
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
        width: 14em;
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
<h1> Browse: </h1>
</div>

% if c.returned_facets:
<div id="facet_container">
<div id="facet_box_container">
% for facet in c.browsable:
<div id="${c.browsable[facet]}">
<strong>${c.field_names[c.browsable[facet]]} ${h.link_to("see more", h.url(controller='/browse', action='field', field=facet))}</strong>
<ul>
% if facet=="collection":
% for result,value in c.returned_facets[c.browsable[facet]]:
<li><span class="label">${h.link_to(g.f.ri.getDCTitle(result), h.url(controller='/browse', action='field', field=facet, item=c.quote(result)))} - (${value})</li>
% endfor
% else:
% for result,value in c.returned_facets[c.browsable[facet]]:
<li><span class="label">${h.link_to(result, h.url(controller='/browse', action='field', field=facet, item=c.quote(result)))} - (${value})</li>
% endfor
</ul>
% endif
</div>
% endfor
</div>
</div>
% endif
