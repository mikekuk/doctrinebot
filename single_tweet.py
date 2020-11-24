import tweepy
from generate import single_tweet
from tweeter import login, twitter_keys
from parse_txt import parse_for_tweeter
import re

api = login(twitter_keys)
string = single_tweet()

tweet = parse_for_tweeter(string)

# api.update_status(tweet)

if __name__ == '__main__':
    print('\n--------------------\n')
    print(tweet)
    print('\n--------------------\n')