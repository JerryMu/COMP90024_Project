import os
from time import time
from flask import Flask
import logging
from . import index


# # create logger
logging.basicConfig(filename='flask.log',
                    filemode='w',
                    format='"%(asctime)s;%(levelname)s;%(message)s"',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger("\nflask")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to loggertestApis
logger.addHandler(ch)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    """
    register blueprints
    """
    app.register_blueprint(index.bp)


    return app