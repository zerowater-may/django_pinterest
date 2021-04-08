from .base import *


def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret
    

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env(
    env_file= os.path.join(BASE_DIR, '.env')
    # env_file = './.env'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '5nb@rlfrak967e6#g4pr)8&s2tf*zsquyhbh7_x52d@7g+__+@'
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zerowater',
        'USER': 'zerowater',
        'PASSWORD': read_secret('MYSQL_PASSWORD'),
        # 'PASSWORD': 'fkaustkfl123!',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}