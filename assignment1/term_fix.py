import sys
import json

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

tweet_file = open("tweet_file",'rU')

new_scores ={}

for element in tweet_file:
	sentiment = 0.0
	response = json.loads(element)
	tweet= response[u'text']
	print tweet
	term_list = tweet.split()
	print term_list
	
	for j in term_list:
		#print scores.get(j)
		if (scores.get(j) !=  None):
			sentiment = sentiment + scores.get(j)
		else:
			sentiment = sentiment + 0.0 	
				
	print sentiment
	print "-----------"
	
	for j in term_list:
		
		if (scores.get(j) is  None):
			new_scores[j]=sentiment
			
			
	print "============================================="	
print "********************************************************************************************************************"

#print sorted(new_scores.items())

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

print '\t\t\n\n'

new_list = []

for i in giant_list:
	if ( i in new_scores.keys()):
		#print i
		new_list.append(i)	

print new_list	
