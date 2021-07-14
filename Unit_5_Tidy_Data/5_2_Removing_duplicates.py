# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Removing duplicates

# %% load packages
import pandas as pd

# %% generate sample data
df = pd.DataFrame({
    'firstname': ['Peter', 'Peter', 'Bruce', \
        'Bruce', 'Bruce'],
    'lastname': ['Parker', 'Parker', 'Parker', \
        'Banner', 'Banner'],
    'age': [24, 24, 23, 35, 25]
})

# %% drop duplicates
df.drop_duplicates()

# %% drop duplicates based on one column
df.drop_duplicates(subset=['firstname'])

# %% drop duplicates based on two columns
# keep the last of duplicated entries
df.drop_duplicates(\
    subset=['firstname', 'lastname'], \
    keep='last')