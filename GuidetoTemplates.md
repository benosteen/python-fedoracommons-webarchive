# Introduction #
The markup used in the templates is called Mako, and documentation on working with Mako can be found here: http://wiki.pylonshq.com/display/pylonscookbook/Mako+for+people+in+a+hurry. This is not a guide to the underlying language used in the templates, but it's a guide to the templates as already laid out in this application.

[Also, although this project doesn't use a gettext style for internationalisation, it is built into the templating language. This (http://wiki.pylonshq.com/display/pylonsdocs/Internationalization+and+Localization) is a good guide to how to make this Pylons-based application 'speak' other languages.]

# Guide #

## Guide to templates ##

### base.mak ###

This is the base of all templates - it is intended to be inherited by all. It contains the HTML wrapper for the rest of the items, and gives the site its look and feel.

In terms of structure, base.mak looks like this:

The usual html declaration

**In the**

&lt;head&gt;

 element

  * OpenSearch auto-discovery section
  * unAPI auto-discovery section
  * OAI-ORE Resource map auto-discovery section
  * 

&lt;style&gt;

 section that is applied to all pages
  * Import the <%def head\_tags()%> from child templates
    * All child templates declare a function 'head\_tags()' which is imported here. Enables per-page styling and allows for the setting of the 

&lt;title&gt;

 element and addition of additional meta/link elements.

**In the**

&lt;body&gt;

:

```
<div id="header">
Default 'static' content
Import from <%def header() /> from child templates
</div>
<div id="page_content">
Default 'static' content
Import the body of text from child templates (See below)
</div>
<div id="footer">
Default 'static' content
Import from <%def footer()> from child templates
</div>
```

It is useful to include your overall site navigation in the header div.

### Child templates ###

The minimal form of the average child template is as follows:

```
# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Information - Minimal template</title>
* Insert things you wish to add to the _head_ element here *
</%def>
<%def name="header()">
* Insert things you wish to add to the header _div_ element here *
</%def>
<%def name="footer()">
* Insert things you wish to add to the footer _div_ element here *
</%def>
*Insert your page content from this point on*
```

### Front Page ###

This uses, by default, **root\_page.mak**

### Controller Specific templates ###

This will often have _controllerName_ preceding the template filename.

### Browse pages ###

  * browse\_root.mak
    * This is the template used when going to the index of the browse controller. By default, it runs through c.returned\_facets, showing the results of the Solr search made by browse.py's index method.
  * browse\_cloud.mak
    * This takes in the list of returned fields from a given facet and displays them in a 'tag-cloud'.
  * browse\_field.mak
    * This simply displays the list of returned fields from a given facet in an alphabetical list.
  * browse\_facet.mak
    * This shows a list of items resulting from filtering a given facet on a given field, such as facet:subject and field:Astronomy.