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
list_of_subs = ["descendants", "members", "episodes", "related", ""]
ARGS.add_argument('mid', type=str, nargs=1, help='The mid  of the object to get')
ARGS.add_argument('sub', type=str, nargs='?', default="", choices=list_of_subs,
                  help="Sub call for the mediaobject. On default the mediaobject itself is returned, but ou can also opt for one of these choices")

ARGS.add_argument('-s', "--sort", type=str, default=None, choices={"asc", "desc"},
                  help="sort (only relevant when using sub)")
ARGS.add_argument('-a', "--accept", type=str, default=None, choices={"json", "xml"})

args = ARGS.parse_args()
client = Media().command_line_client()
print(client.get(args.mid[0], 
                 sub="" if args.sub == "" else "/" + args.sub, 
                 sort=args.sort, 
                 accept="application/" + args.accept if args.accept else None))
