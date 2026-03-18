import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['faccinengenharia.com', 'www.faccinengenharia.com', '68.183.24.170']
SECRET_KEY = os.environ['SECRET_KEY']

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

try:
    from .local import *
except ImportError:
    pass
