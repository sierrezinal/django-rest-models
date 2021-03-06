import copy

from testsettings import *

DATABASES = copy.deepcopy(DATABASES)
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'django-rest-models',
    'USER': os.environ.get('DB_USER', 'postgres'),
    'PASSWORD': os.environ.get('DB_PWD', ''),
    'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
    'PORT': '5432',
}
