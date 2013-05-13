# Compute sentiment score of new term based on tweet scores
#         python term_sentiment.py <sentiment_file> <tweet_file>
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
    sentiment_dict = dict(sentiments)
    for tweet, tweetwords in zip(tweet_list, tweet_words_list):
        tweet_dict = {}
        sentiments_sum = sum([int(sentiment_dict.get(word, 0)) 
            for word in tweetwords])
        tweet_dict["tweet"] = tweet
        tweet_dict["tweetwords"] = tweetwords
        tweet_dict["score"] = sentiments_sum
        tweet_dict_list.append(tweet_dict)
    return tweet_dict_list

def list_sentiments(sentiments):
    sentiment_list = [sentiment[0] for sentiment in sentiments]
    return sentiment_list
    
def list_terms(tweet_words_list, sentiment_list):
    term_list = []
    for tweet in tweet_words_list:
        for word in tweet:
            if word not in sentiment_list:
                term_list.append(word)
    seen = set()
    seen_add = seen.add
    term_list = [term for term in term_list if term not in seen and not seen_add(term)]
    return term_list

def dict_terms(term_list, tweet_dict_list):
    term_dict_list = []
    for term in term_list:
        for tweet_dict in tweet_dict_list:
            if term in tweet_dict['tweetwords']:
                term_dict = {}
                term_dict["term"] = term
                term_dict["score"] = tweet_dict['score']
                term_dict_list.append(term_dict)            
    return term_dict_list

def calc_termscore(term_list, term_dict_list):
    for term in term_list:
        score_sum = 0
        count = 0
        for term_dict in term_dict_list:
            if term_dict["term"] == term:
                count += 1
                score_sum += term_dict["score"]
        term_score = score_sum / count
        print term, term_score            
    
if __name__ == '__main__':
    sentimentslist = read_sentiments(argv[1])
    tweetslist = read_tweets(argv[2])
    tweet, tweetwords = parse_tweet(tweetslist)
    sentlist = list_sentiments(sentimentslist)
    termlist = list_terms(tweetwords, sentlist)
    tweetscores = calc_sentimentscore(sentimentslist, tweet, tweetwords)
    termdict = dict_terms(termlist, tweetscores)
    calc_termscore(termlist, termdict)