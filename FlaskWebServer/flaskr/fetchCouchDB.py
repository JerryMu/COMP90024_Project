import couchdb2
from flask import current_app, g
from flask.cli import with_appcontext

MASTER_NODE = 'http://admin:admin@172.26.128.217:5984/'


def get_db(db_name):
    server = couchdb2.Server(MASTER_NODE)
    if db_name not in g:
        g.db_name = server[db_name]
    return g.db_name
