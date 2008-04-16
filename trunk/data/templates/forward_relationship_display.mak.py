from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1207140336.0631881
_template_filename='/home/ben/Desktop/archive/archive/templates/forward_relationship_display.mak'
_template_uri='/forward_relationship_display.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 2
        if c.graph:
            # SOURCE LINE 3
            for term in c.f_ontol:
                # SOURCE LINE 4
                for s,p,o in c.graph.triples((c.fedora_uri, c.f_ontol[term], None)):
                    # SOURCE LINE 5
                    if o.startswith('info:fedora/') and not o.startswith('info:fedora/type'):
                        # SOURCE LINE 6
                        if len(o.split('/'))==3:
                            # SOURCE LINE 7
                            context.write(u'<p> <span class="verbal_relationship">')
                            context.write(filters.decode.utf8(term % ('<a href="%sresolve/%s">%s</a>)' % (g.root, o, o.split("/")[2]) )))
                            context.write(u'</span></p>\n')
                            # SOURCE LINE 8
                        else:
                            # SOURCE LINE 9
                            context.write(u'<p> <span class="verbal_relationship">')
                            context.write(filters.decode.utf8(term % (h.link_to(g.f.ri.getDCTitle(o.split('/')[1]), h.url_for(controller="/objects", id=o.split('/')[1])))))
                            context.write(u'</span></p>\n')
                        # SOURCE LINE 11
                    elif o.startswith('http://'):
                        # SOURCE LINE 12
                        context.write(u'<p> <span class="verbal_relationship">')
                        context.write(filters.decode.utf8(term % ('<a href="%s">%s</a>' % (o,o))))
                        context.write(u'</span></p>\n')
                        # SOURCE LINE 13
                    else:
                        # SOURCE LINE 14
                        context.write(u'<p> <span class="verbal_relationship">')
                        context.write(filters.decode.utf8(term % (o)))
                        context.write(u'</span></p>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


