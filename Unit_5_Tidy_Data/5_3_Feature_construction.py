# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Feature construction

# %% load packages
import pandas as pd

# %% create sample data
values = pd.date_range("2021-02-01", periods=7, freq='D')
df = pd.DataFrame(values,columns=["Date"])

# %% construct a weekday feature based on the date
df['day_of_week'] = df['Date'].dt.day_name()

# %% construct a Boolean weekeend feature based on the date
df['weekend'] = pd.DatetimeIndex(df.Date).dayofweek // 5

# %%