# Importy all packages
import pandas as pd
from api_connection import youtube
from datetime import datetime


def collector_video(video_id:str):
    request = youtube.videos().list(
        part='id, snippet, statistics, contentDetails',
        id=video_id,
        )

    response = request.execute()

    video_ids = []
    video_titles = []
    publication_dates = []
    view_counts = []
    like_counts = []
    comment_counts = []
    video_durations = []
    channel_ids = []
    category_ids = []
    record_dates = []

    for item in response['items']:
        video_ids.append(item['id'])
        video_titles.append(item['snippet']['title'])
        publication_dates.append(item['snippet']['publishedAt'])
        view_counts.append(item['statistics']['viewCount'])
        like_counts.append(item['statistics']['likeCount'])
        comment_counts.append(item['statistics']['commentCount'])
        video_durations.append(item['contentDetails']['duration'])
        channel_ids.append(item['snippet']['channelId'])
        category_ids.append(item['snippet']['categoryId'])
        record_dates.append(datetime.now())

    collector_data = pd.DataFrame({
        'video_id': video_ids,
        'video_title': video_titles,
        'publication_date': publication_dates,
        'view_count': view_counts,
        'like_count': like_counts,
        'comment_count': comment_counts,
        'video_duration': video_durations,
        'channel_id': channel_ids,
        'category_id': category_ids,
        'record_date': record_dates,
    })
    
    return collector_data