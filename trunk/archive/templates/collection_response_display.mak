<p>
% if c.numFound:
 Number of items in collection: <span class="highlight"> ${ c.numFound } </span> - 
% elif c.q:
 Sorry, but your query <em>${c.q}</em> resulted in no matches.</p>
% endif
% if c.docs:
 Showing results ${c.start+1} to 
% if (c.start+c.rows) > c.numFound:
${c.numFound}
% else:
${c.start+c.rows}
% endif
</p>
<div class="clear">&nbsp;</div>
% if c.permissible_offsets:
<div class="paginated_results">
%   for offset in c.permissible_offsets:
%   if not (offset=='...'):
.. <span class="pagination_label">
${h.link_to(offset or '0', h.url_for(start=offset))}</span> .. 
% else:
.. ${offset} ..
% endif
%   endfor
</div>
% endif
%   for doc_index in xrange(len(c.docs)):
<div class="response_doc">
<span class="document_number"><strong>${c.start+1+doc_index}</strong></span>
<dt class="label">${c.field_list['title']}</dt><dd class="value">${h.link_to(c.docs[doc_index].get('title', 'Link'), h.url_for(controller="/objects", id=c.docs[doc_index].get('id',None)))}</dd>
%     for field in [x for x in c.all_fields if x!='title']:
%       if field in c.docs[doc_index]:
<dt class="label">${c.field_list[field]}</dt><dd class="value">
%         if isinstance(c.docs[doc_index][field], list):
${ " ; ".join(c.docs[doc_index][field]) }
%         elif c.truncate and isinstance(c.truncate, int) and not isinstance(c.docs[doc_index][field],bool) and len(c.docs[doc_index][field]) > c.truncate:
${ c.docs[doc_index][field][:c.truncate] } ... [truncated at ${c.truncate} characters in length]
%         else:
${c.docs[doc_index][field]}
%         endif
</dt>
%       endif
%     endfor
</dl>
</div>
%   endfor
% if c.permissible_offsets:
<div class="paginated_results">
%   for offset in c.permissible_offsets:
%   if not (offset=='...'):
.. <span class="pagination_label">
${h.link_to(offset or '0', h.url_for(start=offset))}</span> .. 
% else:
.. ${offset} ..
% endif
%   endfor
</div>
% endif
% endif
