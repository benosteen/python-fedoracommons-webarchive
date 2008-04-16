from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206479871.856847
_template_filename='/home/archive/archive/archive/templates/search_response_display.mak'
_template_uri='/search_response_display.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        key = context.get('key', UNDEFINED)
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
            # SOURCE LINE 15
            if c.search:
                # SOURCE LINE 16
                if c.hide_basic_search:
                    # SOURCE LINE 17
                    context.write(u'<div id="link_to_this_search">\n')
                    # SOURCE LINE 18
                    context.write(filters.decode.utf8(h.link_to('Link to these search results', h.url_for(controller='search', action="detailed", **dict([(key, c.search[key]) for key in c.search if key!='start'])))))
                    context.write(u' - ')
                    context.write(filters.decode.utf8(h.link_to('Atom <img src="/atom.png" border="0"/>', h.url_for(controller='search', action="detailed", format='atom', **dict([(key, c.search[key]) for key in c.search if key!='start'])))))
                    context.write(u'\n</div>\n')
                    # SOURCE LINE 20
                else:
                    # SOURCE LINE 21
                    context.write(u'<div id="link_to_this_search">\n')
                    # SOURCE LINE 22
                    context.write(filters.decode.utf8(h.link_to('Link to these search results', h.url_for(controller='search', action="basic", **dict([(key, c.search[key]) for key in c.search if key!='start'])))))
                    context.write(u'\n</div>\n')
            # SOURCE LINE 26
            context.write(u'<div class="clear">&nbsp;</div>\n')
            # SOURCE LINE 27
            if c.sort_text:
                # SOURCE LINE 28
                context.write(u'<div class="subheading"> Sorting by \'')
                context.write(filters.decode.utf8(c.sort_text))
                context.write(u"'</div>\n")
            # SOURCE LINE 30
            if c.hide_basic_search:
                # SOURCE LINE 31
                context.write(u'<div class="paginated_results">\n')
                # SOURCE LINE 32
                for offset in c.permissible_offsets:
                    # SOURCE LINE 33
                    if not (offset=='...'):
                        # SOURCE LINE 34
                        context.write(u'.. <span class="pagination_label">\n')
                        # SOURCE LINE 35
                        context.write(filters.decode.utf8(h.link_to(offset or '0', h.url_for(controller='search', action="detailed", **dict([(key, c.search[key]) for key in c.search if key!='start'], start=offset)))))
                        context.write(u'</span> .. \n')
                        # SOURCE LINE 36
                    else:
                        # SOURCE LINE 37
                        context.write(u'.. ')
                        context.write(filters.decode.utf8(offset))
                        context.write(u' ..\n')
                # SOURCE LINE 40
                context.write(u'</div>\n')
                # SOURCE LINE 41
            else:
                # SOURCE LINE 42
                context.write(u'<div class="paginated_results">\n')
                # SOURCE LINE 43
                for offset in c.permissible_offsets:
                    # SOURCE LINE 44
                    if not (offset=='...'):
                        # SOURCE LINE 45
                        context.write(u'.. <span class="pagination_label">\n')
                        # SOURCE LINE 46
                        context.write(filters.decode.utf8(h.link_to(offset or '0', h.url_for(controller='search', action="basic", **dict([(key, c.search[key]) for key in c.search if key!='start'], start=offset)))))
                        context.write(u'</span> .. \n')
                        # SOURCE LINE 47
                    else:
                        # SOURCE LINE 48
                        context.write(u'.. ')
                        context.write(filters.decode.utf8(offset))
                        context.write(u' ..\n')
                # SOURCE LINE 51
                context.write(u'</div>\n')
            # SOURCE LINE 53
            for doc_index in xrange(len(c.docs)):
                # SOURCE LINE 54
                context.write(u'<div class="response_doc">\n<span class="document_number">')
                # SOURCE LINE 55
                context.write(filters.decode.utf8(c.start+1+doc_index))
                context.write(u'</span>\n<dl>\n<dt class="label">')
                # SOURCE LINE 57
                context.write(filters.decode.utf8(c.field_names['title']))
                context.write(u'</dt><dd class="value">')
                context.write(filters.decode.utf8(h.link_to(c.docs[doc_index].get('title', 'Link'), h.url_for(controller="/objects", id=c.docs[doc_index].get('id',None)))))
                context.write(u'</dd>\n')
                # SOURCE LINE 58
                for field in [x for x in c.all_fields if x!='title']:
                    # SOURCE LINE 59
                    if field in c.docs[doc_index]:
                        # SOURCE LINE 60
                        context.write(u'<dt class="label">')
                        context.write(filters.decode.utf8(c.field_names[field]))
                        context.write(u'</dt><dd class="value">\n')
                        # SOURCE LINE 61
                        if isinstance(c.docs[doc_index][field], list):
                            # SOURCE LINE 62
                            context.write(filters.decode.utf8( " ; ".join(c.docs[doc_index][field]) ))
                            context.write(u'\n')
                            # SOURCE LINE 63
                        elif c.truncate and isinstance(c.truncate, int) and not isinstance(c.docs[doc_index][field],bool) and len(c.docs[doc_index][field]) > c.truncate:
                            # SOURCE LINE 64
                            context.write(filters.decode.utf8( c.docs[doc_index][field][:c.truncate] ))
                            context.write(u' ... [truncated at ')
                            context.write(filters.decode.utf8(c.truncate))
                            context.write(u' characters in length]\n')
                            # SOURCE LINE 65
                        else:
                            # SOURCE LINE 66
                            context.write(filters.decode.utf8(c.docs[doc_index][field]))
                            context.write(u'\n')
                        # SOURCE LINE 68
                        context.write(u'</dt>\n')
                # SOURCE LINE 71
                context.write(u'</dl>\n</div>\n')
            # SOURCE LINE 74
            if c.hide_basic_search:
                # SOURCE LINE 75
                context.write(u'<div class="paginated_results">\n')
                # SOURCE LINE 76
                for offset in c.permissible_offsets:
                    # SOURCE LINE 77
                    if not (offset=='...'):
                        # SOURCE LINE 78
                        context.write(u'.. <span class="pagination_label">\n')
                        # SOURCE LINE 79
                        context.write(filters.decode.utf8(h.link_to(offset or '0', h.url_for(controller='search', action="detailed", **dict([(key, c.search[key]) for key in c.search if key!='start'], start=offset)))))
                        context.write(u'</span> .. \n')
                        # SOURCE LINE 80
                    else:
                        # SOURCE LINE 81
                        context.write(u'.. ')
                        context.write(filters.decode.utf8(offset))
                        context.write(u' ..\n')
                # SOURCE LINE 84
                context.write(u'</div>\n')
                # SOURCE LINE 85
            else:
                # SOURCE LINE 86
                context.write(u'<div class="paginated_results">\n')
                # SOURCE LINE 87
                for offset in c.permissible_offsets:
                    # SOURCE LINE 88
                    if not (offset=='...'):
                        # SOURCE LINE 89
                        context.write(u'.. <span class="pagination_label">\n')
                        # SOURCE LINE 90
                        context.write(filters.decode.utf8(h.link_to(offset or '0', h.url_for(controller='search', action="basic", **dict([(key, c.search[key]) for key in c.search if key!='start'], start=offset)))))
                        context.write(u'</span> .. \n')
                        # SOURCE LINE 91
                    else:
                        # SOURCE LINE 92
                        context.write(u'.. ')
                        context.write(filters.decode.utf8(offset))
                        context.write(u' ..\n')
                # SOURCE LINE 95
                context.write(u'</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


