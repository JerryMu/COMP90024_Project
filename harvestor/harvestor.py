import tweepy
import os
from pprint import pprint
import couchdb
import json

def createdb(couchserver,dbname):
    if dbname in couchserver:
        return couchserver[dbname]
    else:
        return couchserver.create(dbname)

def create_region(couch_database):
    with open('region.json') as file:
        for region in file.readlines():
            data=json.loads(region)
            try:
                pushdata(data, 'region', couch_database)
            except:
                pass

def pushdata(data, database_name, couch_database):
    for db in couch_database:
        if db._name == database_name:
            db.save(data)
            break
    else:
        print('no such database')

f=open("ip.txt", "r")
couchdb_master_ip=f.readline().rstrip()
couchdb_master_login_url='http://admin:admin@'+couchdb_master_ip+':5984/'
db_children=f.read().splitlines()
f.close()

couchserver = couchdb.Server('http://'+couchdb_master_ip+':5984/')
couchserver.resource.credentials=('admin','admin')

couch_database = []
database_name = ['tweet','region']

for dbname in database_name:
    couch_database = couch_database+[createdb(couchserver,dbname)]
    for child in db_children:
        couchserver.replicate(couchdb_master_login_url+dbname,'http://admin:admin@'+child+':5984/'+dbname,create_target=True,continuous=True)

create_region(couch_database)


"""
for dbname in dbnamelist:
    self.db=self.db+[self.createdb(couchserver,dbname)]
    for child in db_children:
        couchserver.replicate(couchdb_master_login_url+dbname,'http://admin:admin@'+child+':5984/'+dbname,create_target=True,continuous=True)
"""

# access twitterApi's key and token
consumer_key = "oLA7aTp8LXxn4MtfSdGVjWTJQ"
consumer_secret = "SH6NDeJg5YkfcxOmtvxtu52FlHv9SddAyOzn12PKZPxc1nSw3C"
access_token = "1385952256810389507-9Kmzf60GptC1sLDEWr2gjthN5wIpct"
access_token_secret = "O9LyTLbi1Zhj6J3PVGBUhMmBBGhUm6I3HWFrgPg4IXUXu"

# 创建认证对象
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# 设置你的access token和access secret
auth.set_access_token(access_token, access_token_secret)
# 传入认证信息，并创建API对象
api = tweepy.API(auth, timeout=15, wait_on_rate_limit=True)

# 国家地区
places = api.geo_search(query="Australia", granularity="country", trim_place="false")
place_id = places[0].id

# Define the search term and the date_since date as variables
search = "place:%s #covid-19 OR #Covid -filter:retweets" % place_id
#date_since = "2019-11-16"

#tweets = tweepy.Cursor(api.search,
#          q=search,
#          lang="en",
#          since=date_since).items(600)

#tweets = api.search(q="place:%s fuck" % place_id)

all_tweets = []
for index, tweet in enumerate(tweepy.Cursor(api.search,q="place:%s"%place_id,lang="en").items(700)) :
    print(index, tweet.text + " | " + tweet.place.name  + " | " + str(tweet.created_at))
    #all_tweets.append({"id":str(tweet.id), "uid":str(tweet.user.id), "text":str(tweet.text), "created_at":str(tweet.created_at), "city":str(tweet.place.name), "country":str(tweet.place.country), "box":str(tweet.place.bounding_box.coordinates)})

#for tweet in all_tweets:
    #pushdata(tweet,'tweet',couch_database)
    #print(tweet)
del(all_tweets)

print('------------------')
