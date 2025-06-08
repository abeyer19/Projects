import pandas as pd
import psycopg
import sys
from dotenv import load_dotenv
import os

# Use path of Scrapers folder to load in categories.py from the Scrapers
sys.path.insert(0, '/Users/projects/Desktop/Python/Projects/SQL - ETL/YouTube/Scrapers')

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
        cur.execute("SELECT * FROM categories")
        data = cur.fetchall()
        id, title = zip(*data)

        categories_df = pd.DataFrame({
            'category_id': id,
            'category_title':title
        })