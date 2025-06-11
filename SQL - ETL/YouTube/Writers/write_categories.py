import psycopg
import sys
from dotenv import load_dotenv
import os

# Use path of Scrapers folder to load in categories.py from the Scrapers
sys.path.insert(0, '/Users/projects/Desktop/Python/Projects/SQL - ETL/YouTube/Scrapers')
from categories import categories # type:ignore

categories_df = categories()

# Load in config.env file for Database connection secrets
load_dotenv("config.env")
host = os.getenv("host")
port:int = os.getenv("port")
user = os.getenv("user")
dbname1 = os.getenv("dbname1")

# Connect to an existing database to DBS1
with psycopg.connect(host=host, port=port, dbname=dbname1, user=user) as conn_dbs1:

    # Open a cursor to perform database operations on BDS1
    with conn_dbs1.cursor() as cur:

        cur.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                category_id INTEGER,
                category_title TEXT)
            """)

        for index, id in categories_df.iterrows():
            print(id['category_id'], id['category_title'])
            cur.execute("INSERT INTO categories (category_id, category_title) VALUES (%s, %s) ON CONFLICT (category_id) DO NOTHING",
                        (id['category_id'], id['category_title'],))
            
            conn_dbs1.commit()