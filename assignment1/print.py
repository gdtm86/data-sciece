import urllib
import json

for i in range(1,11): 
	url = ("http://search.twitter.com/search.json?q=microsoft&page="+str(i))
	print url
	response = urllib.urlopen(url)
	response_dict = json.load(response)
	results_list= response_dict[u'results']

	for element in results_list:
		print element[u'from_user']
		print element[u'text']
	
	print "====================================================================================================================================================================================" 

