import pandas as pd
from pully import pully
from dotenv import load_dotenv
import os

# Load in config.env file for Database connection secrets
load_dotenv("config.env")
host = os.getenv("host")
port:int = os.getenv("port")
user = os.getenv("user")
dbname1 = os.getenv("dbname1")

df = pully(host=host, port=port, user=user, dbname=dbname1, table='videos')

video_timeline = df.pivot_table(index=['video_title', 'video_id', 'record_date'], values='view_count').reset_index()

video_timeline = video_timeline.groupby(['video_id', 'video_title', 'view_count'])['record_date'].max().reset_index()

top_videos = video_timeline

print(video_timeline)


                #video_title TEXT,
                #publication_date TIMESTAMP,
                #view_count BIGINT,
                #like_count BIGINT,
                #comment_count BIGINT,
                #video_duration TEXT,
                #channel_id TEXT,
                #category_id