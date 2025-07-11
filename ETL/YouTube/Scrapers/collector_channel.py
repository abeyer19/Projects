# Importy all packages
import pandas as pd
from api_connection import youtube
from datetime import datetime


def collector_channel(channel_id:str):
    request = youtube.channels().list(
        part='id, snippet, statistics',
        id=channel_id,
        )

    response = request.execute()

    channel_ids = []
    channel_names = []
    channel_view_counts = []
    subscriber_counts = []
    video_counts = []
    record_dates = []

    for item in response['items']:
        channel_ids.append(item['id'])
        channel_names.append(item['snippet']['title'])
        channel_view_counts.append(item['statistics']['viewCount'])
        subscriber_counts.append(item['statistics']['subscriberCount'])
        video_counts.append(item['statistics']['videoCount'])
        record_dates.append(datetime.now())

    collector_data = pd.DataFrame({
        'channel_id': channel_ids,
        'channel_name': channel_names,
        'channel_view_count': channel_view_counts,
        'subscriber_count': subscriber_counts,
        'video_count': video_counts,
        'record_date': record_dates,
    })

    return collector_data