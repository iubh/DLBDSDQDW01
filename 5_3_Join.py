# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Join

# %% load packages
import pandas as pd

# %% generate sample data
df_company = pd.DataFrame([ \
    ["MI6", "007"], \
    ["MI6", "001"], \
    ["MI6", "006"], \
    ["MI6", "005"], \
    ["MI5", "105"]], \
        columns = ["Employer","Employee-ID"])

df_employee = pd.DataFrame([ \
    ["007", "James Bond"], \
    ["001", "Edward Donne"], \
    ["005", "Stuart Thomas"], \
    ["0012", "Sam Jonston"]], \
        columns = ["Employee-ID","Employee-Name"])

# %% inner join
df_company.merge(df_employee, on='Employee-ID', \
    how = "inner")

# console output:
#   Employer Employee-ID  Employee-Name
# 0      MI6         007     James Bond
# 1      MI6         001   Edward Donne
# 2      MI6         005  Stuart Thomas

# %% left join
df_company.merge(df_employee, on='Employee-ID', \
    how = "left")

# console output:
#   Employer Employee-ID  Employee-Name
# 0      MI6         007     James Bond
# 1      MI6         001   Edward Donne
# 2      MI6         006            NaN
# 3      MI6         005  Stuart Thomas
# 4      MI5         105            NaN

# %% right join
df_company.merge(df_employee, on='Employee-ID', \
    how = "right")

# console output:
#   Employer Employee-ID  Employee-Name
# 0      MI6         007     James Bond
# 1      MI6         001   Edward Donne
# 2      MI6         005  Stuart Thomas
# 3      NaN        0012    Sam Jonston

# %% full join
df_company.merge(df_employee, on='Employee-ID', \
    how = "outer")

# console output:
#   Employer Employee-ID  Employee-Name
# 0      MI6         007     James Bond
# 1      MI6         001   Edward Donne
# 2      MI6         006            NaN
# 3      MI6         005  Stuart Thomas
# 4      MI5         105            NaN
# 5      NaN        0012    Sam Jonston