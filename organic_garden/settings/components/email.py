# EMAIL_HOST = env('EMAIL_HOST', default='email-smtp.ap-south-1.amazonaws.com')
EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
SERVER_EMAIL = f"admin@{DOMAIN_NAME}"
DEFAULT_FROM_EMAIL = f"Do not reply<admin@{DOMAIN_NAME}>"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = True
EMAIL_PORT = 587

