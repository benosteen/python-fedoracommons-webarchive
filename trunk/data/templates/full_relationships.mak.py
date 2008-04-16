from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206477462.968914
_template_filename='/home/archive/archive/archive/templates/full_relationships.mak'
_template_uri='/full_relationships.mak'
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
        # SOURCE LINE 35
        context.write(u'\n')
        # SOURCE LINE 37
        context.write(u'\n')
        # SOURCE LINE 39
        context.write(u'\n<div id="relationships_wrapper">\n<div id="relationships">\n')
        # SOURCE LINE 42
        runtime._include_file(context, '/relationship_display.mak', _template_uri)
        context.write(u'\n<div id="all_relationships">\n<div class="subheading"> All relationships for ')
        # SOURCE LINE 44
        context.write(filters.decode.utf8(c.title))
        context.write(u'</div>\n<ul>\n')
        # SOURCE LINE 46
        for s,p,o in c.graph.triples((None, None, None)):
            # SOURCE LINE 47
            context.write(u'<li>\n')
            # SOURCE LINE 48
            if s.startswith('info:fedora/uuid') or s.startswith('info:fedora/ora'):
                # SOURCE LINE 49
                if len(s.split('/'))==3:
                    # SOURCE LINE 50
                    context.write(u'<a href="')
                    context.write(filters.decode.utf8("%sresolve/%s" % (g.root, s)))
                    context.write(u'">')
                    context.write(filters.decode.utf8("%s" % s.split('/')[2]))
                    context.write(u'</a>\n')
                    # SOURCE LINE 51
                else:
                    # SOURCE LINE 52
                    context.write(filters.decode.utf8(h.link_to(g.f.ri.getDCTitle(s.split('/')[1]), h.url_for(controller="/objects", id=s.split('/')[1]))))
                    context.write(u'\n')
                # SOURCE LINE 54
            elif s.startswith('http://'):
                # SOURCE LINE 55
                context.write(u'<a href="')
                context.write(filters.decode.utf8(s))
                context.write(u'">')
                context.write(filters.decode.utf8(s))
                context.write(u'</a>\n')
                # SOURCE LINE 56
            else:
                # SOURCE LINE 57
                context.write(filters.decode.utf8(s))
                context.write(u'\n')
            # SOURCE LINE 59
            if p.startswith('http://'):
                # SOURCE LINE 60
                context.write(u'<a href="')
                context.write(filters.decode.utf8(p))
                context.write(u'">')
                context.write(filters.decode.utf8(p))
                context.write(u'</a>\n')
                # SOURCE LINE 61
            else:
                # SOURCE LINE 62
                context.write(filters.decode.utf8(p))
                context.write(u'\n')
            # SOURCE LINE 64
            if o.startswith('info:fedora/uuid') or o.startswith('info:fedora/ora'):
                # SOURCE LINE 65
                if len(o.split('/'))==3:
                    # SOURCE LINE 66
                    context.write(u'<a href="')
                    context.write(filters.decode.utf8("%sresolve/%s" % (g.root, o)))
                    context.write(u'">')
                    context.write(filters.decode.utf8("%s" % o.split('/')[2]))
                    context.write(u'</a>\n')
                    # SOURCE LINE 67
                else:
                    # SOURCE LINE 68
                    context.write(filters.decode.utf8(h.link_to(g.f.ri.getDCTitle(o.split('/')[1]), h.url_for(controller="/objects", id=o.split('/')[1]))))
                    context.write(u'\n')
                # SOURCE LINE 70
            elif o.startswith('http://'):
                # SOURCE LINE 71
                context.write(u'<a href="')
                context.write(filters.decode.utf8(o))
                context.write(u'">')
                context.write(filters.decode.utf8(o))
                context.write(u'</a>\n')
                # SOURCE LINE 72
            else:
                # SOURCE LINE 73
                context.write(filters.decode.utf8(o))
                context.write(u'\n')
            # SOURCE LINE 75
            context.write(u'</li>\n')
        # SOURCE LINE 77
        context.write(u'</ul>\n</div>\n</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 36
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 38
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
        context.write(u'</title>\n  <style>\n    div#relationships {\n       margin: 1em 2em;\n       float:left;\n       background: transparent;\n    }\n    div#relationships_navigation {\n       margin: 1em 2em;\n       float:right;\n       background: transparent;\n       border: 1px solid #888;\n    }\n    div#relationships_navigation ul li {\n        list-style: none;\n        display: inline;\n    }\n    \n    span.object_title {\n        color: #2288dd;\n    }\n    \n    span.uuid {\n        color: #999 !important;\n        font-style: italic !important;\n        font-size: 0.8em !important;\n    }\n    div#all_relationships {\n        font-size: 0.8em;\n    }\n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


