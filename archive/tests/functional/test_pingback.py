from archive.tests import *

class TestPingbackController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='pingback'))
        # Test response...
