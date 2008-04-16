from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206604420.433728
_template_filename='/home/archive/archive/archive/templates/type/documentation.mak'
_template_uri='/type/documentation.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['page_style', 'title_text']


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
    return runtime._inherit_from(context, '/type/default.mak', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 9
        context.write(u'\n')
        # SOURCE LINE 15
        context.write(u'\n<div id="record_wrapper">\n')
        # SOURCE LINE 17
        if c.title:
            # SOURCE LINE 18
            context.write(u'<p> ORA Documentation: <strong>"')
            context.write(filters.decode.utf8(c.title))
            context.write(u'"</strong></p>\n')
            # SOURCE LINE 19
        elif c.id:
            # SOURCE LINE 20
            context.write(u'<p> ORA Documentation: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</p>\n')
        # SOURCE LINE 22
        context.write(u'<div>\n')
        # SOURCE LINE 23
        for text in c.inline_text:
            # SOURCE LINE 24
            context.write(u'<div id="')
            context.write(filters.decode.utf8(text))
            context.write(u'" class="text">')
            context.write(filters.decode.utf8(c.inline_text[text]))
            context.write(u'</div>\n')
        # SOURCE LINE 26
        context.write(u'</div>\n')
        # SOURCE LINE 27
        context.write(filters.decode.utf8(self.record_information()))
        context.write(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_page_style(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 10
        context.write(u'\n    div.text {\n        border: 0px !important;\n        margin: 0em !important;\n    }\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_title_text(context):
    context.caller_stack.push_frame()
    try:
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 3
        context.write(u'\n')
        # SOURCE LINE 4
        if c.title:
            # SOURCE LINE 5
            context.write(u'<title> ORA Documentation: "')
            context.write(filters.decode.utf8(c.title))
            context.write(u'" - ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
            # SOURCE LINE 6
        elif c.id:
            # SOURCE LINE 7
            context.write(u'<title> ORA Documentation: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


