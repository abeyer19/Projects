import pandas as pd
import psycopg
import sys
from dotenv import load_dotenv
import os

# Load in config.env file for Database connection secrets
load_dotenv("config.env")
host = os.getenv("host")
port:int = os.getenv("port")
user = os.getenv("user")
dbname1 = os.getenv("dbname1")

def pully(host:str, port:int, user:str, dbname:str, table:str, limit:int=None):
    with psycopg.connect(host=host, port=port, user=user, dbname=dbname) as dbs1:
        with dbs1.cursor() as cur:
            cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = %s ORDER BY ordinal_position;", (table,))
            response_columns = cur.fetchall()

            table_columns = []

            for record in response_columns:
                table_columns.append(record[0])
            
            if limit is None:
                cur.execute("SELECT * FROM {}".format(table))
                response_data = cur.fetchall()
            else:
                cur.execute("SELECT * FROM {} LIMIT {}".format(table, limit))
                response_data = cur.fetchall()

            df = pd.DataFrame(data=response_data, columns=table_columns)

            cur.close()

            return df

# Testing only -- delete after finalization
print(pully(host=host, port=port, user=user, dbname=dbname1, table='videos'))