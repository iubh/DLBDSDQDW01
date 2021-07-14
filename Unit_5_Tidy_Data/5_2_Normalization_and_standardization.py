# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Normalization and standardization

# %% load packages
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# %% generate the sample data
data = np.array([ \
    [201, 0.003], \
    [14, 0.09], \
    [40, 0.003], \
    [78, 0.02], \
    [3, 0.3] \
])

# %% create and apply the MinMax Scaler
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

print(data_scaled)
# console output:
# [[1.         0.        ]
#  [0.05555556 0.29292929]
#  [0.18686869 0.        ]
#  [0.37878788 0.05723906]
#  [0.         1.        ]]

# %% create and apply standardization
# to the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

print(data_scaled)
# console output:
# [[ 1.86587833 -0.70939126]
#  [-0.74188884  0.06014789]
#  [-0.37931159 -0.70939126]
#  [ 0.15060901 -0.55902154]
#  [-0.89528691  1.91765618]]