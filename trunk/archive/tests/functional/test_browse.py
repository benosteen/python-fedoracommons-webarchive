from archive.tests import *

class TestBrowseController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='browse'))
        # Test response...
