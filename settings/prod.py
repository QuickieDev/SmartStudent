# -*- coding: utf-8 -*-
"""Smart Student app development settings.
"""


DEBUG = False

server_secret = '#$51365871273092qhwjdjasd913'

SERVER_HOST = 'smart-student'

WSGI_OPTS = {
    'server': 'gunicorn',
    'reloader': True,
    'port': 8000,
    'host': '127.0.0.1'
}


class Singleton(object):
    _instance = None
    _cls = None

    @classmethod
    def make(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls._cls(*args, **kwargs)
        return cls._instance

