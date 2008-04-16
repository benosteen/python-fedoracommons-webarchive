from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1207079748.772527
_template_filename='/home/ben/Desktop/archive/archive/templates/browse_root.mak'
_template_uri='/browse_root.mak'
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
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 32
        context.write(u'\n')
        # SOURCE LINE 34
        context.write(u'\n')
        # SOURCE LINE 36
        context.write(u'\n<div id="browse">\n<h1> Browse: </h1>\n</div>\n\n')
        # SOURCE LINE 41
        if c.returned_facets:
            # SOURCE LINE 42
            context.write(u'<div id="facet_container">\n<div id="facet_box_container">\n')
            # SOURCE LINE 44
            for facet in c.browsable:
                # SOURCE LINE 45
                context.write(u'<div id="')
                context.write(filters.decode.utf8(c.browsable[facet]))
                context.write(u'">\n<strong>')
                # SOURCE LINE 46
                context.write(filters.decode.utf8(c.field_names[c.browsable[facet]]))
                context.write(u' ')
                context.write(filters.decode.utf8(h.link_to("see more", h.url(controller='/browse', action='field', field=facet))))
                context.write(u'</strong>\n<ul>\n')
                # SOURCE LINE 48
                if facet=="collection":
                    # SOURCE LINE 49
                    for result,value in c.returned_facets[c.browsable[facet]]:
                        # SOURCE LINE 50
                        context.write(u'<li><span class="label">')
                        context.write(filters.decode.utf8(h.link_to(g.f.ri.getDCTitle(result), h.url(controller='/browse', action='field', field=facet, item=c.quote(result)))))
                        context.write(u' - (')
                        context.write(filters.decode.utf8(value))
                        context.write(u')</li>\n')
                    # SOURCE LINE 52
                else:
                    # SOURCE LINE 53
                    for result,value in c.returned_facets[c.browsable[facet]]:
                        # SOURCE LINE 54
                        context.write(u'<li><span class="label">')
                        context.write(filters.decode.utf8(h.link_to(result, h.url(controller='/browse', action='field', field=facet, item=c.quote(result)))))
                        context.write(u' - (')
                        context.write(filters.decode.utf8(value))
                        context.write(u')</li>\n')
                    # SOURCE LINE 56
                    context.write(u'</ul>\n')
                # SOURCE LINE 58
                context.write(u'</div>\n')
            # SOURCE LINE 60
            context.write(u'</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 33
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 35
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 3
        context.write(u'\n  <title> Browse - Search through the archive</title>\n  <style>\n    div#browse {\n       margin: 1em 2em;\n    }\n    div#facet_container {\n        margin-left: 3em;\n        border: 1px solid #cdcdcd;\n        background-color: #efefef;\n        float: left;\n    }\n    \n    div#facet_container h1 {\n        padding-left: 3em;\n    }\n    \n    div#facet_container div {\n        margin: 0 auto;\n        width: 100%;\n    }\n    \n    div#facet_container div div {\n        width: 14em;\n        float:left;\n        padding: 1em;\n    }\n    \n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


