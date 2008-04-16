from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206898265.1880131
_template_filename='/home/archive/archive/archive/templates/type/collection.mak'
_template_uri='/type/collection.mak'
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
        # SOURCE LINE 26
        context.write(u'\n<div id="record_wrapper">\n')
        # SOURCE LINE 28
        if c.title:
            # SOURCE LINE 29
            context.write(u'<p> ORA Collection: <strong>"')
            context.write(filters.decode.utf8(c.title))
            context.write(u'"</strong></p>\n')
            # SOURCE LINE 30
        elif c.id:
            # SOURCE LINE 31
            context.write(u'<p> ORA Collection: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</p>\n')
        # SOURCE LINE 33
        if c.image_list:
            # SOURCE LINE 34
            context.write(u'<div id="branding_container">\n')
            # SOURCE LINE 35
            if c.metadata.get('DC', None) and '{http://purl.org/dc/elements/1.1/}relation' in [e.tag for e in c.metadata['DC'].getchildren()]:
                # SOURCE LINE 36
                context.write(u'<a href="')
                context.write(filters.decode.utf8(c.metadata['DC'].find('{http://purl.org/dc/elements/1.1/}relation').text))
                context.write(u'">\n')
                # SOURCE LINE 37
                for image in c.image_list:
                    # SOURCE LINE 38
                    context.write(u'<img class="branding" src="')
                    context.write(filters.decode.utf8(h.url_for(controller="/objects", action="download", id=c.id, dsid=image['dsid'])))
                    context.write(u'"/>\n')
                # SOURCE LINE 40
                context.write(u'</a>\n')
                # SOURCE LINE 41
            else:
                # SOURCE LINE 42
                for image in c.image_list:
                    # SOURCE LINE 43
                    context.write(u'<img class="branding" src="')
                    context.write(filters.decode.utf8(h.url_for(controller="/objects", action="download", id=c.id, dsid=image['dsid'])))
                    context.write(u'"/>\n')
            # SOURCE LINE 46
            context.write(u'</div>\n<div id="collection_metadata_with_branding">\n')
            # SOURCE LINE 48
            runtime._include_file(context, '/metadata/dc.mak', _template_uri)
            context.write(u'\n<div id="trackback_link">Trackback URL: ')
            # SOURCE LINE 49
            context.write(filters.decode.utf8("%strackback/%s" % (g.root, c.id)))
            context.write(u'</div>\n</div>\n')
            # SOURCE LINE 51
        else:
            # SOURCE LINE 52
            context.write(u'<div id="collection_metadata_without_branding">\n')
            # SOURCE LINE 53
            runtime._include_file(context, '/metadata/dc.mak', _template_uri)
            context.write(u'\n<div id="trackback_link">\n<a href="')
            # SOURCE LINE 55
            context.write(filters.decode.utf8("%strackback/%s" % (g.root, c.id)))
            context.write(u'">Trackback URL</a>\n</div>\n</div>\n')
        # SOURCE LINE 59
        context.write(u'<div class="clear">&nbsp;</div>\n<div id="collection">\n')
        # SOURCE LINE 61
        runtime._include_file(context, '/collection_response_display.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 62
        runtime._include_file(context, '/relationship_display.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 63
        runtime._include_file(context, '/trackback_display.mak', _template_uri)
        context.write(u'\n</div>\n')
        # SOURCE LINE 65
        runtime._include_file(context, '/type/terms.mak', _template_uri)
        context.write(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_page_style(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 10
        context.write(u'\n    div#branding_container {\n        float:right;\n        width: auto;\n        margin-left: 0em !important;\n    }\n    div#collection_metadata_with_branding {\n        float: left;\n        width: 25em;\n        margin-right: 0em !important;\n    }\n    div#collection_metadata_without_branding {\n        float: left;\n        width: 65em;\n        margin-right: 0em !important;\n    }\n')
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
            context.write(u'<title> ORA Collection: "')
            context.write(filters.decode.utf8(c.title))
            context.write(u'" - ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
            # SOURCE LINE 6
        elif c.id:
            # SOURCE LINE 7
            context.write(u'<title> ORA Collection: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


