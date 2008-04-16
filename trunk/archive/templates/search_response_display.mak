<p>
% if c.numFound:
 Number of hits: <span class="highlight"> ${ c.numFound } </span> - 
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
% if c.search:
%  if c.hide_basic_search:
<div id="link_to_this_search">
${h.link_to('Link to these search results', h.url_for(controller='search', action="detailed", **dict([(key, c.search[key]) for key in c.search if key!='start'])))} - ${h.link_to('Atom <img src="/atom.png" border="0"/>', h.url_for(controller='search', action="detailed", format='atom', **dict([(key, c.search[key]) for key in c.search if key!='start'])))}
</div>
%  else:
<div id="link_to_this_search">
${h.link_to('Link to these search results', h.url_for(controller='search', action="basic", **dict([(key, c.search[key]) for key in c.search if key!='start'])))}
</div>
%  endif
% endif
<div class="clear">&nbsp;</div>
% if c.sort_text:
<div class="subheading"> Sorting by '${c.sort_text}'</div>
% endif
%  if c.hide_basic_search:
<div class="paginated_results">
%   for offset in c.permissible_offsets:
%   if not (offset=='...'):
.. <span class="pagination_label">
${h.link_to(offset or '0', h.url_for(controller='search', action="detailed", **dict([(key, c.search[key]) for key in c.search if key!='start'], start=offset)))}</span> .. 
% else:
.. ${offset} ..
% endif
%   endfor
</div>
% else:
<div class="paginated_results">
%   for offset in c.permissible_offsets:
%   if not (offset=='...'):
.. <span class="pagination_label">
${h.link_to(offset or '0', h.url_for(controller='search', action="basic", **dict([(key, c.search[key]) for key in c.search if key!='start'], start=offset)))}</span> .. 
% else:
.. ${offset} ..
% endif
%   endfor
</div>
% endif
%   for doc_index in xrange(len(c.docs)):
<div class="response_doc">
<span class="document_number">${c.start+1+doc_index}</span>
<dl>
<dt class="label">${c.field_names['title']}</dt><dd class="value">${h.link_to(c.docs[doc_index].get('title', 'Link'), h.url_for(controller="/objects", id=c.docs[doc_index].get('id',None)))}</dd>
%     for field in [x for x in c.all_fields if x!='title']:
%       if field in c.docs[doc_index]:
<dt class="label">${c.field_names[field]}</dt><dd class="value">
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
%  if c.hide_basic_search:
<div class="paginated_results">
%   for offset in c.permissible_offsets:
%   if not (offset=='...'):
.. <span class="pagination_label">
${h.link_to(offset or '0', h.url_for(controller='search', action="detailed", **dict([(key, c.search[key]) for key in c.search if key!='start'], start=offset)))}</span> .. 
% else:
.. ${offset} ..
% endif
%   endfor
</div>
% else:
<div class="paginated_results">
%   for offset in c.permissible_offsets:
%   if not (offset=='...'):
.. <span class="pagination_label">
${h.link_to(offset or '0', h.url_for(controller='search', action="basic", **dict([(key, c.search[key]) for key in c.search if key!='start'], start=offset)))}</span> .. 
% else:
.. ${offset} ..
% endif
%   endfor
</div>
% endif
% endif
