# -*- coding: utf-8 -*-
<div id="relationships_navigation">
<label for="relationships_navigation_list">View full list as RDF in format:</label>
<ul id="relationships_navigation_list">
<li>${h.link_to( 'HTML Lite', h.url_for(action="relationships", format='htmllite') )}</li>
<li>${h.link_to( 'HTML Full', h.url_for(action="relationships",format='html') )}</li>
<li>${h.link_to( 'RDF/XML', h.url_for(action="relationships",format='xml') )}</li>
<li>${h.link_to( 'N-Triples', h.url_for(action="relationships",format='nt') )}</li>
<li>${h.link_to( 'N3', h.url_for(action="relationships",format='n3') )}</li>
<li>${h.link_to( 'Turtle', h.url_for(action="relationships",format='turtle') )}</li>
</ul>
</div>
