from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206898265.23649
_template_filename='/home/archive/archive/archive/templates/type/default.mak'
_template_uri='/type/default.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['header', 'record_information', 'footer', 'head_tags']


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
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 117
        context.write(u'\n')
        # SOURCE LINE 119
        context.write(u'\n')
        # SOURCE LINE 121
        context.write(u'\n')
        # SOURCE LINE 138
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 118
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_record_information(context):
    context.caller_stack.push_frame()
    try:
        c = context.get('c', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 122
        context.write(u'\n<div id="metadata">\n')
        # SOURCE LINE 124
        runtime._include_file(context, '/type/citation.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 125
        runtime._include_file(context, '/type/display_search_terms.mak', _template_uri)
        context.write(u'\n<div id="trackback_link">Trackback URL: ')
        # SOURCE LINE 126
        context.write(filters.decode.utf8("%strackback/%s" % (g.root, c.id)))
        context.write(u'</div>\n<div id="relationships">\n')
        # SOURCE LINE 128
        runtime._include_file(context, '/relationship_display.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 129
        runtime._include_file(context, '/trackback_display.mak', _template_uri)
        context.write(u'\n</div>\n</div>\n<div id="right_column">\n')
        # SOURCE LINE 133
        runtime._include_file(context, '/type/terms.mak', _template_uri)
        context.write(u'\n')
        # SOURCE LINE 134
        if c.download_list:
            # SOURCE LINE 135
            runtime._include_file(context, '/type/downloads.mak', _template_uri)
            context.write(u'\n')
        # SOURCE LINE 137
        context.write(u'</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 120
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 3
        context.write(u'\n')
        # SOURCE LINE 4
        if c.id:
            # SOURCE LINE 5
            context.write(u'<!--\n<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n             xmlns:dc="http://purl.org/dc/elements/1.1/"\n             xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/">\n    <rdf:Description\n        rdf:about="')
            # SOURCE LINE 10
            context.write(filters.decode.utf8("info:fedora/%s" % c.id))
            context.write(u'"\n        dc:identifier="')
            # SOURCE LINE 11
            context.write(filters.decode.utf8("%sobjects/%s" % (g.root, c.id)))
            context.write(u'"\n        dc:title="')
            # SOURCE LINE 12
            context.write(filters.decode.utf8(c.title))
            context.write(u'"\n        trackback:ping=')
            # SOURCE LINE 13
            context.write(filters.decode.utf8("%strackback/%s" % (g.root, c.id)))
            context.write(u' />\n    </rdf:RDF>\n-->\n')
        # SOURCE LINE 17
        context.write(u'  ')
        context.write(filters.decode.utf8(self.title_text()))
        context.write(u'\n  <style>\n    div#record_wrapper {\n      margin: 1em 2em;\n      width: 95%\n    }\n    div#record_wrapper div {\n      margin: 0.8em;\n      border: 1px solid #cdcdcd;\n      background-color: #efefef;\n      padding: 0.8em;\n    }\n    div#record_wrapper div ul li {\n        line-height: 1.5em;\n    }\n    div#relationships_navigation {\n       margin: 0.5em auto !important;\n       background: transparent;\n       border: 1px solid #888;\n    }\n    div#relationships_navigation ul li {\n        list-style: none;\n        display: inline;\n    }\n    div#metadata{\n        float: left;\n        width: 49em;\n        padding: 0.5em 1em;\n    }\n    div.citation {\n        float: left;\n        border: 0px !important;\n        margin: 1em 0.3em !important;\n        background: transparent !important;\n    }\n    div.citation dl {\n        margin-left: 2em;\n    }\n    div#right_column {\n        margin: 0em !important;\n        padding: 0em !important;\n        float: right;\n        width: 15em;\n        border: 0px !important;\n        background: transparent !important;\n    }\n    div#right_column div {\n        width: 14em;\n        float: right;\n        font-size: 0.9em;\n        padding: 0.1em 0.8em !important;\n        background: #dedede;\n    }\n    div.link {\n        float: right;\n        margin-top:1em;\n        margin-right: 0.3em;\n    }\n    div#mods {\n        margin: 0em !important;\n        border: 0px !important;\n        background: transparent !important;\n        padding: 0em !important;\n    }\n    \n    div#mods div {\n        margin: 0em !important;\n        border: 0px !important;\n        background: transparent !important;\n        padding: 0em !important;\n    }\n    div#mods dl {\n        font-size: 0.8em;\n    }\n    div#mods .affiliations {\n        width: 25em;\n        float: right;\n    }\n    div#mods .mods_name_left {\n        float: left;\n        width: 14em;\n    }\n    div.clear {\n        clear: both;\n        height: 0px;\n        border: 0px !important;\n        background: transparent !important;\n        margin: 0em !important;\n        padding: 0em !important;\n    }\n    \n    dl.trackback {\n        font-size: 0.85em;\n    }\n    div#trackback_link {\n        text-align: right;\n        border: 0px !important;\n    }\n  ')
        # SOURCE LINE 115
        context.write(filters.decode.utf8(self.page_style()))
        context.write(u'\n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


