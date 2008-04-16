from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1204902496.527976
_template_filename='/home/archive/archive/archive/templates/tools.mak'
_template_uri='/tools.mak'
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
        # SOURCE LINE 2
        context.write(u'\n')
        # SOURCE LINE 10
        context.write(u'\n')
        # SOURCE LINE 12
        context.write(u'\n')
        # SOURCE LINE 14
        context.write(u'\n<div id="tools_wrapper">\n<div id="information_for_users">\n<h4> For Users of this site </h4>\n<dl>\n<dt>Freedom to search how you need to</dt>\n<dd>We have tried to make searching as flexible as possible</dd>\n</dl>\n<pre>\nOpenSearch compliant\nAtom feeds for search\nUNapi rollout for zotero/syndication\nComment/annotation overlay system\nItem view level\nImage collections\n</pre>\n</div>\n<div id="information_for_developers">\n<pre>\nFaceted search is url hackable\nSearch engine is exposed\nsensible/semantic urls via routes</pre>\n</div>\n</div>\n')
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
        context.write(u'\n  <title> Information - Tools for researchers and developers</title>\n  <style>\n    div#tools_wrapper {\n       margin: 1em 2em;\n    }\n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


