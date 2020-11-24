import gpt_2_simple as gpt2
import os
import requests
import re

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name="run2")

def make_text(user_input):
    # def parse_text(text):
        # list = text.split('\n')
        # list_start = list[:2]
        # string_start = " ".join(list_start)

        # list_end = list[2:-1]
        # string_end = "\n".join(list_end)

        # string_full = string_start + string_end

        # return string_full

    text = gpt2.generate(sess, length=200, return_as_list=True ,temperature=0.8, prefix=user_input, include_prefix=True, truncate='<|endoftext|>')[0]
    
    return text.replace('<|startoftext|>', '')

def single_tweet():
    return gpt2.generate(sess, length=200, return_as_list=True, temperature=1, prefix='<|startoftext|>', include_prefix=False, truncate='<|endoftext|>')[0]

if __name__ == "__main__":
    print("\n --------------------- \n")

    print(make_text('The RAF is'))
    # print(single_tweet())

    print("\n --------------------- \n")