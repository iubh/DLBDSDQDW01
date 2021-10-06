# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Fuzzy matching

# %% load packages
from fuzzywuzzy import fuzz

# %% generate sample data
my_records = [{ \
    'song': 'Sound of Silence', \
    'movie': '2 fast 2 furious', \
    'book': 'The Hitchhikers Guide to the Galaxy', \
    }, { \
    'song': 'The sound of silence', \
    'movie': 'Too fast too furious',
    'book': 'The Hitchhikers Guide to the Galaxie', \
}]

# %% calculate the overall similarity between the
# two records
fuzz.ratio(my_records[0], my_records[1])

# console output:
# 91

# %% calculate the similarity between songs
fuzz.ratio(my_records[0]['song'], \
           my_records[1]['song'])
# console output:
# 78

# %% calculate the similarity between movies
fuzz.ratio(my_records[0]['movie'], \
           my_records[1]['movie'])
# console output:
# 78

# %% calculate the similarity between books
fuzz.ratio(my_records[0]['book'], \
           my_records[1]['book'])
# console output:
# 96

# %% calculate the partial similarity between songs
fuzz.partial_ratio(my_records[0]['song'], \
                   my_records[1]['song'])
# console output:
# 88

# %% calculate the partial similarity between movies
fuzz.partial_ratio(my_records[0]['movie'], \
                   my_records[1]['movie'])
# console output:
# 81

# %% calculate the partial similarity between books
fuzz.partial_ratio(my_records[0]['book'], \
                   my_records[1]['book'])
# console output:
# 97

# %%