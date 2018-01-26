#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API
access_token = "848245039125774336-nkTeqhgSofKDzmHQ31TBZSNhJqSGaWY"
access_token_secret = "JzTtGqs7UORQXCFToyXbvrUdRhg4zXFhgUcPshmhB7em7"
consumer_key = "0N0Yq0ceGeVRXBA918EtfhK6K"
consumer_secret = "qbVzKfBLeiBw7He39tI11KHlbCziZkS43rZLjNxHCYs4VqbtdI"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_status(self, status):
	print status.text
	return True

    def on_error(self, status_code):
         if status_code == 420:
		return False


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keyword: 'python'
    stream.filter(track=['god'], async=True)

