from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206467863.7517171
_template_filename='/home/archive/archive/archive/templates/type/terms.mak'
_template_uri='/type/terms.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<div id="terms_of_use">\n<div class="subheading">Terms of Use</div>\n<p>The copyright of this item rests with the author and/or other copyright holder(s).</p>\n<p> ')
        # SOURCE LINE 4
        context.write(filters.decode.utf8(h.link_to('Click here for our Terms of Use', h.url_for(controller="/objects", id="uuid:1d00eebb-8fed-46ad-8e38-45dbdb4b224c") )))
        context.write(u'</p>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


