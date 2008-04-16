<div class="citation">
<dl>
<dt>Citation: </dt>
<dd>
% if 'person_name' in c.search_terms:
<span class="names">
%         if isinstance(c.search_terms['person_name'], list):
${ " ; ".join(c.search_terms['person_name']) }
%         else:
${c.search_terms['person_name']}
%         endif
</span>, 
% elif 'creator' in c.search_terms:
<span class="names">
%         if isinstance(c.search_terms['creator'], list):
${ " ; ".join(c.search_terms['creator']) }
%         else:
${c.search_terms['creator']}
%         endif
</span>, 
% endif
% if 'copyright_date' in c.search_terms:
(<span class="date">${c.search_terms['copyright_date']}</span>).
% elif 'creation_date' in c.search_terms:
(<span class="date">${c.search_terms['creation_date']}</span>).
% elif 'date' in c.search_terms:
(<span class="date">
%         if isinstance(c.search_terms['date'], list):
${ " ".join(c.search_terms['date']) }
%         else:
${c.search_terms['date']}
%         endif
</span>).
% endif
% if 'title' in c.search_terms:
<span class="title">
%         if isinstance(c.search_terms['title'], list):
${ " ; ".join(c.search_terms['title']) }
%         else:
${c.search_terms['title']}
%         endif
</span>.
%       endif
% if 'host' in c.search_terms:
<span class="host"><em>
%         if isinstance(c.search_terms['host'], list):
${ " ; ".join(c.search_terms['host']) }
%         else:
${c.search_terms['host']}
%         endif
</em></span>,
% if 'volume' in c.search_terms:
<strong><span class="volume">${c.search_terms['volume']}</span></strong>
% endif
% if 'issue' in c.search_terms:
(<span class="issue">${c.search_terms['issue']}</span>),
% endif
% if 'pages' in c.search_terms:
 <span class="pages">${c.search_terms['pages']}</span>
% endif
% endif
% if 'thesis_type' in c.search_terms:
<span class="thesis_type">${c.search_terms['thesis_type']}</span>, 
% if 'thesis_awarding_body' in c.search_terms:
<span class="thesis_awarding_body">${c.search_terms['thesis_awarding_body']}</span>
% else:
<span class="thesis_awarding_body">University of Oxford</span>
% endif
% endif
 <span class="small_link">${h.link_to( "%sobjects/%s" % (g.root, c.id), h.url_for(controller="/objects", id=c.id ))}</span>
</dd>
</dl>
</div>
<div class="clear">&nbsp;</div>
