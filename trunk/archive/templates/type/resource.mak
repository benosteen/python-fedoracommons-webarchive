# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> ORA Archived Resource: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> ORA Archived Resource: ${c.id}</title>
% endif
</%def>
<%def name="page_style()">
    div.text {
        border: 0px !important;
        margin: 0em !important;
    }
</%def>
<div id="record_wrapper">
% if c.title:
<p> ORA Archived Resource: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Archived Resource: ${c.id}</p>
% endif
<div>
% for text in c.inline_text:
<div id="${text}" class="text">${c.inline_text[text]}</div>
% endfor
</div>
<div id="metadata">
<%include file="/metadata/dc.mak"/>
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
