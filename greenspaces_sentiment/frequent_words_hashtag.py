
# coding: utf-8
# Inspired by: https://marcobonzanini.com/2015/03/09/mining-twitter-data-with-python-part-2/

import json
from nltk.tokenize import word_tokenize

import operator 
from collections import Counter


### enter file name here!
fname = ' .json'


import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP \u2026'
tweet = tweet.decode('unicode_escape').encode('ascii','ignore')
print(preprocess(tweet))
# ['RT', '@marcobonzanini', ':', 'just', 'an', 'example', '!', ':D', 'http://example.com', '#NLP']


with open(fname, 'r') as f:
    for line in f:
        tweet = line
        #print tweet
        tweet = tweet.decode('unicode_escape').encode('ascii','ignore')
        tokens = preprocess(tweet)
        #print tokens
        #do_something_else(tokens)

with open(fname, 'r') as f:
   count_all = Counter()
   for line in f:
       tweet = line
       tweet = tweet.decode('unicode_escape').encode('ascii','ignore')
       # Create a list with all the terms
       terms_all = [term for term in preprocess(tweet)]
       # Update the counter
       count_all.update(terms_all)
   # Print the first 5 most frequent words
   print(count_all.most_common(100))


#removing stop-words
from nltk.corpus import stopwords
import string
 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']


with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = line
        tweet = tweet.decode('unicode_escape').encode('ascii','ignore')
        # Create a list with all the terms
        terms_stop = [term for term in preprocess(tweet) if term not in stop]
        # Update the counter
        count_all.update(terms_stop)
    # Print the first 5 most frequent words
    print(count_all.most_common(100))


# Count terms only once, equivalent to Document Frequency
terms_single = set(terms_all)
# Count hashtags only
terms_hash = [term for term in preprocess(tweet) 
              if term.startswith('#')]
# Count terms only (no hashtags, no mentions)
terms_only = [term for term in preprocess(tweet) 
              if term not in stop and
              not term.startswith(('#', '@'))] 
              # mind the ((double brackets))
              # startswith() takes a tuple (not a list) if 
              # we pass a list of inputs


# most common hashtag in twitter
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_hash = [term for term in preprocess(tweet) 
              if term.startswith('#')]
        # Update the counter
        count_all.update(terms_hash)
    # Print the first 5 most frequent words
    print(count_all.most_common(100))

