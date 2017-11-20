import os
from django.core.wsgi import get_wsgi_application

import config.environment.local as  SETTINGS_MODULE
from whitenoise.django import DjangoWhiteNoise



os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
application = get_wsgi_application()
application = DjangoWhiteNoise(application)