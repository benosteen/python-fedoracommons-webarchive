# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> ORA Conference: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> ORA Conference: ${c.id}</title>
% endif
</%def>
<%def name="page_style()">
    div#conferenceitems ul {
        margin-left: 2em;
    }
    
    div#conferenceitems ul li {    
        padding-bottom: 0.5em;
    }
</%def>
<div id="record_wrapper">
% if c.title:
<p> ORA Conference: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Conference: ${c.id}</p>
% endif
<div id="metadata">
<%include file="/type/citation.mak"/>
<%include file="/type/display_search_terms.mak"/>
<div id="trackback_link">Trackback URL: ${"%strackback/%s" % (g.root, c.id)}</div>
% if c.graph:
<div id="conferenceitems">
<div class="subheading">Conference/Workshop Papers:</div>
<ul>
%   for s,p,o in c.graph.triples((None, c.rel['isPartOf'], c.fedora_uri)):
<li>${h.link_to(g.f.ri.getDCTitle(s.split('/')[1]), h.url_for(controller="/objects", id=s.split('/')[1]))}</li>
%   endfor
</ul>
% endif
</div>

<div id="relationships">
<%include file="/forward_relationship_display.mak"/>
<%include file="/object_relationship_navigation.mak"/>
<%include file="/trackback_display.mak"/>
</div>
</div>
<div id="right_column">
<%include file="/type/terms.mak"/>
% if c.download_list:
<%include file="/type/downloads.mak"/>
% endif
</div>
</div>
