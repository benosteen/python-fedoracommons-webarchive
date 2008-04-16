# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Help - Disclaimer and Data Protection statement</title>
  <style>
    div#disclaimer, div#dataprotection, div#external_help {
       margin: 1em 2em;
    }
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="disclaimer">
<h1>Disclaimer</h1>
<p>Oxford University Library Services (OULS) provides some information to end users about the legitimate use and re-use of items held in ORA. However the University of Oxford is not responsible for any improper use made of the items by other parties.</p>
<p>Staff at Oxford University Research Archive endeavour to comply with copyright permissions for all content of the archive. If they are made aware of the possibility of infringement of copyright for any item in ORA, the item will be removed from the archive as soon as possible whilst the complaint is investigated.</p>
<p>ORA staff may offer advice and assistance checking and clearing copyright held by third parties but the responsibility for making an item available via ORA lies with the depositor.</p>
</div>
<div id="dataprotection">
<h1>Data Protection</h1>
<p>The information you supply will be used by the University of Oxford for administrative purposes within the terms of the Data Protection Act 1998. We shall not supply it to third parties.</p>
</div>
<div id="external_help">
<p>For any additional help, please see the external ORA help and guidance website ${h.link_to('here', "http://www.ouls.ox.ac.uk/ora")}</p>
</div>
