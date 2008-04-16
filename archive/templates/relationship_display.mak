# -*- coding: utf-8 -*-
% if c.title:
<p><strong> Relationships for "${h.link_to('<span class="object_title">%s</span>' % c.title, h.url_for(controller="/objects", id=c.id))}":</strong></p>
% elif c.id:
<p><strong> Relationships for Object ${h.link_to('<span class="uuid">%s</span>' % c.id, h.url_for(controller="/objects", id=c.id))}:</strong></p>
% endif
% if c.graph:
<%include file="/forward_relationship_display.mak"/>
<%include file="/back_relationship_display.mak"/>
<%include file="/object_relationship_navigation.mak"/>
% endif
