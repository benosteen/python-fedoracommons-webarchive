from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206476314.4588339
_template_filename='/home/archive/archive/archive/templates/metadata/mods.mak'
_template_uri='/metadata/mods.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 2
        for mods in c.metadata.get('MODS', None):
            # SOURCE LINE 3
            context.write(u'<div id="mods">\n')
            # SOURCE LINE 4
            for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):
                # SOURCE LINE 5
                context.write(u'<div id="mods_titleInfo">\n<div class="subheading"> ')
                # SOURCE LINE 6
                context.write(filters.decode.utf8( title.find('{http://www.loc.gov/mods/v3}title').text ))
                context.write(u'\n')
                # SOURCE LINE 7
                if title.find('{http://www.loc.gov/mods/v3}subTitle') != None:
                    # SOURCE LINE 8
                    context.write(u': ')
                    context.write(filters.decode.utf8( title.find('{http://www.loc.gov/mods/v3}subTitle').text ))
                    context.write(u' </div>\n')
                    # SOURCE LINE 9
                else:
                    # SOURCE LINE 10
                    context.write(u'</div>\n')
                # SOURCE LINE 12
                context.write(u'</div>\n')
            # SOURCE LINE 14
            for name in mods.findall('{http://www.loc.gov/mods/v3}name'):
                # SOURCE LINE 15
                context.write(u'<div class="mods_name">\n')
                # SOURCE LINE 16
                if name.get('type', None)=='personal':
                    # SOURCE LINE 17
                    context.write(u'<div class="mods_name_left">\n')
                    # SOURCE LINE 18
                    if name.find('{http://www.loc.gov/mods/v3}role/{http://www.loc.gov/mods/v3}roleTerm') != None:
                        # SOURCE LINE 19
                        context.write(u'<strong><span class="role">')
                        context.write(filters.decode.utf8(name.find('{http://www.loc.gov/mods/v3}role/{http://www.loc.gov/mods/v3}roleTerm').text))
                        context.write(u': </span></strong>\n')
                    # SOURCE LINE 21
                    if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
                        # SOURCE LINE 22
                        context.write(filters.decode.utf8( name.find('{http://www.loc.gov/mods/v3}displayForm').text ))
                        context.write(u'\n')
                    # SOURCE LINE 24
                    if name.find('{http://www.loc.gov/mods/v3}namePart') != None:
                        # SOURCE LINE 25
                        if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
                            # SOURCE LINE 26
                            context.write(u'<p>(\n')
                        # SOURCE LINE 28
                        for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
                            # SOURCE LINE 29
                            if fragment.get('type', None) == 'termsOfAddress':
                                # SOURCE LINE 30
                                context.write(filters.decode.utf8(fragment.text))
                                context.write(u'\n')
                        # SOURCE LINE 33
                        for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
                            # SOURCE LINE 34
                            if fragment.get('type', None) == 'given':
                                # SOURCE LINE 35
                                context.write(filters.decode.utf8(fragment.text))
                                context.write(u' \n')
                        # SOURCE LINE 38
                        for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
                            # SOURCE LINE 39
                            if fragment.get('type', None) == 'family':
                                # SOURCE LINE 40
                                context.write(filters.decode.utf8(fragment.text))
                                context.write(u'\n')
                        # SOURCE LINE 43
                        if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
                            # SOURCE LINE 44
                            context.write(u')</p>\n')
                    # SOURCE LINE 47
                    context.write(u'</div>\n')
                    # SOURCE LINE 48
                    if name.find('{http://www.loc.gov/mods/v3}affiliation') != None:
                        # SOURCE LINE 49
                        context.write(u'<div class="affiliations">\n')
                        # SOURCE LINE 50
                        if name.find('{http://www.loc.gov/mods/v3}affiliation').get('type', None):
                            # SOURCE LINE 51
                            context.write(u'<dl>\n')
                            # SOURCE LINE 52
                            for affiliation in name.findall('{http://www.loc.gov/mods/v3}affiliation'):
                                # SOURCE LINE 53
                                if affiliation.text and affiliation.text.startswith('http://'):
                                    # SOURCE LINE 54
                                    context.write(u'<dt>')
                                    context.write(filters.decode.utf8(c.field_list.get(affiliation.get('type', None), affiliation.get('type', None))))
                                    context.write(u'</dt><dd><a href="')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'">')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'</a></dd>\n')
                                    # SOURCE LINE 55
                                elif affiliation.text:
                                    # SOURCE LINE 56
                                    context.write(u'<dt>')
                                    context.write(filters.decode.utf8(c.field_list.get(affiliation.get('type', None), affiliation.get('type', None))))
                                    context.write(u'</dt><dd>')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'</dd>\n')
                            # SOURCE LINE 59
                            context.write(u'</dl>\n')
                            # SOURCE LINE 60
                        else:
                            # SOURCE LINE 61
                            context.write(u'<ul>\n')
                            # SOURCE LINE 62
                            for affiliation in name.findall('{http://www.loc.gov/mods/v3}affiliation'):
                                # SOURCE LINE 63
                                if affiliation.text and affiliation.text.startswith('http://'):
                                    # SOURCE LINE 64
                                    context.write(u'<li><a href="')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'">')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'</a></li>\n')
                                    # SOURCE LINE 65
                                elif affiliation.text:
                                    # SOURCE LINE 66
                                    context.write(u'<li>')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'</li>\n')
                            # SOURCE LINE 69
                            context.write(u'</ul>\n')
                        # SOURCE LINE 71
                        context.write(u'</div>\n')
                    # SOURCE LINE 73
                else:
                    # SOURCE LINE 74
                    context.write(u'\n\n\n\n\n<p>\n')
                    # SOURCE LINE 80
                    if name.find('{http://www.loc.gov/mods/v3}role/{http://www.loc.gov/mods/v3}roleTerm') != None:
                        # SOURCE LINE 81
                        context.write(u'<strong><span class="role">')
                        context.write(filters.decode.utf8(name.find('{http://www.loc.gov/mods/v3}role/{http://www.loc.gov/mods/v3}roleTerm').text))
                        context.write(u': </span></strong>\n')
                    # SOURCE LINE 83
                    if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
                        # SOURCE LINE 84
                        context.write(filters.decode.utf8( name.find('{http://www.loc.gov/mods/v3}displayForm').text ))
                        context.write(u'\n')
                    # SOURCE LINE 86
                    if name.find('{http://www.loc.gov/mods/v3}namePart') != None:
                        # SOURCE LINE 87
                        if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
                            # SOURCE LINE 88
                            context.write(u'- (\n')
                        # SOURCE LINE 90
                        for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
                            # SOURCE LINE 91
                            if fragment.get('type', None) == 'termsOfAddress':
                                # SOURCE LINE 92
                                context.write(filters.decode.utf8(fragment.text))
                                context.write(u'\n')
                        # SOURCE LINE 95
                        for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
                            # SOURCE LINE 96
                            if fragment.get('type', None) == 'given':
                                # SOURCE LINE 97
                                context.write(filters.decode.utf8(fragment.text))
                                context.write(u' \n')
                        # SOURCE LINE 100
                        for fragment in name.findall('{http://www.loc.gov/mods/v3}namePart'):
                            # SOURCE LINE 101
                            if fragment.get('type', None) == 'family':
                                # SOURCE LINE 102
                                context.write(filters.decode.utf8(fragment.text))
                                context.write(u'\n')
                        # SOURCE LINE 105
                        if name.find('{http://www.loc.gov/mods/v3}displayForm') != None:
                            # SOURCE LINE 106
                            context.write(u')\n')
                    # SOURCE LINE 109
                    context.write(u'\n')
                    # SOURCE LINE 110
                    if name.find('{http://www.loc.gov/mods/v3}affiliation') != None:
                        # SOURCE LINE 111
                        context.write(u'- \n')
                        # SOURCE LINE 112
                        if name.find('{http://www.loc.gov/mods/v3}affiliation').get('type', None):
                            # SOURCE LINE 113
                            context.write(u'\n')
                            # SOURCE LINE 114
                            for affiliation in name.findall('{http://www.loc.gov/mods/v3}affiliation'):
                                # SOURCE LINE 115
                                if affiliation.text and affiliation.text.startswith('http://'):
                                    # SOURCE LINE 116
                                    context.write(u' <a href="')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'"><em>')
                                    context.write(filters.decode.utf8(c.field_list.get(affiliation.get('type', None), affiliation.get('type', None))))
                                    context.write(u':</em></a>\n')
                                    # SOURCE LINE 117
                                elif affiliation.text:
                                    # SOURCE LINE 118
                                    context.write(u'<em>')
                                    context.write(filters.decode.utf8(c.field_list.get(affiliation.get('type', None), affiliation.get('type', None))))
                                    context.write(u':</em> ')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'\n')
                            # SOURCE LINE 121
                            context.write(u'\n')
                            # SOURCE LINE 122
                        else:
                            # SOURCE LINE 123
                            context.write(u'\n')
                            # SOURCE LINE 124
                            for affiliation in name.findall('{http://www.loc.gov/mods/v3}affiliation'):
                                # SOURCE LINE 125
                                if affiliation.text and affiliation.text.startswith('http://'):
                                    # SOURCE LINE 126
                                    context.write(u'<a href="')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'">')
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'</a>\n')
                                    # SOURCE LINE 127
                                elif affiliation.text:
                                    # SOURCE LINE 128
                                    context.write(filters.decode.utf8(affiliation.text))
                                    context.write(u'\n')
                            # SOURCE LINE 131
                            context.write(u'\n')
                    # SOURCE LINE 134
                    context.write(u'</p>\n\n')
                # SOURCE LINE 137
                context.write(u'</div>\n<div class="clear">&nbsp;</div>\n<hr/>\n')
            # SOURCE LINE 141
            for related in mods.findall('{http://www.loc.gov/mods/v3}relatedItem'):
                # SOURCE LINE 142
                if related.get('type', None) == 'host':
                    # SOURCE LINE 143
                    context.write(u'<strong>Appears in: </strong>\n')
                    # SOURCE LINE 144
                    if related.find('{http://www.loc.gov/mods/v3}titleInfo/{http://www.loc.gov/mods/v3}title') != None:
                        # SOURCE LINE 145
                        if related.find('{http://www.loc.gov/mods/v3}location/{http://www.loc.gov/mods/v3}url') != None:
                            # SOURCE LINE 146
                            context.write(u'<a href="related.find(\'{http://www.loc.gov/mods/v3}location/{http://www.loc.gov/mods/v3}url\').text">')
                            context.write(filters.decode.utf8( related.find('{http://www.loc.gov/mods/v3}titleInfo/{http://www.loc.gov/mods/v3}title').text ))
                            context.write(u' (')
                            context.write(filters.decode.utf8(related.find('{http://www.loc.gov/mods/v3}location/{http://www.loc.gov/mods/v3}url').text))
                            context.write(u')</a>\n')
                            # SOURCE LINE 147
                        else:
                            # SOURCE LINE 148
                            context.write(filters.decode.utf8( related.find('{http://www.loc.gov/mods/v3}titleInfo/{http://www.loc.gov/mods/v3}title').text ))
                            context.write(u'\n')
                    # SOURCE LINE 151
                    for detail in related.findall('{http://www.loc.gov/mods/v3}part/{http://www.loc.gov/mods/v3}detail'):
                        # SOURCE LINE 152
                        if detail.get('type', None) == 'Volume':
                            # SOURCE LINE 153
                            context.write(u'<strong>')
                            context.write(filters.decode.utf8(detail.getchildren()[0].text))
                            context.write(u'</strong>\n')
                    # SOURCE LINE 156
                    for detail in related.findall('{http://www.loc.gov/mods/v3}part/{http://www.loc.gov/mods/v3}detail'):
                        # SOURCE LINE 157
                        if detail.get('type', None) == 'issue':
                            # SOURCE LINE 158
                            context.write(u'(')
                            context.write(filters.decode.utf8(detail.getchildren()[0].text))
                            context.write(u')\n')
                    # SOURCE LINE 161
                    for extent in related.findall('{http://www.loc.gov/mods/v3}part/{http://www.loc.gov/mods/v3}extent'):
                        # SOURCE LINE 162
                        context.write(filters.decode.utf8(extent.getchildren()[0].text))
                        context.write(u'\n')
                    # SOURCE LINE 164
                else:
                    # SOURCE LINE 165
                    context.write(u'\n')
            # SOURCE LINE 168
            for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):
                # SOURCE LINE 169
                context.write(u'\n')
            # SOURCE LINE 171
            for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):
                # SOURCE LINE 172
                context.write(u'\n')
            # SOURCE LINE 174
            for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):
                # SOURCE LINE 175
                context.write(u'\n')
            # SOURCE LINE 177
            for title in mods.findall('{http://www.loc.gov/mods/v3}titleInfo'):
                # SOURCE LINE 178
                context.write(u'\n')
            # SOURCE LINE 180
            context.write(u'</div>\n')
            # SOURCE LINE 181
            """
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
    &addrelatedItem($self);""" 
            
            # SOURCE LINE 204
            context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


