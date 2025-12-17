from dotenv import load_dotenv
import os

# Load in config.env file for Database connection secrets
load_dotenv("Atlas of Sound/config.env")
host:str = os.getenv("host")
port:int = os.getenv("port")
user:str = os.getenv("user")
dbname1:str = os.getenv("dbname1")
scrapers_path:str = os.getenv("scrapers_path")