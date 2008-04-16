from archive.tests import *

class TestObjectsController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='objects'))
        # Test response...
