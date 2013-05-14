# Identify top ten hash tags from tweets
#         python top_ten_hash.py <tweet_file>
#         <tweet_file> = output.json

from sys import argv
from collections import Counter
import json

def read_tweets(input_tweet_file):
    json_data = open(input_tweet_file, 'r')
    tweets = [json.loads(line) for line in json_data]
    return tweets

def parse_tweet(tweets):
    hash_list = []
    for tweet in tweets:
        for item in tweet["entities"]["hashtags"]:
            hash_list.append(item["text"])
    return hash_list  
 
def tally(hash_list):
    tally = Counter()
    for term in hash_list:
        tally[term] += 1
    toptenhash = tally.most_common(10)
    for hash in toptenhash:
        print hash[0].replace("#",""), float(hash[1]) 
    
if __name__ == '__main__':
    tweetslist = read_tweets(argv[1])
    hash_list = parse_tweet(tweetslist)
    tally(hash_list)
