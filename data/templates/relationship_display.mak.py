from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206625097.3725419
_template_filename='/home/archive/archive/archive/templates/relationship_display.mak'
_template_uri='/relationship_display.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 2
        if c.title:
            # SOURCE LINE 3
            context.write(u'<p><strong> Relationships for "')
            context.write(filters.decode.utf8(h.link_to('<span class="object_title">%s</span>' % c.title, h.url_for(controller="/objects", id=c.id))))
            context.write(u'":</strong></p>\n')
            # SOURCE LINE 4
        elif c.id:
            # SOURCE LINE 5
            context.write(u'<p><strong> Relationships for Object ')
            context.write(filters.decode.utf8(h.link_to('<span class="uuid">%s</span>' % c.id, h.url_for(controller="/objects", id=c.id))))
            context.write(u':</strong></p>\n')
        # SOURCE LINE 7
        if c.graph:
            # SOURCE LINE 8
            runtime._include_file(context, '/forward_relationship_display.mak', _template_uri)
            context.write(u'\n')
            # SOURCE LINE 9
            runtime._include_file(context, '/back_relationship_display.mak', _template_uri)
            context.write(u'\n')
            # SOURCE LINE 10
            runtime._include_file(context, '/object_relationship_navigation.mak', _template_uri)
            context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


