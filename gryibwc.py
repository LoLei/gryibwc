#!/usr/bin/env python3
"""
GRYIBWC
"""

__author__ = "Lorenz Leitner"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import configparser
import goodreads_api_client as gr
import dateutil.parser
import requests
from bs4 import BeautifulSoup


def get_word_count(isbn):
    url = "https://www.readinglength.com/book/isbn-" + isbn
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    text = soup.get_text()
    if "wordCount" in text:
        print("Found stirng")
        pos = text.rfind("wordCount")
        wc_str = text[pos:pos+18]
        com_pos = wc_str.find(',')
        col_pos = wc_str.find(':')
        wc = int(wc_str[col_pos+1:com_pos])
        print(wc)
    return wc

def main(args):
    config = configparser.ConfigParser()
    config.read('apikey.ini')
    key = config['api']['key']

    client = gr.Client(developer_key=key)
    # result = client.Review.list(args.userid, name="read", sort="date_read",
                                # per_page=200)
    # reviews = result['reviews']['review']

    # for review in reviews:
        # Since output is sorted from recently read to older,
        # break when the first book of the previous year is reached
        # year_read = int(dateutil.parser.parse(review['read_at']).year)
        # if year_read < args.year:
            # break
        # print(review['book']['title'])
        # print(review['book']['isbn'])
        # print(review['read_at'])
        # print(year_read)

    word_count = get_word_count("0765326361")
    print(word_count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("userid", help="goodreads user id")
    parser.add_argument("year", type=int, help="desired year")
    parser.add_argument(
            "--version",
            action="version",
            version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
