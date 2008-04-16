"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('error/:action/:id', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('home', controller='information', action='index')
    map.connect('browse/:field', controller='browse', action='field')
    map.connect('browse/:field/:item', controller='browse', action='field')
    map.connect('browse/:field/:item/:part', controller='browse', action='field')
    
    map.connect('', controller='information', action='index')
    
    
    # Object display mappings 
    map.connect('objects/:id', controller="objects", action="index")
    map.connect('objects/:id/show', controller="objects", action="index")
    map.connect('objects/:id/format', controller="objects", action="format")
    map.connect('objects/:id/format/:format', controller="objects", action="format")
    map.connect('objects/:id/datastreams', controller="objects", action="datastreams")
    map.connect('objects/:id/datastreams/:dsid', controller="objects", action="download")
    map.connect('objects/:id/relationships', controller="objects", action="relationships")

    # OAI-ORE
        
    map.connect('objects/:id/aggregation', controller="objects", action="resource_map")
    map.connect('objects/:id/aggregation.:format', controller="objects", action="resource_map")

    # For versioning
    map.connect('objects/:id/:date/datastreams', controller="objects", action="datastreams")
    map.connect('objects/:id/:date/datastreams/:dsid', controller="objects", action="download")
    map.connect('objects/:id/:date', controller="objects", action="index")
    map.connect('objects/:id/:date/show', controller="objects", action="index")
    map.connect('objects/:id/:date/format', controller="objects", action="format")
    map.connect('objects/:id/:date/format/:format', controller="objects", action="format")
    map.connect('objects/:id/:date/relationships', controller="objects", action="relationships")
    
    # Trackback
    map.connect('trackback/:id', controller="trackback", action="index")
    
    # Fedora URI mapping
    map.connect('resolve/info:fedora/:id', controller="objects", action="redirect")
    map.connect('resolve/info:fedora/:id/:dsid', controller="objects", action="download")
    
    # Fake handles resolution, change 10030 to your handles resolver
    # :id => info:fedora/namespace*:id*
    map.connect('10030/:id', controller="objects", action="handle")    
    
    # Legacy VITAL 2.1 urls
    map.connect('access/adv_search.php', controller='search', action='redirect')
    map.connect('access/detail.php', controller='objects', action='redirect')
    
    # Semantic search (UNTESTED with the DC only interface) 
    map.connect('person/:q', controller='search', action='person')
    map.connect('title/:q', controller='search', action='title')
    map.connect('date/:q', controller='search', action='date')
    map.connect('collection/:q', controller='search', action='collection')
    map.connect('faculty/:q', controller='search', action='faculty')
    map.connect('subject/:q', controller='search', action='subject')
    
    map.connect('search/basic', controller='search', action='basic')
    map.connect('search/basic/:q', controller='search', action='basic')
    
    map.connect(':controller/:action/:id')
    map.connect('*url', controller='template', action='view')

    return map
