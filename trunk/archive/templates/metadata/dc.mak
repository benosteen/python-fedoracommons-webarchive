# -*- coding: utf-8 -*-
% if c.metadata.get('DC', None):
<dl>
% for element in  c.metadata['DC'].getchildren():
%   if element.text:
<dt>${element.tag.split('}')[-1].capitalize()}</dt>
%   if element.text.startswith('http://'):
<dd><a href="${element.text}">${element.text}</a></dd>
%   elif element.text.startswith('uuid:') or element.text.startswith('ora:'):
<dd><a href="${"%sobjects/%s" % (g.root, element.text)}">${element.text}</a></dd>
%   elif element.text.startswith('urn:uuid:'):
<dd><a href="${"%sobjects/%s" % (g.root, element.text[4:])}">${element.text}</a></dd>
%   else:
<dd>${element.text}</dd>
%   endif
%   endif
% endfor
</dl>
% endif
