import click
from flask import Flask, jsonify
from flask.cli import FlaskGroup

myapi = Flask(__name__)


@myapi.route('/api/healthcheck')
def healthcheck():
    """A simple HTTP route."""
    return jsonify({'status': 'green'})


@click.group(cls=FlaskGroup, create_app=lambda _info: myapi)
def cli():
    """
    Based on http://flask.pocoo.org/docs/0.12/cli/#custom-scripts
    This function allows to expose the Flask CLI commands with the application
    already binded.
    """
    pass
