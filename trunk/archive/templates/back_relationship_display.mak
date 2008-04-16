# -*- coding: utf-8 -*-
% if c.graph:
% for term in c.b_ontol:
%   for s,p,o in c.graph.triples((None, c.b_ontol[term], c.fedora_uri)):
<p> <span class="verbal_relationship">${term % (h.link_to(g.f.ri.getDCTitle(s.split('/')[1]), h.url_for(controller="/objects", id=s.split('/')[1])))}</span></p>
%   endfor
% endfor
% endif
