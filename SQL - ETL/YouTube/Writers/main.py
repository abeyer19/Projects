import pandas as pd
import psycopg
import sys
from dotenv import load_dotenv
import os

# Use path of Scrapers folder to load in __ from the Scrapers
sys.path.insert(0, '/Users/projects/Desktop/Python/Projects/SQL - ETL/YouTube/Scrapers')
from search import search # type:ignore

# Load in config.env file for Database connection secrets
load_dotenv("config.env")
host:str = os.getenv("host")
port:int = os.getenv("port")
user:str = os.getenv("user")
dbname1:str = os.getenv("dbname1")

# Connect to an existing database to DBS1
with psycopg.connect(host="localhost", port=5432, dbname="DBS1", user="postgres") as conn_dbs1:

    # Open a cursor to perform database operations on BDS1
    with conn_dbs1.cursor() as cur:
        # Pull all data from categories db in PGAdmin4
        cur.execute("SELECT * FROM categories")
        data = cur.fetchall()
        id, title = zip(*data)

        # Convert data into a pandas dataframe
        categories_df = pd.DataFrame({
            'category_id': id,
            'category_title':title
        })

        # Limit search categories upfront --- customizable
        categories_filter = [1, 2, 18, 19, 20, 24, 27, 28, 31, 35]
        categories_df = categories_df[categories_df['category_id'].isin(categories_filter)]
        
        #TODO: Search for videos in filtered category df
        for id, title in categories_df.iterrows():
            print(id, title)
            print(search(result_limit=1, type='channel', video_category_id=id))