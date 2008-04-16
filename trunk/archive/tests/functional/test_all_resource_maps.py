from archive.tests import *

class TestAllResourceMapsController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='all_resource_maps'))
        # Test response...
