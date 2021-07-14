# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Regular expressions

# %% load packages
import re
from bs4 import BeautifulSoup

# %% generate sample data
txt = "The rain in Germany"

# %% apply RegEx to find patterns in the data
re.findall("^The.*Germany$", txt)
# console output: ['The rain in Germany']

# %%
txt = "The rain in Spain"
re.findall("ai", txt)
# console output: ['ai', 'ai']

# %% create sample HTML
email_example = """<br/>
    <div>
        This is an example HTML document to showcase
        how email adresses can be retrieved using regex
    </div> 
    tutor@iu.org
    <div>student@iu.org</div>
    <span>professor@iu.org</span>
 """

# %% parse the HTML
soup = BeautifulSoup(email_example,"lxml")

# %% compile a RegEx
regex = re.compile("\w+@\w+\.\w+")

# %% use the RegEx to extract email addresses from
# the HTML
print(soup.find(text = regex))
# console output: tutor@iu.org