"""
RePEc - ReDIF parser.
Aim: Harvest an 'rdf' file, given by a urllib gettable URI, and parse it into a
dictionary. The dictionary keys will be the XXX of the 'Number: XXX' line in a 
given record, and the values will be a simple dict of the name value pairs.

TODO: If necessary, group the author params into individual dictionaries. This isn't
used in the Oxford Economics RePEc archive, but is in the ReDIF spec, so might be
used by other institutions. User, beware :)
"""

import StringIO, urllib2, urllib, re

from archive.lib.dc import *

class Repec(object):
    def __init__(self, url=None, file_ending="\r\n", encoding='latin1'):
        """
        Pass a parameter of 'url' to initiate the parser. This should be
        the location of the 'papers.rdf' file
        """
        self.url = url
        self.cached_file = None
        self.records = []
        self.encoding = encoding
        self.number_regex = re.compile('Number: ([0-9]*)', re.MULTILINE)
        self.file_ending = file_ending
    
    def getFile(self):
        if self.url != None:
            response = None
            try:
                # Get the file and read it all into memory
                response = urllib2.urlopen( self.url )
            except urllib2.HTTPError, exc:
                response = exc.code
            
            if not isinstance(response, int):
                self.cached_file = response
                # return True for a loaded file
                return True
        else:
            # return False for an unusable URL/no network connection/etc.
            return False
    
    def reload(self):
        # Null the records and the file handle
        self.records = []
        self.cached_file = None
        
        return self.fragment()
    
    def fragment(self):
        if self.cached_file == None and self.getFile() == False:
            return False
        
        if self.records != None and len(self.records)>0:
            return True
        
        individual_record = []
        for line in self.cached_file:
            line = unicode(line,self.encoding)
            
            if line == self.file_ending:
                record = ''.join(individual_record)
                # Check to see if the record is more than just a number of
                # line terminators.
                if len(record)>2:
                    self.records.append(record)
                individual_record = []
            else:
                individual_record.append(line)
            
        # Add the final record, if present
        record = ''.join(individual_record)
        if len(record)>2:
            self.records.append(record)
        
        self.cached_file.close()
        self.cached_file = None
        
        # Reverse the order of the list, to aid incremental updates
        self.records.reverse()
        
        return True
    
    def get_largest_index_of_record(self):
        if self.url != None and self.fragment() != False and self.records != None:
            return self.number_regex.findall(self.records[0])[0]
        else:
            return '0'

    def get_number_of_records(self):
        if self.url != None and self.fragment() != False and self.records != None:
            return len(self.records)
        else:
            return '0'

    def render_record_to_params(self, record, parse_til_record=0):
        # Get the number of this record:
        number = self.number_regex.findall(record)[0]
        try:
            if int(number)<=parse_til_record:
                return False, False
        except ValueError:
            print 'Not a number... :('
            return False, False
        
        params = {}
        for line in record.split(self.file_ending):
            fragments = line.split(':')
            name = fragments.pop(0)
            value = ':'.join(fragments)
            if params.get(name, None) != None:
                # Check to see if it is a list yet
                if not isinstance(params[name], list):
                    params[name]=[params[name]]
                # append the new value
                params[name].append(value)
            else:
                params[name] = value
        
        return number, params
        
    def harvest(self, last_highest_number=0):
        if self.url != None and self.fragment() != False:
            records = {}
            for record in self.records:
                number, params = self.render_record_to_params(record, parse_til_record=last_highest_number)
                if number == False and params == False:
                    break
                params['original_redif'] = record
                records[number] = params
            return records
        return None
       
    def get_as_DublinCore(self, last_highest_number=0):
        records = self.harvest(last_highest_number=last_highest_number)
        for index in records.iterkeys():
            records[index] = self.translate_ReDIF_to_DC(records[index])
        return records

    def translate_ReDIF_to_DC(self, params):
        # Initiate new DC metadata helper
        dc = DC()
        
        # Handle the fields that translate into the dc:identifier field
        identifiers = {'Number':'RePeC-number: ',
                       'Handle':'RePeC-Handle: ',
                       'File-URL':'Original-URL: '}
        
        # One to one field mapping
        mapping = {'Template-Type':'type',
                   'Title':'title',
                   'Abstract':'abstract',
                   'Author-Name':'creator',
                   'File-Format':'format',
                   'Creation-Date':'date'}
        
        # Get some handy fields out for ready usage
        file_url = None
        if params.get('File-URL', None) != None:
            file_url = params['File-URL']
            
        title = None
        if params.get('Title', None) != None:
            title = params['Title']
        
        # Simple mapping
        for name in mapping:
            if params.get(name, None) != None:
                # List or literal?
                if isinstance(params[name], list):
                    for value in params[name]:
                        dc.addField(mapping[name], value)
                else:
                    dc.addField(mapping[name], params[name])
        
        # Multiple value fields:
        # JEL-classification
        if params.get('Classification-JEL',None) != None:
            for classification in params['Classification-JEL'].split(','):
                dc.addField('subject','Classification-JEL: '+classification)

        # Keywords
        if params.get('Keywords',None) != None:
            for keyword in params['Keywords'].split(','):
                dc.addField('subject', keyword)
        
        # Handle the various identifiers
        for identifier in identifiers:
            if params.get(identifier, None) != None:
                # List or literal?
                if isinstance(params[identifier], list):
                    for value in params[identifier]:
                        dc.addField('identifier', identifiers[identifier]+value)
                else:
                    dc.addField('identifier', identifiers[identifier]+params[identifier])
        
        return {'title':title,'url':file_url, 'dc':dc, 'redif':params.get('original_redif',None)}

