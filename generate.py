import gpt_2_simple as gpt2
import os
import requests
import re

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name="run2")

def make_text(user_input):
    text = gpt2.generate(sess, length=200, return_as_list=True ,temperature=0.8, prefix=user_input, include_prefix=True, truncate='<|endoftext|>')[0]
    
    return text.replace('<|startoftext|>', '')

def single_tweet():
    return gpt2.generate(sess, length=200, return_as_list=True, temperature=1, prefix='<|startoftext|>', include_prefix=False, truncate='<|endoftext|>')[0].replace('<|startoftext|>', '')

if __name__ == "__main__":
    print("\n --------------------- \n")

    print(make_text('Did you write this ?'))
    # print(single_tweet())

    print("\n --------------------- \n")