from .common import *

SECRET_KEY = '_dt^q^-^9*ea%@s#h^3#2m)#vk(u(8l*o3cc&s6Xi2AuABlrQ2'
debug = True
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "######",
        'HOST': "127.0.0.1",
        'PORT': 5432,
        'USER': "",
        'PASSWORD': "",
    }
}
