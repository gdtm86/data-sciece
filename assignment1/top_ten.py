import sys
import json
import ordereddict

def main():
    tweet_file = open(sys.argv[1])
    hashtags_text_dict = {} 
    for object in tweet_file:
        #sentiment = 0.0
        response = json.loads(object)
	if ( "delete" in response.keys()):
		pass
	else:
		if (response[u'entities'] is None):
			pass
		else:
			entities = response[u'entities']
			hashtags =  entities[u'hashtags']
			if (len(hashtags) == 0):
				pass
			else:
				#print type(hashtags)
				for item in hashtags:
					#print i[u'text']
					hashtag_text = item[u'text']
					hashtags_text_dict[hashtag_text] = 1 + hashtags_text_dict.get(hashtag_text,0.0)
    top_ten_hashtags = sorted(hashtags_text_dict.items(), key = lambda item: item[1], reverse=True)[0:10]
    for i in top_ten_hashtags:
	print i[0], i[1] 

if __name__ == '__main__':
    main()

