from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206467863.6233881
_template_filename='/home/archive/archive/archive/templates/type/downloads.mak'
_template_uri='/type/downloads.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<div id="download_list">\n<div class="subheading"> Downloads </div>\n')
        # SOURCE LINE 3
        for dsid_props in c.download_list:
            # SOURCE LINE 4
            context.write(u'<p>')
            context.write(filters.decode.utf8(h.link_to( "%s" % (dsid_props.get('winname', '-Download').split('-')[-1]), h.url_for(controller="/objects", action="download", id=c.id, dsid=dsid_props.get('dsid', None)) )))
            context.write(u'  ')
            context.write(filters.decode.utf8(dsid_props.get('label', '')))
            context.write(u'</p>\n')
        # SOURCE LINE 6
        context.write(u'</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


