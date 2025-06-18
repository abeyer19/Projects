import pandas as pd
import psycopg
import sys
from dotenv import load_dotenv
import os


# SUDO-CODE:
# -- pull data from database -> specified by items in config.env
# -- return as a pandas df for easy manipulation
# -- 

# Load in config.env file for Database connection secrets
load_dotenv("config.env")
host = os.getenv("host")
port:int = os.getenv("port")
user = os.getenv("user")
dbname1 = os.getenv("dbname1")

def pully(host:str, port:int, user:str, dbname1:str, table:str=None, query_limit:int=None):
    with psycopg.connect(host=host, port=port, user=user, dbname=dbname1) as conn_dbs1:
        with conn_dbs1.cursor() as cur:
    # -- take all arguments and select * from said table -> allowing limit of return values
            cur.execute("SELECT * FROM %s LIMIT %s" % (table, query_limit))
            videos = cur.fetchall()
            video_ids, video_titles, publication_dates, view_counts, like_counts, comment_counts, video_durations, channel_ids, category_ids, record_dates = zip(*videos)

            video_df = pd.DataFrame({
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

            return video_df

        conn_dbs1.close()

print(pully(host=host, port=port, user=user, dbname1=dbname1, table="videos", query_limit=2))