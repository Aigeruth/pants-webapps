# Application as a library to make the binary target specificions shorter.
python_library(
    name='myapi',
    sources=['app.py'],
    dependencies=[
        '3rdparty/python:Flask',
    ],
)
# This is a binary target for development that exposes Flask CLI commands.
# Docs: http://flask.pocoo.org/docs/0.12/cli/
# Note: FLASK_APP does not have to be specified, because it is bind through
#       the wrapper method.
python_binary(
    name='myapi-cli',
    dependencies=[':myapi'],
    entry_point='myorg.myapi.app:cli',
)
# This is a binary target for production use. It exposes gunicorn command,
# therefore it expects an application module.
# Example use: myapi-gunicorn.pex myorg.myapi.app:myapi
python_binary(
    name='myapi-gunicorn',
    dependencies=[
      '3rdparty/python:gunicorn',
      ':myapi',
    ],
    entry_point='gunicorn.app.wsgiapp:run',
)
