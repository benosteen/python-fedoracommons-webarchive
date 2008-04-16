# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
% if c.id:
<!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:dc="http://purl.org/dc/elements/1.1/"
             xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/">
    <rdf:Description
        rdf:about="${"info:fedora/%s" % c.id}"
        dc:identifier="${"%sobjects/%s" % (g.root, c.id)}"
        dc:title="${c.title}"
        trackback:ping=${"%strackback/%s" % (g.root, c.id)} />
    </rdf:RDF>
-->
% endif
  ${self.title_text()}
  <style>
    div#record_wrapper {
      margin: 1em 2em;
      width: 95%
    }
    div#record_wrapper div {
      margin: 0.8em;
      border: 1px solid #cdcdcd;
      background-color: #efefef;
      padding: 0.8em;
    }
    div#record_wrapper div ul li {
        line-height: 1.5em;
    }
    div#relationships_navigation {
       margin: 0.5em auto !important;
       background: transparent;
       border: 1px solid #888;
    }
    div#relationships_navigation ul li {
        list-style: none;
        display: inline;
    }
    div#metadata{
        float: left;
        width: 49em;
        padding: 0.5em 1em;
    }
    div.citation {
        float: left;
        border: 0px !important;
        margin: 1em 0.3em !important;
        background: transparent !important;
    }
    div.citation dl {
        margin-left: 2em;
    }
    div#right_column {
        margin: 0em !important;
        padding: 0em !important;
        float: right;
        width: 15em;
        border: 0px !important;
        background: transparent !important;
    }
    div#right_column div {
        width: 14em;
        float: right;
        font-size: 0.9em;
        padding: 0.1em 0.8em !important;
        background: #dedede;
    }
    div.link {
        float: right;
        margin-top:1em;
        margin-right: 0.3em;
    }
    div#mods {
        margin: 0em !important;
        border: 0px !important;
        background: transparent !important;
        padding: 0em !important;
    }
    
    div#mods div {
        margin: 0em !important;
        border: 0px !important;
        background: transparent !important;
        padding: 0em !important;
    }
    div#mods dl {
        font-size: 0.8em;
    }
    div#mods .affiliations {
        width: 25em;
        float: right;
    }
    div#mods .mods_name_left {
        float: left;
        width: 14em;
    }
    div.clear {
        clear: both;
        height: 0px;
        border: 0px !important;
        background: transparent !important;
        margin: 0em !important;
        padding: 0em !important;
    }
    
    dl.trackback {
        font-size: 0.85em;
    }
    div#trackback_link {
        text-align: right;
        border: 0px !important;
    }
  ${self.page_style()}
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<%def name="record_information()">
<div id="metadata">
<%include file="/type/citation.mak"/>
<%include file="/type/display_search_terms.mak"/>
<div id="trackback_link">Trackback URL: ${"%strackback/%s" % (g.root, c.id)}</div>
<div id="relationships">
<%include file="/relationship_display.mak"/>
<%include file="/trackback_display.mak"/>
</div>
</div>
<div id="right_column">
<%include file="/type/terms.mak"/>
% if c.download_list:
<%include file="/type/downloads.mak"/>
% endif
</div>
</%def>
