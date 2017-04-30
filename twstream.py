from distutils.command.clean import clean

try:
    import json
except ImportError:
    import simplejson as json
import tweepy
import re
import requests
import summarize
import time
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#import nltk
#nltk.download('punkt')
# Variables that contains the user credentials to access Twitter API
class twiSummary:
    def getSummary(self, inp):
        print("function called")
        ACCESS_TOKEN = '949253929-o6YjLSBSF6wLSqRgazQ0Dgg3g1YgaSowvVdQC0iK'
        ACCESS_SECRET = 'cA3gerIJIssnMR83vqXSAHPpI5wloJ2DhuDlHXy97qMCO'
        CONSUMER_KEY = 'SPpUOTLLnqlzR8roaO7adrGMi'
        CONSUMER_SECRET = 'ZRaA1vB9FMFG6QXKZR2wDMrrjD2oZi4bTTG9TSDaqL6akzdoha'
        LANGUAGE = 'English'
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        print("auth set")
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        print("authorized")
        text_file = open('Output.txt', 'w')
        tweet_count = 1000
        search_results = api.search(q=inp, count=10000)
        for tweet in search_results:
            tweettext = tweet.text
            print(tweet_count)
            cleanstring = re.sub('(@[A-Za-z0-9]:)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweettext)
            c = re.sub('RT', ' ', tweettext)
            l = c.split()
            for word in l:
                if (word.startswith("@")):
                    l.remove(word)
                if (word.startswith("http://")):
                    l.remove(word)
                if (word.startswith("https://")):
                    l.remove(word)
                if (word.startswith("&")):
                    l.remove(word)
            cleanString = ' '.join(l)
            print(cleanString)
            try:
                text_file.write(cleanString)
                text_file.write(".")
            except UnicodeEncodeError:
                tweet_count - +1
            if tweet_count <= 0:
                break
        text_file.close()
        print("\n")
        print("SUMMARY")
        ss = summarize.SimpleSummarizer()
        file = open('Output.txt', 'r')
        data = file.read()
        summ = ss.summarize(data, 5, inp)
        summary = "\n".__add__(summ)
        print(summary)
        return summary