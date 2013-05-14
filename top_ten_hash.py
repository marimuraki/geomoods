# Identify top ten hash tags from tweets
#         python top_ten_hash.py <tweet_file>
#         <tweet_file> = output.json

from sys import argv
from collections import Counter
import csv
import json

def read_tweets(input_tweet_file):
    json_data = open(input_tweet_file, 'r')
    tweets = [json.loads(line) for line in json_data]
    return tweets

def parse_tweet(tweets):
    tweet_list = [tweet["text"].encode('utf-8') for tweet in tweets]
    tweet_words_list = [tweet.split() for tweet in tweet_list]
    return tweet_list, tweet_words_list  
        
def list_terms(tweet_words_list):
    term_list = []
    for tweet in tweet_words_list:
        for word in tweet:
            if word.startswith("#"):
                term_list.append(word)
    return term_list
 
def tally(term_list):
    tally = Counter()
    for term in term_list:
        tally[term] += 1
    toptenhash = tally.most_common(10)
    for hash in toptenhash:
        print hash[0].replace("#",""), float(hash[1]) 
    
if __name__ == '__main__':
    tweetslist = read_tweets(argv[1])
    tweet, tweetwords = parse_tweet(tweetslist)
    termlist = list_terms(tweetwords)
    tally(termlist)
