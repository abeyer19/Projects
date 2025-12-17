#SUDO Code 

# 1. use Requests packaged to access https://www.whosampled.com/
    # https://www.whosampled.com/sitemap/artist/A/ - example
# 2. specify URLs and length of pages to pull in pull function
# 3. extract data needed and transform this into a pandas df
#  a. get: artist, album name, song name, album year, sampled song(s) name, sampled song artist, sampled song album, sampled song album year

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.status_code)  # HTTP status code (200 = OK)
print(response.text)
data = response.json()
print(data["title"])