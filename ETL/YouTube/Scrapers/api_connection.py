# Importy all packages
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# --- Intro for pulling data via API ---
# Load in 'congif.env' file for API Key
load_dotenv("config.env")
api_key = os.getenv("API_KEY")

# Create a service object
youtube = build('youtube', 'v3', developerKey=api_key)