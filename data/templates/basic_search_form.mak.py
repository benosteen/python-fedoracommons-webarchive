from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206476900.41925
_template_filename='/home/archive/archive/archive/templates/basic_search_form.mak'
_template_uri='/basic_search_form.mak'
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
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'\n\n')
        # SOURCE LINE 178
        context.write(u'\n')
        # SOURCE LINE 180
        context.write(u'\n')
        # SOURCE LINE 182
        context.write(u'\n<div id="results_wrapper">\n<div id="results" style="width:70em;">\n<p>Search results from query: <em>')
        # SOURCE LINE 185
        context.write(filters.decode.utf8(c.q))
        context.write(u'</em> </p>\n')
        # SOURCE LINE 186
        runtime._include_file(context, '/search_response_display.mak', _template_uri)
        context.write(u'\n</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 179
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 181
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 4
        context.write(u'\n  <title> Advanced Search - Functionality Demo</title>\n  <style>    \n    #q {\n        width: 8em;\n    }\n        \n    div#search_wrapper {\n        width: 100%;\n        min-width: 740px;\n        margin: 0 auto;\n    }\n    \n    div.link {\n        float: right;\n        margin-top:1em;\n        margin-right: 0.3em;\n    }\n    div.link a {\n        padding: 0.1em;\n        border: 1px solid #5599dd;\n\n    }\n    dt.label {\n        font-weight: bold;\n        color: #3399ee;\n        padding-left:3.5em;\n    }\n    dd.value {\n        font-weight: normal;\n        color: #565656;\n    }\n    li.title span {\n        font-size: +1;\n    }\n    \n    \n    #facets {\n        float: left;\n        width: 45em;\n        margin-left: 1em;\n    }\n    \n    \n    #search_box {\n        float: left;\n        width: 20em;\n        margin-left: 1em;\n    }\n    \n    div.response_doc {\n        margin: 0.4em;\n        border: 1px solid #aaa8a1;\n        background-color: #efefef;\n    }\n    span.toggle {\n        padding: 0.1em;\n        margin: 0.1em;\n        background-color: #ffffff;\n        border: 1px solid #5599dd;\n        float: left;\n        width: 14em;\n    }\n    span.toggle_label {\n        float: right;\n        margin-right: 0.3em;\n        margin-top: 0.2em;\n    }\n    \n    span.toggle input {\n        float: left;\n        margin-right: 0.5em;\n        color: #000000; \n        border: 1px #7799aa solid;\n    }\n    \n    div.clear {\n        clear: both;\n    }\n    \n    div.facets {\n        padding: 0.3em;\n        border: 1px solid #aaa8a1;\n        background-color: #efefef;\n        max-width: 62em;\n    }\n    \n    div#fields {\n        float: right;\n    }\n    \n    #rows {\n        width: 3em;\n    }\n    \n    #view {\n        width: 6em;\n    }\n    \n\n    #search_box p, #facets p {\n        font-size: 1.5em;\n    }\n    \n    .facet_results {\n        float: left;\n        width: 14em;\n        padding-bottom: 1em;\n    }\n    \n    .facet_results ul li {\n        list-decoration: none;\n    }\n    \n    span.pagination_label form, span.label form {\n        display:inline;\n        cursor: pointer;\n    }\n    \n    span.pagination_label form button, span.pagination_label form input {\n        border: 0px;\n        background-color: #fff;\n        color: #3355ee;\n        cursor: pointer;\n    }\n    \n    p.no_facets {\n        color: #aaaaaa;\n        font-style: italic;\n        width: 10em;\n    }\n    div#facet_container {\n        background-color: #fff;\n        width: 15em;\n        float: left;\n    }\n    div#results {\n        background-color: #fff;\n        width: 54em;\n        float: right;\n    }\n    div#results_wrapper, div#search_box_wrapper {\n        background-color:#fff;\n        width: 70em;\n        margin: 0 auto;\n        \n    }\n    span.document_number {\n        float: left;\n        padding: 0.2em;\n        margin: 0.2em;\n        border:1px solid #999;\n        font-weight: bold;\n    }\n    \n    .checkbox {\n        // !important Because IE doesn\'t want to listen...\n        border: 0px !important;\n    }\n    \n  </style>\n  <script type="text/javascript">\n<!--\nfunction switchMenu(obj) {\n\tvar el = document.getElementById(obj);\n\tif ( el.style.display != "none" ) {\n\t\tel.style.display = \'none\';\n\t}\n\telse {\n\t\tel.style.display = \'\';\n\t}\n}\n//-->\n</script>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


