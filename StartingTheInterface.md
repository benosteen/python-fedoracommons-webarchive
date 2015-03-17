# Introduction #

A simple guide to starting your application and a few tips on debugging.

# Details #

  1. easy\_install pylons
  1. easy\_install uuid
  1. easy\_install elementtree
  1. easy\_install beautifulsoup
  1. easy\_install rdflib==2.4.0
  1. Install Fedora and Solr according to my (verbose) guide [here](http://oxfordrepo.blogspot.com/2008/02/creating-web-application-from-scratch.html) starting from Step 5.
  1. Download and unarchive the archive\_vXX.tar.gz from [here](http://code.google.com/p/python-fedoracommons-webarchive/downloads/list)
  1. If you are planning on using simple dublin core metadata as your core metadata vocabulary, there is a 'default\_solr\_schema.xml' in the archive root directory that will create fields for the default 14 terms. The fields are directly linked to the dublin core names, e.g. dc:title -> 'title' field in Solr. Also, all fields have an additional facet field, which has a prefix of f_- therefore, 'title' is the field to search, but 'f\_title' is the field to draw facets from.
  1. After restarting Solr with its new schema.xml, go from the archive's root directory, and_cd_into archive/lib/ folder.
  1. Edit the 'search\_terms.py' file to reflect the fields present in Solr. This is currently a static hand-edited list, but it is a library function as I intend to 'auto-magically' derive the fields from the Solr instance itself, by downloading it's schema, and parsing it.  If someone wants to add this code for me, that'll be great :)
  1. Open app\_globals.py for editing. Change the URL and credentials for the Fedora Commons service and the Solr service present at the top of this file. (If your Solr service needs no password, just use '' strings) Also, look for the setting of_self.root_. This is the host of your application, so change it from 'http://localhost:5000/' to whatever your server location is.
  1. Head back up to the archive root and run the following command:
    * ` paster serve --reload development.ini `
      * This should start serving the application, by using the settings present in development.ini (which has debugging turned **on** by default) and uses the --reload flag, which will quietly and automatically reload any pages, controllers or templates that it detects to have changed.
  1. Should you want to change the port at which this application runs at, the .ini file contains a property near the beginning of the file, reading 'port: 5000'. Change this to whichever port is needed, but bear in mind that low ports, such as port 80 and 443, are restricted and the server would need to by run with elevated permissions.
  1. Need to make it https? Create or get a ssl.pem file (as you might for an Apache server) and add this to the root of the web application. Add into the .ini file, just under the 'port' declaration - 'ssl\_pem: name\_of\_pem\_file.pem'_

### Debugging ###

Two main methods, both incredibly powerful and useful:

# Pylons has an interactive debugger that is active by default when using the 'development.ini' configuration. The documentation for it is as follows and I recommend reading it, as this tool is very, very, very helpful: http://wiki.pylonshq.com/display/pylonsdocs/Interactive+Application+Debugging

# The second way is to open a commandline, in the environment of the application. This is like when running the python interpreter with no arguments:
```
~$ python
Python 2.5.1 (r251:54863, Mar  7 2008, 04:10:12) 
[GCC 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print "Interactive shell"
Interactive shell
```

If you go to the root of the web application and type in the command 'paster shell', you will be placed at a python prompt, but you will have the same environment available to you, preloaded, that a controller method would. So, the Pylon's objects of h (helper), and g (globals) and others are available to you. By default, the Fedora client is 'g.f', the RISearch client is 'g.f.ri'
```
webarchive$ paster shell
No handlers could be found for logger "wsgi"
Pylons Interactive Shell
Python 2.5.1 (r251:54863, Mar  7 2008, 04:10:12) 
[GCC 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)]

  All objects from archive.lib.base are available
  Additional Objects:
  mapper     -  Routes mapper object
  wsgiapp    -  This project's WSGI App instance
  app        -  paste.fixture wrapped around wsgiapp

>>> h.url_for(controller="objects", action="resource_map", id="uuid:1234")
'/objects/uuid%3A1234/aggregation?url=_test_vars'
>>> g.f
<archive.lib.fedoraClient30.FedoraClient object at 0x8a377ec>
>>> dir(g.f)
['__class__', '__delattr__', '__dict__', '__doc__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__str__', '__weakref__', '_createNewObject', '_getText', 'createNewObject', 'create_UUID_Object', 'deleteDatastream', 'deleteObject', 'exportObject', 'fedora', 'getDatastream', 'getDatastreamUrl', 'getNextPID', 'getObjectHistory', 'getObjectProfile', 'getSingleUUID', 'get_tiny_pid', 'listDatastreams', 'mimetypes', 'putFile', 'putString', 'resolve_Non_UUID_pid', 'retrieveObjectXML', 'ri', 'server', 'use_UUID', 'username', 'uuid_id_regex', 'version']
>>> help(g.f.listDatastreams)
Help on method listDatastreams in module archive.lib.fedoraClient30:

listDatastreams(self, pid, format='xml', params=None, date=None) method of archive.lib.fedoraClient30.FedoraClient instance

>>> g.f.listDatastreams('ora:admin', format="xml")
'<?xml version="1.0" encoding="UTF-8"?><objectDatastreams xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.fedora.info/definitions/1/0/access/ http://archive.sers.ox.ac.uk:8080/listDatastreams.xsd" pid="ora:admin" baseURL="http://archive.sers.ox.ac.uk:8080/fedora/" >    <datastream dsid="RELS-EXT" label="Relationships" mimeType="text/xml" />    <datastream dsid="DC" label="Dublin Core Metadata" mimeType="text/xml" /></objectDatastreams>'

>>> g.f.listDatastreams('ora:admin', format="python")
{'RELS-EXT': {'mimetype': 'text/xml', 'winname': 'ora_admin-RELS-EXT.xml', 'dsid': 'RELS-EXT', 'label': 'Relationships'}, 'DC': {'mimetype': 'text/xml', 'winname': 'ora_admin-DC.xml', 'dsid': 'DC', 'label': 'Dublin Core Metadata'}}
```