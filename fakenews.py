import botornot
import tweepy
import requests
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from requests import ConnectionError, Timeout

twitter_app_auth = {
	"access_token": "2208305132-4VDnZQ4iU7Jnk3a35BJnSiPvHcFO08fvGijBOzq",
	"access_token_secret": "6doGffK5c8QXMWkgOOmpYw5PemkgeVXsoFyyEs4ZNGGr9", 
	"consumer_key": "lEi4ZCaCJYb0XeI1NbbT5ON7m", 
	"consumer_secret": "sembzN32IjowIpO4MbfAuPcoCrGEBgl6Bdcs8BLMGccSW1P7RZ"
	}

bon = botornot.BotOrNot(**twitter_app_auth)

access_token = "2208305132-4VDnZQ4iU7Jnk3a35BJnSiPvHcFO08fvGijBOzq"
access_token_secret = "6doGffK5c8QXMWkgOOmpYw5PemkgeVXsoFyyEs4ZNGGr9"
consumer_key = "lEi4ZCaCJYb0XeI1NbbT5ON7m"
consumer_secret = "sembzN32IjowIpO4MbfAuPcoCrGEBgl6Bdcs8BLMGccSW1P7RZ"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

accounts = []
for tweet in tweepy.Cursor(api.search, q=('"#boycotthamilton"')).items(500):
    user = tweet.author.screen_name 
    if not accounts.__contains__(user):
        accounts.append(user)

results = list(bon.check_accounts_in(accounts))
# score_list = []
# for user in results:
# 	score = results['value'] 
# 	score_list.append(score)

print(results[0:10])


