from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="your twiiter app consumer key goes here"
csecret="your twiiter app consumer secretr key goes here"
atoken="your twiiter app access token goes here"
asecret="your twiiter app access secret goes here"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = ascii(all_data["text"])
        sentiment_value, confidence = s.sentiment(tweet)
        print((tweet, sentiment_value, confidence))

        if confidence*100 >=80:
            output = open("your output file goes here","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        time.sleep(0.3)
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["enter your key word here"])
