import requests
from bs4 import BeautifulSoup
import os
from markdownify import markdownify as md
import re

from utils import check_url, sanitize_url

start_url = "https://daffodilvarsity.edu.bd/"

link_queue = [start_url]


def crawl():
    while True:
        try:
            url = link_queue.pop(0)
            print("Scrapping: {}".format(url))

            response = requests.get(url)
            soup = BeautifulSoup(response.content, features="html.parser")

            temp = []
            for link in soup.find_all('a', href=True):
                link_url = link["href"]
                if check_url(link_url):
                    if url not in link_queue:
                        temp.append(link_url)
            if len(temp) > 0:
                for temp_url in temp:
                    link_queue.append(temp_url)
                print("Added {} URLs in the queue, total: {}".format(len(temp), len(link_queue)))

            markdown = md(response.content, strip=['a', 'img', 'nav'])
            with open(os.path.join('data/md', sanitize_url(url)), "w", encoding="utf-8") as md_file:
                markdown = re.sub(r'\n\s*\n', '\n\n', markdown)
                md_file.write(markdown)

            print("URLs Left: {}".format(len(link_queue)))

            if len(link_queue) == 0:
                print("=== CRAWLING DONE ===")
                break
        except:
            print("ERROR: Skipping...")


if __name__ == "__main__":
    if not os.path.exists("data/md"):
        os.mkdir("data")
        os.mkdir("data/md")
    crawl()
