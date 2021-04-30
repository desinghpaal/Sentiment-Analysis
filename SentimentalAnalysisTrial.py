import tweepy
from textblob import TextBlob
consumer_key = 'RxlvB9EOulCFLO0n7D6B9DNCn'
consumer_secret = 'V57nNgToH3iip0HXNXqh4Sw3LpYzJbGCMobUI5MaTEhPzj5VEA'
access_token = '984360223581204480-lSUxqpDhd8wId6EXtfhCIHHhhSlRgi6'
access_token_secret = '1LVkjjYoua8Aw4lSBIuF8PuA0fHbuhIJNsCkvc9hAGVPD'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api =tweepy.API(auth)
public_tweets = api.search('Covid')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)