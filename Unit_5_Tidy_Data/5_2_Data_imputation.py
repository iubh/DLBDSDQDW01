# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Data imputation

# %% load packages
import numpy as np
import pandas as pd

# %% generate a sample dataset
df = pd.DataFrame(np.random.randn(8,4),\
    columns = ["zero", "one", "two", "three"])

# %% add missing values
df.iloc[:6,0] = np.nan
df.iloc[:4,1] = np.nan
df.iloc[:2,2] = np.nan

# %% show the sample data
df

# console output:
#        zero       one       two     three
# 0       NaN       NaN       NaN -0.722502
# 1       NaN       NaN       NaN  0.461928
# 2       NaN       NaN -1.123492 -0.870373
# 3       NaN       NaN  0.438706 -0.410326
# 4       NaN  1.274561 -0.073225 -0.553929
# 5       NaN  0.569232  1.088357 -0.353911
# 6 -0.065522  0.666667 -1.753920 -2.093555
# 7 -0.558569 -1.302122  0.092451  1.122218

# %% substitution by default value
# maximum value and mean
df.fillna({ \
    "zero":0, \
    "one":df.one.max(), \
    "two":df.two.mean() \
})

# console output:
#        zero       one       two     three
# 0  0.000000  1.274561 -0.221854 -0.722502
# 1  0.000000  1.274561 -0.221854  0.461928
# 2  0.000000  1.274561 -1.123492 -0.870373
# 3  0.000000  1.274561  0.438706 -0.410326
# 4  0.000000  1.274561 -0.073225 -0.553929
# 5  0.000000  0.569232  1.088357 -0.353911
# 6 -0.065522  0.666667 -1.753920 -2.093555
# 7 -0.558569 -1.302122  0.092451  1.122218

# %% generate another sample data set
df = pd.DataFrame({ \
    "city": ["tokyo", None, "london", \
        "seattle", "san francisco", "tokyo"], \
    "boolean": ["yes", "no", None, \
        "no", "no", "yes"], \
    "ordinal_column": ["somewhat like", "like", \
        "somewhat like", "like", \
        "somewhat like", "dislike"], \
    "quatitative_column": [1, 11, -0.5, 10, None, 20]})

# %% identify the mode
sub_val = df['city'].value_counts().index[0]
print(sub_val)
# console output: 'tokyo'

# %% mode substitution
df_sub = df.fillna({'city': sub_val})

print(df_sub.city)
# console output:
# 0            tokyo
# 1            tokyo
# 2           london
# 3          seattle
# 4    san francisco
# 5            tokyo
# Name: city, dtype: object

# %% generate sample data
df = pd.DataFrame({ \
    'age': [34, 27, 89, 23, 34, None, 32], \
    'height': [178, 173, 198, 167, None, 174, 165]
})

# %% apply mean substitution using the SimpleImputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
imputer.fit_transform(df)

# console output:
# array([[ 34.        , 178.        ],
#        [ 27.        , 173.        ],
#        [ 89.        , 198.        ],
#        [ 23.        , 167.        ],
#        [ 34.        , 175.83333333],
#        [ 39.83333333, 174.        ],
#        [ 32.        , 165.        ]])

# %%
