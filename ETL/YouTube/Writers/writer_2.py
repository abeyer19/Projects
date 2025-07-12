import pandas as pd
import psycopg
from dotenv import load_dotenv
import os
import sys

# Load in config.env file for Database connection secrets
load_dotenv("config.env")
host = os.getenv("host")
port:int = os.getenv("port")
user = os.getenv("user")
dbname1 = os.getenv("dbname1")
dbname2 = os.getenv("dbname2")
scrapers_path:str = os.getenv("scrapers_path")

# Use path of Scrapers folder to load in __ from the Scrapers
sys.path.insert(0, scrapers_path)
from search import search # type:ignore
from collector_video import collector_video # type:ignore
from collector_channel import collector_channel # type:ignore

# use the search function like usual
# connect with collector_video
# create a function that dynamically takes in a set of column from a pandas df (object) and CREATES TABLE IF NOT EXISTS and pushes data at the same time
def writer(host, port, user, dbname, table:str, dataframe:object):
    with psycopg.connect(host=host, port=port, user=user, dbname=dbname) as dbs1:
        with dbs1.cursor() as cur:
            dataframe.columns
            dataframe.dtypes
            print(dataframe)
            print(dataframe.columns)
            print(dataframe.dtypes)

            # cur.execute("""
            # CREATE TABLE IF NOT EXISTS %s (
            #     STUFF AND STUFF TEXT,
            #     video_title TEXT,
            #     publication_date TIMESTAMP,
            #     view_count BIGINT,
            #     like_count BIGINT,
            #     comment_count BIGINT,
            #     video_duration TEXT,
            #     channel_id TEXT,
            #     category_id BIGINT,
            #     record_date TIMESTAMP)
            # """).format((table,))


# testing purposes only
categories_filter = [20]
vid_srch_result_list = []
for cat_id in categories_filter:
    vid_srch_result_list.append(search(result_limit=1, type='video', video_category_id=cat_id, video_duration='medium'))
vid_srch_result_df = pd.concat(vid_srch_result_list, ignore_index=True)

collector_video_results = []
for index,row in vid_srch_result_df.iterrows():
    video_id = row['video_id']
    collector_video_results.append(collector_video(video_id=video_id))
collector_video_results_df = pd.concat(collector_video_results, ignore_index=True)

writer(collector_video_results_df)