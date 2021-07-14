# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Streaming APIs

# %% Set credentials
# !!! DO NOT PUT ANY CREDENTIALS IN CLEAR TEXT !!!
# Do not expose your credentials here.
# Store your credentials to a secure key vault
# or use environment variables.
# This example is only for educational purpose.
# Do not use this code in production.
API_KEY = 'xxx'
API_SECRET = 'xxx'
TOKEN_KEY = 'xxx'
TOKEN_SECRET = 'xxx'

## Access the Twitter API with oauth2

# %% load packages
import oauth2

# %% define a function to access the API
def oauth_req(url, key, secret, http_method="GET", \
    post_body=b"", http_headers=None):
    
    # set consumer and token and use those to create
    # a client object
    consumer = oauth2.Consumer(key=API_KEY, \
        secret=API_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token) 
    
    # access the API
    resp, content = client.request(url, \
        method=http_method, \
        body=post_body, headers=http_headers)
    
    # return the content of the API response
    return content

# %% specify the URL to be accessed
url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23climatechange'

# %% call the API
data = oauth_req(url, TOKEN_KEY, TOKEN_SECRET)

# %% convert response to a pandas dataframe
data_df = json_normalize(data)

## Access the Twitter API with tweepy

# %% load package
import tweepy

# %% specify credentials and create an API object
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

# %% query the API
query = '#climatechange'
cursor = tweepy.Cursor(api.search, q=query, lang="en")

# %% iterate over the items in the page
for page in cursor.pages():
    for item in page:
     	print(item._json)

## Access the Twitter streaming API

# %% load packages
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

# %% create a listener class
class Listener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

# %% listen to a topic within the stream
stream = Stream(auth, Listener())
stream.filter(track = ["climatechange"])
