import httplib, urllib
import simplejson

class Term_extraction(object):
    def __init__(self):
        #set up the defaults
        self.AppId = 'hqUYzXXV34ET.aZ8tP5KsI7hz3YQ4rlavTHR45fIAW46Je0U7a6x.4jOiMV3PcG42w--'
        self.output = 'json'
        
    def get_term_list(self, context=''):
        params = urllib.urlencode({'appid': self.AppId, 'context': context.encode('UTF-8'), 'output': self.output})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPConnection("search.yahooapis.com:80")
        conn.request("POST", "/ContentAnalysisService/V1/termExtraction", params, headers)
        response = conn.getresponse()
        if response.status == 200:
            resultset = simplejson.load(response)
            return resultset['ResultSet']['Result']
        else:
            return ['error']

