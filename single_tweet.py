import tweepy
from generate import single_tweet
from tweeter import login, twitter_keys
from parse_txt import parse_for_tweeter
import re

api = login(twitter_keys)
string = single_tweet()

tweet = parse_for_tweeter(string)

print(tweet)
api.update_status(tweet)