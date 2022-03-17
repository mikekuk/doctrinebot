import tweepy
from generate import single_tweet, make_text
from tweeter import login, twitter_keys
from parse_txt import parse_for_tweeter
import re

api = login(twitter_keys)

username='@BritishArmy'
tweets_list= api.user_timeline(username, count=1, include_rts=False) 
text = tweets_list[0].text

split_text = text.split()

if len(split_text) >= 6:
    fir_words = " ".join(split_text[:6])
else:
    fir_words = " ".join(split_text[:-1])

string = make_text(fir_words)


tweet = parse_for_tweeter(string)

api.update_status(tweet)

if __name__ == '__main__':
    print('\n--------------------\n')
    print(tweet)
    print('\n--------------------\n')