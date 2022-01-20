#!/usr/bin/env python
import argparse
import urllib.parse
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def main(query):
    query = urllib.parse.quote_plus(query)

    # url = f"https://web.archive.org/web/*/{query}"
    url=f'https://web.archive.org/__wb/search/anchor?q={query}'
    print(f"{query=}")
    r = requests.get(url)
    for result in r.json():
        print(result['link'])
    # with open("index.html", "w") as f:
    #     f.write(str(r.text))

    # b = BeautifulSoup(r.text, "html.parser")
    # for link in b.find_all("a"):
    #     print(link.get("href"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    args = parser.parse_args()
    main(args.query)
