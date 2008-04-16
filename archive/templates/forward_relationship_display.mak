# -*- coding: utf-8 -*-
% if c.graph:
% for term in c.f_ontol:
%   for s,p,o in c.graph.triples((c.fedora_uri, c.f_ontol[term], None)):
%     if o.startswith('info:fedora/') and not o.startswith('info:fedora/type'):
%       if len(o.split('/'))==3:
<p> <span class="verbal_relationship">${term % ('<a href="%sresolve/%s">%s</a>)' % (g.root, o, o.split("/")[2]) )}</span></p>
%       else:
<p> <span class="verbal_relationship">${term % (h.link_to(g.f.ri.getDCTitle(o.split('/')[1]), h.url_for(controller="/objects", id=o.split('/')[1])))}</span></p>
%       endif
%     elif o.startswith('http://'):
<p> <span class="verbal_relationship">${term % ('<a href="%s">%s</a>' % (o,o))}</span></p>
%     else:
<p> <span class="verbal_relationship">${term % (o)}</span></p>
%     endif
%   endfor
% endfor
% endif
