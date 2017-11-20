import sys

sys.path.append('..') 

ENVIRONMENT = 'local'
SETTINGS_MODULE = 'config.settings.local'

if ENVIRONMENT == 'local':
    SETTINGS_MODULE = 'config.settings.local'
