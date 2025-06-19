# Importy all packages
import pandas as pd
from api_connection import youtube
from datetime import datetime

# Search is only to be used for basic searching of channel, video, and playlist metadata such as ID and Titles; all other statistics to be collected through collector.py
def search(result_limit:int, type:str, query:str=None, video_category_id:int=None, video_duration:str=None):
    # To be used only if 'type' = 'channel'
    if type == 'channel':
        request = youtube.search().list(
            part='id, snippet',
            maxResults=result_limit,
            order='relevance',
            relevanceLanguage='en', 
            type=type, 
            q=query,
            videoDuration=video_duration,
            )
        
        response = request.execute()

        channel_ids = []

        for item in response['items']:
            channel_ids.append(item['id']['channelId'])

        channel_data = pd.DataFrame({
            'channel_id': channel_ids,
        })

        return channel_data

    # To be used only if 'type' = 'video'
    elif type == 'video':
        request = youtube.search().list(
            part='id, snippet',
            maxResults=result_limit,
            order='relevance',
            relevanceLanguage='en',
            type=type,
            q=query,
            videoCategoryId=video_category_id,
            videoDuration=video_duration,)
        
        response = request.execute()

        video_ids = []

        for item in response['items']:
            video_ids.append(item['id']['videoId'])

        video_data = pd.DataFrame({
            'video_id': video_ids,
        })

        return video_data


# --- TESTING ---
#print(search(result_limit=1, type='video', video_category_id=35))