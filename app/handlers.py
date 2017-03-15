# -*- coding: utf-8 -*-
"""`app.handlers` module.

Provides application web handlers.
"""

from bottle import jinja2_template
from bottle_neck import BaseHandler



class IndexHandler(BaseHandler):
    """Main page handler.
    """

    render = jinja2_template

    def get(self):
        return self.render('index.html', {})
