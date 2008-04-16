import sys
import ZSI
from archive.lib.Fedora_API_M_WSDL_services import *
kw={'tracefile':sys.stdout, 'auth' : (ZSI.auth.AUTH.httpbasic, 'fedoraAdmin', 'fedoraAdmin') }
loc = Fedora_API_M_ServiceLocator()
api_m = loc.getFedora_API_M(**kw)


