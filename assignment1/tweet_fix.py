import sys
import json

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

tweet_file = open("tweet_file",'rU')

for element in tweet_file:
	sentiment = 0.0
	response = json.loads(element)
	tweet= response[u'text']
	term_list = tweet.split()
	#print term_list
	
	term_dict = {}
	for k in term_list:
		term_dict[k]=0.0
	#print term_dict.items()
	
	for j in term_dict.keys():
		#print scores.get(j)
		if (scores.get(j) is  None):
			sentiment = sentiment + 0.0
		else:
			sentiment = sentiment + scores.get(j)
		
	print sentiment
	print "============================================="	
print "********************************************************************************************************************"

