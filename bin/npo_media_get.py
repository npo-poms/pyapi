#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint
"""
from npoapi import Media
import argparse

ARGS = argparse.ArgumentParser(
    description="Get an media object from the NPO Frontend API",
    epilog=Media.EPILOG
)
ARGS.add_argument('mid', type=str, nargs=1, help='The mid  of the object to get')
ARGS.add_argument('sub', type=str, nargs='?', default="", help='[|descendants|members]')

args = ARGS.parse_args()
client = Media().command_line_client()
sub = args.sub
if len(sub) > 0:
    sub = "/" + sub

print(client.get(args.mid[0], sub))
