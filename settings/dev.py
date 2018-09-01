# -*- coding: utf-8 -*-
"""Smart Student app development settings.
"""


DEBUG = True

server_secret = '#$51365871273092qhwjdjasd913'

SERVER_HOST = 'localhost'

WSGI_OPTS = {
    'server': 'gunicorn',
    'reloader': True,
    'port': 8085,
    'host': 'localhost'
}


POSTGRES = {
    'host': 'localhost',
    'port': 7654,
    'user': 'pav',
    'password': 'iverson87',
    'database': 'geotag_platform'
}


class Singleton(object):
    _instance = None
    _cls = None

    @classmethod
    def make(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls._cls(*args, **kwargs)
        return cls._instance

