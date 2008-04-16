from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1205602827.454428
_template_filename='/home/archive/archive/archive/templates/unapi.mak'
_template_uri='/unapi.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<?xml version="1.0" encoding="UTF-8"?>\n')
        # SOURCE LINE 2
        context.write(filters.decode.utf8(c.unapi))
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


