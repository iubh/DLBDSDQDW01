# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Structuring

## Intrarecord Structuring

### extracting subdata into new columns

# %% import libraries
import pandas as pd

# %% generate data with date strings
dates = pd.DataFrame([ \
    "02082021", "02152021", "02122021", \
    "02212021","02012021","02062021"], \
        columns = ["Date"])

# %% extract the day from a date string
dates['Day'] = dates['Date'].str.slice(2, 4)

print(dates)
# console output:
#        Date Day
# 0  02082021  08
# 1  02152021  15
# 2  02122021  12
# 3  02212021  21
# 4  02012021  01
# 5  02062021  06


### combining columns

# %% generate sample data
customers = pd.DataFrame([
    ["P. Sherman 42 Wallaby Way","2000","Sydney"],
    ["221B Baker Street","NW1 6XE","London"]],
        columns = ["Street", "Zip Code", "City"])

# %% combine fields to a human readable address
customers["Address"] = customers["Street"].astype(str) + \
    ' , ' + customers["Zip Code"] + ' ' + customers["City"]

## Interrecord Structuring

### filtering

# %% generate the data
cars = pd.DataFrame([ \
    ['VW', 'GOlf'], \
    ['VW', 'Passat'], \
    ['VW', 'Polo'], \
    ['Mercedes', 'A-Class'], \
    ['Mercedes', 'AMG'], \
    ['Tesla', 'Model 3'], \
    ['Tesla', 'Cybertruck'], \
    ], columns=['Brand', 'Model']
)

# %% filter the data by brand
cars.loc[cars.Brand == "VW"]

### aggregation

# %% generate the sample data
sales = pd.DataFrame([ \
    [2020, "January", 212182], \
    [2020,"February",221921], \
    [2020, "March", 152281], \
    [2021, "January", 243822], \
    [2021,"February",123212], \
    [2021,"March",162319]
    ], columns = ["Year", "Month", "Sales"]
)

# %% aggregate by group
sales.groupby("Year").sum()

### pivoting
# %% generate the sample data
df = pd.DataFrame({ \
    "Account-NR": [ \
        "A0023","A0023","A0024", \
        "A0024","A0024","A0024"], \
    "Job": [ \
        "Ice cream Vendor", "Ice cream Vendor", \
        "Barkeeper", "Barkeeper", \
        "Ice cream Vendor", "Waiter"], \
    "Amount": [450, 200, 350, 350, 200, 250]})

# %% pivot the table
import numpy as np
pivot = pd.pivot_table(df, values="Amount", \
    index=["Account-NR"], columns=["Job"], \
        aggfunc=np.sum)

print(pivot)
# console output:
# Job         Barkeeper  Ice cream Vendor  Waiter
# Account-NR                                     
# A0023             NaN             650.0     NaN
# A0024           700.0             200.0   250.0