# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Text-based Format (JSON)

# %% load packages
import pandas as pd
import json

# %% load the data
json_data = open('LondonWeather.json').read()

# %% convert the data into a dictionary
data = json.loads(json_data)

# %% query the data
data["main"]

# %% convert into a pandas dataframe
weather_data = pd.DataFrame(data["main"], \
    index = [data["name"]])

# %% alternatively
pd.io.json.json_normalize(data['main'])