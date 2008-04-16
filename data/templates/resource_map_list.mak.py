from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1207070144.8489339
_template_filename='/home/ben/Desktop/archive/archive/templates/resource_map_list.mak'
_template_uri='/resource_map_list.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 1
        for pid in c.csv:
            # SOURCE LINE 2
            context.write(filters.decode.utf8("%sobjects/%s/rem" % (g.root, pid)))
            context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


