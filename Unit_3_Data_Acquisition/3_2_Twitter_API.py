# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Twitter API

# %% import modules
import oauth2
import json
from pandas.io.json import json_normalize
import os
import twitter_api_cred_to_envir

# %% define a function to connect to the URL
# using authentification
def oauth_req(url, api_key, api_secret, \
    token_key, token_secret, \
    http_method="GET", post_body=b"", \
    http_headers=None):
    
    # set consumer and token and use those to create
    # a client object
    consumer = oauth2.Consumer(key=api_key, \
        secret=api_secret)
    token = oauth2.Token(key=token_key, \
        secret=token_secret)
    client = oauth2.Client(consumer, token) 
    
    # access the API
    resp, content = client.request(url, \
        method=http_method, body=post_body, \
        headers=http_headers)
    
    # return the content of the API response
    return content

# %% specify the URL to connect to
url = 'https://api.twitter.com/1.1/search/'
url += 'tweets.json?q=%climatechange'

# %% read credentials from environment variables
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
TOKEN_KEY = os.environ["TOKEN_KEY"]
TOKEN_SECRET = os.environ["TOKEN_SECRET"]

# %% call the API
data = oauth_req(url, API_KEY, API_SECRET, \
    TOKEN_KEY, TOKEN_SECRET)
print(data)

# %% convert the resulting string to JSON
data_json = json.loads(data)

# %% convert response to a pandas DataFrame
data_df = json_normalize(data_json)

# %% using tweepy to connect to the Twitter API
import tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

# %% load the data using tweepy
query = '#climatechange'
cursor = tweepy.Cursor(api.search, q=query, lang="en")
for page in cursor.pages():
    for item in page:
        print(item._json)

## Accessing the streaming API
# %% load packages
from tweepy.streaming import StreamListener
from tweepy import Stream

# %% create a listener class
class Listener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

# %% listen to a topic within the stream
stream = Stream(auth, Listener())
stream.filter(track = ["climatechange"])

# %%