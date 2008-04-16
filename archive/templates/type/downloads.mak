<div id="download_list">
<div class="subheading"> Downloads </div>
% for dsid_props in c.download_list:
<p>${h.link_to( "%s" % (dsid_props.get('winname', '-Download').split('-')[-1]), h.url_for(controller="/objects", action="download", id=c.id, dsid=dsid_props.get('dsid', None)) )}  ${dsid_props.get('label', '')}</p>
% endfor
</div>
