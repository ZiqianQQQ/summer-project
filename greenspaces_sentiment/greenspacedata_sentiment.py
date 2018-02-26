
# coding: utf-8

# In[1]:


import json
from textblob import TextBlob


# In[ ]:


import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sid = SIA()


# In[3]:


from nltk.tokenize import word_tokenize


# In[27]:


fname = '.json'
all_twitter_data = '.json'


# In[12]:


def sentiment(message):
    text = TextBlob(message)
    response = [text.polarity , text.subjectivity]
    return response


# In[ ]:


##### textblob: polarity without objective data
count = 0
po_sum = 0
with open(fname, 'r') as f:
    for line in f:
        po, su = sentiment(line)
        if su != 0.0:
            print po, su
            print line
            count = count + 1
            po_sum = po_sum + po

print count
print (po_sum/count)



# In[ ]:


##### textblob: polarity of all green data
count = 0
po_sum = 0
with open(fname, 'r') as f:
    for line in f:
        po, su = sentiment(line)
        #print line
        count = count + 1
        po_sum = po_sum + po

print count
print (po_sum/count)



# In[ ]:


##### textblob: all sydney ins/twiiter data, for comparison

count = 0
po_sum = 0

with open(all_twitter_data, 'r') as f:
    for line in f:
        po, su = sentiment(line)
        #print line
        count = count + 1
        po_sum = po_sum + po

print count
print (po_sum/count)


# In[ ]:


####### nltk: polarity without objective data
count = 0
po_sum = 0
with open(fname, 'r') as f:
    for line in f:
        ss = sid.polarity_scores(line)
        if ss['neu'] != 1.0:
            
            print ss
            print line
            po_sum = po_sum + ss['compound']
            count = count + 1

print count
print (po_sum/count)


# In[ ]:


####### nltk: polarity of all green space data
count = 0
po_sum = 0
with open(fname, 'r') as f:
    for line in f:
        ss = sid.polarity_scores(line)
        po_sum = po_sum + ss['compound']
        count = count + 1
        #print ss
        #print line

print count
print (po_sum/count)


# In[ ]:


####### nltk: polarity of all ins/twitter data
count = 0
po_sum = 0
with open(all_twitter_data, 'r') as f:
    for line in f:
        ss = sid.polarity_scores(line)
        po_sum = po_sum + ss['compound']
        count = count + 1

print count
print (po_sum/count)


# In[ ]:


####### nltk: polarity of all green space data
training_data = []

with open(fname, 'r') as f:
    for line in f:
        ss = sid.polarity_scores(line)
       
        if (ss['compound'] >= 0.5):
            line = (line, 'pos')
        elif (ss['compound'] <= -0.5):
            line = (line, 'neg')
        else:
            line = (line, 'neu')
            
        training_data.append(line)
        
print training_data


# In[45]:


train = []


# In[ ]:


i = 0
correct = 0
incorrect = 0
for i in range():
    if train[i][1] == training_data[i][1]:
        correct += 1
    else:
        incorrect += 1
    i += 1
        
print correct
print incorrect


# In[ ]:


# Step 2
dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
  
# Step 3
t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
  
# Step 4 – the classifier is trained with sample data
classifier = nltk.NaiveBayesClassifier.train(t)
  
test_data = "Manchurian was hot and spicy"
test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
  
print (classifier.classify(test_data_features))


# In[ ]:


test_trained_data = []
with open(fname, 'r') as f:
    for line in f:
        test_data = line
        test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
        emo = classifier.classify(test_data_features)
        line = (line, emo)
        test_trained_data.append(line)

print test_trained_data


# In[ ]:


i = 0
correct = 0
incorrect = 0
for i in range():
    if train[i][1] == test_trained_data[i][1]:
        correct += 1
    else:
        incorrect += 1
    i += 1
        
print correct
print incorrect        

