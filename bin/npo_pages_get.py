#!/usr/bin/env python3
"""
  Simple client to get an page from the NPO Frontend API pages endpoint
"""
from npoapi import Pages
import argparse

ARGS = argparse.ArgumentParser(
    description="Get a page from the NPO Frontend API",
    epilog=Pages.EPILOG
)
ARGS.add_argument('url', type=str, nargs=1, help='The url  of the object to get')

args = ARGS.parse_args()
client = Pages().command_line_client()

print(client.get(args.url[0]))
