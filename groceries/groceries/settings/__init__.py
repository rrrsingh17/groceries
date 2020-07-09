from os import environ  # NOQA

env = environ['ENV'].lower() if 'ENV' in environ else 'development'

if env == "production":
    from .production import *  # NOQA
elif env == "staging":
    from .staging import *  # NOQA
else:
    from .local import *  # NOQA
