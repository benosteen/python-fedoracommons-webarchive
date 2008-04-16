from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1207139504.1239879
_template_filename='/home/ben/Desktop/archive/archive/templates/type/citation.mak'
_template_uri='/type/citation.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<div class="citation">\n<dl>\n<dt>Citation: </dt>\n<dd>\n')
        # SOURCE LINE 5
        if 'person_name' in c.search_terms:
            # SOURCE LINE 6
            context.write(u'<span class="names">\n')
            # SOURCE LINE 7
            if isinstance(c.search_terms['person_name'], list):
                # SOURCE LINE 8
                context.write(filters.decode.utf8( " ; ".join(c.search_terms['person_name']) ))
                context.write(u'\n')
                # SOURCE LINE 9
            else:
                # SOURCE LINE 10
                context.write(filters.decode.utf8(c.search_terms['person_name']))
                context.write(u'\n')
            # SOURCE LINE 12
            context.write(u'</span>, \n')
            # SOURCE LINE 13
        elif 'creator' in c.search_terms:
            # SOURCE LINE 14
            context.write(u'<span class="names">\n')
            # SOURCE LINE 15
            if isinstance(c.search_terms['creator'], list):
                # SOURCE LINE 16
                context.write(filters.decode.utf8( " ; ".join(c.search_terms['creator']) ))
                context.write(u'\n')
                # SOURCE LINE 17
            else:
                # SOURCE LINE 18
                context.write(filters.decode.utf8(c.search_terms['creator']))
                context.write(u'\n')
            # SOURCE LINE 20
            context.write(u'</span>, \n')
        # SOURCE LINE 22
        if 'copyright_date' in c.search_terms:
            # SOURCE LINE 23
            context.write(u'(<span class="date">')
            context.write(filters.decode.utf8(c.search_terms['copyright_date']))
            context.write(u'</span>).\n')
            # SOURCE LINE 24
        elif 'creation_date' in c.search_terms:
            # SOURCE LINE 25
            context.write(u'(<span class="date">')
            context.write(filters.decode.utf8(c.search_terms['creation_date']))
            context.write(u'</span>).\n')
            # SOURCE LINE 26
        elif 'date' in c.search_terms:
            # SOURCE LINE 27
            context.write(u'(<span class="date">\n')
            # SOURCE LINE 28
            if isinstance(c.search_terms['date'], list):
                # SOURCE LINE 29
                context.write(filters.decode.utf8( " ".join(c.search_terms['date']) ))
                context.write(u'\n')
                # SOURCE LINE 30
            else:
                # SOURCE LINE 31
                context.write(filters.decode.utf8(c.search_terms['date']))
                context.write(u'\n')
            # SOURCE LINE 33
            context.write(u'</span>).\n')
        # SOURCE LINE 35
        if 'title' in c.search_terms:
            # SOURCE LINE 36
            context.write(u'<span class="title">\n')
            # SOURCE LINE 37
            if isinstance(c.search_terms['title'], list):
                # SOURCE LINE 38
                context.write(filters.decode.utf8( " ; ".join(c.search_terms['title']) ))
                context.write(u'\n')
                # SOURCE LINE 39
            else:
                # SOURCE LINE 40
                context.write(filters.decode.utf8(c.search_terms['title']))
                context.write(u'\n')
            # SOURCE LINE 42
            context.write(u'</span>.\n')
        # SOURCE LINE 44
        if 'host' in c.search_terms:
            # SOURCE LINE 45
            context.write(u'<span class="host"><em>\n')
            # SOURCE LINE 46
            if isinstance(c.search_terms['host'], list):
                # SOURCE LINE 47
                context.write(filters.decode.utf8( " ; ".join(c.search_terms['host']) ))
                context.write(u'\n')
                # SOURCE LINE 48
            else:
                # SOURCE LINE 49
                context.write(filters.decode.utf8(c.search_terms['host']))
                context.write(u'\n')
            # SOURCE LINE 51
            context.write(u'</em></span>,\n')
            # SOURCE LINE 52
            if 'volume' in c.search_terms:
                # SOURCE LINE 53
                context.write(u'<strong><span class="volume">')
                context.write(filters.decode.utf8(c.search_terms['volume']))
                context.write(u'</span></strong>\n')
            # SOURCE LINE 55
            if 'issue' in c.search_terms:
                # SOURCE LINE 56
                context.write(u'(<span class="issue">')
                context.write(filters.decode.utf8(c.search_terms['issue']))
                context.write(u'</span>),\n')
            # SOURCE LINE 58
            if 'pages' in c.search_terms:
                # SOURCE LINE 59
                context.write(u' <span class="pages">')
                context.write(filters.decode.utf8(c.search_terms['pages']))
                context.write(u'</span>\n')
        # SOURCE LINE 62
        if 'thesis_type' in c.search_terms:
            # SOURCE LINE 63
            context.write(u'<span class="thesis_type">')
            context.write(filters.decode.utf8(c.search_terms['thesis_type']))
            context.write(u'</span>, \n')
            # SOURCE LINE 64
            if 'thesis_awarding_body' in c.search_terms:
                # SOURCE LINE 65
                context.write(u'<span class="thesis_awarding_body">')
                context.write(filters.decode.utf8(c.search_terms['thesis_awarding_body']))
                context.write(u'</span>\n')
                # SOURCE LINE 66
            else:
                # SOURCE LINE 67
                context.write(u'<span class="thesis_awarding_body">University of Oxford</span>\n')
        # SOURCE LINE 70
        context.write(u' <span class="small_link">')
        context.write(filters.decode.utf8(h.link_to( "%sobjects/%s" % (g.root, c.id), h.url_for(controller="/objects", id=c.id ))))
        context.write(u'</span>\n</dd>\n</dl>\n</div>\n<div class="clear">&nbsp;</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


