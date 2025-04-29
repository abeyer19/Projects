from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# Replace with API key
load_dotenv("config.env")
api_key = os.getenv("API_KEY")

# Create a service object
youtube = build('youtube', 'v3', developerKey=api_key)

# Example: Search for videos with a keyword
request = youtube.search().list(
    part='snippet',
    q='OpenAI',
    maxResults=5
)

response = request.execute()

# Print the results
for item in response['items']:
    print(f"Title: {item['snippet']['title']}")
    print(f"Channel: {item['snippet']['channelTitle']}")
    print(f"Published At: {item['snippet']['publishedAt']}")
    print(f"Video ID: {item['id'].get('videoId')}")
    print('-' * 50)
