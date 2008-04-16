# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> ORA - Oxford University Research Archive - List of datastreams for ${c.id}</title>
  <style>
    div#object_wrapper {
      margin: 1em 2em;
    }
    div#object_wrapper div {
      margin: 1em 2em;
    }
    div#dsid_list {
      border: 1px solid #cdcdcd;
      background-color: #efefef;
    }
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="object_wrapper">
<div id="object_details">

</div>
<div id="downloads">
<ul>
% for dsid in c.datastream_list:
% if dsid not in ['MODS','DC','MARC21','REDIF','RELS-EXT','FULLTEXT', 'DROID', 'EVENT']:
%   if c.datastream_list[dsid].get('label', None):
<li>${h.link_to('"%s" - %s' % (c.datastream_list[dsid]['label'], c.datastream_list[dsid]['winname']) , h.url_for(controller='/objects', action='download', id=c.id, dsid=dsid))}</li>
%   endif
% endif
% endfor
</ul>
</div>
</div>
