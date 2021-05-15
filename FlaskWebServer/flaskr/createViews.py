import couchdb2



master_node = 'http://admin:admin@172.26.128.217:5984/'
couch = couchdb2.Server(master_node)
tweet_db = couch['all_tweet']
tweet_design = 'tweetDesign'

# all views
views_json = {
                  "views":{
                      "test0": {"map": "function (doc) {emit(doc.uid, doc.text);}"},
                      "get_basic_data": {"map": "function (doc) {emit(doc.uid, doc.text, doc.created_at, doc.city);}"}
                  }
              }


tweet_db.put_design("tweetDesign", views_json)

