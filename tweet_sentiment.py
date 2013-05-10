# Compute sentiment score of tweet as the sum of sentiment scores of terms in tweet
# 		python tweet_sentiment.py <sentiment_file> <tweet_file>
#  		<sentiment_file> = AFINN-111.txt
# 		<tweet_file> = output.json

from sys import argv
import codecs
import csv
import json
import re

def read_tweets(input_tweet_file):
	tweets = []
	json_data=open(input_tweet_file, 'r')
	for line in json_data:
		tweets.append(json.loads(line))
	return tweets

def read_sentiments(input_sentiment_file):
	sentiments = list(csv.reader(open(input_sentiment_file, 'rb'), delimiter='\t'))
	return sentiments

def parse_tweet(tweets):
	tweet_list = []
	tweet_words_list = []
	for i in range(len(tweets)):
		if tweets[i]["user"]["lang"] == "en":
			tweet = tweets[i]["text"]
			tweet = tweet.encode('utf-8')
			tweet = tweet.lower()
			tweet_words = re.findall(r"[\w']+", tweet)
			tweet_words_list.append(tweet_words)
			tweet_list.append(tweet)
	return tweet_list, tweet_words_list	
	
def calc_sentimentscore(sentiments, tweet_list, tweet_words_list):
	tweet_score_dict = {}
	for i in range(len(tweet_words_list)):
		sentiments_sum = 0
		for word in tweet_words_list[i]:
			for j in range(len(sentiments)):
				if sentiments[j][0] == word:
					sentiment_value = int(float(sentiments[j][1]))
					sentiments_sum += sentiment_value				
		tweet_score_dict[tweet_list[i]] = sentiments_sum			
		print tweet_list[i], sentiments_sum
	return tweet_score_dict
		

if __name__ == '__main__':
	sentimentslist = read_sentiments(argv[1])
	tweetslist = read_tweets(argv[2])
	tweet, tweetwords = parse_tweet(tweetslist)
	calc_sentimentscore(sentimentslist, tweet, tweetwords)
