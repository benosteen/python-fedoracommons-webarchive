from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206972661.662071
_template_filename='/home/archive/archive/archive/templates/type/book.mak'
_template_uri='/type/book.mak'
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
        # SOURCE LINE 15
        context.write(u'\n<div id="record_wrapper">\n')
        # SOURCE LINE 17
        if c.title:
            # SOURCE LINE 18
            context.write(u'<p> ORA Book: <strong>"')
            context.write(filters.decode.utf8(c.title))
            context.write(u'"</strong></p>\n')
            # SOURCE LINE 19
        elif c.id:
            # SOURCE LINE 20
            context.write(u'<p> ORA Book: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</p>\n')
        # SOURCE LINE 22
        context.write(u'<div>\n')
        # SOURCE LINE 23
        for relation in c.relations:
            # SOURCE LINE 24
            if relation == 'isPartOf':
                # SOURCE LINE 25
                if [x for x in c.relations[relation] if x[2]=='type:imagecollection']:
                    # SOURCE LINE 26
                    context.write(u'<div class="subheading">Section List</div>\n')
                    # SOURCE LINE 27
                    context.write(filters.decode.utf8(h.form(h.url(controller="/objects"), method='get')))
                    context.write(u'\n    <select name="id">\n')
                    # SOURCE LINE 29
                    for item in [x for x in c.relations[relation] if x[2]=='type:imagecollection']:
                        # SOURCE LINE 30
                        context.write(u'      <option value="')
                        context.write(filters.decode.utf8(item[0]))
                        context.write(u'">')
                        context.write(filters.decode.utf8(item[1]))
                        context.write(u'</option>\n')
                    # SOURCE LINE 32
                    context.write(u'    </select>\n    ')
                    # SOURCE LINE 33
                    context.write(filters.decode.utf8(h.submit('Go')))
                    context.write(u'\n    ')
                    # SOURCE LINE 34
                    context.write(filters.decode.utf8(h.end_form()))
                    context.write(u'\n')
                    # SOURCE LINE 35
                elif [x for x in c.relations[relation] if x[2]=='type:image']:
                    # SOURCE LINE 36
                    context.write(u'<div class="subheading">Page List</div>\n')
                    # SOURCE LINE 37
                    context.write(filters.decode.utf8(h.form(h.url(controller="/objects", id=c.id), method='post')))
                    context.write(u'\n    <select name="inline">\n')
                    # SOURCE LINE 39
                    for item in [x for x in c.relations[relation] if x[2]=='type:image']:
                        # SOURCE LINE 40
                        context.write(u'      <option value="')
                        context.write(filters.decode.utf8(item[0]))
                        context.write(u'"\n')
                        # SOURCE LINE 41
                        if c.inline_object and c.inline_object==item[0]:
                            # SOURCE LINE 42
                            context.write(u" selected='true' \n")
                        # SOURCE LINE 44
                        context.write(u'      >')
                        context.write(filters.decode.utf8(item[1]))
                        context.write(u'</option>\n')
                    # SOURCE LINE 46
                    context.write(u'    </select>\n    ')
                    # SOURCE LINE 47
                    context.write(filters.decode.utf8(h.submit('Go')))
                    context.write(u'\n    ')
                    # SOURCE LINE 48
                    context.write(filters.decode.utf8(h.end_form()))
                    context.write(u'\n')
        # SOURCE LINE 52
        context.write(u'</div>\n')
        # SOURCE LINE 53
        if c.inline_object:
            # SOURCE LINE 54
            context.write(u'<div id="image_container">\n<a href="')
            # SOURCE LINE 55
            context.write(filters.decode.utf8(h.url_for(controller="/objects", id=c.inline_object)))
            context.write(u'">\n<img class="inline_image" src="')
            # SOURCE LINE 56
            context.write(filters.decode.utf8(h.url_for(controller="/objects", action="download", id=c.inline_object, dsid=c.model['inline_images'])))
            context.write(u'"/>\n</a>\n</div>\n')
        # SOURCE LINE 60
        context.write(u'<div class="clear">&nbsp;</div>\n<div id="metadata">\n')
        # SOURCE LINE 62
        runtime._include_file(context, '/type/display_search_terms.mak', _template_uri)
        context.write(u'\n<div id="trackback_link">Trackback URL: ')
        # SOURCE LINE 63
        context.write(filters.decode.utf8("%strackback/%s" % (g.root, c.id)))
        context.write(u'</div>\n<div id="relationships">\n')
        # SOURCE LINE 65
        runtime._include_file(context, '/forward_relationship_display.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 66
        runtime._include_file(context, '/object_relationship_navigation.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 67
        runtime._include_file(context, '/trackback_display.mak', _template_uri)
        context.write(u'\n</div>\n</div>\n<div id="right_column">\n')
        # SOURCE LINE 71
        if c.download_list:
            # SOURCE LINE 72
            runtime._include_file(context, '/type/downloads.mak', _template_uri)
            context.write(u'\n')
        # SOURCE LINE 74
        runtime._include_file(context, '/type/terms.mak', _template_uri)
        context.write(u'\n</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_page_style(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 10
        context.write(u'\n    img.inline_image {\n        max-width:60em;\n        height: auto;\n    }\n')
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
            context.write(u'<title> ORA Book: "')
            context.write(filters.decode.utf8(c.title))
            context.write(u'" - ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
            # SOURCE LINE 6
        elif c.id:
            # SOURCE LINE 7
            context.write(u'<title> ORA Book: ')
            context.write(filters.decode.utf8(c.id))
            context.write(u'</title>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


