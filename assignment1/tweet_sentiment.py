import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
  	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	scores[term] = int(score)  # Convert the score to an integer.

    for element in tweet_file:
        sentiment = 0.0
        response = json.loads(element)
        tweet= response[u'text']
        term_list = tweet.split()

        for term in term_list:
                if (scores.get(term) is  None):
                        sentiment = sentiment + 0.0
                else:
                        sentiment = sentiment + scores.get(term)

        print sentiment



if __name__ == '__main__':
    main()

