#https://www.geeksforgeeks.org/artificial-intelligence/introduction-to-langchain/
#https://www.geeksforgeeks.org/artificial-intelligence/artificial-intelligence/

import threading
import requests
from bs4 import BeautifulSoup
urls = [
    "https://www.geeksforgeeks.org/artificial-intelligence/introduction-to-langchain/",
    "https://www.geeksforgeeks.org/artificial-intelligence/artificial-intelligence/"
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.get_text())} characters from {url}')

    threads = []

    for url in urls:
        thread = threading.Thread(target=fetch_content, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

print("All threads have completed.")