import tweepy
import os
from pprint import pprint

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
for index, tweet in enumerate(tweepy.Cursor(api.search,q="place:%s"%place_id,lang="zh",since="2020-03-15").items(700)) :
    print(index, tweet.text + " | " + tweet.place.name  + " | " + str(tweet.created_at))
    #all_tweets.append({"id":str(tweet.id), "uid":str(tweet.user.id), "text":str(tweet.text), "created_at":str(tweet.created_at), "city":str(tweet.place.name), "country":str(tweet.place.country), "box":str(tweet.place.bounding_box.coordinates)})

#for tweet in all_tweets:
    #pushdata(tweet,'tweet',couch_database)
    #print(tweet)
del(all_tweets)

print('------------------')
