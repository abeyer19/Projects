# Importy all packages
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import pandas as pd


# Import other file functions
from search import search

# Search for items on YouTube
# 3 inputs needed -> query, type, and output limit
    # Query -> string of text defining the search
    # Type -> string of text of 3 options: channel, video, or playlist
    # Output limit -> integer for the number of search results
print(search('Outdoor Boys', 'channel', 5))