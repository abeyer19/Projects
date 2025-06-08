import psycopg
import sys
from dotenv import load_dotenv
import os

# Use path of Scrapers folder to load in categories.py from the Scrapers
sys.path.insert(0, '/Users/projects/Desktop/Python/Projects/SQL - ETL/YouTube/Scrapers')
from YouTube.Scrapers.categories import categories

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
            CREATE TABLE categories (
                category_id integer,
                category_title text)
            """)

        for index, id in categories_df.iterrows():
            print(id['category_id'], id['category_title'])
            cur.execute("INSERT INTO categories (category_id, category_title) VALUES (%s, %s)",
                        (id['category_id'], id['category_title'],))
            
            # Un-Commented out the commit function below when moving to production
            #conn_dbs1.commit()