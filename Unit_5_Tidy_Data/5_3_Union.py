# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Union

# %% load packages
import pandas as pd

# %% generate sample data
df_total = pd.DataFrame([ \
    ["21.01.2021", "UI-92716", "Banner click"], \
    ["21.01.2021", "UI-92716", "Video view"], \
    ["21.01.2021", "UI-92717", "Video view"], \
    ["21.01.2021", "UI-92717", "Form entry"], \
    ["21.01.2021", "UI-92717", "Purchase"]], \
         columns = ["Date","User-ID","Action"])

df_new = pd.DataFrame([ \
    ["22.01.2021", "UI-92718", "contact form"], \
    ["22.01.2021", "UI-92719", "Video view"]], \
        columns = ["Date","User-ID","Action"])

# %% union both dataframes
df_total = pd.concat([df_total, df_new], \
    ignore_index=True)

print(df_total)
# console output:
#          Date   User-ID        Action
# 0  21.01.2021  UI-92716  Banner click
# 1  21.01.2021  UI-92716    Video view
# 2  21.01.2021  UI-92717    Video view
# 3  21.01.2021  UI-92717    Form entry
# 4  21.01.2021  UI-92717      Purchase
# 5  22.01.2021  UI-92718  contact form
# 6  22.01.2021  UI-92719    Video view
# 7  22.01.2021  UI-92718  contact form
# 8  22.01.2021  UI-92719    Video view