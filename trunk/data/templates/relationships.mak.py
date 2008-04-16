from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1205736615.610065
_template_filename='/home/archive/archive/archive/templates/relationships.mak'
_template_uri='/relationships.mak'
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
        # SOURCE LINE 33
        context.write(u'\n')
        # SOURCE LINE 35
        context.write(u'\n')
        # SOURCE LINE 37
        context.write(u'\n<div id="relationships_wrapper">\n<div id="relationships">\n')
        # SOURCE LINE 40
        runtime._include_file(context, '/relationship_display.mak', _template_uri)
        context.write(u'\n</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 34
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 36
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 3
        context.write(u'\n  <title> Relationships for ')
        # SOURCE LINE 4
        context.write(filters.decode.utf8(c.id))
        context.write(u'</title>\n  <style>\n    div#relationships {\n       margin: 1em 2em;\n       float:left;\n       background: transparent;\n    }\n    div#relationships_navigation {\n       margin: 1em 2em;\n       float:right;\n       background: transparent;\n       border: 1px solid #888;\n    }\n    div#relationships_navigation ul li {\n        list-style: none;\n        display: inline;\n    }\n    \n    span.object_title {\n        color: #2288dd;\n    }\n    \n    span.uuid {\n        color: #999 !important;\n        font-style: italic !important;\n        font-size: 0.8em !important;\n    }\n    \n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


