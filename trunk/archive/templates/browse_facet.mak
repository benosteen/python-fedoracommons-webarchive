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
        width: 14em;
        float:left;
        padding: 1em;
    }
    
    div.response_doc {
        margin: 1.5em;
        border: 1px solid #aaa8a1;
        background-color: #efefef;
    }
    
    div.response_doc div.link {
        margin-left: 1em;
        line-height: 2em;
    }    
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="browse">
<h1> Browse: ${c.facet.capitalize()}
% if c.facet=="collection":
<span class="small_link"> ${h.link_to('Click here to view collection "%s"' % (c.item) , h.url(controller="/objects", id=c.item))} </span>
% endif
</h1>
<div class="subheading">showing only results that have "${c.item}" in the <em>${c.facet}</em> field: </div>
<div class="subheading"> ${h.link_to('Click here to browse full <em>%s</em> list' % (c.facet) , h.url(controller="/browse", action="field", field=c.facet))} </div>
</div>
<%include file="/minimal_search_response_display.mak"/>
