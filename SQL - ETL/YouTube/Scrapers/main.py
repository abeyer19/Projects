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

def search_channels(query, result_limit):
    request = youtube.search().list(part='id, snippet, statistics', type='channel', q=query, maxResults=result_limit)
    response = request.execute()
    
    channel_ids = []
    channel_titles = []

    for item in response['items']:
        channel_ids.append(item['id']['channelId'])
        channel_titles.append(item['snippet']['channelTitle'])

    channel_data = pd.DataFrame({
        'channel_id': channel_ids,
        'channel_title': channel_titles
    })

    return channel_data

print(search_channels('Outdoor Boys', 5))