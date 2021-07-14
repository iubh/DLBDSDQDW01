# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Data APIs

# %% load packages
import requests
from pandas.io.json import json_normalize
import pandas as pd

# %% get data via RESTful API
api_url = "https://seeclickfix.com/api/v2/issues?"
response = requests.get(api_url)
response.json()

# %% get data via RESTful API with specifications
api_url = "https://seeclickfix.com/api/v2/issues?"
api_url += "&after=2021-01-01T00:00:00"
api_url += "&before=2021-01-03T00:00:00"
api_url += "&page=1"
data = requests.get(api_url).json()["issues"]

# %% convert the JSON response from the API to
# a pandas dataframe
data_df = json_normalize(data)

# %%
