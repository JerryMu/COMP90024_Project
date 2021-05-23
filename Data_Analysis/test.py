import couchdb

MASTER_NODE_URL = 'http://admin:admin@172.26.128.217:5984/'
server = couchdb.Server(MASTER_NODE_URL)
try:
    server.create("scenario_1")
except couchdb.http.PreconditionFailed:
    print('data base already exists')