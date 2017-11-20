import os
from django.core.wsgi import get_wsgi_application

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(sys.path)

from config.environment import SETTINGS_MODULE
from whitenoise.django import DjangoWhiteNoise



os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
application = get_wsgi_application()
application = DjangoWhiteNoise(application)