from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1207020247.5233481
_template_filename='/home/archive/archive/archive/templates/accessibility.mak'
_template_uri='/accessibility.mak'
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
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 10
        context.write(u'\n')
        # SOURCE LINE 12
        context.write(u'\n')
        # SOURCE LINE 14
        context.write(u'\n<div id="accessibility_statement">\n<h1>Accessibility Statement</h1>\n<p>This is the accessibility statement for the Oxford University Libraries website. It covers the main site at http://ora.ouls.ox.ac.uk/. Other sites which are linked from the top level  are not covered by this statement. Work is continuing to further improve the accessibility and usability of the site.</p>\n<p>If you have any questions or comments about the accessibility of this site, please contact the webmaster.</p>\n\n<dl>\n<dt>Navigation aids</dt>\n<dd>The site uses a consistent navigation system visually located at the top right of the page.</dd>\n<dt>Tables</dt>\n<dd>Tables are used to display tabular information only. The content of the page is contained in semantically labelled \'div\' elements.</dd>\n<dt>Images</dt>\n<dd>Images include descriptive ALT attributes. Purely decorative graphics would include null ALT attributes.</dd>\n<dt>Visual design</dt>\n<dd>This site uses cascading style sheets for visual layout. If your browser or browsing device does not support style sheets at all, the content of each page is still readable. The website uses a layout scheme that allows the scale of the page to be increased by increasing the text size in visual browsers for the visually-impaired.</dd>\n</dl>\n<p>See also the central ')
        # SOURCE LINE 30
        context.write(filters.decode.utf8(h.link_to("Oxford University's Web Accessibility Policy", "http://www.ox.ac.uk/web/accessibility.html")))
        context.write(u'. </p>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 11
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 13
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 3
        context.write(u'\n  <title> Information - Disclaimer and Data Protection statement</title>\n  <style>\n    div#accessibility_statement {\n       margin: 1em 2em;\n    }\n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


