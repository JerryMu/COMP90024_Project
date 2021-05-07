import couchdb2
master_node = 'http://admin:admin@172.26.128.217:5984/'
couch = couchdb2.Server(master_node)
tweet_db = couch['tweet']


"""    
def view(self, designname, viewname,
     key=None, keys=None, startkey=None, endkey=None,
     skip=None, limit=None, sorted=True, descending=False,
     group=False, group_level=None, reduce=None, include_docs=False,
     update=None):
"""

result = tweet_db.view("tweetDesign", "test2", key=None, group_level=2)
for item in result:
    print(item)