from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206468531.014246
_template_filename='/home/archive/archive/archive/templates/browse_facet.mak'
_template_uri='/browse_facet.mak'
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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 42
        context.write(u'\n')
        # SOURCE LINE 44
        context.write(u'\n')
        # SOURCE LINE 46
        context.write(u'\n<div id="browse">\n<h1> Browse: ')
        # SOURCE LINE 48
        context.write(filters.decode.utf8(c.facet.capitalize()))
        context.write(u'\n')
        # SOURCE LINE 49
        if c.facet=="collection":
            # SOURCE LINE 50
            context.write(u'<span class="small_link"> ')
            context.write(filters.decode.utf8(h.link_to('Click here to view collection "%s"' % (c.item) , h.url(controller="/objects", id=c.item))))
            context.write(u' </span>\n')
        # SOURCE LINE 52
        context.write(u'</h1>\n<div class="subheading">showing only results that have "')
        # SOURCE LINE 53
        context.write(filters.decode.utf8(c.item))
        context.write(u'" in the <em>')
        context.write(filters.decode.utf8(c.facet))
        context.write(u'</em> field: </div>\n<div class="subheading"> ')
        # SOURCE LINE 54
        context.write(filters.decode.utf8(h.link_to('Click here to browse full <em>%s</em> list' % (c.facet) , h.url(controller="/browse", action="field", field=c.facet))))
        context.write(u' </div>\n</div>\n')
        # SOURCE LINE 56
        runtime._include_file(context, '/minimal_search_response_display.mak', _template_uri)
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 43
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 45
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 3
        context.write(u'\n  <title> Browse - Search through the </title>\n  <style>\n    div#browse {\n       margin: 1em 2em;\n    }\n    div#facet_container {\n        margin-left: 3em;\n        border: 1px solid #cdcdcd;\n        background-color: #efefef;\n        float: left;\n    }\n    \n    div#facet_container h1 {\n        padding-left: 3em;\n    }\n    \n    div#facet_container div {\n        margin: 0 auto;\n        width: 100%;\n    }\n    \n    div#facet_container div div {\n        width: 14em;\n        float:left;\n        padding: 1em;\n    }\n    \n    div.response_doc {\n        margin: 1.5em;\n        border: 1px solid #aaa8a1;\n        background-color: #efefef;\n    }\n    \n    div.response_doc div.link {\n        margin-left: 1em;\n        line-height: 2em;\n    }    \n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


