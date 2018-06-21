# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-c&qt=71oi^e5s8(ene*$b89^#%*0xeve$x_trs91veok9#'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'asifkjakdfj-m6o6pqsdkfjakdf8er7jiso4mmgbaoseku.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'skdfjkdjfkdsfkjdkjfdk'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# [START db_setup]
import os
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/<proj_name>:<instance_name>',
            'NAME': '<database_name>',
            'PASSWORD': '<password>',
            'USER': 'root',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '<database_name>',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
# [END db_setup]