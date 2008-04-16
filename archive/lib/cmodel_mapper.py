class cmodel_mapper():
    def __init__(self):
        self.model = {}
        self.add_model("type:default", ["DC"], ["DC", "EVENT", "DROID"], ["RELS-EXT"], 'type/default')

    def add_model(self, model_id, metadata_for_page, metadata_formats, admin_datastreams, mako_template, inline_text=[], inline_images=[], ordered_relations=[], rdf_graph='Full Graph', search_terms=True, trackbacks=True):
        """
        model_id: This is the content model for an object - it's what links an object to the model via
                    $obj <isMemberOf> <info:fedora/*model_id*>
        metadata_for_page: List of DSIDs that should be loaded as XML ElementTree objects and passed  
                    to the template in the c.metadata dictionary. E.g. ['MODS'] here will result in 
                    c.metadata['MODS'] = ElementTree XML object.
        metadata_formats: List of DSIDs that contain item's metadata in other formats (desc)
                            (Will be linked to canonical DSID from 'metadata_for_page' via
                            dcterms:hasFormat in the aggregation)
        admin_datastreams: List of DSIDs that contain metadata about the object (adm)
            NB If a DSID is in either of the two previous lists, it will not be included in the
            Download list. It will still be downloadable however, and the XML datastream list will
            include it.
        mako_template: If desired template is at "archive_root/templates/type/basic.mak", 
                    this should read 'type.basic'. Likewise 'templates/metadata/dc.mak' becomes
                    'metadata.dc'
        inline_text: List of DSIDs to load as plain text and pass to the template in 
                        c.inline_text[dsid]
        inline_images: List of Image DSIDs to check for the existance of, and if so, export to 
                    the template information from the listDatastreams call in c.inline_images.
                    E.g. ['THUMBNAIL'] here => c.inline_image['THUMBNAIL']={'dsid':'THUMBNAIL', etc}
        ordered_relations: List of 'fedora-rels-ext' relations to query for and to return
                    them in alphabetical order. 
                    E.g. c.relations['isPartOf'] = Risearch.getOrderedRelations(pid, 'isPartOf')
        rdf_graph: 'forward' or 'all' - 'forward' exports to the template all rdf triples from 
                    the triplestore that this item is the subject of. 'all' passes a graph object
                    that contains the triples that the item is either subject to or object of.
                    c.graph => RDFLib.ConjunctiveGraph(stored in RAM)
                    NB c.rdfs, c.rdf, c.ore, c.rel and c.sioc RDFLib.Namespaces are exported to
                    the template to aid query and display of the graph object.
        search_terms: Whether or not to query Solr for all the terms for the given items and to
                    pass this to the template in c.search_terms
                    NB This will also pass c.field_list (contains field to name mapping from lib/search_terms.py and c.all_fields, containing all known fields (again from lib/search_terms.py)
        trackbacks: Whether to query and load the trackback items - linked by 
                    <trackback> <sioc#reply_of> <this_pid> rdf. Loads c.trackbacks[trackback_pid] with
                    basic dc name:value dictionary.
        """
        self.model[model_id] = {"model_id":model_id,
                                "metadata_for_page":metadata_for_page,
                                "metadata_formats":metadata_formats,
                                "admin_datastreams":admin_datastreams,
                                "mako_template":mako_template,
                                "inline_text":inline_text,
                                "inline_images":inline_images,
                                "ordered_relations":ordered_relations,
                                "rdf_graph":rdf_graph,
                                "search_terms":search_terms,
                                "trackbacks":trackbacks}

    def get_model(self, model_id):
        if model_id in self.model:
            return self.model[model_id]
        else:
            return self.model["type:default"]       
