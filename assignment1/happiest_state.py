import sys
import json
import ordereddict

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
  	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	scores[term] = int(score)  # Convert the score to an integer.
    state_total_sentiment={} #initialize an empty dictionary

    for element in tweet_file:
        sentiment = 0.0
        response = json.loads(element)
        tweet= response[u'text']
	term_list = tweet.split()
	place_dict = response[u'place']
	
	if place_dict is None:
		pass
	else:
		country_code = place_dict.get('country_code')
		if (country_code != "US"):
			pass
		else:
			#print country_code
			location_name = place_dict.get('full_name')
			#print location_name
			state_name = location_name.split(", ")[1]
			if (len(state_name) != 2):
				pass
			else:
				#print state_name
        			for term in term_list:
                			if (scores.get(term) is  None):
                        			sentiment = sentiment + 0.0
                			else:
                        			sentiment = sentiment + scores.get(term)
			
				state_total_sentiment[state_name] = sentiment + state_total_sentiment.get(state_name,0.0)
        			#print sentiment
				#print "=================================="
	
    #print sorted(state_total_sentiment.items(), key=lambda item: item[1], reverse=True)
    happiest_state = sorted(state_total_sentiment.items(), key=lambda item: item[1], reverse=True)[0]
    #print happiest_state
    print happiest_state[0]
    #print type(happiest_state)	

if __name__ == '__main__':
    main()

