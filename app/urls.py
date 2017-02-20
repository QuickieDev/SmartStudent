# -*- coding: utf-8 -*-
"""`app.urls` module.

Provides application routing.
"""

from app.handlers import IndexHandler
from bottle import static_file
from bottle_neck import Router


static_server = lambda filename: static_file(filename, root='static')

router = Router()
router.register_handler(IndexHandler, entrypoint='/')
router.register_handler(static_server, entrypoint='/static/<filename:path>')
