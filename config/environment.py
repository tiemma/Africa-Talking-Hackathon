import os

ENVIRONMENT = os.environ['DEVPATH_ENVIRONMENT']

if ENVIRONMENT == 'local':
    SETTINGS_MODULE = 'config.settings.local'
elif ENVIRONMENT == 'development':
    SETTINGS_MODULE = 'config.settings.development'
    