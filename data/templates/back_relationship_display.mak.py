from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206480633.685518
_template_filename='/home/archive/archive/archive/templates/back_relationship_display.mak'
_template_uri='/back_relationship_display.mak'
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
            for term in c.b_ontol:
                # SOURCE LINE 4
                for s,p,o in c.graph.triples((None, c.b_ontol[term], c.fedora_uri)):
                    # SOURCE LINE 5
                    context.write(u'<p> <span class="verbal_relationship">')
                    context.write(filters.decode.utf8(term % (h.link_to(g.f.ri.getDCTitle(s.split('/')[1]), h.url_for(controller="/objects", id=s.split('/')[1])))))
                    context.write(u'</span></p>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


