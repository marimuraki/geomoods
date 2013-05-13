# Compute sentiment score of tweet as the sum of sentiment scores of terms in tweet
#         python tweet_sentiment.py <sentiment_file> <tweet_file>
#          <sentiment_file> = AFINN-111.txt
#        -- file should be encoded UTF-8 without BOM
#         <tweet_file> = output.json

from sys import argv
import csv
import json
import re

def read_tweets(input_tweet_file):
    json_data = open(input_tweet_file, 'r')
    tweets = [json.loads(line) for line in json_data]
    return tweets

def read_sentiments(input_sentiment_file):
    sentiments = list(csv.reader(open(input_sentiment_file, 'rb'), delimiter='\t'))
    return sentiments

def parse_tweet(tweets):
    tweet_list = [tweet["text"].encode('utf-8').lower() for tweet in tweets]
    tweet_words_list = [tweet.split() for tweet in tweet_list]
    return tweet_list, tweet_words_list    
        
def calc_sentimentscore(sentiments, tweet_list, tweet_words_list):
    tweet_dict_list = []
    for i in range(len(tweet_words_list)):
        tweet_dict = {}
        sentiments_sum = 0
        for word in tweet_words_list[i]:
            for j in range(len(sentiments)):
                if sentiments[j][0] == word:
                    sentiment_value = int(float(sentiments[j][1]))
                    sentiments_sum += sentiment_value                
        tweet_dict["tweet"] = tweet_list[i]
        tweet_dict["tweetwords"] = tweet_words_list[i]
        tweet_dict["score"] = sentiments_sum
        tweet_dict_list.append(tweet_dict)
        print tweet_list[i], sentiments_sum
    return tweet_dict_list
        

if __name__ == '__main__':
    sentimentslist = read_sentiments(argv[1])
    tweetslist = read_tweets(argv[2])
    tweet, tweetwords = parse_tweet(tweetslist)
    calc_sentimentscore(sentimentslist, tweet, tweetwords)
