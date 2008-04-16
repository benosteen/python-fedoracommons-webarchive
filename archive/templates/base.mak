# -*- coding: utf-8 -*-
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en-gb">
  <head>
     <link rel="search"
           type="application/opensearchdescription+xml" 
           href="search/opensearch"
           title="ORA Search" />
     <link rel="unapi-server" type="application/xml" title="unAPI" href="http://archive.sers.ox.ac.uk:5000/unapi/" />
% if c.resource_map_url:
     <link href="${c.resource_map_url}" type="application/rdf+xml" rel="resourcemap" />
% endif
% if c.id:
     <abbr class="unapi-id" title="${c.id}"></abbr>
     <link rel="pingback" href="${"%spingback" % g.root}"/>
% endif
     <style>

     body {
        font-family: Helvetica, sans-serif;
        font-size: 76%;
        padding: 0em;
        background: #e7e5d8;
    }
    
    h1 {
        font-size: 1.3em;
    }
    
    a img {
        border: 0;
    }
    
    .highlight {
        color: red;
    }
    
    input, .checkbox {
        border: 1px solid #5599dd;
    }
    
    input:focus {
        background: #ffc;
    }
    
    ul {
        margin: 0.1em;
        padding: 0.1em;
    }
    
    ul li {
        list-style: none;
    }
    
    div.clear {
        clear: both;
        border: 0px !important;
        background: transparent !important;
        margin: 0em !important;
        padding: 0em !important;
    }
    
    span.small_link {
        font-size: 0.8em;
    }
    
    a {
        color: blue;
        cursor: pointer;
    }
    
    #oxford_logo {
        /* float: right; */
    }
    #eprints_logo {
        /* float: right; */
    }
    
    div#page_container {
        width: 72em;
        margin: 0 auto;
        border: 1px solid #aaa8a1;
        padding: 0.1em;
        background: #fff url('/backing.png') repeat-x top;
    }
    
    div#link_to_this_search {
        float: right;
    }
    
    #header {
        background: #111 url('/header.jpg') no-repeat top left;
        height: 9em;
        min-height: 100px;
        /* border-bottom: 1px solid #aaa8a1; */
    }
    
    .footer_img {
        height: 38px;
        width: auto;
    }
    
    #footer {
    
    }
    
    #footer ul li {
        font-size: 0.8em;
        display: inline;
        padding: 0em 0.5em;
    }
    
    #footer ul li.leftborder {
        border-left:1px solid #CCCCCC;
    }
    
    p#inline_search {
        margin-left: 45em;
        float: left;
        margin-top: 1em;
    }
    
    p#inline_search span input {
        width: 10em;
    }
    
    p#inline_search a {
        color: #fff !important;
        text-decoration: none;
    }
    
    ul#header_navigation {
        float:right;
        line-height: 1.9em;
        padding: 0.3em 1em;
        background: #444;
    }
    
    ul#header_navigation a {   
        text-decoration: none;
        color: white !important;
        cursor: pointer;
    }
    
    div#copyright_statement {
        float: right;
        width: 37em;
        color: #999;
    }
    div#copyright_statement p {
        font-size: 0.8em;
    }
    dl {
        line-height: 1.7em;
        width: 90%;
    }
    dt {
        font-weight: bold;
        font-size: 1.2em;
        color: #3399ee;
    }
    dd {
        font-weight: normal;
        color: #565656;
    }
    
    div#response_message {
        width: 95%;
        background-color: #888;
        font-weight: bold;
        color: #fff;
        margin: 0 auto;
    }
    
    div#response_message span {
        margin: 0.3em 1em;
    }
    div#termsofuse {
        font-size: 0.8em;
        padding: 1em;
    }
    div.subheading {
        font-size: 1.2em;
        font-weight: bold;
        border: 0px !important;
    }
    
    span.small_link {
        font-size: 0.7em;
    }    
    </style>
    ${self.head_tags()}
  </head>
  <body>
    <div id="page_container">
    <div id="header">
    <ul id="header_navigation">
	<li>${h.link_to('Browse', h.url_for(controller="/browse", action="index"))}</li>
	<li>${h.link_to('Tools', h.url_for(controller="/information", action="urls"))}</li>
    </ul>
% if not c.hide_basic_search:
    ${h.form(h.url(controller="/search", action="basic"), method='post')}
    <p id='inline_search'><span class='label'>${ h.text_field('q', value=c.q)}</span> ${h.submit('Search')} ${h.link_to('Detailed Search', h.url_for(controller="/search", action="index"))}</p>
    ${ h.hidden_field('rows', value=c.rows)}
    ${ h.hidden_field('truncate', value=c.truncate)}
    ${ h.hidden_field('view', value="Default")}
    ${h.end_form()}
% endif
    ${self.header()}
    </div>
    <div id="page_content">
% if c.message:
<div id="response_message"><span>${c.message}</span></div>
% endif
    ${self.body()}
    <div class="clear">&nbsp;</div>
    </div>
    <div id="footer">
    <ul id="footer_list">
	<li>${h.link_to('Disclaimer and Data Protection statement', h.url_for(controller="/information", action="disclaimer"))}</li>
	<li class="leftborder">${h.link_to('Accessibility statement', h.url_for(controller="/information", action="accessibility"))}</li>
    </ul>
    ${self.footer()}
    <div id="copyright_statement"><p>Site powered by <strong>Fedora</strong> and Apache Solr. Data source and information management system is powered by <strong>EPrints.org</strong>.</p></div>
    
    <a href="http://www.ox.ac.uk">
    <img class="footer_img" src="/logo_oxford.jpg" alt="Oxford University Logo"/>
    </a>
    <a href="http://eprints.org">
    <img class="footer_img" src="/eprints.gif" alt="EPrints"/>
    </a>
    <a href="http://www.fedora-commons.org">
    <img class="footer_img" src="/fedora.png" alt="Fedora Commons" />
    </a>
    </div>
    </div>
  </body>
</html>

