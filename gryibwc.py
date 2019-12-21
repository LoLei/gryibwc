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
import time
from bs4 import BeautifulSoup


def get_word_count(isbn):
    url = "https://www.readinglength.com/book/isbn-" + isbn
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="lxml")
    text = soup.get_text()
    wc = 0
    if "wordCount\"" in text:
        pos = text.rfind("wordCount\"")
        wc_str = text[pos:pos+18]
        com_pos = wc_str.find(',')
        col_pos = wc_str.find(':')
        wc = int(wc_str[col_pos+1:com_pos])
    elif "Word Count" in text:
        pos = text.rfind("Word Count")
        wc_str = text[pos:pos+22]
        num_start_pos = wc_str.find('t')
        num_end_pos = wc_str.rfind(' ')
        wc_num_str = wc_str[num_start_pos+1:num_end_pos]
        wc_num_str = wc_num_str.replace(',', '')
        wc = int(wc_num_str)
    return wc

def main(args):
    config = configparser.ConfigParser()
    config.read('apikey.ini')
    key = config['api']['key']

    client = gr.Client(developer_key=key)
    result = client.Review.list(args.userid, name="read", sort="date_read",
                                per_page=200)
    reviews = result['reviews']['review']

    wc_all = 0
    for review in reviews:
        # Since output is sorted from recently read to older,
        # break when the first book of the previous year is reached
        year_read = 0
        try:
            year_read = int(dateutil.parser.parse(review['read_at']).year)
        except TypeError:
            continue
        if year_read < args.year:
            break
        if year_read != args.year:
            continue

        title = review['book']['title']
        print(title)
        isbn = review['book']['isbn']
        if isinstance(isbn, dict):
            print("No ISBN found for {}".format(title))
            continue
        print("ISBN:", isbn)

        wc = get_word_count(isbn)
        print(wc)
        if wc == 0:
            print("No word count found for {}".format(isbn))
        wc_all += wc
        if not args.fast:
            time.sleep(1)

    print("Overall word count for year {}: {}".format(args.year, wc_all))
    return wc_all


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("userid", help="goodreads user id")
    parser.add_argument("year", type=int, help="desired year")
    parser.add_argument(
            "--version",
            action="version",
            version="%(prog)s (version {version})".format(version=__version__))
    parser.add_argument("--fast", help="skip wait time - risk getting banned",
                        action="store_true", default=False)

    args = parser.parse_args()
    main(args)
