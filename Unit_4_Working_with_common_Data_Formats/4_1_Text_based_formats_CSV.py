# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Text-based Formats (CSV)

# %% read data line by line as text
with open('Islands.csv') as f:
    content = f.read()
    print(content)

# %% load packages
import pandas as pd

# %% load the data
data = pd.read_csv("Islands.csv", sep = ";")

# %% load data without headers (bad)
data = pd.read_csv("Islands_noHeader.csv", sep = ";")

# %% load data without headers (correcgt)
column_names = ["Island", "Year", "Residents", \
    "Capital","Continent"]
data = pd.read_csv("Islands_noHeader.csv", \
    names = column_names, sep = ";")

# %% read data with meta information in
# first couple of lines
data = pd.read_csv("Islands_meta.csv", sep = ";", \
    skiprows = range(0,4))

# %% read a data file with UTF-8 encoding
data = pd.read_csv("Islands.csv", sep = ";", \
    skiprows = range(0,4), encoding = "utf-8")

# %% writing data to file
data.to_csv("Islands_output.csv", sep = ";")