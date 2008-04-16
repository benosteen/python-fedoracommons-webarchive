from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1207151995.226433
_template_filename='/home/ben/Desktop/archive/archive/templates/base.mak'
_template_uri='/base.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        g = context.get('g', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html lang="en-gb">\n  <head>\n     <link rel="search"\n           type="application/opensearchdescription+xml" \n           href="search/opensearch"\n           title="ORA Search" />\n     <link rel="unapi-server" type="application/xml" title="unAPI" href="http://archive.sers.ox.ac.uk:5000/unapi/" />\n')
        # SOURCE LINE 11
        if c.resource_map_url:
            # SOURCE LINE 12
            context.write(u'     <link href="')
            context.write(filters.decode.utf8(c.resource_map_url))
            context.write(u'" type="application/rdf+xml" rel="resourcemap" />\n')
        # SOURCE LINE 14
        if c.id:
            # SOURCE LINE 15
            context.write(u'     <abbr class="unapi-id" title="')
            context.write(filters.decode.utf8(c.id))
            context.write(u'"></abbr>\n     <link rel="pingback" href="')
            # SOURCE LINE 16
            context.write(filters.decode.utf8("%spingback" % g.root))
            context.write(u'"/>\n')
        # SOURCE LINE 18
        context.write(u"     <style>\n\n     body {\n        font-family: Helvetica, sans-serif;\n        font-size: 76%;\n        padding: 0em;\n        background: #e7e5d8;\n    }\n    \n    h1 {\n        font-size: 1.3em;\n    }\n    \n    a img {\n        border: 0;\n    }\n    \n    .highlight {\n        color: red;\n    }\n    \n    input, .checkbox {\n        border: 1px solid #5599dd;\n    }\n    \n    input:focus {\n        background: #ffc;\n    }\n    \n    ul {\n        margin: 0.1em;\n        padding: 0.1em;\n    }\n    \n    ul li {\n        list-style: none;\n    }\n    \n    div.clear {\n        clear: both;\n        border: 0px !important;\n        background: transparent !important;\n        margin: 0em !important;\n        padding: 0em !important;\n    }\n    \n    span.small_link {\n        font-size: 0.8em;\n    }\n    \n    a {\n        color: blue;\n        cursor: pointer;\n    }\n    \n    #oxford_logo {\n        /* float: right; */\n    }\n    #eprints_logo {\n        /* float: right; */\n    }\n    \n    div#page_container {\n        width: 72em;\n        margin: 0 auto;\n        border: 1px solid #aaa8a1;\n        padding: 0.1em;\n        background: #fff url('/backing.png') repeat-x top;\n    }\n    \n    div#link_to_this_search {\n        float: right;\n    }\n    \n    #header {\n        background: #111 url('/header.jpg') no-repeat top left;\n        height: 9em;\n        min-height: 100px;\n        /* border-bottom: 1px solid #aaa8a1; */\n    }\n    \n    .footer_img {\n        height: 38px;\n        width: auto;\n    }\n    \n    #footer {\n    \n    }\n    \n    #footer ul li {\n        font-size: 0.8em;\n        display: inline;\n        padding: 0em 0.5em;\n    }\n    \n    #footer ul li.leftborder {\n        border-left:1px solid #CCCCCC;\n    }\n    \n    p#inline_search {\n        margin-left: 45em;\n        float: left;\n        margin-top: 1em;\n    }\n    \n    p#inline_search span input {\n        width: 10em;\n    }\n    \n    p#inline_search a {\n        color: #fff !important;\n        text-decoration: none;\n    }\n    \n    ul#header_navigation {\n        float:right;\n        line-height: 1.9em;\n        padding: 0.3em 1em;\n        background: #444;\n    }\n    \n    ul#header_navigation a {   \n        text-decoration: none;\n        color: white !important;\n        cursor: pointer;\n    }\n    \n    div#copyright_statement {\n        float: right;\n        width: 37em;\n        color: #999;\n    }\n    div#copyright_statement p {\n        font-size: 0.8em;\n    }\n    dl {\n        line-height: 1.7em;\n        width: 90%;\n    }\n    dt {\n        font-weight: bold;\n        font-size: 1.2em;\n        color: #3399ee;\n    }\n    dd {\n        font-weight: normal;\n        color: #565656;\n    }\n    \n    div#response_message {\n        width: 95%;\n        background-color: #888;\n        font-weight: bold;\n        color: #fff;\n        margin: 0 auto;\n    }\n    \n    div#response_message span {\n        margin: 0.3em 1em;\n    }\n    div#termsofuse {\n        font-size: 0.8em;\n        padding: 1em;\n    }\n    div.subheading {\n        font-size: 1.2em;\n        font-weight: bold;\n        border: 0px !important;\n    }\n    \n    span.small_link {\n        font-size: 0.7em;\n    }    \n    </style>\n    ")
        # SOURCE LINE 193
        context.write(filters.decode.utf8(self.head_tags()))
        context.write(u'\n  </head>\n  <body>\n    <div id="page_container">\n    <div id="header">\n    <ul id="header_navigation">\n\t<li>')
        # SOURCE LINE 199
        context.write(filters.decode.utf8(h.link_to('Browse', h.url_for(controller="/browse", action="index"))))
        context.write(u'</li>\n\t<li>')
        # SOURCE LINE 200
        context.write(filters.decode.utf8(h.link_to('Tools', h.url_for(controller="/information", action="urls"))))
        context.write(u'</li>\n    </ul>\n')
        # SOURCE LINE 202
        if not c.hide_basic_search:
            # SOURCE LINE 203
            context.write(u'    ')
            context.write(filters.decode.utf8(h.form(h.url(controller="/search", action="basic"), method='post')))
            context.write(u"\n    <p id='inline_search'><span class='label'>")
            # SOURCE LINE 204
            context.write(filters.decode.utf8( h.text_field('q', value=c.q)))
            context.write(u'</span> ')
            context.write(filters.decode.utf8(h.submit('Search')))
            context.write(u' ')
            context.write(filters.decode.utf8(h.link_to('Detailed Search', h.url_for(controller="/search", action="index"))))
            context.write(u'</p>\n    ')
            # SOURCE LINE 205
            context.write(filters.decode.utf8( h.hidden_field('rows', value=c.rows)))
            context.write(u'\n    ')
            # SOURCE LINE 206
            context.write(filters.decode.utf8( h.hidden_field('truncate', value=c.truncate)))
            context.write(u'\n    ')
            # SOURCE LINE 207
            context.write(filters.decode.utf8( h.hidden_field('view', value="Default")))
            context.write(u'\n    ')
            # SOURCE LINE 208
            context.write(filters.decode.utf8(h.end_form()))
            context.write(u'\n')
        # SOURCE LINE 210
        context.write(u'    ')
        context.write(filters.decode.utf8(self.header()))
        context.write(u'\n    </div>\n    <div id="page_content">\n')
        # SOURCE LINE 213
        if c.message:
            # SOURCE LINE 214
            context.write(u'<div id="response_message"><span>')
            context.write(filters.decode.utf8(c.message))
            context.write(u'</span></div>\n')
        # SOURCE LINE 216
        context.write(u'    ')
        context.write(filters.decode.utf8(self.body()))
        context.write(u'\n    <div class="clear">&nbsp;</div>\n    </div>\n    <div id="footer">\n    <ul id="footer_list">\n\t<li>')
        # SOURCE LINE 221
        context.write(filters.decode.utf8(h.link_to('Disclaimer and Data Protection statement', h.url_for(controller="/information", action="disclaimer"))))
        context.write(u'</li>\n\t<li class="leftborder">')
        # SOURCE LINE 222
        context.write(filters.decode.utf8(h.link_to('Accessibility statement', h.url_for(controller="/information", action="accessibility"))))
        context.write(u'</li>\n    </ul>\n    ')
        # SOURCE LINE 224
        context.write(filters.decode.utf8(self.footer()))
        context.write(u'\n    <div id="copyright_statement"><p>Site powered by <strong>Fedora</strong> and Apache Solr. Data source and information management system is powered by <strong>EPrints.org</strong>.</p></div>\n    \n    <a href="http://www.ox.ac.uk">\n    <img class="footer_img" src="/logo_oxford.jpg" alt="Oxford University Logo"/>\n    </a>\n    <a href="http://eprints.org">\n    <img class="footer_img" src="/eprints.gif" alt="EPrints"/>\n    </a>\n    <a href="http://www.fedora-commons.org">\n    <img class="footer_img" src="/fedora.png" alt="Fedora Commons" />\n    </a>\n    </div>\n    </div>\n  </body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


