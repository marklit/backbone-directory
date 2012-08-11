from fabric.api import env
from fabs.dev import *
from fabs.testing import *


env.django_apps = ('api', 'contacts', 'home',)
env.backend_iface = '0.0.0.0:8001'
env.frontend_port = 8000