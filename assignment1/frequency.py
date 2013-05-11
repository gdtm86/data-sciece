import sys
import json

giant_list =[]
tweet_file = open("tweet_file",'rU')
for element1 in tweet_file:
        response1 = json.loads(element1)
        #print response1
        tweet1 =  response1[u'text']
        #print tweet1
        #print type(tweet1)
        term1_list = tweet1.split()
        #print term1_list
        giant_list = giant_list + term1_list
print "============================="
print giant_list

total_terms = len(giant_list)
print total_terms 

print "==================================="
kvMap = {} 
for k in giant_list:
     kvMap[k] = 1 + kvMap.get(k,0)

print kvMap.items()

print len(kvMap)

print "====================================="
## calcuate the term frequency for each item

for i in kvMap.keys():
	
	term_frequency = kvMap[i] / float(total_terms)
	
	print  i, term_frequency

