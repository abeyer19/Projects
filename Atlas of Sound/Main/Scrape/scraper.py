#SUDO Code 

# 1. use Requests packaged to access https://www.whosampled.com/
    # https://www.whosampled.com/sitemap/artist/A/ - example
# 2. specify URLs and length of pages to pull in pull function
# 3. extract data needed and transform this into a pandas df
#  a. get: artist, album name, song name, album year, sampled song(s) name, sampled song artist, sampled song album, sampled song album year

import requests

urls = [
    "https://www.whosampled.com/artist/Daft-Punk/",
    "https://www.whosampled.com/artist/Nirvana/"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

for url in urls:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        filename = url.split("/")[-2] + ".html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Saved {url} as {filename}")
    else:
        print(f"Failed to fetch {url} - Status code: {response.status_code}")