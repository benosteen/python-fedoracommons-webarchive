from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206900538.583565
_template_filename='/home/archive/archive/archive/templates/type/conference.mak'
_template_uri='/type/conference.mak'
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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 9
        context.write(u'\n')
        # SOURCE LINE 18
        context.write(u'\n<div id="record_wrapper">\n')
        # SOURCE LINE 20
        if c.title:
            # SOURCE LINE 21
            context.write(u'<p> ORA Conference: <strong>"')
            context.write(filters.decode.utf8(c.title))
            context.write(u'"</strong></p>\n')
            # SOURCE LINE 22
        elif c.id:
            # SOURCE LINE 23
            context.write(u'<p> ORA Conference: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</p>\n')
        # SOURCE LINE 25
        context.write(u'<div id="metadata">\n')
        # SOURCE LINE 26
        runtime._include_file(context, '/type/citation.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 27
        runtime._include_file(context, '/type/display_search_terms.mak', _template_uri)
        context.write(u'\n<div id="trackback_link">Trackback URL: ')
        # SOURCE LINE 28
        context.write(filters.decode.utf8("%strackback/%s" % (g.root, c.id)))
        context.write(u'</div>\n')
        # SOURCE LINE 29
        if c.graph:
            # SOURCE LINE 30
            context.write(u'<div id="conferenceitems">\n<div class="subheading">Conference/Workshop Papers:</div>\n<ul>\n')
            # SOURCE LINE 33
            for s,p,o in c.graph.triples((None, c.rel['isPartOf'], c.fedora_uri)):
                # SOURCE LINE 34
                context.write(u'<li>')
                context.write(filters.decode.utf8(h.link_to(g.f.ri.getDCTitle(s.split('/')[1]), h.url_for(controller="/objects", id=s.split('/')[1]))))
                context.write(u'</li>\n')
            # SOURCE LINE 36
            context.write(u'</ul>\n')
        # SOURCE LINE 38
        context.write(u'</div>\n\n<div id="relationships">\n')
        # SOURCE LINE 41
        runtime._include_file(context, '/forward_relationship_display.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 42
        runtime._include_file(context, '/object_relationship_navigation.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 43
        runtime._include_file(context, '/trackback_display.mak', _template_uri)
        context.write(u'\n</div>\n</div>\n<div id="right_column">\n')
        # SOURCE LINE 47
        runtime._include_file(context, '/type/terms.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 48
        if c.download_list:
            # SOURCE LINE 49
            runtime._include_file(context, '/type/downloads.mak', _template_uri)
            context.write(u'\n')
        # SOURCE LINE 51
        context.write(u'</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_page_style(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 10
        context.write(u'\n    div#conferenceitems ul {\n        margin-left: 2em;\n    }\n    \n    div#conferenceitems ul li {    \n        padding-bottom: 0.5em;\n    }\n')
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
            context.write(u'<title> ORA Conference: "')
            context.write(filters.decode.utf8(c.title))
            context.write(u'" - ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
            # SOURCE LINE 6
        elif c.id:
            # SOURCE LINE 7
            context.write(u'<title> ORA Conference: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


