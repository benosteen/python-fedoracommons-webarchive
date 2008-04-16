import logging

from archive.lib.base import *

from elementtree import ElementTree as ET

log = logging.getLogger(__name__)

class UnapiController(BaseController):
    """
    In the unAPI spec, it states that :

    "UNAPI (no parameters)

    Provide a list of object formats which should be supported for all objects available through the unAPI service. Content-type must be "application/xml". An example response for a site that supports "oai_dc", and "jpeg" formats might be:"

    As the types of metadata and more that can be relayed through the unAPI depends on the type of
    object, I will need to add an 'endpoint' for each nominal 'type' - likely grouping all the text
    based materials together (MODS, DC, FULLTEXT + generated ones for refWorks, Endnote, depending on time.
    """
    def index(self, id=None):
        """
        Pillage for the unAPI params and switch accordingly:
        UNAPI (no parameters) = Provide a list of object formats common to all
        UNAPI?id=IDENTIFIER = Provide a list of formats available for the object identified by IDENTIFIER.
        UNAPI?id=IDENTIFIER&format=FORMAT = Provide the bare datastream/export        
        """
        
        if not id:
            id =  request.params.get('id', None)
        format = request.params.get('format', None)
            
        if not id and not format:
            # Spit out basic format list for ALL objects (so DC and EVENT)
            root = ET.Element('formats')
            format = ET.SubElement(root, "format")
            format.set('name', 'DC')
            format.set('type', 'application/xml')
            format.set('docs', 'http://www.openarchives.org/OAI/2.0/oai_dc.xsd')
            
            format = ET.SubElement(root, "format")
            format.set('name', 'EVENT')
            format.set('type', 'text/calendar')
            
            # Generated streams
            format = ET.SubElement(root, "format")
            format.set('name', 'rem')
            format.set('type', 'application/rdf+xml')
            format.set('docs', 'http://www.openarchives.org/ore/toc')
            
            format = ET.SubElement(root, "format")
            format.set('name', 'relationships')
            format.set('type', 'application/rdf+xml')
            
            response.headers['Content-Type'] = 'application/xml'
            c.unapi = ET.tostring(root)
            return render('unapi')
            
        if id and g.f.ri.doesPIDExist(id):
            if not format:
                content_type = g.f.ri.getContentType(id)
                model = g.cm.get_model(content_type)
                ds_list = g.f.listDatastreams(id, format='python')
                root = ET.Element('formats')

                if 'MODS' in ds_list or 'MODS' in model['metadata_formats']:
                    format = ET.SubElement(root, "format")
                    format.set('name', 'MODS')
                    format.set('type', ds_list['MODS']['mimetype'])
                    format.set('title', ds_list['MODS']['label'])
                    format.set('docs', 'http://www.loc.gov/standards/mods/v3/mods-3-2.xsd')
                    ds_list.pop('MODS')


                # Just to bolster up the list with pointers to relevant docs
                if 'DC' in ds_list and 'DC' in model['metadata_formats']:
                    format = ET.SubElement(root, "format")
                    format.set('name', 'DC')
                    format.set('type', ds_list['DC']['mimetype'])
                    format.set('title', ds_list['DC']['label'])
                    format.set('docs', 'http://www.openarchives.org/OAI/2.0/oai_dc.xsd')
                    ds_list.pop('DC')

                # Generated streams
                format = ET.SubElement(root, "format")
                format.set('name', 'rem')
                format.set('type', 'application/rdf+xml')
                format.set('docs', 'http://www.openarchives.org/ore/toc')
                
                format = ET.SubElement(root, "format")
                format.set('name', 'relationships')
                format.set('type', 'application/rdf+xml')
                
                for ds in ds_list:
                    if ds not in model['admin_datastreams']:
                        format = ET.SubElement(root, "format")
                        format.set('name', ds_list[ds]['dsid'])
                        format.set('type', ds_list[ds]['mimetype'])
                        format.set('title', ds_list[ds]['label'])

                response.headers['Content-Type'] = 'application/xml'
                c.unapi = ET.tostring(root)
                return render('unapi')
            else:
                if format=='rem':
                    h.redirect_to(controller='/objects', action='resource_map', id=id)
                    
                if format=='relationships':
                    h.redirect_to(controller='/objects', action='relationships', id=id, format='xml')
                    
                if format=='oai_dc':
                    h.redirect_to(controller='/objects', action='download', id=id, dsid='DC')
                    
                ds_list = g.f.listDatastreams(id, format='python')
                if format in ds_list:
                    h.redirect_to(controller='/objects', action='download', id=id, dsid=format)
                else:
                    abort(404, 'No such datastream')
