from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206608597.482795
_template_filename='/home/archive/archive/archive/templates/error.mak'
_template_uri='/error.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['header', 'footer', 'head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.mak', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 10
        context.write(u'\n')
        # SOURCE LINE 12
        context.write(u'\n')
        # SOURCE LINE 14
        context.write(u'\n<div id="error">\n<h1> ')
        # SOURCE LINE 16
        context.write(filters.decode.utf8(c.code))
        context.write(u' - ')
        context.write(filters.decode.utf8(c.message))
        context.write(u' </h1>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 11
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 13
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 3
        context.write(u'\n  <title> Error - ')
        # SOURCE LINE 4
        context.write(filters.decode.utf8(c.code))
        context.write(u' - ')
        context.write(filters.decode.utf8(c.message))
        context.write(u' </title>\n  <style>\n  div#error {\n       margin: 1em 2em;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


