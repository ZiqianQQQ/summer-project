
# coding: utf-8
#This part was written by Fangfang Huang

import couchdb
import json
import re


# info for couch DB
user = "admin"
password = "12345678"
# info to retrieve view
dbname = "perth"
design = ""
view = ""
# connects to couchDB
couch = couchdb.Server("http://%s:%s@43.240.96.22:5984//" % (user, password))
#couch = couchdb.Server("http://%s:%s@45.113.232.90:5984//" % (user, password))
# requesting exist view from database
 

counts = couch[dbname].view(design+'/'+view,
                            reduce=False,
                            descending=True)


# save it locally for further manipulate
#,ensure_ascii=False
tweets = []
for count in counts:
    tweet = json.dumps(count['value'])  
    tweets.append(tweet)
# check duplicates by tweets
seen = set()
for x in tweets: 
    if x not in seen:
        seen.add(x)


with open('' ,'w') as nf, open('', 'w') as b:
#with open('qiao-perthins.json' ,'w') as nf: 
    for values in seen:  
        #save the tweet into the document along with the sentiment result
        y= json.loads(values)   
        nf.write(json.dumps(y[0]))
        nf.write(",")
        nf.write(json.dumps(y[1])) 
        nf.write("\n")
        text = json.dumps(y[1])
        
        b.write(text)
        b.write("\n")



with open('' ,'w') as nf:
#with open('qiao-perthins.json' ,'w') as nf: 
    for values in seen:  
        #save the tweet into the document along with the sentiment result
        y = json.loads(values)   
        nf.write(json.dumps(y))
        nf.write("\n")
        

