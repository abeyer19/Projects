# Importy all packages
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import pandas as pd

# Import other file functions
from search import search
from categories import categories
from collector_video import collector_video
from collector_channels import collector_channel


# Search for items on YouTube
category_df = categories()
category_df['category_id'] = category_df['category_id'].astype('string')

# SUDO-code
# print out n number of video IDs per search by category ID
# get collector video data
# get collector channel data based on collector video data

for id in category_df['category_id']:
    print(search(result_limit=1, type='video', video_category_id=id, video_duration='long'))
    print(id)
    print('---------')