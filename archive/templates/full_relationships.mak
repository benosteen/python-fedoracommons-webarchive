# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Relationships for ${c.id}</title>
  <style>
    div#relationships {
       margin: 1em 2em;
       float:left;
       background: transparent;
    }
    div#relationships_navigation {
       margin: 1em 2em;
       float:right;
       background: transparent;
       border: 1px solid #888;
    }
    div#relationships_navigation ul li {
        list-style: none;
        display: inline;
    }
    
    span.object_title {
        color: #2288dd;
    }
    
    span.uuid {
        color: #999 !important;
        font-style: italic !important;
        font-size: 0.8em !important;
    }
    div#all_relationships {
        font-size: 0.8em;
    }
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="relationships_wrapper">
<div id="relationships">
<%include file="/relationship_display.mak"/>
<div id="all_relationships">
<div class="subheading"> All relationships for ${c.title}</div>
<ul>
%   for s,p,o in c.graph.triples((None, None, None)):
<li>
%     if s.startswith('info:fedora/uuid') or s.startswith('info:fedora/ora'):
%       if len(s.split('/'))==3:
<a href="${"%sresolve/%s" % (g.root, s)}">${"%s" % s.split('/')[2]}</a>
%       else:
${h.link_to(g.f.ri.getDCTitle(s.split('/')[1]), h.url_for(controller="/objects", id=s.split('/')[1]))}
%       endif
%     elif s.startswith('http://'):
<a href="${s}">${s}</a>
%     else:
${s}
%     endif
% if p.startswith('http://'):
<a href="${p}">${p}</a>
% else:
${p}
% endif
%     if o.startswith('info:fedora/uuid') or o.startswith('info:fedora/ora'):
%       if len(o.split('/'))==3:
<a href="${"%sresolve/%s" % (g.root, o)}">${"%s" % o.split('/')[2]}</a>
%       else:
${h.link_to(g.f.ri.getDCTitle(o.split('/')[1]), h.url_for(controller="/objects", id=o.split('/')[1]))}
%       endif
%     elif o.startswith('http://'):
<a href="${o}">${o}</a>
%     else:
${o}
%     endif
</li>
%   endfor
</ul>
</div>
</div>
</div>
