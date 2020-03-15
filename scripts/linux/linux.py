    #print("operating system not supported")
from sys import platform
import os

#os.system('sudo apt install wireguard')

import apt

cache = apt.Cache()
if cache['wireguard'].is_installed:
    print "YES it's installed"
else:
    print "NO it's NOT installed"
