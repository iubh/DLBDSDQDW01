# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Feature transformation

# %% load packages
import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from scipy.stats import shapiro
from scipy.stats import boxcox

# %% create sample data
df = pd.DataFrame([30.5, 23.2, 16.6, \
    8.5, 0.1, -6.5], \
        columns = ["temp_C"])

# %% transform units
df["temp_F"] = (df["temp_C"] * 9 / 5) + 32

# %% create sample data
df = pd.DataFrame(np.random.randint(0,100, \
    size=(100)), columns=["Values"])

# %%
pd.cut(df['Values'], bins=4).value_counts()

# %% create a normally distributed data set
x_data = np.arange(-5, 5, 0.001)
y_data = stats.norm.pdf(x_data, 0, 1)
plt.plot(x_data, y_data)

# %% create a new data set
data = 20 * np.random.randn(2000) + 200

# %% create a histogram
plt.hist(data, bins = 200)

# %% conduct a Shapiro-Wilk test
from scipy.stats import shapiro
stat, p = shapiro(data)
print(stat, p)

# %% read sample data
df = pd.read_csv('data.csv')

##### needs testing

# %% apply square tranformation
df.insert(len(df.columns), 'Squared', \
    np.sqrt(df['Moderate Positive Skew']))

# %%create histograms
df_viz = df[["Moderate Positive Skew","Squared"]]
df_viz.hist(grid=False, figsize=(10, 6), bins=30)

# %% apply logarithmic transformation
df.insert(len(df.columns), 'Logarithmic', \
    np.log(df['Moderate Positive Skew']))

# %% apply Box-Cox transformation
df.insert(len(df.columns), 'Boxcox', \
    boxcox(df['Moderate Positive Skew'])[0])
