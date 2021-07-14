# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Text-based Formats (CSV)

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