# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Binary Formats (HDF5)

## Create an empty HDF5 dataset

# %% load packages
import h5py

# %% create an HDF5 file
file = h5py.File('iu.h5','w')

# %% create an empty dataset in the HDF5 file
dataset = file.create_dataset("iu", (4, 6)) 

# %% print information about the dataset
print("Dataset shape is", dataset.shape )
print("Dataset name is", dataset.name)
print("Dataset is a member of the group", \
    dataset.parent )

# %% close the file
file.close()

## Fill an HDF5 dataset with values

# %% load packages
import numpy as np

# %% read/write HDF5 file
file = h5py.File('iu.h5','r+')

# %% list existing datasets in the file
list(file.keys())

# %% create an empty dataset in the HDF5 file
# if this dataset does not already exist
if not "iu_numbers" in list(file.keys()):
    dataset = file.create_dataset("iu_numbers", (4, 6)) 
else:
    dataset = file['/iu_numbers']

# %% generate sample data
data = np.random.rand(4*6).round(2).reshape(4, 6)

# %% add the data to the HDF5 dataset
dataset[...] = data

# %% read the data back from the HDF5 file
data_read = dataset[...]
print(data_read)
# console output:
# [[0.65 0.96 0.77 0.33 0.19 0.93]
#  [0.11 0.31 0.99 0.01 0.61 0.48]
#  [0.09 0.79 0.4  0.15 0.3  0.35]
#  [0.97 0.36 0.27 0.45 0.21 0.59]]

# %% adding meta data to a data set
dataset.attrs["User"] = "ME"

# %% print the meta data for the data set
for k in dataset.attrs.keys():
    print(k, dataset.attrs[k])
# console output:
# User ME

# %% close the file
file.close()