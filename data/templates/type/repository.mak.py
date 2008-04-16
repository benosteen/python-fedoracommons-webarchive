from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206906655.312993
_template_filename='/home/archive/archive/archive/templates/type/repository.mak'
_template_uri='/type/repository.mak'
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
        # SOURCE LINE 15
        context.write(u'\n<div id="record_wrapper">\n')
        # SOURCE LINE 17
        if c.title:
            # SOURCE LINE 18
            context.write(u'<p> Repository: <strong>"')
            context.write(filters.decode.utf8(c.title))
            context.write(u'"</strong></p>\n')
            # SOURCE LINE 19
        elif c.id:
            # SOURCE LINE 20
            context.write(u'<p> Repository: ')
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
        context.write(u'</div>\n<div id="metadata">\n')
        # SOURCE LINE 28
        runtime._include_file(context, '/metadata/dc.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 29
        if c.metadata.get('REPOSITORY', None):
            # SOURCE LINE 30
            context.write(u'<div id="endpoints">\n<p> Endpoints: </p>\n<dl>\n')
            # SOURCE LINE 33
            for endpoint in c.metadata['REPOSITORY'].findall('endpoint'):
                # SOURCE LINE 34
                if endpoint.text:
                    # SOURCE LINE 35
                    context.write(u'<dt>')
                    context.write(filters.decode.utf8(endpoint.get('type').capitalize()))
                    context.write(u'</dt>\n')
                    # SOURCE LINE 36
                    if endpoint.text.startswith('http://'):
                        # SOURCE LINE 37
                        context.write(u'<dd><a href="')
                        context.write(filters.decode.utf8(endpoint.text))
                        context.write(u'">')
                        context.write(filters.decode.utf8(endpoint.text))
                        context.write(u'</a></dd>\n')
                        # SOURCE LINE 38
                    elif endpoint.text.startswith('uuid:') or endpoint.text.startswith('ora:'):
                        # SOURCE LINE 39
                        context.write(u'<dd><a href="')
                        context.write(filters.decode.utf8("%sobjects/%s" % (g.root, endpoint.text)))
                        context.write(u'">')
                        context.write(filters.decode.utf8(endpoint.text))
                        context.write(u'</a></dd>\n')
                        # SOURCE LINE 40
                    elif endpoint.text.startswith('urn:uuid:'):
                        # SOURCE LINE 41
                        context.write(u'<dd><a href="')
                        context.write(filters.decode.utf8("%sobjects/%s" % (g.root, endpoint.text[4:])))
                        context.write(u'">')
                        context.write(filters.decode.utf8(endpoint.text))
                        context.write(u'</a></dd>\n')
                        # SOURCE LINE 42
                    else:
                        # SOURCE LINE 43
                        context.write(u'<dd>')
                        context.write(filters.decode.utf8(endpoint.text))
                        context.write(u'</dd>\n')
            # SOURCE LINE 47
            context.write(u'</dl>\n</div>\n')
        # SOURCE LINE 50
        context.write(u'<div id="trackback_link">Trackback URL: ')
        context.write(filters.decode.utf8("%strackback/%s" % (g.root, c.id)))
        context.write(u'</div>\n<div id="relationships">\n')
        # SOURCE LINE 52
        runtime._include_file(context, '/relationship_display.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 53
        runtime._include_file(context, '/trackback_display.mak', _template_uri)
        context.write(u'\n</div>\n</div>\n<div id="right_column">\n')
        # SOURCE LINE 57
        runtime._include_file(context, '/type/terms.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 58
        if c.download_list:
            # SOURCE LINE 59
            runtime._include_file(context, '/type/downloads.mak', _template_uri)
            context.write(u'\n')
        # SOURCE LINE 61
        context.write(u'</div>\n</div>\n')
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
            context.write(u'<title> Repository: "')
            context.write(filters.decode.utf8(c.title))
            context.write(u'" - ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
            # SOURCE LINE 6
        elif c.id:
            # SOURCE LINE 7
            context.write(u'<title> Repository: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


