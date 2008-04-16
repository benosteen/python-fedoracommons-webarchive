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
    div#image_container {
        width: 90%;
        float: left;
    }
    img.inline_image {
        max-width:60em;
        height: auto;
    }
</%def>
<div id="record_wrapper">
% if c.title:
<p> ORA Image: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Image: ${c.id}</p>
% endif
<div id="image_container">
% for image in c.image_list:
<a href="${h.url_for(controller="/objects", action="download", id=c.id, dsid=image['dsid'])}">
<img class="inline_image" src="${h.url_for(controller="/objects", action="download", id=c.id, dsid=image['dsid'])}"/>
</a>
% endfor
</div>
<div id="metadata">
<%include file="/metadata/dc.mak"/>
<div id="trackback_link">Trackback URL: ${"%strackback/%s" % (g.root, c.id)}</div>
<%include file="/relationship_display.mak"/>
<%include file="/trackback_display.mak"/>
</div>
<div id="right_column">
% if c.download_list:
<%include file="/type/downloads.mak"/>
% endif
<%include file="/type/terms.mak"/>
</div>
</div>
