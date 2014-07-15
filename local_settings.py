__author__ = 'Michael'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'party',
    }
}
INTERNAL_IPS = ("127.0.0.1", "10.0.2.2")