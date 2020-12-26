import tweepy
import json
import re
from generate import create_reply

account = 'BotDoctrine'

with open('keys.json', 'r') as json_file:
    twitter_keys = json.load(json_file)
    json_file.close()

with open('latest_id.txt') as doc:
    lateset_id = int(doc.read())
    doc.close()

class MessageQue:
    def __init__(self):
        self.que = []
        self.length = len(self.que)
    
    def __repr__(self):
        return str([tweet for tweet in self.que])
    
    def add(self, item):
        self.que.append(item)
        self.length = len(self.que)

    def pop(self):
        last = self.que.pop(0)
        self.length -= 1
        return last

class Tweet:
    def __init__(self, text, username, id):
        self.username = username.lower()
        self.text = str(text)
        self._account_removed = re.sub(rf'(?i)@{account}', '', self.text)
        self.hook = re.sub(r'https://\S+', '', self._account_removed)
        self.id = id
    
    def __repr__(self):
        return f"< Tweet Object {self.id}: From {self.username}, Text: {self.text}, Hook: {self.hook} >"

def login(twitter_keys):
    auth = tweepy.OAuthHandler(twitter_keys["CONSUMER_KEY"], twitter_keys["CONSUMER_SECRET"])
    auth.set_access_token(twitter_keys["ACCESS_TOKEN"], twitter_keys["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth)
    if __name__ == "__main__":
        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
    return api

def get_mentions(api):
    que = MessageQue()
    mentions = api.mentions_timeline(since_id = lateset_id)
    for mention in mentions:
        que.add(Tweet(mention.text, mention.user.screen_name, mention.id))
    return que


def post_replies(que):
    while que.length > 0:
        tweet = que.pop()
        reply, id = create_reply(tweet)
        try:
            api.update_status(reply, id)
        except:
            print('tweepy error')
            pass
        latest_id = tweet.id
        with open('latest_id.txt', 'w') as doc:
            doc.write(str(latest_id))
            doc.close()

if __name__ == '__main__':
    api = login(twitter_keys)
    mentions = get_mentions(api)
    post_replies(mentions)