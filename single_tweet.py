import tweepy
from generate import single_tweet
from tweeter import login, twitter_keys
import re

api = login(twitter_keys)
string = single_tweet()

para_number_regex = re.compile(r'[1-9]+[\.|\-][A-Z]?[\.|\-]?[1-9]+\.\s?')
para_numbers = re.findall(para_number_regex, string)
maping = {}
for match in para_numbers:
    maping[match] = ''
for i, j in maping.items():
    string = string.replace(i, j)

sentance_list = string.split('.')
tweet = ""
for sentnace in sentance_list:
    if len(tweet) + len(sentnace) <= 280:
        tweet += sentnace + '. '

print(tweet)
# api.update_status(tweet)