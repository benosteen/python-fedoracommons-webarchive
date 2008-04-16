from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206480892.1005449
_template_filename='/home/archive/archive/archive/templates/collection_response_display.mak'
_template_uri='/collection_response_display.mak'
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
            context.write(u' Number of items in collection: <span class="highlight"> ')
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
            context.write(u'</p>\n<div class="clear">&nbsp;</div>\n')
            # SOURCE LINE 16
            if c.permissible_offsets:
                # SOURCE LINE 17
                context.write(u'<div class="paginated_results">\n')
                # SOURCE LINE 18
                for offset in c.permissible_offsets:
                    # SOURCE LINE 19
                    if not (offset=='...'):
                        # SOURCE LINE 20
                        context.write(u'.. <span class="pagination_label">\n')
                        # SOURCE LINE 21
                        context.write(filters.decode.utf8(h.link_to(offset or '0', h.url_for(start=offset))))
                        context.write(u'</span> .. \n')
                        # SOURCE LINE 22
                    else:
                        # SOURCE LINE 23
                        context.write(u'.. ')
                        context.write(filters.decode.utf8(offset))
                        context.write(u' ..\n')
                # SOURCE LINE 26
                context.write(u'</div>\n')
            # SOURCE LINE 28
            for doc_index in xrange(len(c.docs)):
                # SOURCE LINE 29
                context.write(u'<div class="response_doc">\n<span class="document_number"><strong>')
                # SOURCE LINE 30
                context.write(filters.decode.utf8(c.start+1+doc_index))
                context.write(u'</strong></span>\n<dt class="label">')
                # SOURCE LINE 31
                context.write(filters.decode.utf8(c.field_list['title']))
                context.write(u'</dt><dd class="value">')
                context.write(filters.decode.utf8(h.link_to(c.docs[doc_index].get('title', 'Link'), h.url_for(controller="/objects", id=c.docs[doc_index].get('id',None)))))
                context.write(u'</dd>\n')
                # SOURCE LINE 32
                for field in [x for x in c.all_fields if x!='title']:
                    # SOURCE LINE 33
                    if field in c.docs[doc_index]:
                        # SOURCE LINE 34
                        context.write(u'<dt class="label">')
                        context.write(filters.decode.utf8(c.field_list[field]))
                        context.write(u'</dt><dd class="value">\n')
                        # SOURCE LINE 35
                        if isinstance(c.docs[doc_index][field], list):
                            # SOURCE LINE 36
                            context.write(filters.decode.utf8( " ; ".join(c.docs[doc_index][field]) ))
                            context.write(u'\n')
                            # SOURCE LINE 37
                        elif c.truncate and isinstance(c.truncate, int) and not isinstance(c.docs[doc_index][field],bool) and len(c.docs[doc_index][field]) > c.truncate:
                            # SOURCE LINE 38
                            context.write(filters.decode.utf8( c.docs[doc_index][field][:c.truncate] ))
                            context.write(u' ... [truncated at ')
                            context.write(filters.decode.utf8(c.truncate))
                            context.write(u' characters in length]\n')
                            # SOURCE LINE 39
                        else:
                            # SOURCE LINE 40
                            context.write(filters.decode.utf8(c.docs[doc_index][field]))
                            context.write(u'\n')
                        # SOURCE LINE 42
                        context.write(u'</dt>\n')
                # SOURCE LINE 45
                context.write(u'</dl>\n</div>\n')
            # SOURCE LINE 48
            if c.permissible_offsets:
                # SOURCE LINE 49
                context.write(u'<div class="paginated_results">\n')
                # SOURCE LINE 50
                for offset in c.permissible_offsets:
                    # SOURCE LINE 51
                    if not (offset=='...'):
                        # SOURCE LINE 52
                        context.write(u'.. <span class="pagination_label">\n')
                        # SOURCE LINE 53
                        context.write(filters.decode.utf8(h.link_to(offset or '0', h.url_for(start=offset))))
                        context.write(u'</span> .. \n')
                        # SOURCE LINE 54
                    else:
                        # SOURCE LINE 55
                        context.write(u'.. ')
                        context.write(filters.decode.utf8(offset))
                        context.write(u' ..\n')
                # SOURCE LINE 58
                context.write(u'</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


