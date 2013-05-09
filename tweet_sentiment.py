# Compute sentiment score of tweet as the sum of sentiment scores of terms in tweet
# 		python tweet_sentiment.py <sentiment_file> <tweet_file>
#  		<sentiment_file> = AFINN-111.txt
# 		<tweet_file> = output.json

from sys import argv
import csv
import json
import re

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

def calc_sentimentscore(sentiments, tweets):
	for i in range(len(tweets)):
		sentiments_sum = 0
		if tweets[i]["user"]["lang"] == "en":
			tweet = tweets[i]["text"]
			tweet = tweet.encode('utf-8')
			tweet = tweet.lower()
			tweet_words_list = re.findall(r"[\w']+", tweet)
			for j in range(len(sentiments)):
				for word in tweet_words_list:
					if sentiments[j][0] == word:
						sentiment_value = int(float(sentiments[j][1]))
						sentiments_sum += sentiment_value
			print tweet, sentiments_sum

if __name__ == '__main__':
	sentimentsdict = identify_sentiments(argv[1])
	tweetslist = read_tweets(argv[2])
	calc_sentimentscore(sentimentsdict, tweetslist)
