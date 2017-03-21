# -*- coding:utf-8 -*-
"""Application manager module.

Provides script commands for deploying, testing, building.
"""

from app import app
import bottle
import click
import subprocess
from settings import WSGI_OPTS, DEBUG


@click.group()
def manager():
    pass


@manager.command()
@click.option('--host', default=WSGI_OPTS['host'], type=str, help='Set Application server host.')
@click.option('--port', default=WSGI_OPTS['port'], type=int, help='Set Application server port.')
@click.option('--server', default=WSGI_OPTS['server'], type=str, help='Set Application server wsgi container.')
@click.option('--reloader', default=WSGI_OPTS['reloader'], type=bool, help='Set server host reloader option.')
@click.option('--debug', default=DEBUG, type=bool, help='Set Application server host debug mode.')
def runserver(host, port, server, reloader, debug):
    """deploy application

    Args:
        host (str): Application IP or domain name.
        port (int): Application port.
        server (str): Application wsgi server alias.
        reloader (bool): Enable Application auto-reload on change.
        debug (bool): Enable Application DEBUG mode.
    
    """

    bottle.debug(debug)

    bottle.run(
        app=app,
        server=server,
        host=host,
        port=port,
        reloader=reloader
    )


@manager.command()
def build():
    """Compile Web components in plain javascript.
    """
    subprocess.Popen(
        ["riot", "components/app", "static/app/components"]
    )

    subprocess.Popen(
        ["riot", "components/admin", "static/admin/components"]
    )

if __name__ == '__main__':

    manager()
