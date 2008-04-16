# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> ORA Journal Article: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> ORA Journal Article: ${c.id}</title>
% endif
</%def>
<%def name="page_style()">
</%def>
<div id="record_wrapper">
% if c.title:
<p> ORA Journal Article: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Journal Article: ${c.id}</p>
% endif
<div id="metadata">
<%include file="/type/citation.mak"/>
<%include file="/metadata/mods.mak"/>
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
</div>
