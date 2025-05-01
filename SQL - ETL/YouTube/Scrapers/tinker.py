# Importy all packages
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import pandas as pd

# --- Intro for pulling data via API ---
# Load in 'congif.env' file for API Key
load_dotenv("config.env")
api_key = os.getenv("API_KEY")

# Create a service object
youtube = build('youtube', 'v3', developerKey=api_key)

def categories():
    request = youtube.videoCategories().list(part='snippet', regionCode='US')
    response = request.execute()
    
    category_ids = []
    category_titles = []

    for item in response['items']:
        category_ids.append(item['id'])
        category_titles.append(item['snippet']['title'])

    channel_data = pd.DataFrame({
        'category_id': category_ids,
        'category_title': category_titles
    })

    return channel_data

print(categories())