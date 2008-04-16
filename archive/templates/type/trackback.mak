# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> Trackback: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> Trackback: ${c.id}</title>
% endif
</%def>
<%def name="page_style()">
</%def>
<div id="record_wrapper">
% if c.title:
<p> Trackback: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> Trackback: ${c.id}</p>
% endif
<div id="metadata">
<%include file="/metadata/dc.mak"/>
<div id="relationships">
<%include file="/relationship_display.mak"/>
</div>
</div>
<div id="right_column">
% if c.download_list:
<%include file="/type/downloads.mak"/>
% endif

<%include file="/type/terms.mak"/>
</div>
</div>
