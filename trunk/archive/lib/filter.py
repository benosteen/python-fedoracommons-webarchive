import re

class Filter(object):
    def __init__(self):
        self.illegal_regex = self.make_illegal_xml_regex()
        
    def raw_illegal_xml_regex(self):
        """ From http://boodebr.org/main/python/all-about-python-and-unicode"""
        """    
        I want to define a regexp to match *illegal* characters.
        That way, I can do "re.search()" to find a single character,
        instead of "re.match()" to match the entire string. [Based on
        my assumption that .search() would be faster in this case.]

        Here is a verbose map of the XML character space (as defined
        in section 2.2 of the XML specification):
        
             u0000 - u0008           = Illegal
             u0009 - u000A           = Legal
             u000B - u000C           = Illegal
             u000D                   = Legal
             u000E - u001F           = Illegal
             u0020 - uD7FF           = Legal
             uD800 - uDFFF           = Illegal (See note!)
             uE000 - uFFFD           = Legal
             uFFFE - uFFFF           = Illegal
             U00010000 - U0010FFFF = Legal (See note!)
        
        Note:
        
           The range U00010000 - U0010FFFF is coded as 2-character sequences
           using the codes (D800-DBFF),(DC00-DFFF), which are both illegal
           when used as single chars, from above.
        
           Python won't let you define \U character ranges, so you can't
           just say '\U00010000-\U0010FFFF'. However, you can take advantage
           of the fact that (D800-DBFF) and (DC00-DFFF) are illegal, unless
           part of a 2-character sequence, to match for the \U characters.
        """

        # First, add a group for all the basic illegal areas above
        re_xml_illegal = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])'

        re_xml_illegal += u"|"

        # Next, we know that (uD800-uDBFF) must ALWAYS be followed by (uDC00-uDFFF),
        # and (uDC00-uDFFF) must ALWAYS be preceded by (uD800-uDBFF), so this
        # is how we check for the U00010000-U0010FFFF range. There are also special
        # case checks for start & end of string cases.

        # I've defined this oddly due to the bug mentioned at the top of this file
        re_xml_illegal += u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
                          (unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                           unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                           unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff))

        return re_xml_illegal
        
    def make_illegal_xml_regex(self):
        return re.compile( self.raw_illegal_xml_regex() )

    def filter_non_XML_text(self, text):
        # Replace all the non-XML acceptable unicode text with ?
        filtered_text = None
        if text != '' and text != None:
            filtered_text = self.illegal_regex.sub('?', text)
        return filtered_text
        
    def xmlEntityDecode(self, string):
        if string:
            string = string.replace('&lt;','<')
            string = string.replace('&gt;','>')
            string = string.replace('&amp;','&')
            string = string.replace('&apos;','\'')
            string = string.replace('&quot;','"')
        return string

    def xmlEntityEncode(self, string):
        if string:
            string = string.replace('<','&lt;')
            string = string.replace('>','&gt;')
            string = string.replace('&','&amp;')
            string = string.replace('\'','&apos;')
            string = string.replace('"','&quot;')
            string = string.replace('href=&quot;','href="')
            string = string.replace('&quot;>','">') 
        return string

    def filter_params_to_author(self, params):
        # hash to hold author details
        allowed_fields = ['termsofaddress','family','given','displayform', 'description']
        affiliation_types = ['email', 'website','institution',
                             'faculty','researchgroup','pid',
                             'college','funding','grantnumber',
                             'depiction']
        
        a = {}
        
        # Handle the basic fields:
        for field in allowed_fields:
            field_value = self.filter_non_XML_text(params.get(field, None))
            if field_value != None and field_value != u'':
                a[field] = field_value
        
        # Handle the affiliations:
        affiliation = {}
        for field in affiliation_types:
            field_value = self.filter_non_XML_text(params.get(field, None))
            if field_value != None and field_value != u'':
                affiliation[field] = field_value
                
        a['affiliation'] = affiliation
                
        # Now to handle the multiple fields
        # Roles
        roles = []
        stem = 'role'
        index_label = 1
        while( self.filter_non_XML_text(params.get(stem+str(index_label), None)) != None  and self.filter_non_XML_text(params.get(stem+str(index_label), None)) != u''):
            roles.append(self.filter_non_XML_text(params[stem+str(index_label)]))
            index_label += 1
            # limit -> 20 roles
            # sensible number of roles x 5, but small enough to stop malicious use
            if index_label > 20:
                break
        
        a['roles'] = roles
        
        return a
            
        
        
