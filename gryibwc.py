#!/usr/bin/env python3
"""
GRYIBWC
"""

__author__ = "Lorenz Leitner"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import configparser
from pprint import pprint
import goodreads_api_client as gr


def main(args):
    config = configparser.ConfigParser()
    config.read('apikey.ini')
    key = config['api']['key']
    client = gr.Client(developer_key=key)
    books = client.Review.list(args.userid, "read")
    pprint(books)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("userid", help="goodreads user id")
    parser.add_argument(
            "--version",
            action="version",
            version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
