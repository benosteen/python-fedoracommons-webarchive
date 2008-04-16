from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1205507530.3117659
_template_filename='/home/archive/archive/archive/templates/record_page.mak'
_template_uri='/record_page.mak'
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
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 17
        context.write(u'\n')
        # SOURCE LINE 19
        context.write(u'\n')
        # SOURCE LINE 21
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 18
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 20
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 3
        context.write(u'\n  <title> ORA - Oxford University Research Archive - Item ')
        # SOURCE LINE 4
        context.write(filters.decode.utf8(c.id))
        context.write(u'</title>\n  <style>\n    div#object_wrapper {\n      margin: 1em 2em;\n    }\n    div#object_wrapper div {\n      margin: 1em 2em;\n    }\n    div#dsid_list {\n      border: 1px solid #cdcdcd;\n      background-color: #efefef;\n    }\n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


