
# coding: utf-8
# NB, SVM and decision tree classifier

import json
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sid = SIA()

from nltk.tokenize import word_tokenize



fname = ''
all_ins_data = ''
all_twitter_data = ''


import csv

#step 1
####### nltk labelled data
f = 'nltk_label_grtw.csv'
nltk_train = []
with open(f) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        t = (row[0],row[1])
        nltk_train.append(t)
        
nltk_train.remove(nltk_train[0])
print len(nltk_train)


####### manually labelled data
f1 = 'manu_label_grtw.csv'
manually_train = []
with open(f1) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        t = (row[0],row[1])
        manually_train.append(t)
        
manually_train.remove(manually_train[0])

print len(manually_train)



####### compare: nltk labelled data && manually labelled data
i = 0
correct = 0
incorrect = 0
for i in range(300):
    if (nltk_train[i][1] == manually_train[i][1]):
        correct += 1
    else:
        incorrect += 1
    i += 1
        
print correct
print incorrect


# Step 2
dictionary = set(word.lower() for passage in manually_train for word in word_tokenize(passage[0]))
  
# Step 3
t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in manually_train]
  
# Step 4 – the classifier is trained with sample data
classifier = nltk.NaiveBayesClassifier.train(t)
  
#import nltk.classify, SVM classifier
from sklearn.svm import LinearSVC

classifier_svm = nltk.classify.SklearnClassifier(LinearSVC())
classifier_svm.train(t)

####### Decision tree
classifier_dt = nltk.classify.DecisionTreeClassifier.train(t)

#test_data = "Manchurian was hot and spicy"
#test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
  
#print (classifier.classify(test_data_features))




####### NB classifier labelled data
test_trained_data = []

fname = '.json'
with open(fname, 'r') as f:
    for line in f:
        test_data = line
        test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
        emo = classifier.classify(test_data_features)
        line = (line, emo)
        test_trained_data.append(line)

print len(test_trained_data)


####### compare: classifier labelled data && manually labelled data
i = 0
correct = 0
incorrect = 0
for i in range(245):
    if manually_train[i][1] == test_trained_data[i][1]:
        correct += 1
    else:
        incorrect += 1
    i += 1
        
print correct
print incorrect        



####### classifier_svm labelled data
test_trained_data = []

fname = 'all-twitter-greenspace.json'
with open(fname, 'r') as f:
    for line in f:
        test_data = line
        test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
        emo = classifier_svm.classify(test_data_features)
        line = (line, emo)
        test_trained_data.append(line)

print len(test_trained_data)



####### compare: SVM classifier labelled data && manually labelled data
i = 0
correct = 0
incorrect = 0
for i in range(245):
    if train[i][1] == test_trained_data[i][1]:
        correct += 1
    else:
        incorrect += 1
    i += 1
        
print correct
print incorrect        



####### classifier_dt labelled data
test_trained_data = []

fname = 'all-twitter-greenspace.json'
with open(fname, 'r') as f:
    for line in f:
        test_data = line
        test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
        emo = classifier_dt.classify(test_data_features)
        line = (line, emo)
        test_trained_data.append(line)

print len(test_trained_data)



####### compare: classifier_dt labelled data && manually labelled data
i = 0
correct = 0
incorrect = 0
for i in range(245):
    if train[i][1] == test_trained_data[i][1]:
        correct += 1
    else:
        incorrect += 1
    i += 1
        
print correct
print incorrect        




count_pos = 0
count_neg = 0
for i in test_trained_data:
    #print i[1]
    if (i[1] == 'pos'):
        count_pos += 1
    elif (i[1] == 'neg'):
        count_neg += 1

print count_pos
print count_neg
