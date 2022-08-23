from split_settings.tools import optional, include

BASE_SETTING=[
    'components/common.py',
    'components/database.py',    
]

include(*BASE_SETTING)