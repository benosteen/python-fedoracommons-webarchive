# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Relationships for ${c.id}</title>
  <style>
    div#relationships {
       margin: 1em 2em;
       float:left;
       background: transparent;
    }
    div#relationships_navigation {
       margin: 1em 2em;
       float:right;
       background: transparent;
       border: 1px solid #888;
    }
    div#relationships_navigation ul li {
        list-style: none;
        display: inline;
    }
    
    span.object_title {
        color: #2288dd;
    }
    
    span.uuid {
        color: #999 !important;
        font-style: italic !important;
        font-size: 0.8em !important;
    }
    
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="relationships_wrapper">
<div id="relationships">
<%include file="/relationship_display.mak"/>
</div>
</div>
