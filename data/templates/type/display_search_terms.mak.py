from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1205668996.640219
_template_filename='/home/archive/archive/archive/templates/type/display_search_terms.mak'
_template_uri='/type/display_search_terms.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<dl>\n')
        # SOURCE LINE 2
        for field in c.all_fields:
            # SOURCE LINE 3
            if field in c.search_terms:
                # SOURCE LINE 4
                context.write(u'<dt class="label">')
                context.write(filters.decode.utf8(c.field_list[field]))
                context.write(u'</dt><dd class="value">\n')
                # SOURCE LINE 5
                if isinstance(c.search_terms[field], list):
                    # SOURCE LINE 6
                    context.write(filters.decode.utf8( " ; ".join(c.search_terms[field]) ))
                    context.write(u'\n')
                    # SOURCE LINE 7
                elif c.truncate and isinstance(c.truncate, int) and not isinstance(c.search_terms[field],bool) and len(c.search_terms[field]) > c.truncate:
                    # SOURCE LINE 8
                    context.write(filters.decode.utf8( c.search_terms[field][:c.truncate] ))
                    context.write(u' ... [truncated at ')
                    context.write(filters.decode.utf8(c.truncate))
                    context.write(u' characters in length]\n')
                    # SOURCE LINE 9
                else:
                    # SOURCE LINE 10
                    context.write(filters.decode.utf8(c.search_terms[field]))
                    context.write(u'\n')
                # SOURCE LINE 12
                context.write(u'</dt>\n')
        # SOURCE LINE 15
        context.write(u'</dl>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


