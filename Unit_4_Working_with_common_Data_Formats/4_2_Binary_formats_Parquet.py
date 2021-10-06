# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Binary Formats (Parquet)

# %% load packages
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
import numpy as np

# %% create a pandas DataFrame
df = pd.DataFrame(np.random.randn(100).\
    reshape(25,4), columns = ["one", "two", \
        "three", "four"])

# %% convert the pandas DataFrame to a parquet table
tableToWrite = pa.Table.from_pandas(df)

# %% write the parquet table to file
pq.write_table(tableToWrite, "myPQFile.parquet")

# %% read data from parquet file
tableToRead = pq.read_table("myPQFile.parquet")

# %% convert the data to a pandas DataFrame
tableToRead.to_pandas()

# %% show metadata about the file
file = pq.ParquetFile("myPQFile.parquet")
file.metadata

# %%
