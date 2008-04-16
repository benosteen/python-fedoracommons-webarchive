# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Information - Disclaimer and Data Protection statement</title>
  <style>
    div#accessibility_statement {
       margin: 1em 2em;
    }
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="accessibility_statement">
<h1>Accessibility Statement</h1>
<p>This is the accessibility statement for the Oxford University Libraries website. It covers the main site at http://ora.ouls.ox.ac.uk/. Other sites which are linked from the top level  are not covered by this statement. Work is continuing to further improve the accessibility and usability of the site.</p>
<p>If you have any questions or comments about the accessibility of this site, please contact the webmaster.</p>

<dl>
<dt>Navigation aids</dt>
<dd>The site uses a consistent navigation system visually located at the top right of the page.</dd>
<dt>Tables</dt>
<dd>Tables are used to display tabular information only. The content of the page is contained in semantically labelled 'div' elements.</dd>
<dt>Images</dt>
<dd>Images include descriptive ALT attributes. Purely decorative graphics would include null ALT attributes.</dd>
<dt>Visual design</dt>
<dd>This site uses cascading style sheets for visual layout. If your browser or browsing device does not support style sheets at all, the content of each page is still readable. The website uses a layout scheme that allows the scale of the page to be increased by increasing the text size in visual browsers for the visually-impaired.</dd>
</dl>
<p>See also the central ${h.link_to("Oxford University's Web Accessibility Policy", "http://www.ox.ac.uk/web/accessibility.html")}. </p>
</div>
