import copy

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s:%(funcName)s:'
                      '%(lineno)s %(processName)s %(process)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s:%(funcName)s:%(lineno)s::'
                      '%(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': []
        }
    },
    'loggers': {
        '': {
            'handlers': ['mail_admins', 'console'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['mail_admins', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.db.backends': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'amqp': {
            'handlers': ['mail_admins', 'console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'auth': {
            'handlers': ['mail_admins', 'console'],
            'level': 'DEBUG',
        },
        # APP_NAME: {
        #     'handlers': ['mail_admins', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    }
}

local_logger_conf = {
    'handlers': ['mail_admins', 'console'],
    'level': 'DEBUG',
    'propagate': False,
}

LOGGING['loggers'].update({
    app: copy.deepcopy(local_logger_conf) for app in LOCAL_APPS
})
