from archive.tests import *

class TestTrackbackController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='trackback'))
        # Test response...
