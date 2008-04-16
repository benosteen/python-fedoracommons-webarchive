# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> Repository: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> Repository: ${c.id}</title>
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
<p> Repository: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> Repository: ${c.id}</p>
% endif
<div>
% for text in c.inline_text:
<div id="${text}" class="text">${c.inline_text[text]}</div>
% endfor
</div>
<div id="metadata">
<%include file="/metadata/dc.mak"/>
% if c.metadata.get('REPOSITORY', None):
<div id="endpoints">
<p> Endpoints: </p>
<dl>
% for endpoint in c.metadata['REPOSITORY'].findall('endpoint'):
%   if endpoint.text:
<dt>${endpoint.get('type').capitalize()}</dt>
%   if endpoint.text.startswith('http://'):
<dd><a href="${endpoint.text}">${endpoint.text}</a></dd>
%   elif endpoint.text.startswith('uuid:') or endpoint.text.startswith('ora:'):
<dd><a href="${"%sobjects/%s" % (g.root, endpoint.text)}">${endpoint.text}</a></dd>
%   elif endpoint.text.startswith('urn:uuid:'):
<dd><a href="${"%sobjects/%s" % (g.root, endpoint.text[4:])}">${endpoint.text}</a></dd>
%   else:
<dd>${endpoint.text}</dd>
%   endif
%   endif
% endfor
</dl>
</div>
% endif
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
