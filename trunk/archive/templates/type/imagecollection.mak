# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> ORA Image: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> ORA Documentation: ${c.id}</title>
% endif
</%def>
<%def name="page_style()">
    div.thumbnail {
        width: auto;
        float: left;
        margin: 0.2em !important;
    }
</%def>
<div id="record_wrapper">
% if c.title:
<p> ORA Image Collection: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Image Collection: ${c.id}</p>
% endif
<div id="metadata">
<%include file="/type/citation.mak"/>
<%include file="/metadata/dc.mak"/>
<div id="trackback_link">Trackback URL: ${"%strackback/%s" % (g.root, c.id)}</div>
<div id="relationships">
<%include file="/relationship_display.mak"/>
<%include file="/trackback_display.mak"/>
</div>
% for image_list in c.relations:
% if image_list == 'isPartOf':
% for item in c.relations[image_list]:
<div class="thumbnail">
<a href="${h.url_for(controller="/objects", id=item[0])}">
<img id="${item[0]}" src="${h.url_for(controller="/objects", action="download", id=item[0], dsid=c.model['inline_images'])}"/>
</a>
<label for="${item[0]}">${item[1]}</label>
</div>
% endfor
% endif
% endfor
</div>
<div id="right_column">
% if c.download_list:
<%include file="/type/downloads.mak"/>
% endif
<%include file="/type/terms.mak"/>
</div>
</div>
