# Importy all packages
import pandas as pd
from api_connection import youtube

from categories import categories

def search(result_limit:int, type:str, query:str, video_category_id:str=None, video_duration:str=None):
    # To be used only if 'type' = 'channel'
    if type == 'channel':
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

    # To be used only if 'type' = 'video'
    #TODO: Find how to pull in video views
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

        video_titles = []
        video_ids = []
        video_views = []
        channel_ids = []
        channel_titles = []
        date_postings = []

        for item in response['items']:
            video_titles.append(item['snippet']['title'])
            video_ids.append(item['id']['videoId'])
            #video_views.append(item[])
            channel_ids.append(item['snippet']['channelId'])
            channel_titles.append(item['snippet']['channelTitle'])
            date_postings.append(item['snippet']['publishedAt'])

        video_data = pd.DataFrame({
            'video_title': video_titles,
            'video_id': video_ids,
            #'video_view' = [],
            'channel_id': channel_ids,
            'channel_title': channel_titles,
            'date_posted': date_postings,
        })

        return video_data


# --- TESTING ---
#categories_df = categories()
print(search(1, 'channel', 'Gaming'))
print(search(1, 'video', 'Ninja', '20', 'long'))