# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> ORA Thesis: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> ORA Thesis: ${c.id}</title>
% endif
</%def>
<%def name="page_style()">
</%def>
<div id="record_wrapper">
% if c.title:
<p> ORA Thesis: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Thesis: ${c.id}</p>
% endif
${self.record_information()}
</div>
