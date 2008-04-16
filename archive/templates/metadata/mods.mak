# -*- coding: utf-8 -*-
% for mods in c.metadata.get('MODS', None):
<div id="mods">
%   for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):
<div id="mods_titleInfo">
<div class="subheading"> ${ title.find('{http://www.loc.gov/mods/v3}title').text }
%     if title.find('{http://www.loc.gov/mods/v3}subTitle') != None:
: ${ title.find('{http://www.loc.gov/mods/v3}subTitle').text } </div>
%     else:
</div>
%     endif
</div>
%   endfor
%   for name in mods.findall('{http://www.loc.gov/mods/v3}name'):
<div class="mods_name">
%     if name.get('type', None)=='personal':
<div class="mods_name_left">
%       if name.find('{http://www.loc.gov/mods/v3}role/{http://www.loc.gov/mods/v3}roleTerm') != None:
<strong><span class="role">${name.find('{http://www.loc.gov/mods/v3}role/{http://www.loc.gov/mods/v3}roleTerm').text}: </span></strong>
%       endif
%       if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
${ name.find('{http://www.loc.gov/mods/v3}displayForm').text }
%       endif
%       if name.find('{http://www.loc.gov/mods/v3}namePart') != None:
%         if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
<p>(
%         endif
%         for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
%           if fragment.get('type', None) == 'termsOfAddress':
${fragment.text}
%           endif
%         endfor
%         for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
%           if fragment.get('type', None) == 'given':
${fragment.text} 
%           endif
%         endfor
%         for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
%           if fragment.get('type', None) == 'family':
${fragment.text}
%           endif
%         endfor
%         if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
)</p>
%         endif
%       endif
</div>
%       if name.find('{http://www.loc.gov/mods/v3}affiliation') != None:
<div class="affiliations">
%         if name.find('{http://www.loc.gov/mods/v3}affiliation').get('type', None):
<dl>
%           for affiliation in name.findall('{http://www.loc.gov/mods/v3}affiliation'):
%             if affiliation.text and affiliation.text.startswith('http://'):
<dt>${c.field_list.get(affiliation.get('type', None), affiliation.get('type', None))}</dt><dd><a href="${affiliation.text}">${affiliation.text}</a></dd>
%             elif affiliation.text:
<dt>${c.field_list.get(affiliation.get('type', None), affiliation.get('type', None))}</dt><dd>${affiliation.text}</dd>
%             endif
%           endfor
</dl>
%         else:
<ul>
%           for affiliation in name.findall('{http://www.loc.gov/mods/v3}affiliation'):
%             if affiliation.text and affiliation.text.startswith('http://'):
<li><a href="${affiliation.text}">${affiliation.text}</a></li>
%             elif affiliation.text:
<li>${affiliation.text}</li>
%             endif
%           endfor
</ul>
%         endif
</div>
%       endif
%     else:





<p>
%       if name.find('{http://www.loc.gov/mods/v3}role/{http://www.loc.gov/mods/v3}roleTerm') != None:
<strong><span class="role">${name.find('{http://www.loc.gov/mods/v3}role/{http://www.loc.gov/mods/v3}roleTerm').text}: </span></strong>
%       endif
%       if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
${ name.find('{http://www.loc.gov/mods/v3}displayForm').text }
%       endif
%       if name.find('{http://www.loc.gov/mods/v3}namePart') != None:
%         if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
- (
%         endif
%         for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
%           if fragment.get('type', None) == 'termsOfAddress':
${fragment.text}
%           endif
%         endfor
%         for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
%           if fragment.get('type', None) == 'given':
${fragment.text} 
%           endif
%         endfor
%         for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
%           if fragment.get('type', None) == 'family':
${fragment.text}
%           endif
%         endfor
%         if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
)
%         endif
%       endif

%       if name.find('{http://www.loc.gov/mods/v3}affiliation') != None:
- 
%         if name.find('{http://www.loc.gov/mods/v3}affiliation').get('type', None):

%           for affiliation in name.findall('{http://www.loc.gov/mods/v3}affiliation'):
%             if affiliation.text and affiliation.text.startswith('http://'):
 <a href="${affiliation.text}"><em>${c.field_list.get(affiliation.get('type', None), affiliation.get('type', None))}:</em></a>
%             elif affiliation.text:
<em>${c.field_list.get(affiliation.get('type', None), affiliation.get('type', None))}:</em> ${affiliation.text}
%             endif
%           endfor

%         else:

%           for affiliation in name.findall('{http://www.loc.gov/mods/v3}affiliation'):
%             if affiliation.text and affiliation.text.startswith('http://'):
<a href="${affiliation.text}">${affiliation.text}</a>
%             elif affiliation.text:
${affiliation.text}
%             endif
%           endfor

%         endif
%       endif
</p>

%     endif
</div>
<div class="clear">&nbsp;</div>
<hr/>
%   endfor
%   for related in mods.findall('{http://www.loc.gov/mods/v3}relatedItem'):
%     if related.get('type', None) == 'host':
<strong>Appears in: </strong>
%       if related.find('{http://www.loc.gov/mods/v3}titleInfo/{http://www.loc.gov/mods/v3}title') != None:
%         if related.find('{http://www.loc.gov/mods/v3}location/{http://www.loc.gov/mods/v3}url') != None:
<a href="related.find('{http://www.loc.gov/mods/v3}location/{http://www.loc.gov/mods/v3}url').text">${ related.find('{http://www.loc.gov/mods/v3}titleInfo/{http://www.loc.gov/mods/v3}title').text } (${related.find('{http://www.loc.gov/mods/v3}location/{http://www.loc.gov/mods/v3}url').text})</a>
%         else:
${ related.find('{http://www.loc.gov/mods/v3}titleInfo/{http://www.loc.gov/mods/v3}title').text }
%         endif
%       endif
%       for detail in related.findall('{http://www.loc.gov/mods/v3}part/{http://www.loc.gov/mods/v3}detail'):
%         if detail.get('type', None) == 'Volume':
<strong>${detail.getchildren()[0].text}</strong>
%         endif
%       endfor
%       for detail in related.findall('{http://www.loc.gov/mods/v3}part/{http://www.loc.gov/mods/v3}detail'):
%         if detail.get('type', None) == 'issue':
(${detail.getchildren()[0].text})
%         endif
%       endfor
%       for extent in related.findall('{http://www.loc.gov/mods/v3}part/{http://www.loc.gov/mods/v3}extent'):
${extent.getchildren()[0].text}
%       endfor
%     else:

%     endif
%   endfor
%   for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):

%   endfor
%   for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):

%   endfor
%   for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):

%   endfor
%   for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):

%   endfor
</div>
<% """
    &addtitleInfo($self);
    &addname($self);
    &addtypeOfResource($self);
    &addgenre($self);
    &addoriginInfo($self);
    &addlanguage($self);
    &addphysicalDescription($self);
    &addabstract($self);
    &addtableOfContents($self);
    &addtargetAudience($self);
    &addnote($self);
    &addsubject($self);
    &addclassification($self);
    if ( $self->{doctype} eq 'conferenceitem' ) {
	&addConference($self);
    }
    &addidentifier($self);
    &addlocation($self);
    &addaccessCondition($self);
    &addpart($self);
    &addextension($self);
    &addrecordInfo($self);
    &addrelatedItem($self);""" %>
% endfor
