# -*- coding: utf-8 -*-
<%inherit file="/type/default.mak" />
<%def name="title_text()">
% if c.title:
<title> ORA Book: "${c.title}" - ${c.id}</title>
% elif c.id:
<title> ORA Book: ${c.id}</title>
% endif
</%def>
<%def name="page_style()">
    img.inline_image {
        max-width:60em;
        height: auto;
    }
</%def>
<div id="record_wrapper">
% if c.title:
<p> ORA Book: <strong>"${c.title}"</strong></p>
% elif c.id:
<p> ORA Book: ${c.id}</p>
% endif
<div>
% for relation in c.relations:
%  if relation == 'isPartOf':
%   if [x for x in c.relations[relation] if x[2]=='type:imagecollection']:
<div class="subheading">Section List</div>
${h.form(h.url(controller="/objects"), method='get')}
    <select name="id">
%    for item in [x for x in c.relations[relation] if x[2]=='type:imagecollection']:
      <option value="${item[0]}">${item[1]}</option>
%    endfor
    </select>
    ${h.submit('Go')}
    ${h.end_form()}
%  elif [x for x in c.relations[relation] if x[2]=='type:image']:
<div class="subheading">Page List</div>
${h.form(h.url(controller="/objects", id=c.id), method='post')}
    <select name="inline">
%    for item in [x for x in c.relations[relation] if x[2]=='type:image']:
      <option value="${item[0]}"
% if c.inline_object and c.inline_object==item[0]:
 selected='true' 
% endif
      >${item[1]}</option>
%    endfor
    </select>
    ${h.submit('Go')}
    ${h.end_form()}
%   endif
%  endif
% endfor
</div>
% if c.inline_object:
<div id="image_container">
<a href="${h.url_for(controller="/objects", id=c.inline_object)}">
<img class="inline_image" src="${h.url_for(controller="/objects", action="download", id=c.inline_object, dsid=c.model['inline_images'])}"/>
</a>
</div>
% endif
<div class="clear">&nbsp;</div>
<div id="metadata">
<%include file="/type/display_search_terms.mak"/>
<div id="trackback_link">Trackback URL: ${"%strackback/%s" % (g.root, c.id)}</div>
<div id="relationships">
<%include file="/forward_relationship_display.mak"/>
<%include file="/object_relationship_navigation.mak"/>
<%include file="/trackback_display.mak"/>
</div>
</div>
<div id="right_column">
% if c.download_list:
<%include file="/type/downloads.mak"/>
% endif
<%include file="/type/terms.mak"/>
</div>
</div>
