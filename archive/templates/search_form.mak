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
        background: transparent;
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
    
    #search_box p, #facets p {
        font-size: 1.3em;
    }
    
    p#search_term_block {
        margin: 1em;
        margin-left: 16em;
        font-size: 1.5em;
    }
    
    p#search_term_block span input {
        width: 10em;
    }
    
    div.response_doc {
        margin: 0.4em;
        border: 1px solid #aaa8a1;
        background-color: #efefef;
    }
    span.toggle {
        padding: 0.1em;
        margin: 0.1em;
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
        border: 1px solid #aaa8a1;
    }
    
    div.clear {
        clear: both;
    }
    
    div.facets {
        padding: 0.3em;
        border: 1px solid #cdcdcd;
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
    
    .facet_results {
        float: left;
        width: 14em;
        padding-bottom: 1em;
    }
    
    .facet_results ul li {
        list-style: none;
    }
    
    span.pagination_label form, span.label form {
        display:inline;
        cursor: pointer;
    }
    
    span.pagination_label form button, span.pagination_label form input {
        border: 0px;
        color: #3355ee;
        cursor: pointer;
    }
    
    p.no_facets {
        color: #aaaaaa;
        font-style: italic;
        width: 10em;
    }
    div#facet_container {
        width: 15em;
        float: left;
    }
    div#results {
        width: 54em;
        float: right;
    }
    div#results_wrapper, div#search_box_wrapper {
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
        /* !important Because IE doesn't want to listen...  */
        border: 0px !important;
    }
    
    span.small_label {
        font-size: 0.7em;
    }
    
  </style>
% if c.search:
  <link rel="alternate" type="application/atom+xml"
href="${h.url_for(controller='search', action="detailed", format='atom', **dict([(key, c.search[key]) for key in c.search if key!='start']))}" title="ORA Search results for \"${c.search.get('q',None)}\""/>
% endif

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
<div id="search_box_wrapper">
${h.form(h.url(controller="search", action="detailed"), method='post')}
<div id="search_wrapper">
<p id="search_term_block"><span class='label'>${ h.text_field('q', value=c.q)}</span> ${h.submit('Search')}
%   if c.fulltext:
<span class="small_label"> Search inside full-text items </span> <input type="checkbox" class="checkbox" name="fulltext" checked="True"/> </span>
%   else:
<span class="small_label"> Search inside full-text items </span> <input type="checkbox" class="checkbox" name="fulltext"/> </span>
%   endif
</p>
<div id="search_box">
<p><span class='label'>Return in sets of 
<select id="rows" name="rows">
% for row in [5,10,25,50]:
%  if row==c.rows:
<option value="${row}" selected="True">${row}</option>
%  else:
<option value="${row}">${row}</option>
%  endif
% endfor
</select> hits.</span></p>
<p><span class='label'>Level of detail to return?</span></p>
<select id="view" name="view">
% for view in c.views:
%  if view==c.view:
<option value="${view}" selected="True">${view}</option>
%  else:
<option value="${view}">${view}</option>
%  endif
% endfor
</select>
<p><span class='label'>Sort by: </span>
<select id="sort" name="sort">
% for sort in c.sort_options:
%  if sort==c.sort:
<option value="${sort}" selected="True">${c.sort_options[sort]}</option>
%  else:
<option value="${sort}">${c.sort_options[sort]}</option>
%  endif
% endfor
</select></p>
${ h.hidden_field('truncate', value=c.truncate)}
</div>
<div id="facets">
<p>Show groupings by: </p>
<div class="facets">
<div class="container">
% for field in c.facetable_fields:
%   if field in c.fields_to_facet:
<span class="toggle"><span class="toggle_label">${ c.field_names[field] } </span> <input type="checkbox" class="checkbox" name="facet${field}" checked="True"/> </span>
%   else:
<span class="toggle"><span class="toggle_label">${ c.field_names[field] } </span> <input type="checkbox" class="checkbox" name="facet${field}"/> </span>
%   endif
% endfor
</div>
<div class="clear">&nbsp;</div>
</div>
</div>
</div>
<div class="clear">&nbsp;</div>
${h.end_form()}
</div>
<hr/>
<div id="results_wrapper">
<div id="results" 
% if not c.returned_facets: 
 style="width:70em;" 
% endif
>
<%include file="/search_response_display.mak"/>
</div>
% if c.returned_facets:
<div id="facet_container">
%   for facet in c.returned_facets:
%     if facet in c.chosen_facets:
<div class="facet_results">
<div class="subheading">${c.field_names[facet]}</div>
<p>${c.field_names[facet]} : "${ c.chosen_facets[facet] }"
<span class="pagination_label">${h.form(h.url(controller="search", action="detailed"), method='post')}
${ h.hidden_field('q', value=c.q)}
${ h.hidden_field('rows', value=c.rows)}
${ h.hidden_field('truncate', value=c.truncate)}
%     for facet_field in c.fields_to_facet:
<input type="hidden" name="facet${facet_field}" value="true"/>
%     endfor
%     for chosen_field in c.chosen_fields:
<input type="hidden" name="${chosen_field}" value="true"/>
%     endfor
%     for chosen_facet in c.chosen_facets:
%       if isinstance(c.chosen_facets[chosen_facet], list):
%         for item in c.chosen_facets[chosen_facet]:
%           if not (facet==chosen_facet):
<input type="hidden" name="filter${facet}" value="${item}"/>
%           endif
%         endfor
%       else:
%         if not (facet==chosen_facet):
<input type="hidden" name="filter${chosen_facet}" value="${c.chosen_facets[chosen_facet]}"/>
%         endif
%       endif
%     endfor
${h.submit("Remove")}${h.end_form()}</span></p>
</div>
%     else:
% if c.returned_facets[facet]:
<div class="facet_results">
<div class="subheading">${c.field_names[facet]}</div>
<ul>
%     for result,value in c.returned_facets[facet]:
<li><span class="label">
<a href="${c.add_facet % (facet, result)}">${" ".join(result.split('-'))}</a>
</span>: <span class="value">${value}</span></li>
%     endfor
</ul>
</div>
% else:
<div class="facet_results">
<div class="subheading">${facet}</div>
<p class="no_facets"> There are no groupings of this field in your search results. </p>
</div>
% endif
% endif
% endfor
</div>
% endif
</div>
