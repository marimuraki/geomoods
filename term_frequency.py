# Compute frequency of words in tweets
#         python term_frequency.py <tweet_file>
#         <tweet_file> = output.json

from __future__ import division
from sys import argv
import json

def read_tweets(input_tweet_file):
    json_data = open(input_tweet_file, 'r')
    tweets = [json.loads(line) for line in json_data]
    return tweets

def parse_tweet(tweets):
    tweet_list = [tweet["text"].encode('utf-8').lower() for tweet in tweets]
    tweet_words_list = [tweet.split() for tweet in tweet_list]
    return tweet_list, tweet_words_list  

def freq_term(tweet_words_list):
    count = 0
    tweetword_dict = dict()
    for tweet in tweet_words_list:
        for word in tweet:
            count += 1
            tweetword_dict[word] = tweetword_dict.get(word, 0) + 1
    for key, value in tweetword_dict.items():
        print key, "{0:.4f}".format(float(value/count))


if __name__ == '__main__':
	tweets = read_tweets(argv[1])
	tweet_list, tweet_words_list = parse_tweet(tweets)
	freq_term(tweet_words_list)
    