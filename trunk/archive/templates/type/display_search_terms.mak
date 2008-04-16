<dl>
%     for field in c.all_fields:
%       if field in c.search_terms:
<dt class="label">${c.field_list[field]}</dt><dd class="value">
%         if isinstance(c.search_terms[field], list):
${ " ; ".join(c.search_terms[field]) }
%         elif c.truncate and isinstance(c.truncate, int) and not isinstance(c.search_terms[field],bool) and len(c.search_terms[field]) > c.truncate:
${ c.search_terms[field][:c.truncate] } ... [truncated at ${c.truncate} characters in length]
%         else:
${c.search_terms[field]}
%         endif
</dt>
%       endif
%     endfor
</dl>
