% if c.trackbacks:
<div id="trackbacks">
<p><strong>Trackbacks</strong></p>
    <dl class="trackback">
% for trackback in c.trackbacks:
% if c.trackbacks[trackback].get("dc:title", None):
<dt>${c.trackbacks[trackback]["dc:title"][0]}</dt>
% endif
<dd>
% if c.trackbacks[trackback].get("dc:abstract", None):
<em>${c.trackbacks[trackback]["dc:abstract"][0]}</em> - 
% endif
% if c.trackbacks[trackback].get("dc:creator", None):
%   if c.trackbacks[trackback].get("dc:creator", None)[0].startswith('http://'):
<a href="${c.trackbacks[trackback]["dc:creator"][0]}">${c.trackbacks[trackback]["dc:creator"][0]}</a>
%   else:
${c.trackbacks[trackback]["dc:creator"][0]} 
%   endif
% endif
% for ident in c.trackbacks[trackback].get("dc:identifier", []):
%   if ident.startswith('http://'):
<a href="${ident}">${ident}</a>
%   elif ident.startswith('uuid:'):
 
%   else:
${ident}
%   endif
% endfor
% for ident in c.trackbacks[trackback].get("dc:identifier", []):
%   if ident.startswith('uuid:'):
- <span class="small_link"><a href="${"%sobjects/%s" % (g.root, ident)}"> (Archived information)</a></span>
%   endif
% endfor
<dd>
% endfor
</dl>
</div>
% endif
