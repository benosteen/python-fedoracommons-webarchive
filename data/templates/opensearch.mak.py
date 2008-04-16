from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206713105.6909239
_template_filename='/home/archive/archive/archive/templates/opensearch.mak'
_template_uri='/opensearch.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='UTF-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<?xml version="1.0" encoding="UTF-8"?>\n <OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/" xmlns:moz="http://www.mozilla.org/2006/browser/search/">\n   <ShortName>ORA Search</ShortName>\n   <Description>Search inside the content of the Oxford University Research Archive.</Description>\n   <Url type="application/atom+xml"\n        template="')
        # SOURCE LINE 6
        context.write(filters.decode.utf8(g.root))
        context.write(filters.decode.utf8(h.url_for(controller='search', action='detailed')))
        context.write(u'?q={searchTerms}&amp;view=Default&amp;start={startIndex?}&amp;format=atom"/>\n   <Url type="text/html" \n        template="')
        # SOURCE LINE 8
        context.write(filters.decode.utf8(g.root))
        context.write(filters.decode.utf8(h.url_for(controller='search', action='detailed')))
        context.write(u'?q={searchTerms}&amp;start={startIndex?}"/>\n   <Image height="16" width="16" type="image/x-icon">http://archive.sers.ox.ac.uk:5000/favicon.ico</Image>\n   <Tags>example web</Tags>\n   <Contact>admin@example.com</Contact>\n   <AdultContent>false</AdultContent>\n   <Language>en-gb</Language>\n   <OutputEncoding>UTF-8</OutputEncoding>\n   <InputEncoding>UTF-8</InputEncoding>\n   <moz:SearchForm>')
        # SOURCE LINE 16
        context.write(filters.decode.utf8(g.root))
        context.write(filters.decode.utf8(h.url_for(controller='search', action='detailed')))
        context.write(u'</moz:SearchForm>\n   <moz:UpdateUrl>')
        # SOURCE LINE 17
        context.write(filters.decode.utf8(g.root))
        context.write(filters.decode.utf8(h.url_for(controller='search', action='opensearch')))
        context.write(u'</moz:UpdateUrl>\n   <moz:UpdateInterval>7</moz:UpdateInterval>\n </OpenSearchDescription>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


