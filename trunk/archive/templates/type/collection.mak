# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> ORA Collection: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> ORA Collection: ${c.id}</title>
% endif
</%def>
<%def name="page_style()">
    div#branding_container {
        float:right;
        width: auto;
        margin-left: 0em !important;
    }
    div#collection_metadata_with_branding {
        float: left;
        width: 25em;
        margin-right: 0em !important;
    }
    div#collection_metadata_without_branding {
        float: left;
        width: 65em;
        margin-right: 0em !important;
    }
</%def>
<div id="record_wrapper">
% if c.title:
<p> ORA Collection: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Collection: ${c.id}</p>
% endif
% if c.image_list:
<div id="branding_container">
%   if c.metadata.get('DC', None) and '{http://purl.org/dc/elements/1.1/}relation' in [e.tag for e in c.metadata['DC'].getchildren()]:
<a href="${c.metadata['DC'].find('{http://purl.org/dc/elements/1.1/}relation').text}">
%     for image in c.image_list:
<img class="branding" src="${h.url_for(controller="/objects", action="download", id=c.id, dsid=image['dsid'])}"/>
%     endfor
</a>
%   else:
%     for image in c.image_list:
<img class="branding" src="${h.url_for(controller="/objects", action="download", id=c.id, dsid=image['dsid'])}"/>
%     endfor
%   endif
</div>
<div id="collection_metadata_with_branding">
<%include file="/metadata/dc.mak"/>
<div id="trackback_link">Trackback URL: ${"%strackback/%s" % (g.root, c.id)}</div>
</div>
% else:
<div id="collection_metadata_without_branding">
<%include file="/metadata/dc.mak"/>
<div id="trackback_link">
<a href="${"%strackback/%s" % (g.root, c.id)}">Trackback URL</a>
</div>
</div>
% endif
<div class="clear">&nbsp;</div>
<div id="collection">
<%include file="/collection_response_display.mak"/>
<%include file="/relationship_display.mak"/>
<%include file="/trackback_display.mak"/>
</div>
<%include file="/type/terms.mak"/>
</div>
