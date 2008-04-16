from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1204716622.9953361
_template_filename='/home/archive/archive/archive/templates/contribute.mak'
_template_uri='/contribute.mak'
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
        # SOURCE LINE 28
        context.write(u'\n')
        # SOURCE LINE 30
        context.write(u'\n')
        # SOURCE LINE 32
        context.write(u'\n<div id="contribute">\n<h3>Contribute to the Oxford University Research Archive</h3>\n<div id="thesis_submission">\n<p>')
        # SOURCE LINE 36
        context.write(filters.decode.utf8(h.link_to('Click here to submit a <strong>Thesis</strong> to the Oxford Research Archive', "http://ora.ouls.ox.ac.uk/cgi-bin/valet/submit.cgi?view=ethesis")))
        context.write(u'</p>\n</div>\n<div id="general_item_submission">\n<p>')
        # SOURCE LINE 39
        context.write(filters.decode.utf8(h.link_to('Click here to submit a <strong>Journal article</strong> or a <strong>conference/workshop paper</strong> or any other <strong>general item of research</strong> (Image, report, book chapter, etc) to the Oxford Research Archive', "http://ora.ouls.ox.ac.uk/cgi-bin/valet/submit.cgi?view=epapers")))
        context.write(u'</p>\n</div>\n<div id="conference">\n<p>')
        # SOURCE LINE 42
        context.write(filters.decode.utf8(h.link_to('Click here to register a <strong>conference or workshop</strong> with the Oxford Research Archive - This is to help group together papers which were given at the same conference or workshop.', "http://ora.ouls.ox.ac.uk/cgi-bin/valet/submit.cgi?view=conference")))
        context.write(u'</p>\n</div>\n<div id="notices">\n<p><em>* OUCS-provided Oxford Single-Sign-On account is required:</em></p>\n<p>')
        # SOURCE LINE 46
        context.write(filters.decode.utf8(h.link_to('See more information about getting an account here.', "http://www.oucs.ox.ac.uk/registration/oxford/index.xml.ID=body.1_div.2")))
        context.write(u'</p>\n</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 29
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 31
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 3
        context.write(u'\n  <title> Information - Disclaimer and Data Protection statement</title>\n  <style>\n    div#contribute {\n       margin: 1em 2em;\n    }\n    div#thesis_submission, div#general_item_submission, div#conference {\n        margin: 2em;\n        border: 1px solid #e7e5d8;\n    }\n    div#notices {\n        margin: 2em;\n    }\n    \n    div#thesis_submission p, div#general_item_submission p, div#conference p, div#notices p {\n        margin: 2em;\n        font-size: 1.3em;\n    }\n    \n    div#thesis_submission p a, div#general_item_submission p a, div#conference p a, div#notices p a {\n        font-weight:normal;\n        text-transform:none;\n        text-decoration:none;\n    }\n  </style>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


