from archive.tests import *

class TestUnapiController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='unapi'))
        # Test response...
