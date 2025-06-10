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
with psycopg.connect(host=host, port=port, dbname=dbname1, user=user) as conn_dbs1:

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

        cur.execute("""
            CREATE TABLE IF NOT EXISTS video_search (
                video_id INTEGER,
                video_title TEXT,
                category_id INTEGER,
                record_date TIMESTAMP)
            """)

        # Limit search categories upfront --- customizable
        categories_filter = [1, 2, 19, 20, 24, 27, 28, 35]

        # Search video by category -> can change to all by calling categories_df instead
        #for id in categories_filter:
        #    print(id)
        #    print(search(result_limit=1, type='video', video_category_id=id))
        
        #cur.execute("INSERT INTO video_search VALUES (%s, %s, %s, %s, %s)",)