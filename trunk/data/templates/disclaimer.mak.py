from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206481644.0811019
_template_filename='/home/archive/archive/archive/templates/disclaimer.mak'
_template_uri='/disclaimer.mak'
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
        context.write(u'\n<div id="disclaimer">\n<h1>Disclaimer</h1>\n<p>Oxford University Library Services (OULS) provides some information to end users about the legitimate use and re-use of items held in ORA. However the University of Oxford is not responsible for any improper use made of the items by other parties.</p>\n<p>Staff at Oxford University Research Archive endeavour to comply with copyright permissions for all content of the archive. If they are made aware of the possibility of infringement of copyright for any item in ORA, the item will be removed from the archive as soon as possible whilst the complaint is investigated.</p>\n<p>ORA staff may offer advice and assistance checking and clearing copyright held by third parties but the responsibility for making an item available via ORA lies with the depositor.</p>\n</div>\n<div id="dataprotection">\n<h1>Data Protection</h1>\n<p>The information you supply will be used by the University of Oxford for administrative purposes within the terms of the Data Protection Act 1998. We shall not supply it to third parties.</p>\n</div>\n<div id="external_help">\n<p>For any additional help, please see the external ORA help and guidance website ')
        # SOURCE LINE 26
        context.write(filters.decode.utf8(h.link_to('here', "http://www.ouls.ox.ac.uk/ora")))
        context.write(u'</p>\n</div>\n')
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
        context.write(u'\n  <title> Help - Disclaimer and Data Protection statement</title>\n  <style>\n    div#disclaimer, div#dataprotection, div#external_help {\n       margin: 1em 2em;\n    }\n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


