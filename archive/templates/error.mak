# -*- coding: utf-8 -*-
<%inherit file="/base.mak" />
<%def name="head_tags()">
  <title> Error - ${c.code} - ${c.message} </title>
  <style>
  div#error {
       margin: 1em 2em;
    }
    </style>
</%def>
<%def name="header()">
</%def>
<%def name="footer()">
</%def>
<div id="error">
<h1> ${c.code} - ${c.message} </h1>
</div>
