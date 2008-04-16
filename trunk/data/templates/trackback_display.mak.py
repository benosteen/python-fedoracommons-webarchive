from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206604420.523649
_template_filename='/home/archive/archive/archive/templates/trackback_display.mak'
_template_uri='/trackback_display.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 1
        if c.trackbacks:
            # SOURCE LINE 2
            context.write(u'<div id="trackbacks">\n<p><strong>Trackbacks</strong></p>\n    <dl class="trackback">\n')
            # SOURCE LINE 5
            for trackback in c.trackbacks:
                # SOURCE LINE 6
                if c.trackbacks[trackback].get("dc:title", None):
                    # SOURCE LINE 7
                    context.write(u'<dt>')
                    context.write(filters.decode.utf8(c.trackbacks[trackback]["dc:title"][0]))
                    context.write(u'</dt>\n')
                # SOURCE LINE 9
                context.write(u'<dd>\n')
                # SOURCE LINE 10
                if c.trackbacks[trackback].get("dc:abstract", None):
                    # SOURCE LINE 11
                    context.write(u'<em>')
                    context.write(filters.decode.utf8(c.trackbacks[trackback]["dc:abstract"][0]))
                    context.write(u'</em> - \n')
                # SOURCE LINE 13
                if c.trackbacks[trackback].get("dc:creator", None):
                    # SOURCE LINE 14
                    if c.trackbacks[trackback].get("dc:creator", None)[0].startswith('http://'):
                        # SOURCE LINE 15
                        context.write(u'<a href="')
                        context.write(filters.decode.utf8(c.trackbacks[trackback]["dc:creator"][0]))
                        context.write(u'">')
                        context.write(filters.decode.utf8(c.trackbacks[trackback]["dc:creator"][0]))
                        context.write(u'</a>\n')
                        # SOURCE LINE 16
                    else:
                        # SOURCE LINE 17
                        context.write(filters.decode.utf8(c.trackbacks[trackback]["dc:creator"][0]))
                        context.write(u' \n')
                # SOURCE LINE 20
                for ident in c.trackbacks[trackback].get("dc:identifier", []):
                    # SOURCE LINE 21
                    if ident.startswith('http://'):
                        # SOURCE LINE 22
                        context.write(u'<a href="')
                        context.write(filters.decode.utf8(ident))
                        context.write(u'">')
                        context.write(filters.decode.utf8(ident))
                        context.write(u'</a>\n')
                        # SOURCE LINE 23
                    elif ident.startswith('uuid:'):
                        # SOURCE LINE 24
                        context.write(u' \n')
                        # SOURCE LINE 25
                    else:
                        # SOURCE LINE 26
                        context.write(filters.decode.utf8(ident))
                        context.write(u'\n')
                # SOURCE LINE 29
                for ident in c.trackbacks[trackback].get("dc:identifier", []):
                    # SOURCE LINE 30
                    if ident.startswith('uuid:'):
                        # SOURCE LINE 31
                        context.write(u'- <span class="small_link"><a href="')
                        context.write(filters.decode.utf8("%sobjects/%s" % (g.root, ident)))
                        context.write(u'"> (Archived information)</a></span>\n')
                # SOURCE LINE 34
                context.write(u'<dd>\n')
            # SOURCE LINE 36
            context.write(u'</dl>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


