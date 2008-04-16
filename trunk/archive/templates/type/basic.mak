# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> ORA Basic Item: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> ORA Basic Item: ${c.id}</title>
% endif
</%def>
<%def name="page_style()">
</%def>
<div id="record_wrapper">
% if c.title:
<p> ORA Basic Item: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Basic Item: ${c.id}</p>
% endif
<div>
<%include file="/type/citation.mak"/>
<%include file="/metadata/dc.mak"/>
<div id="trackback_link">Trackback URL: ${"%strackback/%s" % (g.root, c.id)}</div>
<div id="relationships">
<%include file="/relationship_display.mak"/>
<%include file="/trackback_display.mak"/>
% if c.download_list:
<%include file="/type/downloads.mak"/>
% endif
<%include file="/type/terms.mak"/>
</div>
</div>
</div>
