# doctrinebot_v1

DoctrineBot V1 is built on GPT2-Simple, fine tuned in UK MoD Doctrine.

Due to size constraints, the model and checkpoints are not included in the repo.

## hosting

DoctrineBot is hosted on an AWS EC2 instance. Scripts are run from crontab. To run pipenv environments from crontab, it is best to write a shell script to define the correct PATH, cd into the directory before running. As below:

> latest_id='1332777243836354564'
> echo $latest_id > latest_id.txt

> nano run.sh
Copy and past in ..

#!/usr/bin/env bas
PATH=/usr/local/bin/:$PATH
cd doctrinebot/
pipenv run python tweeter.py >> ~/log.txt 2>&1

> nano single_tweet.sh
Copy and past in ..

#!/usr/bin/env bas
PATH=/usr/local/bin/:$PATH
cd doctrinebot/
pipenv run python single_tweet.py >> ~/log.txt 2>&1


> crontab -e

0,3,6 8-23 * * * ./doctrinebot/run.sh >/dev/null 2>&1
0 8,14,20 * * * ./doctrinebot/single_tweet.sh >/dev/null 2>&1

## generate.py

This produces the test from the model

## parse_text.py

This parses the text into a suitable format for twitter

## tweeter.py

This pulls tweets and constructs replies. You will need to create a keys.json file with you twitter access credentials.

## single_tweet.py

This constructs a single tweet.