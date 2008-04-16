from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206902278.819129
_template_filename='/home/archive/archive/archive/templates/type/journal_article.mak'
_template_uri='/type/journal_article.mak'
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
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 9
        context.write(u'\n')
        # SOURCE LINE 11
        context.write(u'\n<div id="record_wrapper">\n')
        # SOURCE LINE 13
        if c.title:
            # SOURCE LINE 14
            context.write(u'<p> ORA Journal Article: <strong>"')
            context.write(filters.decode.utf8(c.title))
            context.write(u'"</strong></p>\n')
            # SOURCE LINE 15
        elif c.id:
            # SOURCE LINE 16
            context.write(u'<p> ORA Journal Article: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</p>\n')
        # SOURCE LINE 18
        context.write(u'<div id="metadata">\n')
        # SOURCE LINE 19
        runtime._include_file(context, '/type/citation.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 20
        runtime._include_file(context, '/metadata/mods.mak', _template_uri)
        context.write(u'\n<div id="trackback_link">Trackback URL: ')
        # SOURCE LINE 21
        context.write(filters.decode.utf8("%strackback/%s" % (g.root, c.id)))
        context.write(u'</div>\n<div id="relationships">\n')
        # SOURCE LINE 23
        runtime._include_file(context, '/relationship_display.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 24
        runtime._include_file(context, '/trackback_display.mak', _template_uri)
        context.write(u'\n</div>\n</div>\n<div id="right_column">\n')
        # SOURCE LINE 28
        runtime._include_file(context, '/type/terms.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 29
        if c.download_list:
            # SOURCE LINE 30
            runtime._include_file(context, '/type/downloads.mak', _template_uri)
            context.write(u'\n')
        # SOURCE LINE 32
        context.write(u'</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_page_style(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 10
        context.write(u'\n')
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
            context.write(u'<title> ORA Journal Article: "')
            context.write(filters.decode.utf8(c.title))
            context.write(u'" - ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
            # SOURCE LINE 6
        elif c.id:
            # SOURCE LINE 7
            context.write(u'<title> ORA Journal Article: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


