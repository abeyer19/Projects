import pandas as pd
import psycopg
import sys
from dotenv import load_dotenv
import os

# Use path of Scrapers folder to load in __ from the Scrapers
sys.path.insert(0, '/Users/projects/Desktop/Python/Projects/SQL - ETL/YouTube/Scrapers')
from search import search # type:ignore
from collector_video import collector_video # type:ignore
from collector_channel import collector_channel # type:ignore

# Load in config.env file for Database connection secrets
load_dotenv("config.env")
host:str = os.getenv("host")
port:int = os.getenv("port")
user:str = os.getenv("user")
dbname1:str = os.getenv("dbname1")

# Connect to an existing database to DBS1
with psycopg.connect(host=host, port=port, dbname=dbname1, user=user) as conn_dbs1:

    # Open a cursor to perform database operations on BDS1
    with conn_dbs1.cursor() as cur:
        # Pull all data from categories db in PGAdmin4
        cur.execute("SELECT * FROM categories")
        categories = cur.fetchall()
        id, title = zip(*categories)

        # Convert data into a pandas dataframe
        categories_df = pd.DataFrame({
            'category_id': id,
            'category_title':title
        })

        # --------------------------------------------------------------------------

        # Create videos table in PGAdmin4
        cur.execute("""
            CREATE TABLE IF NOT EXISTS videos (
                video_id TEXT,
                video_title TEXT,
                publication_date TIMESTAMP,
                view_count INTEGER,
                like_count INTEGER,
                comment_count INTEGER,
                video_duration TEXT,
                channel_id TEXT,
                category_id INTEGER,
                record_date TIMESTAMP)
            """)

        # Limit search categories upfront --- customizable
        categories_filter = [1, 2, 19, 20, 24, 27, 28, 35]

        # Search by video IDs and concat into a new df
        video_search_results_list = []

        for id in categories_filter:
            video_search_results_list.append(search(result_limit=1, type='video', video_duration='medium',  video_category_id=id))

        video_search_results_df = pd.concat(video_search_results_list, ignore_index=True)

        # Take video IDs and use video_collector
        collector_video_results = []

        for index, row in video_search_results_df.iterrows():
            collector_video_results.append(collector_video(video_id=video_search_results_df['video_id']))

        collector_video_results_df = pd.concat(collector_video_results, ignore_index=True)
        
        # Push video_collector results to PGAdmin4
        cur.execute("INSERT INTO videos (video_id, video_title, publication_date, view_count, like_count, comment_count, video_duration, channel_id, category_id, record_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (collector_video_results_df['video_id'], collector_video_results_df['video_title'], collector_video_results_df['publication_date'], collector_video_results_df['view_count'], collector_video_results_df['like_count'], collector_video_results_df['comment_count'], collector_video_results_df['video_duration'], collector_video_results_df['channel_id'], collector_video_results_df['category_id'], collector_video_results_df['record_date'],))
        
        # --------------------------------------------------------------------------

        # Create channels table in PGAdmin4
        cur.execute("""
            CREATE TABLE IF NOT EXISTS channels (
                channel_id TEXT,
                channel_name TEXT,
                channel_view_count INTEGER,
                subscriber_count INTEGER,
                video_count INTEGER,
                record_date TIMESTAMP)
            """)
        
        # Search by channel IDs and concat into a new df
        channel_search_results = []

        for index, row in collector_video_results_df.iterrows():
            channel_search_results.append(collector_channel(channel_id=collector_video_results_df['channel_id']))

        collector_channel_results_df = pd.concat(channel_search_results, ignore_index=True)

        # Push channel_collector results to PGAdmin4
        cur.execute("INSTERT INTO channels (channel_id, channel_name, channel_view_count, subscriber_count, video_count, record_date) VALUES (%s, %s, %s, %s, %s, %s)",
                    (collector_channel_results_df['channel_id'], collector_channel_results_df['channel_name'], collector_channel_results_df['channel_view_count'], collector_channel_results_df['subscriber_count'], collector_channel_results_df['video_count'], collector_channel_results_df['record_date'],))

        # Commit video and channel data changes to DBS1 tables
        conn_dbs1.commit()