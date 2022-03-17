import gpt_2_simple as gpt2
import os
import requests
import re
from parse_txt import parse_for_tweeter

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name="run2")

TEXT = "The mighty Trojan combat vehicle has"

def make_text(user_input):
    text = gpt2.generate(sess, length=200, return_as_list=True ,temperature=0.8, prefix=user_input, include_prefix=True, truncate='<|endoftext|>')[0]
    
    return text.replace('<|startoftext|>', '')


def create_reply(tweet):
        hook = tweet.hook
        doctrine = make_text(hook)
        # Checks is hook and doctrine are the same, without spaces. If tey are, regenerates until they are diffrent.
        while re.sub(r'\s', '', doctrine) == re.sub(r'\s', '', hook):
            print("Doctrine and hook the same, trying again")
            doctrine = make_text(hook)
        print(f'hook = {hook}')
        # Remeoves prefix if ends in question mark or over 120 char
        print(f'Hook length = {len(hook)} and doc = {doctrine}')
        if ((re.sub(r'\s', '', hook))[-1] == '?' ) or (len(hook) >= 120):
            doctrine = doctrine[len(hook)+1:]
        tweet_reply = parse_for_tweeter(doctrine)
        print("-------------------")
        print(f'@{tweet.username} {tweet_reply}')
        print("-------------------")
        return f'@{tweet.username} {tweet_reply}', tweet.id


def single_tweet():
    return gpt2.generate(sess, length=200, return_as_list=True, temperature=1, prefix='<|startoftext|>', include_prefix=False, truncate='<|endoftext|>')[0].replace('<|startoftext|>', '')

if __name__ == "__main__":
    print("\n --------------------- \n")

    print(make_text(TEXT))
    # print(single_tweet())

    print("\n --------------------- \n")