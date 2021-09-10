# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Web Scraping

# %% import modules
import requests

# %% load a web page
page = requests.get('http://quotes.toscrape.com/')

# %% extract the page's content
contents = page.content

# %% show the page's status code
page.status_code

## Beautiful Soup

# %% load packages
from bs4 import BeautifulSoup

# %% parsing the content of the web page
soup = BeautifulSoup(page.content)

# %% extract the first link tag in the page
soup.link

# %% extract the first link in the page
soup.link['href']

# %% find the first tag of class 'quote'
soup.find(class_ = "quote")

# %% extract the link within the first tag of class 'quote'
soup.find(class_ = "quote").a["href"]

# %% find all tags of class 'text' or of class 'author'
soup.find_all(class_ = ["text","author"])

# %% collect all authors and texts with tags of class 'quote'
quoteList = []
for e in soup.find_all(class_ = "quote"):
    author = e.find(class_ ="author").getText()
    text = e.find(class_ = "text").getText()
    quoteList.append([author, text])

# %% crawl multiple pages of a URL and extract authors and quotes
url = "https://quotes.toscrape.com/page/"
quoteList = []

# iterate over all pages of the URL
for i in range(0,4):
    
    cur_url = "http://quotes.toscrape.com/page/" + str(i)
    page = requests.get(cur_url)
    
    # extract and parse the pages content
    contents = page.content
    soup = BeautifulSoup(page.content)

    # iterate over all tags of class 'quote'
    for e in soup.find_all(class_ = "quote"):
        
        # extract author's names and quotes
        author = e.find(class_ ="author").getText()
        text = e.find(class_ = "text").getText()
        quoteList.append([author, text])

# %% print the number of found qoutes
print(len(quoteList))
# console output: 30

# %% crawl multiple pages of an URL which contain a
# 'Next' button
url = "https://quotes.toscrape.com/page/"
quoteList = []

# iterate over all pages of the URL
for i in range(0, 49):
    
    cur_url = "http://quotes.toscrape.com/page/" + str(i)
    page = requests.get(cur_url)
    
    # extract and parse the pages content
    contents = page.content
    soup = BeautifulSoup(page.content)

    # break out of the loop if there is no 'Next' button
    if soup.find(text = "Next ") == None:
        break

    # iterate over all tags of class 'quote'
    for e in soup.find_all(class_ = "quote"):
        author = e.find(class_ ="author").getText()
        text = e.find(class_ = "text").getText()
        quoteList.append([author, text])

# %% print the number of found qoutes
print(len(quoteList))
# console output: 90

# %%
