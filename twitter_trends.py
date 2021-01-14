import pymongo
import dns
import os
import urllib
from datetime import datetime
import tweepy

consumerKey = os.getenv("TWITTER_CONSUMER_KEY")
consumerSecret = os.getenv("TWITTER+CONSUMER_SECRET")
accessToken = os.getenv("TWITTER_ACCESS_TOKEN")
accessTokenSecret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

print("Here are the secret keys\n")
print(consumerKey)
print(consumerSecret)
print(accessToken)
print(accessTokenSecret)

authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
authenticate.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(authenticate, wait_on_rate_limit=True)
trends = api.trends_place(id=2295414)

password = os.getenv("DB_PASSWORD")
client = pymongo.MongoClient(
    "mongodb+srv://Srujan:" + password + "@cluster0.cqicm.mongodb.net/twitter_trends?retryWrites=true&w=majority")

db = client.get_database('twitter_trends')  # To get database

trends_db = db.twitter  # To take the collection

now = datetime.now()
time_now = now.strftime("%Y-%m-%dT%H:%M:%S")

for i in trends[0]['trends']:
    if i['tweet_volume'] is None:
        i['tweet_volume'] = 0
    new_entry = {
        'name': i['name'],
        'time': time_now,
        'tweet_volume': i['tweet_volume']
    }
    trends_db.insert_one(new_entry)
