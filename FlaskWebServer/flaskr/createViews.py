import couchdb2



master_node = 'http://admin:admin@172.26.128.217:5984/'
couch = couchdb2.Server(master_node)
tweet_db = couch['tweet']
tweet_design = 'tweetDesign'

# all views
views_json = {
                  "views":{
                      "test0": {"map": "function (doc) {emit(doc.uid, doc.text);}"},
                      "test1": {"map": "function (doc) {emit(doc.uid, doc.city);}"},
                      "test2": {"map": "function (doc) {emit([doc.city], 1);}", "reduce": "_count"},
                      "test3": {"map": "function (doc) {emit([doc.city, doc.uid], 1);}", "reduce": "_count"}
                  }
              }


tweet_db.put_design("tweetDesign", views_json)

