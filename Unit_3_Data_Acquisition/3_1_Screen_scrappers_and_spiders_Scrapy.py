# IU - International University of Applied Science
# Data Quality & Data Wranlging
# Course Code: DLBDSDQDW01

# Screen Scrappers and Spiders - Scrapy

# %% load packages
import scrapy
import os

# %% start a scrappy project
os.system('scrapy startproject quotes')

''' specify a spider in the ./quotes/quotes/spiders/Spider1.py script:

import scrapy

class QuotesSpider(scrapy.Spider):
    
    # name the spider
    name = "quotes"
    
    # specify the URLs to crawl
    start_urls = [
        'http://quotes.toscrape.com/page/5/',
        'http://quotes.toscrape.com/page/6/'
        'http://quotes.toscrape.com/page/7/',
    ]

    # define a parser
    def parse(self, response):
        
        # get the divs with the tag 'quote'
        quotes = response.css('div.quote')

        # iterate over each quote
        for quote in quotes:
            
            # extract the text and author of the quote
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get()
            }
'''

# %% start the project (from with the project directory)
os.system('cd ./Unit_3_Data_Acquisition/quotes')
os.system('scrapy crawl quotes -O quotes.json')
