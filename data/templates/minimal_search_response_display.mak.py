from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206468531.0988989
_template_filename='/home/archive/archive/archive/templates/minimal_search_response_display.mak'
_template_uri='/minimal_search_response_display.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<p>\n')
        # SOURCE LINE 2
        if c.numFound:
            # SOURCE LINE 3
            context.write(u' Number of hits: <span class="highlight"> ')
            context.write(filters.decode.utf8( c.numFound ))
            context.write(u' </span> - \n')
            # SOURCE LINE 4
        elif c.q:
            # SOURCE LINE 5
            context.write(u' Sorry, but your query <em>')
            context.write(filters.decode.utf8(c.q))
            context.write(u'</em> resulted in no matches.</p>\n')
        # SOURCE LINE 7
        if c.docs:
            # SOURCE LINE 8
            context.write(u' Showing results ')
            context.write(filters.decode.utf8(c.start+1))
            context.write(u' to \n')
            # SOURCE LINE 9
            if (c.start+c.rows) > c.numFound:
                # SOURCE LINE 10
                context.write(filters.decode.utf8(c.numFound))
                context.write(u'\n')
                # SOURCE LINE 11
            else:
                # SOURCE LINE 12
                context.write(filters.decode.utf8(c.start+c.rows))
                context.write(u'\n')
            # SOURCE LINE 14
            context.write(u'</p>\n')
        # SOURCE LINE 16
        if c.sort_text:
            # SOURCE LINE 17
            context.write(u'<div class="subheading"> Sorting by \'')
            context.write(filters.decode.utf8(c.sort_text))
            context.write(u"'</div>\n")
        # SOURCE LINE 19
        context.write(u'\n<div class="paginated_results">\n')
        # SOURCE LINE 21
        for offset in c.permissible_offsets:
            # SOURCE LINE 22
            if not (offset=='...'):
                # SOURCE LINE 23
                context.write(u'.. <span class="pagination_label">\n')
                # SOURCE LINE 24
                context.write(filters.decode.utf8(h.link_to(offset or '0', h.url_for(controller='browse', action="field", field=c.facet, item=c.item, start=offset))))
                context.write(u'</span> .. \n')
                # SOURCE LINE 25
            else:
                # SOURCE LINE 26
                context.write(u'.. ')
                context.write(filters.decode.utf8(offset))
                context.write(u' ..\n')
        # SOURCE LINE 29
        context.write(u'</div>\n<div class="response_doc">\n')
        # SOURCE LINE 31
        for doc_index in xrange(len(c.docs)):
            # SOURCE LINE 32
            context.write(u'<div class="link"><span class="document_number">')
            context.write(filters.decode.utf8(c.start+1+doc_index))
            context.write(u'</span> - \n<a href="')
            # SOURCE LINE 33
            context.write(filters.decode.utf8(h.url_for(controller="/objects", id=c.docs[doc_index].get('id',None))))
            context.write(u'">\n')
            # SOURCE LINE 34
            if 'person_name' in c.docs[doc_index]:
                # SOURCE LINE 35
                context.write(u'<span class="names">\n')
                # SOURCE LINE 36
                if isinstance(c.docs[doc_index]['person_name'], list):
                    # SOURCE LINE 37
                    context.write(filters.decode.utf8( " ; ".join(c.docs[doc_index]['person_name']) ))
                    context.write(u'\n')
                    # SOURCE LINE 38
                else:
                    # SOURCE LINE 39
                    context.write(filters.decode.utf8(c.docs[doc_index]['person_name']))
                    context.write(u'\n')
                # SOURCE LINE 41
                context.write(u'</span>, \n')
            # SOURCE LINE 43
            if 'copyright_date' in c.docs[doc_index]:
                # SOURCE LINE 44
                context.write(u'(<span class="date">')
                context.write(filters.decode.utf8(c.docs[doc_index]['copyright_date']))
                context.write(u'</span>).\n')
            # SOURCE LINE 46
            if 'title' in c.docs[doc_index]:
                # SOURCE LINE 47
                context.write(u'<span class="title">\n')
                # SOURCE LINE 48
                if isinstance(c.docs[doc_index]['title'], list):
                    # SOURCE LINE 49
                    context.write(filters.decode.utf8( " ; ".join(c.docs[doc_index]['title']) ))
                    context.write(u'\n')
                    # SOURCE LINE 50
                else:
                    # SOURCE LINE 51
                    context.write(filters.decode.utf8(c.docs[doc_index]['title']))
                    context.write(u'\n')
                # SOURCE LINE 53
                context.write(u'</span>.\n')
            # SOURCE LINE 55
            if 'host' in c.docs[doc_index]:
                # SOURCE LINE 56
                context.write(u'<span class="host"><em>\n')
                # SOURCE LINE 57
                if isinstance(c.docs[doc_index]['host'], list):
                    # SOURCE LINE 58
                    context.write(filters.decode.utf8( " ; ".join(c.docs[doc_index]['host']) ))
                    context.write(u'\n')
                    # SOURCE LINE 59
                else:
                    # SOURCE LINE 60
                    context.write(filters.decode.utf8(c.docs[doc_index]['host']))
                    context.write(u'\n')
                # SOURCE LINE 62
                context.write(u'</em></span>,\n')
                # SOURCE LINE 63
                if 'volume' in c.docs[doc_index]:
                    # SOURCE LINE 64
                    context.write(u'<strong><span class="volume">')
                    context.write(filters.decode.utf8(c.docs[doc_index]['volume']))
                    context.write(u'</span></strong>\n')
                # SOURCE LINE 66
                if 'issue' in c.docs[doc_index]:
                    # SOURCE LINE 67
                    context.write(u'(<span class="issue">')
                    context.write(filters.decode.utf8(c.docs[doc_index]['issue']))
                    context.write(u'</span>),\n')
                # SOURCE LINE 69
                if 'pages' in c.docs[doc_index]:
                    # SOURCE LINE 70
                    context.write(u' <span class="pages">')
                    context.write(filters.decode.utf8(c.docs[doc_index]['pages']))
                    context.write(u'</span>\n')
            # SOURCE LINE 73
            if 'thesis_type' in c.docs[doc_index]:
                # SOURCE LINE 74
                context.write(u'<span class="thesis_type">')
                context.write(filters.decode.utf8(c.docs[doc_index]['thesis_type']))
                context.write(u'</span>, \n')
                # SOURCE LINE 75
                if 'thesis_awarding_body' in c.docs[doc_index]:
                    # SOURCE LINE 76
                    context.write(u'<span class="thesis_awarding_body">')
                    context.write(filters.decode.utf8(c.docs[doc_index]['thesis_awarding_body']))
                    context.write(u'</span>\n')
                    # SOURCE LINE 77
                else:
                    # SOURCE LINE 78
                    context.write(u'<span class="thesis_awarding_body">University of Oxford</span>\n')
            # SOURCE LINE 81
            context.write(u'</a>\n</div>\n')
        # SOURCE LINE 84
        context.write(u'</div>\n<div class="paginated_results">\n')
        # SOURCE LINE 86
        for offset in c.permissible_offsets:
            # SOURCE LINE 87
            if not (offset=='...'):
                # SOURCE LINE 88
                context.write(u'.. <span class="pagination_label">\n')
                # SOURCE LINE 89
                context.write(filters.decode.utf8(h.link_to(offset or '0', h.url_for(controller='browse', action="field", field=c.facet, item=c.item, start=offset))))
                context.write(u'</span> .. \n')
                # SOURCE LINE 90
            else:
                # SOURCE LINE 91
                context.write(u'.. ')
                context.write(filters.decode.utf8(offset))
                context.write(u' ..\n')
        # SOURCE LINE 94
        context.write(u'</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


