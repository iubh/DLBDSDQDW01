# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Structuring

## Intrarecord structuring

### extracting subdata into new columns

# %% import libraries
import pandas as pd

# %% generate data with date strings
dates = pd.DataFrame(["02082021","02152021","02122021","02212021","02012021","02062021"], columns = ["Date"])

# %% extract the day from a date string
dates['Day'] = dates['Date'].str.slice(2, 4)

### combining columns

# %% generate sample data
customers = pd.DataFrame([
    ["P. Sherman 42 Wallaby Way","2000","Sydney"],
    ["221B Baker Street","NW1 6XE","London"]],
        columns = ["Street", "Zip Code", "City"])

# %% combine fields to a human readable address
customers["Address"] = customers["Street"].astype(str) + \
    ' , ' + customers["Zip Code"] + ' ' + customers["City"]

