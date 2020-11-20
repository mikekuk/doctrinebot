# doctrinebot_v1

DoctrineBot V1 is built on GPT2-Simple, fine tuned in UK MoD Doctrine.

Due to size constriants, the model and checkpoints are not included in the repo.

## hosting

DoctrineBot is hosted on an AWS EC2 instance. tweeter.py is run from crontab envry 5 miniutes, and single_tweet.py is run every 5 hours. To run pipenv enviroments from crontab, it is best to write a shell script to define the correct PATH, cd into the directory before running. As below:

#!/usr/bin/env bash \n
PATH=/usr/local/bin/:$PATH \n
cd doctrinebot/ \n
pipenv run python example.py >> ~/log.txt 2>&1

## generate.py

This produces the test from the model

## parse_text.py

This parses the text into a suitble format for twitter

## tweeter.py

This pulls tweets and constructs replies. Yoy will need to creat a keys.json file with you twitter access credentials.

## single_tweet.py

This constructs a single tweet.


