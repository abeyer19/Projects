import psycopg
import sys
from dotenv import load_dotenv
import os

# Load in config.env file for Database connection secrets
load_dotenv("config.env")
host:str = os.getenv("host")
port:int = os.getenv("port")
user:str = os.getenv("user")
dbname1:str = os.getenv("dbname1")
scrapers_path:str = os.getenv("scrapers_path")

# Use path of Scrapers folder to load in categories.py from the Scrapers
sys.path.insert(0, scrapers_path)
from categories import categories # type:ignore

categories_df = categories()

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