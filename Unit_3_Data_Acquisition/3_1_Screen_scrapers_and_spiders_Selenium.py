# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Screen Scrapers and Spiders - Selenium

# %% load packages
from selenium import webdriver
from selenium.webdriver.common.by import By

# %% specifiy a webdriver
browser = webdriver.Firefox()

# %% use the browser to go to a web page
browser.get('http://quotes.toscrape.com/')

# %% maximize the window
browser.maximize_window()

# use a simple script to scroll down 2000 units
browser.execute_script("window.scrollTo(0, 2000)")

# %% locate the next button
next_button = browser.\
    find_element(by=By.PARTIAL_LINK_TEXT,value='Next')

# %% click the next button
next_button.click()
# %%
