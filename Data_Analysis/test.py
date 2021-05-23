import couchdb
import pandas as pd
MASTER_NODE_URL = 'http://admin:admin@172.26.128.217:5984/'
server = couchdb.Server(MASTER_NODE_URL)
try:
    server.create("scenario_1")
except couchdb.http.PreconditionFailed:
    print('data base already exists')

# db = server["scenario_1"]
# db['test'] = {'test':'test'}
# try:
#     db.delete(db['test'])
#     db.delete(db['test'])
#     db.delete(db['test'])
#     db.delete(db['test'])
#     db['test'] = {'test':'test'}
# except couchdb.http.ResourceNotFound:
#     pass

df1 = pd.DataFrame()
df1['a'] = [1,2,3,4]
df1['b'] = [1,2,3,4]
df1['c'] = [1,2,3,4]

print(df1.groupby(['a','b']).sum()[1].to_dict())