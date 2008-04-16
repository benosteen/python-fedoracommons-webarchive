import os
import paste.fileapp

class temporaryFileApp(paste.fileapp.FileApp):
    def __init__(self, filename):
        self.temp_file_name = filename
        paste.fileapp.FileApp.__init__(self, filename)
    
    def __del__(self):
        try:
            os.remove(self.temp_file_name)
        except:
            pass
        paste.fileapp.FileApp.__del__(self)
