from distutils.command.clean import clean

try:
    import json
except ImportError:
    import simplejson as json
import re
import requests
import summarize
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#import nltk
#nltk.download('punkt')
# Variables that contains the user credentials to access Twitter API
class twitterSummary:
    def getSummary(self, inp):
        ACCESS_TOKEN = '949253929-o6YjLSBSF6wLSqRgazQ0Dgg3g1YgaSowvVdQC0iK'
        ACCESS_SECRET = 'cA3gerIJIssnMR83vqXSAHPpI5wloJ2DhuDlHXy97qMCO'
        CONSUMER_KEY = 'SPpUOTLLnqlzR8roaO7adrGMi'
        CONSUMER_SECRET = 'ZRaA1vB9FMFG6QXKZR2wDMrrjD2oZi4bTTG9TSDaqL6akzdoha'
        LANGUAGE = 'English'
        oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        twitter_stream = TwitterStream(auth=oauth)
        iterator = twitter_stream.statuses.sample()
        text_file = open('Output.txt', 'w')
        tweet_count = 1000
        iterator = twitter_stream.statuses.filter(track=inp, language='en', tweet_mode='compatibility')
        for tweet in iterator:
            tweet_count -= 1
            keys = tweet.keys()
  #  print(json.dumps(tweet))
            if 'text' in tweet :
                tweettext = tweet['text']
                print (tweet_count)
                cleanstring = re.sub('(@[A-Za-z0-9]:)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweettext)
                c = re.sub('RT', ' ', tweettext)
                l=c.split()
                for word in l:
                    if(word.startswith("@")):
                        l.remove(word)
                    if(word.startswith("http://")):
                        l.remove(word)
                    if (word.startswith("https://")):
                        l.remove(word)
                    if( word.startswith("&")):
                        l.remove(word)
                cleanString= ' '.join(l)
                print(cleanString)
                try:
                    text_file.write(cleanString)
                    text_file.write(".")
                except UnicodeEncodeError:
                    tweet_count-+1
            if tweet_count <= 0:
                break
        text_file.close()
        print ("\n")
        print ("SUMMARY")
        ss = summarize.SimpleSummarizer()
        file=open('Output.txt', 'r')
        data=file.read()
        summ=ss.summarize(data,5,inp)
        print(summ)
        return summ