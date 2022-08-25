from os import environ
from split_settings.tools import optional, include

DOMAIN_NAME = environ.get('DOMAIN_NAME')

BASE_SETTING=[
    'components/common.py',
    'components/database.py', 
    'components/logging.py', 
    'components/email.py',       
]

include(*BASE_SETTING)
