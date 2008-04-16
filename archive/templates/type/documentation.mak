# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> ORA Documentation: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> ORA Documentation: ${c.id}</title>
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
<p> ORA Documentation: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Documentation: ${c.id}</p>
% endif
<div>
% for text in c.inline_text:
<div id="${text}" class="text">${c.inline_text[text]}</div>
% endfor
</div>
${self.record_information()}
</div>
