from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206913005.191421
_template_filename='/home/archive/archive/archive/templates/type/image.mak'
_template_uri='/type/image.mak'
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
        # SOURCE LINE 19
        context.write(u'\n<div id="record_wrapper">\n')
        # SOURCE LINE 21
        if c.title:
            # SOURCE LINE 22
            context.write(u'<p> ORA Image: <strong>"')
            context.write(filters.decode.utf8(c.title))
            context.write(u'"</strong></p>\n')
            # SOURCE LINE 23
        elif c.id:
            # SOURCE LINE 24
            context.write(u'<p> ORA Image: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</p>\n')
        # SOURCE LINE 26
        context.write(u'<div id="image_container">\n')
        # SOURCE LINE 27
        for image in c.image_list:
            # SOURCE LINE 28
            context.write(u'<a href="')
            context.write(filters.decode.utf8(h.url_for(controller="/objects", action="download", id=c.id, dsid=image['dsid'])))
            context.write(u'">\n<img class="inline_image" src="')
            # SOURCE LINE 29
            context.write(filters.decode.utf8(h.url_for(controller="/objects", action="download", id=c.id, dsid=image['dsid'])))
            context.write(u'"/>\n</a>\n')
        # SOURCE LINE 32
        context.write(u'</div>\n<div id="metadata">\n')
        # SOURCE LINE 34
        runtime._include_file(context, '/metadata/dc.mak', _template_uri)
        context.write(u'\n<div id="trackback_link">Trackback URL: ')
        # SOURCE LINE 35
        context.write(filters.decode.utf8("%strackback/%s" % (g.root, c.id)))
        context.write(u'</div>\n')
        # SOURCE LINE 36
        runtime._include_file(context, '/relationship_display.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 37
        runtime._include_file(context, '/trackback_display.mak', _template_uri)
        context.write(u'\n</div>\n<div id="right_column">\n')
        # SOURCE LINE 40
        if c.download_list:
            # SOURCE LINE 41
            runtime._include_file(context, '/type/downloads.mak', _template_uri)
            context.write(u'\n')
        # SOURCE LINE 43
        runtime._include_file(context, '/type/terms.mak', _template_uri)
        context.write(u'\n</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_page_style(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 10
        context.write(u'\n    div#image_container {\n        width: 90%;\n        float: left;\n    }\n    img.inline_image {\n        max-width:60em;\n        height: auto;\n    }\n')
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
            context.write(u'<title> ORA Image: "')
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


