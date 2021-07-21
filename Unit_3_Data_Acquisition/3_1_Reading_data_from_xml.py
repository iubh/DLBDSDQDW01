# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Reading data from XML

# %% load packages
import xml.etree.ElementTree as ET

# %% read the data
tree = ET.parse('data.xml')

# %% get the root of the XML tree
root = tree.getroot()

# %% iterate over each child of the root
for child in root:

    # print the child tag and attribute
    print(child.tag, child.attrib)

# console output:
# country {'name': 'Liechtenstein'}
# country {'name': 'Singapore'}
# country {'name': 'Panama'}


