# Compute sentiment score of tweet as the sum of sentiment scores of terms in tweet
# 		python tweet_sentiment.py <sentiment_file> <tweet_file>
#  		<sentiment_file> = AFINN-111.txt
# 		<tweet_file> = output.json

import csv
import json

def read_tweets(input_tweet_file):
	tweets = []
	json_data=open(input_tweet_file, 'r')
	for line in json_data:
		tweets.append(json.loads(line))
	return tweets

def identify_sentiments(input_sentiment_file):
	sentiments = list(csv.reader(open(input_sentiment_file, 'rb'), delimiter='\t'))
	sentiment_dict = dict()
	for i in range(len(sentiments)):
		key = sentiments[i][0]
		value = sentiments[i][1]
		sentiment_dict[key] = value
	return sentiments
