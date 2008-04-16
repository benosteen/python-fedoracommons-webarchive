# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Information - Disclaimer and Data Protection statement</title>
  <style>
    div#contribute {
       margin: 1em 2em;
    }
    div#thesis_submission, div#general_item_submission, div#conference {
        margin: 2em;
        border: 1px solid #e7e5d8;
    }
    div#notices {
        margin: 2em;
    }
    
    div#thesis_submission p, div#general_item_submission p, div#conference p, div#notices p {
        margin: 2em;
        font-size: 1.3em;
    }
    
    div#thesis_submission p a, div#general_item_submission p a, div#conference p a, div#notices p a {
        font-weight:normal;
        text-transform:none;
        text-decoration:none;
    }
  </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="contribute">
<h3>Contribute to the Oxford University Research Archive</h3>
<div id="thesis_submission">
<p>${h.link_to('Click here to submit a <strong>Thesis</strong> to the Oxford Research Archive', "http://ora.ouls.ox.ac.uk/cgi-bin/valet/submit.cgi?view=ethesis")}</p>
</div>
<div id="general_item_submission">
<p>${h.link_to('Click here to submit a <strong>Journal article</strong> or a <strong>conference/workshop paper</strong> or any other <strong>general item of research</strong> (Image, report, book chapter, etc) to the Oxford Research Archive', "http://ora.ouls.ox.ac.uk/cgi-bin/valet/submit.cgi?view=epapers")}</p>
</div>
<div id="conference">
<p>${h.link_to('Click here to register a <strong>conference or workshop</strong> with the Oxford Research Archive - This is to help group together papers which were given at the same conference or workshop.', "http://ora.ouls.ox.ac.uk/cgi-bin/valet/submit.cgi?view=conference")}</p>
</div>
<div id="notices">
<p><em>* OUCS-provided Oxford Single-Sign-On account is required:</em></p>
<p>${h.link_to('See more information about getting an account here.', "http://www.oucs.ox.ac.uk/registration/oxford/index.xml.ID=body.1_div.2")}</p>
</div>
</div>
