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
% endif
% if c.sort_text:
<div class="subheading"> Sorting by '${c.sort_text}'</div>
% endif

<div class="paginated_results">
%  for offset in c.permissible_offsets:
%   if not (offset=='...'):
.. <span class="pagination_label">
${h.link_to(offset or '0', h.url_for(controller='browse', action="field", field=c.facet, item=c.item, start=offset))}</span> .. 
%  else:
.. ${offset} ..
%  endif
% endfor
</div>
<div class="response_doc">
%   for doc_index in xrange(len(c.docs)):
<div class="link"><span class="document_number">${c.start+1+doc_index}</span> - 
<a href="${h.url_for(controller="/objects", id=c.docs[doc_index].get('id',None))}">
% if 'person_name' in c.docs[doc_index]:
<span class="names">
%         if isinstance(c.docs[doc_index]['person_name'], list):
${ " ; ".join(c.docs[doc_index]['person_name']) }
%         else:
${c.docs[doc_index]['person_name']}
%         endif
</span>, 
%       endif
% if 'copyright_date' in c.docs[doc_index]:
(<span class="date">${c.docs[doc_index]['copyright_date']}</span>).
%       endif
% if 'title' in c.docs[doc_index]:
<span class="title">
%         if isinstance(c.docs[doc_index]['title'], list):
${ " ; ".join(c.docs[doc_index]['title']) }
%         else:
${c.docs[doc_index]['title']}
%         endif
</span>.
%       endif
% if 'host' in c.docs[doc_index]:
<span class="host"><em>
%         if isinstance(c.docs[doc_index]['host'], list):
${ " ; ".join(c.docs[doc_index]['host']) }
%         else:
${c.docs[doc_index]['host']}
%         endif
</em></span>,
% if 'volume' in c.docs[doc_index]:
<strong><span class="volume">${c.docs[doc_index]['volume']}</span></strong>
% endif
% if 'issue' in c.docs[doc_index]:
(<span class="issue">${c.docs[doc_index]['issue']}</span>),
% endif
% if 'pages' in c.docs[doc_index]:
 <span class="pages">${c.docs[doc_index]['pages']}</span>
% endif
% endif
% if 'thesis_type' in c.docs[doc_index]:
<span class="thesis_type">${c.docs[doc_index]['thesis_type']}</span>, 
% if 'thesis_awarding_body' in c.docs[doc_index]:
<span class="thesis_awarding_body">${c.docs[doc_index]['thesis_awarding_body']}</span>
% else:
<span class="thesis_awarding_body">University of Oxford</span>
% endif
% endif
</a>
</div>
% endfor
</div>
<div class="paginated_results">
%   for offset in c.permissible_offsets:
%   if not (offset=='...'):
.. <span class="pagination_label">
${h.link_to(offset or '0', h.url_for(controller='browse', action="field", field=c.facet, item=c.item, start=offset))}</span> .. 
% else:
.. ${offset} ..
% endif
%   endfor
</div>
