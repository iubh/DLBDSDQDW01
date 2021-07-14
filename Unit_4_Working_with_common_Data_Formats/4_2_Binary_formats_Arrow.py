# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Binary Formats (Arrow)

# %% load packages
import pyarrow as pa
import pandas as pd
import numpy as np

# %% generate sample data
df = pd.DataFrame({ \
    'one': [20, np.nan, 2.5], \
    'two': ['january', 'february', 'march'], \
    'three': [True, False, True]}, \
        index=list('abc'))

# %% convert the dataframe to an arrow table
table = pa.Table.from_pandas(df)

# %% convert the arrow table back to a dataframe
df_new = table.to_pandas()
