# Overview #

Provides a web framework and libraries that will enable the creation of highly customisable interfaces that use the Fedora Commons repository software and the Solr search engine appliance.

The framework is in an exemplar setup for simple dublin core based items, but includes templates and a content model typing system that is very extensible. The unused templates should give a lot of information about what is possible with the framework.

The file archive/lib/app\_globals.py contains the section where the Fedora and Solr URLs and username/passwords are set. (I should abstract these to the config .ini, I know!)

## Prerequisites ##

(Detailed guide to setting up Fedora and Solr can be found here: http://oxfordrepo.blogspot.com/2008/02/creating-web-application-from-scratch.html)

Fedora-Commons 3.0b1 installed with REST API on, Triplestore On and XACML turned off (due to it interfering with the REST API)

Solr 1.2 - installed - the out-of-the-box setup for this interface expects it to have the schema included as default\_solr\_scheme.xml.

easy\_install - http://peak.telecommunity.com/DevCenter/EasyInstall

(Make sure you have the development files installed for python, on debian based systems, apt-get install python-dev)

And then some python libraries:

easy\_install rdflib==2.4.0

easy\_install pylons

easy\_install uuid

easy\_install beautifulsoup

easy\_install elementtree