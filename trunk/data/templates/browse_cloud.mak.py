from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206479204.52508
_template_filename='/home/archive/archive/archive/templates/browse_cloud.mak'
_template_uri='/browse_cloud.mak'
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
        # SOURCE LINE 46
        context.write(u'\n')
        # SOURCE LINE 48
        context.write(u'\n')
        # SOURCE LINE 50
        context.write(u'\n<div id="browse">\n<h1> Browse: (')
        # SOURCE LINE 52
        context.write(filters.decode.utf8(h.link_to('as cloud, largest populations only', h.url_for(view='cloud_small') )))
        context.write(u') (')
        context.write(filters.decode.utf8(h.link_to('as cloud, all members', h.url_for(view='cloud') )))
        context.write(u') (')
        context.write(filters.decode.utf8(h.link_to('as alphabetical list', h.url_for(view='list') )))
        context.write(u')</h1>\n<div class="subheading"> ')
        # SOURCE LINE 53
        context.write(filters.decode.utf8(h.link_to('Back to top-level Browse page.', h.url_for(controller="/browse"))))
        context.write(u'</div>\n</div>\n')
        # SOURCE LINE 55
        if c.returned_facets:
            # SOURCE LINE 56
            context.write(u'<div id="facet_container">\n<div id="facet_box_container">\n')
            # SOURCE LINE 58
            for facet in c.returned_facets:
                # SOURCE LINE 59
                context.write(u'<div id="')
                context.write(filters.decode.utf8(facet))
                context.write(u'">\n<strong>')
                # SOURCE LINE 60
                context.write(filters.decode.utf8(c.field_names[facet]))
                context.write(u'</strong>\n<ul id="cloud">\n')
                # SOURCE LINE 62
                if facet=="collection":
                    # SOURCE LINE 63
                    for result,value in c.returned_facets[facet]:
                        # SOURCE LINE 64
                        if result:
                            # SOURCE LINE 65
                            context.write(u'<li><a href="')
                            context.write(filters.decode.utf8(h.url_for(controller='/browse', action='field', field=c.rev_browsable[facet], item=result.decode('utf-8'))))
                            context.write(u'" class="')
                            context.write(filters.decode.utf8("tag%s" % (value)))
                            context.write(u'">')
                            context.write(filters.decode.utf8(g.f.ri.getDCTitle(result)))
                            context.write(u'</a></li>\n')
                    # SOURCE LINE 68
                else:
                    # SOURCE LINE 69
                    for result,value in c.returned_facets[facet]:
                        # SOURCE LINE 70
                        if result:
                            # SOURCE LINE 71
                            context.write(u'<li><a href="')
                            context.write(filters.decode.utf8(h.url_for(controller='/browse', action='field', field=c.rev_browsable[facet], item=result.decode('utf-8'))))
                            context.write(u'" class="')
                            context.write(filters.decode.utf8("tag%s" % (value)))
                            context.write(u'">')
                            context.write(filters.decode.utf8(result))
                            context.write(u'</a></li>\n')
                # SOURCE LINE 75
                context.write(u'</ul>\n</div>\n')
            # SOURCE LINE 78
            context.write(u'</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 47
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 49
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 3
        context.write(u'\n  <title> Browse - Search through the </title>\n  <style>\n    div#browse {\n       margin: 1em 2em;\n    }\n    div#facet_container {\n        margin-left: 3em;\n        border: 1px solid #cdcdcd;\n        background-color: #efefef;\n        float: left;\n    }\n    \n    div#facet_container h1 {\n        padding-left: 3em;\n    }\n    \n    div#facet_container div {\n        margin: 0 auto;\n        width: 100%;\n    }\n    \n    div#facet_container div div {\n        width: 90%;\n        float:left;\n        padding: 1em;\n    }\n    #cloud a.tag0 { font-size: 0.7em; font-weight: 100; }\n    #cloud a.tag1 { font-size: 0.8em; font-weight: 200; }\n    #cloud a.tag2 { font-size: 0.9em; font-weight: 300; }\n    #cloud a.tag3 { font-size: 1.0em; font-weight: 400; }\n    #cloud a.tag4 { font-size: 1.2em; font-weight: 500; }\n    #cloud a.tag5 { font-size: 1.4em; font-weight: 600; }\n    #cloud a.tag6 { font-size: 1.6em; font-weight: 700; }\n    #cloud a.tag7 { font-size: 1.8em; font-weight: 800; }\n    #cloud a.tag8 { font-size: 2.2em; font-weight: 900; }\n    #cloud a.tag9 { font-size: 2.5em; font-weight: 900; }\n    #cloud a.tag10 { font-size: 2.7em; font-weight: 1000; }\n    #cloud { padding: 2px; line-height: 3em; text-align: center; }\n    #cloud a { padding: 0px; }\n    #cloud { margin: 0; }\n    #cloud li { display: inline; }\n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


