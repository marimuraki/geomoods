# Compute sentiment score of tweet as the sum of sentiment scores of terms in tweet
# 		python tweet_sentiment.py <sentiment_file> <tweet_file>
#  		<sentiment_file> = AFINN-111.txt
# 		<tweet_file> = output.json

import json

def read_tweets(input_tweet_file):
	tweets = []
	json_data=open(input_tweet_file, 'r')
	for line in json_data:
		tweets.append(json.loads(line))
	return tweets
