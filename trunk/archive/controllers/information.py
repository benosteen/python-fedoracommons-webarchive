import logging

from archive.lib.base import *

log = logging.getLogger(__name__)

class InformationController(BaseController):

    def index(self):
        return render('root_page')
        
    def help(self):
        return render('help')
        
    def contribute(self):
        return render('contribute')
        
    def disclaimer(self):
        return render('disclaimer')
        
    def accessibility(self):
        return render('accessibility')
        
    def urls(self):
        return render('coolurls')
        
    def tools(self):
        return render('tools')
