from fabric.api import env
from fabs.coding import *
from fabs.serve import *
from fabs.testing import *


env.django_apps = ('api', 'contacts', 'home',)
env.web_interface = '0.0.0.0:8000'