import couchdb2
import pandas as pd
master_node = 'http://admin:admin@172.26.128.217:5984/'
couch = couchdb2.Server(master_node)
tweet_db = couch['all_tweet']


"""    
def view(self, designname, viewname,
     key=None, keys=None, startkey=None, endkey=None,
     skip=None, limit=None, sorted=True, descending=False,
     group=False, group_level=None, reduce=None, include_docs=False,
     update=None):
"""

result = tweet_db.view("tweetDesign", "get_basic_data", include_docs=True)
#for row in result:
 #   print(row)
data = [row['doc'] for row in result]
df = pd.DataFrame(data)
df.to_csv('test.csv')
