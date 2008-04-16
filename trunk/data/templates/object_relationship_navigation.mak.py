from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206480633.7114639
_template_filename='/home/archive/archive/archive/templates/object_relationship_navigation.mak'
_template_uri='/object_relationship_navigation.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'<div id="relationships_navigation">\n<label for="relationships_navigation_list">View full list as RDF in format:</label>\n<ul id="relationships_navigation_list">\n<li>')
        # SOURCE LINE 5
        context.write(filters.decode.utf8(h.link_to( 'HTML Lite', h.url_for(action="relationships", format='htmllite') )))
        context.write(u'</li>\n<li>')
        # SOURCE LINE 6
        context.write(filters.decode.utf8(h.link_to( 'HTML Full', h.url_for(action="relationships",format='html') )))
        context.write(u'</li>\n<li>')
        # SOURCE LINE 7
        context.write(filters.decode.utf8(h.link_to( 'RDF/XML', h.url_for(action="relationships",format='xml') )))
        context.write(u'</li>\n<li>')
        # SOURCE LINE 8
        context.write(filters.decode.utf8(h.link_to( 'N-Triples', h.url_for(action="relationships",format='nt') )))
        context.write(u'</li>\n<li>')
        # SOURCE LINE 9
        context.write(filters.decode.utf8(h.link_to( 'N3', h.url_for(action="relationships",format='n3') )))
        context.write(u'</li>\n<li>')
        # SOURCE LINE 10
        context.write(filters.decode.utf8(h.link_to( 'Turtle', h.url_for(action="relationships",format='turtle') )))
        context.write(u'</li>\n</ul>\n</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


