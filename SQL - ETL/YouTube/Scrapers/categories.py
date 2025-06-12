# Importy all packages
import pandas as pd
from api_connection import youtube


def categories():
    request = youtube.videoCategories().list(part='snippet', regionCode='US')
    response = request.execute()
    
    category_ids = []
    category_titles = []

    for item in response['items']:
        category_ids.append(item['id'])
        category_titles.append(item['snippet']['title'])

    categories = pd.DataFrame({
        'category_id': category_ids,
        'category_title': category_titles
    })

    return categories