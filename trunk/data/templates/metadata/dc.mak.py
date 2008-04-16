from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206683004.6960981
_template_filename='/home/archive/archive/archive/templates/metadata/dc.mak'
_template_uri='/metadata/dc.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 2
        if c.metadata.get('DC', None):
            # SOURCE LINE 3
            context.write(u'<dl>\n')
            # SOURCE LINE 4
            for element in  c.metadata['DC'].getchildren():
                # SOURCE LINE 5
                if element.text:
                    # SOURCE LINE 6
                    context.write(u'<dt>')
                    context.write(filters.decode.utf8(element.tag.split('}')[-1].capitalize()))
                    context.write(u'</dt>\n')
                    # SOURCE LINE 7
                    if element.text.startswith('http://'):
                        # SOURCE LINE 8
                        context.write(u'<dd><a href="')
                        context.write(filters.decode.utf8(element.text))
                        context.write(u'">')
                        context.write(filters.decode.utf8(element.text))
                        context.write(u'</a></dd>\n')
                        # SOURCE LINE 9
                    elif element.text.startswith('uuid:') or element.text.startswith('ora:'):
                        # SOURCE LINE 10
                        context.write(u'<dd><a href="')
                        context.write(filters.decode.utf8("%sobjects/%s" % (g.root, element.text)))
                        context.write(u'">')
                        context.write(filters.decode.utf8(element.text))
                        context.write(u'</a></dd>\n')
                        # SOURCE LINE 11
                    elif element.text.startswith('urn:uuid:'):
                        # SOURCE LINE 12
                        context.write(u'<dd><a href="')
                        context.write(filters.decode.utf8("%sobjects/%s" % (g.root, element.text[4:])))
                        context.write(u'">')
                        context.write(filters.decode.utf8(element.text))
                        context.write(u'</a></dd>\n')
                        # SOURCE LINE 13
                    else:
                        # SOURCE LINE 14
                        context.write(u'<dd>')
                        context.write(filters.decode.utf8(element.text))
                        context.write(u'</dd>\n')
            # SOURCE LINE 18
            context.write(u'</dl>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


