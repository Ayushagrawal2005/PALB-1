# api = 194b2acb2482402f877cf10a3db9a99c

import requests
import json
query = input("Which typeof the news you want to read?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-06-19&sortBy=publishedAt&apiKey=194b2acb2482402f877cf10a3db9a99c"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------")