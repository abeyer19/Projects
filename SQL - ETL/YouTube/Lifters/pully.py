import pandas as pd
import psycopg
import sys
from dotenv import load_dotenv
import os


# SUDO-CODE:
# -- pull data from database -> specified by items in config.env
# -- return as a pandas df for easy manipulation

# Load in config.env file for Database connection secrets
load_dotenv("config.env")
host = os.getenv("host")
port:int = os.getenv("port")
user = os.getenv("user")
dbname1 = os.getenv("dbname1")

def pully(host:str, port:int, user:str, dbname1:str, table:str, query_limit:int):
    pass
    # -- connect to psycopg
    
    # -- take all arguments and select * from said table -> allowing limit of return values

    # form back into a pandas df

    # return said pandas df