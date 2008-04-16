from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1206480574.216758
_template_filename='/home/archive/archive/archive/templates/search_form.mak'
_template_uri='/search_form.mak'
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
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 2
        context.write(u'\n\n')
        # SOURCE LINE 190
        context.write(u'\n')
        # SOURCE LINE 192
        context.write(u'\n')
        # SOURCE LINE 194
        context.write(u'\n<div id="search_box_wrapper">\n')
        # SOURCE LINE 196
        context.write(filters.decode.utf8(h.form(h.url(controller="search", action="detailed"), method='post')))
        context.write(u'\n<div id="search_wrapper">\n<p id="search_term_block"><span class=\'label\'>')
        # SOURCE LINE 198
        context.write(filters.decode.utf8( h.text_field('q', value=c.q)))
        context.write(u'</span> ')
        context.write(filters.decode.utf8(h.submit('Search')))
        context.write(u'\n')
        # SOURCE LINE 199
        if c.fulltext:
            # SOURCE LINE 200
            context.write(u'<span class="small_label"> Search inside full-text items </span> <input type="checkbox" class="checkbox" name="fulltext" checked="True"/> </span>\n')
            # SOURCE LINE 201
        else:
            # SOURCE LINE 202
            context.write(u'<span class="small_label"> Search inside full-text items </span> <input type="checkbox" class="checkbox" name="fulltext"/> </span>\n')
        # SOURCE LINE 204
        context.write(u'</p>\n<div id="search_box">\n<p><span class=\'label\'>Return in sets of \n<select id="rows" name="rows">\n')
        # SOURCE LINE 208
        for row in [5,10,25,50]:
            # SOURCE LINE 209
            if row==c.rows:
                # SOURCE LINE 210
                context.write(u'<option value="')
                context.write(filters.decode.utf8(row))
                context.write(u'" selected="True">')
                context.write(filters.decode.utf8(row))
                context.write(u'</option>\n')
                # SOURCE LINE 211
            else:
                # SOURCE LINE 212
                context.write(u'<option value="')
                context.write(filters.decode.utf8(row))
                context.write(u'">')
                context.write(filters.decode.utf8(row))
                context.write(u'</option>\n')
        # SOURCE LINE 215
        context.write(u'</select> hits.</span></p>\n<p><span class=\'label\'>Level of detail to return?</span></p>\n<select id="view" name="view">\n')
        # SOURCE LINE 218
        for view in c.views:
            # SOURCE LINE 219
            if view==c.view:
                # SOURCE LINE 220
                context.write(u'<option value="')
                context.write(filters.decode.utf8(view))
                context.write(u'" selected="True">')
                context.write(filters.decode.utf8(view))
                context.write(u'</option>\n')
                # SOURCE LINE 221
            else:
                # SOURCE LINE 222
                context.write(u'<option value="')
                context.write(filters.decode.utf8(view))
                context.write(u'">')
                context.write(filters.decode.utf8(view))
                context.write(u'</option>\n')
        # SOURCE LINE 225
        context.write(u'</select>\n<p><span class=\'label\'>Sort by: </span>\n<select id="sort" name="sort">\n')
        # SOURCE LINE 228
        for sort in c.sort_options:
            # SOURCE LINE 229
            if sort==c.sort:
                # SOURCE LINE 230
                context.write(u'<option value="')
                context.write(filters.decode.utf8(sort))
                context.write(u'" selected="True">')
                context.write(filters.decode.utf8(c.sort_options[sort]))
                context.write(u'</option>\n')
                # SOURCE LINE 231
            else:
                # SOURCE LINE 232
                context.write(u'<option value="')
                context.write(filters.decode.utf8(sort))
                context.write(u'">')
                context.write(filters.decode.utf8(c.sort_options[sort]))
                context.write(u'</option>\n')
        # SOURCE LINE 235
        context.write(u'</select></p>\n')
        # SOURCE LINE 236
        context.write(filters.decode.utf8( h.hidden_field('truncate', value=c.truncate)))
        context.write(u'\n</div>\n<div id="facets">\n<p>Show groupings by: </p>\n<div class="facets">\n<div class="container">\n')
        # SOURCE LINE 242
        for field in c.facetable_fields:
            # SOURCE LINE 243
            if field in c.fields_to_facet:
                # SOURCE LINE 244
                context.write(u'<span class="toggle"><span class="toggle_label">')
                context.write(filters.decode.utf8( c.field_names[field] ))
                context.write(u' </span> <input type="checkbox" class="checkbox" name="facet')
                context.write(filters.decode.utf8(field))
                context.write(u'" checked="True"/> </span>\n')
                # SOURCE LINE 245
            else:
                # SOURCE LINE 246
                context.write(u'<span class="toggle"><span class="toggle_label">')
                context.write(filters.decode.utf8( c.field_names[field] ))
                context.write(u' </span> <input type="checkbox" class="checkbox" name="facet')
                context.write(filters.decode.utf8(field))
                context.write(u'"/> </span>\n')
        # SOURCE LINE 249
        context.write(u'</div>\n<div class="clear">&nbsp;</div>\n</div>\n</div>\n</div>\n<div class="clear">&nbsp;</div>\n')
        # SOURCE LINE 255
        context.write(filters.decode.utf8(h.end_form()))
        context.write(u'\n</div>\n<hr/>\n<div id="results_wrapper">\n<div id="results" \n')
        # SOURCE LINE 260
        if not c.returned_facets: 
            # SOURCE LINE 261
            context.write(u' style="width:70em;" \n')
        # SOURCE LINE 263
        context.write(u'>\n')
        # SOURCE LINE 264
        runtime._include_file(context, '/search_response_display.mak', _template_uri)
        context.write(u'\n</div>\n')
        # SOURCE LINE 266
        if c.returned_facets:
            # SOURCE LINE 267
            context.write(u'<div id="facet_container">\n')
            # SOURCE LINE 268
            for facet in c.returned_facets:
                # SOURCE LINE 269
                if facet in c.chosen_facets:
                    # SOURCE LINE 270
                    context.write(u'<div class="facet_results">\n<div class="subheading">')
                    # SOURCE LINE 271
                    context.write(filters.decode.utf8(c.field_names[facet]))
                    context.write(u'</div>\n<p>')
                    # SOURCE LINE 272
                    context.write(filters.decode.utf8(c.field_names[facet]))
                    context.write(u' : "')
                    context.write(filters.decode.utf8( c.chosen_facets[facet] ))
                    context.write(u'"\n<span class="pagination_label">')
                    # SOURCE LINE 273
                    context.write(filters.decode.utf8(h.form(h.url(controller="search", action="detailed"), method='post')))
                    context.write(u'\n')
                    # SOURCE LINE 274
                    context.write(filters.decode.utf8( h.hidden_field('q', value=c.q)))
                    context.write(u'\n')
                    # SOURCE LINE 275
                    context.write(filters.decode.utf8( h.hidden_field('rows', value=c.rows)))
                    context.write(u'\n')
                    # SOURCE LINE 276
                    context.write(filters.decode.utf8( h.hidden_field('truncate', value=c.truncate)))
                    context.write(u'\n')
                    # SOURCE LINE 277
                    for facet_field in c.fields_to_facet:
                        # SOURCE LINE 278
                        context.write(u'<input type="hidden" name="facet')
                        context.write(filters.decode.utf8(facet_field))
                        context.write(u'" value="true"/>\n')
                    # SOURCE LINE 280
                    for chosen_field in c.chosen_fields:
                        # SOURCE LINE 281
                        context.write(u'<input type="hidden" name="')
                        context.write(filters.decode.utf8(chosen_field))
                        context.write(u'" value="true"/>\n')
                    # SOURCE LINE 283
                    for chosen_facet in c.chosen_facets:
                        # SOURCE LINE 284
                        if isinstance(c.chosen_facets[chosen_facet], list):
                            # SOURCE LINE 285
                            for item in c.chosen_facets[chosen_facet]:
                                # SOURCE LINE 286
                                if not (facet==chosen_facet):
                                    # SOURCE LINE 287
                                    context.write(u'<input type="hidden" name="filter')
                                    context.write(filters.decode.utf8(facet))
                                    context.write(u'" value="')
                                    context.write(filters.decode.utf8(item))
                                    context.write(u'"/>\n')
                            # SOURCE LINE 290
                        else:
                            # SOURCE LINE 291
                            if not (facet==chosen_facet):
                                # SOURCE LINE 292
                                context.write(u'<input type="hidden" name="filter')
                                context.write(filters.decode.utf8(chosen_facet))
                                context.write(u'" value="')
                                context.write(filters.decode.utf8(c.chosen_facets[chosen_facet]))
                                context.write(u'"/>\n')
                    # SOURCE LINE 296
                    context.write(filters.decode.utf8(h.submit("Remove")))
                    context.write(filters.decode.utf8(h.end_form()))
                    context.write(u'</span></p>\n</div>\n')
                    # SOURCE LINE 298
                else:
                    # SOURCE LINE 299
                    if c.returned_facets[facet]:
                        # SOURCE LINE 300
                        context.write(u'<div class="facet_results">\n<div class="subheading">')
                        # SOURCE LINE 301
                        context.write(filters.decode.utf8(c.field_names[facet]))
                        context.write(u'</div>\n<ul>\n')
                        # SOURCE LINE 303
                        for result,value in c.returned_facets[facet]:
                            # SOURCE LINE 304
                            context.write(u'<li><span class="label">\n<a href="')
                            # SOURCE LINE 305
                            context.write(filters.decode.utf8(c.add_facet % (facet, result)))
                            context.write(u'">')
                            context.write(filters.decode.utf8(" ".join(result.split('-'))))
                            context.write(u'</a>\n</span>: <span class="value">')
                            # SOURCE LINE 306
                            context.write(filters.decode.utf8(value))
                            context.write(u'</span></li>\n')
                        # SOURCE LINE 308
                        context.write(u'</ul>\n</div>\n')
                        # SOURCE LINE 310
                    else:
                        # SOURCE LINE 311
                        context.write(u'<div class="facet_results">\n<div class="subheading">')
                        # SOURCE LINE 312
                        context.write(filters.decode.utf8(facet))
                        context.write(u'</div>\n<p class="no_facets"> There are no groupings of this field in your search results. </p>\n</div>\n')
            # SOURCE LINE 318
            context.write(u'</div>\n')
        # SOURCE LINE 320
        context.write(u'</div>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_header(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 191
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_footer(context):
    context.caller_stack.push_frame()
    try:
        # SOURCE LINE 193
        context.write(u'\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


def render_head_tags(context):
    context.caller_stack.push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        key = context.get('key', UNDEFINED)
        # SOURCE LINE 4
        context.write(u"\n  <title> Advanced Search - Functionality Demo</title>\n  <style>\n    \n    #q {\n        width: 8em;\n    }\n        \n    div#search_wrapper {\n        width: 100%;\n        min-width: 740px;\n        margin: 0 auto;\n        background: transparent;\n    }\n    \n    div.link {\n        float: right;\n        margin-top:1em;\n        margin-right: 0.3em;\n    }\n    div.link a {\n        padding: 0.1em;\n        border: 1px solid #5599dd;\n\n    }\n    dt.label {\n        font-weight: bold;\n        color: #3399ee;\n        padding-left:3.5em;\n    }\n    dd.value {\n        font-weight: normal;\n        color: #565656;\n    }\n    \n    \n    #facets {\n        float: left;\n        width: 45em;\n        margin-left: 1em;\n    }\n    \n    \n    #search_box {\n        float: left;\n        width: 20em;\n        margin-left: 1em;\n    }\n    \n    #search_box p, #facets p {\n        font-size: 1.3em;\n    }\n    \n    p#search_term_block {\n        margin: 1em;\n        margin-left: 16em;\n        font-size: 1.5em;\n    }\n    \n    p#search_term_block span input {\n        width: 10em;\n    }\n    \n    div.response_doc {\n        margin: 0.4em;\n        border: 1px solid #aaa8a1;\n        background-color: #efefef;\n    }\n    span.toggle {\n        padding: 0.1em;\n        margin: 0.1em;\n        border: 1px solid #5599dd;\n        float: left;\n        width: 14em;\n    }\n    span.toggle_label {\n        float: right;\n        margin-right: 0.3em;\n        margin-top: 0.2em;\n    }\n    \n    span.toggle input {\n        float: left;\n        margin-right: 0.5em;\n        color: #000000; \n        border: 1px solid #aaa8a1;\n    }\n    \n    div.clear {\n        clear: both;\n    }\n    \n    div.facets {\n        padding: 0.3em;\n        border: 1px solid #cdcdcd;\n        background-color: #efefef;\n        max-width: 62em;\n    }\n    \n    div#fields {\n        float: right;\n    }\n    \n    #rows {\n        width: 3em;\n    }\n    \n    #view {\n        width: 6em;\n    }\n    \n    .facet_results {\n        float: left;\n        width: 14em;\n        padding-bottom: 1em;\n    }\n    \n    .facet_results ul li {\n        list-style: none;\n    }\n    \n    span.pagination_label form, span.label form {\n        display:inline;\n        cursor: pointer;\n    }\n    \n    span.pagination_label form button, span.pagination_label form input {\n        border: 0px;\n        color: #3355ee;\n        cursor: pointer;\n    }\n    \n    p.no_facets {\n        color: #aaaaaa;\n        font-style: italic;\n        width: 10em;\n    }\n    div#facet_container {\n        width: 15em;\n        float: left;\n    }\n    div#results {\n        width: 54em;\n        float: right;\n    }\n    div#results_wrapper, div#search_box_wrapper {\n        width: 70em;\n        margin: 0 auto;\n        \n    }\n    span.document_number {\n        float: left;\n        padding: 0.2em;\n        margin: 0.2em;\n        border:1px solid #999;\n        font-weight: bold;\n    }\n    \n    .checkbox {\n        /* !important Because IE doesn't want to listen...  */\n        border: 0px !important;\n    }\n    \n    span.small_label {\n        font-size: 0.7em;\n    }\n    \n  </style>\n")
        # SOURCE LINE 172
        if c.search:
            # SOURCE LINE 173
            context.write(u'  <link rel="alternate" type="application/atom+xml"\nhref="')
            # SOURCE LINE 174
            context.write(filters.decode.utf8(h.url_for(controller='search', action="detailed", format='atom', **dict([(key, c.search[key]) for key in c.search if key!='start']))))
            context.write(u'" title="ORA Search results for \\"')
            context.write(filters.decode.utf8(c.search.get('q',None)))
            context.write(u'\\""/>\n')
        # SOURCE LINE 176
        context.write(u'\n  <script type="text/javascript">\n<!--\nfunction switchMenu(obj) {\n\tvar el = document.getElementById(obj);\n\tif ( el.style.display != "none" ) {\n\t\tel.style.display = \'none\';\n\t}\n\telse {\n\t\tel.style.display = \'\';\n\t}\n}\n//-->\n</script>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


