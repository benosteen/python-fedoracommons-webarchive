# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />

<%def name="head_tags()">
  <title> Advanced Search - Functionality Demo</title>
  <style>    
    #q {
        width: 8em;
    }
        
    div#search_wrapper {
        width: 100%;
        min-width: 740px;
        margin: 0 auto;
    }
    
    div.link {
        float: right;
        margin-top:1em;
        margin-right: 0.3em;
    }
    div.link a {
        padding: 0.1em;
        border: 1px solid #5599dd;

    }
    dt.label {
        font-weight: bold;
        color: #3399ee;
        padding-left:3.5em;
    }
    dd.value {
        font-weight: normal;
        color: #565656;
    }
    li.title span {
        font-size: +1;
    }
    
    
    #facets {
        float: left;
        width: 45em;
        margin-left: 1em;
    }
    
    
    #search_box {
        float: left;
        width: 20em;
        margin-left: 1em;
    }
    
    div.response_doc {
        margin: 0.4em;
        border: 1px solid #aaa8a1;
        background-color: #efefef;
    }
    span.toggle {
        padding: 0.1em;
        margin: 0.1em;
        background-color: #ffffff;
        border: 1px solid #5599dd;
        float: left;
        width: 14em;
    }
    span.toggle_label {
        float: right;
        margin-right: 0.3em;
        margin-top: 0.2em;
    }
    
    span.toggle input {
        float: left;
        margin-right: 0.5em;
        color: #000000; 
        border: 1px #7799aa solid;
    }
    
    div.clear {
        clear: both;
    }
    
    div.facets {
        padding: 0.3em;
        border: 1px solid #aaa8a1;
        background-color: #efefef;
        max-width: 62em;
    }
    
    div#fields {
        float: right;
    }
    
    #rows {
        width: 3em;
    }
    
    #view {
        width: 6em;
    }
    

    #search_box p, #facets p {
        font-size: 1.5em;
    }
    
    .facet_results {
        float: left;
        width: 14em;
        padding-bottom: 1em;
    }
    
    .facet_results ul li {
        list-decoration: none;
    }
    
    span.pagination_label form, span.label form {
        display:inline;
        cursor: pointer;
    }
    
    span.pagination_label form button, span.pagination_label form input {
        border: 0px;
        background-color: #fff;
        color: #3355ee;
        cursor: pointer;
    }
    
    p.no_facets {
        color: #aaaaaa;
        font-style: italic;
        width: 10em;
    }
    div#facet_container {
        background-color: #fff;
        width: 15em;
        float: left;
    }
    div#results {
        background-color: #fff;
        width: 54em;
        float: right;
    }
    div#results_wrapper, div#search_box_wrapper {
        background-color:#fff;
        width: 70em;
        margin: 0 auto;
        
    }
    span.document_number {
        float: left;
        padding: 0.2em;
        margin: 0.2em;
        border:1px solid #999;
        font-weight: bold;
    }
    
    .checkbox {
        // !important Because IE doesn't want to listen...
        border: 0px !important;
    }
    
  </style>
  <script type="text/javascript">
<!--
function switchMenu(obj) {
	var el = document.getElementById(obj);
	if ( el.style.display != "none" ) {
		el.style.display = 'none';
	}
	else {
		el.style.display = '';
	}
}
//-->
</script>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="results_wrapper">
<div id="results" style="width:70em;">
<p>Search results from query: <em>${c.q}</em> </p>
<%include file="/search_response_display.mak"/>
</div>
</div>
