
# coding: utf-8

# In[1]:


import json
from nltk.tokenize import word_tokenize


# In[66]:


fname = 'perth-ins.json'

general_keywords = ['greenlife','greenspace','park','parks','bbq','bbqtime','natural','naturallife','nature','wildlife','botany','botanic','botanical','botanicalgardens','botanicalgarden','royalbotanicalgardens','garden','gardens','reserve','tree','trees','plant','plants','flower','flowers','grass','stadium','golf','picnic','jogging','jogger']


# In[ ]:


with open(fname, 'r') as f:
    line = f.readline() # read only the first tweet/line
    print line
    tweet = line # load it as Python dict
    tweet = tweet.decode('unicode_escape').encode('ascii','ignore')
    print(json.dumps(tweet, indent=4)) # pretty-print
    print (word_tokenize(tweet))


# In[ ]:


erro_finder = 0
sum_count = 0
with open(fname, 'r') as f:
    for line in f:
        erro_finder += 1
        print erro_finder
        tweet = json.loads(line)
        # Create a list with all the terms
        words = word_tokenize(tweet)
        words = [item.lower() for item in words]
        #print words
        for key in general_keywords:
            if key in words:
                sum_count = sum_count + 1
                #print line
                break
        
print sum_count


# In[68]:


#write to a new file
sum_count = 0
outf = open('perth-ins-greenspace.json', 'w')

with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        words = word_tokenize(tweet)
        words = [item.lower() for item in words]
        #print words
        for key in general_keywords:
            if key in words:
                sum_count = sum_count + 1
                outf.write(line)
                break
                
print sum_count
outf.close()

