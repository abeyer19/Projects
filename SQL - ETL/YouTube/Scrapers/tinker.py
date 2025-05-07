# Importy all packages
import pandas as pd
from api_connection import youtube

# Make a function that takes each category and searches the top 10 videos for each category
# - List the unique channels within the search, eliminating duplicates
# - Find only recent video postings - 1-week lag
# - Get metadata for videos and channels such as:
    # Video - ID, title, date posted, 
    # Channel - ID, name, sub count

from categories import categories
from search import search

categories_df = categories()

for index, id in categories_df.iterrows():
    print(search(1,'channel',))
    print(id['category_id'])
    print('--------')