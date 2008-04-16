import os.path

import paste.fileapp
from pylons.middleware import error_document_template, media_path

from archive.lib.base import *

class ErrorController(BaseController):

    def document(self):
        c.code = request.GET.get('code', '')
        c.message = request.GET.get('message', '')
        return render('error')

