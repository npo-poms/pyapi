#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint
"""
from npoapi import Media

client = Media().command_line_client(description="Get an media object from the NPO Frontend API")
list_of_subs = ["descendants", "members", "episodes", "related", ""]
client.add_argument('mid', type=str, nargs=1, help='The mid  of the object to get')
client.add_argument('sub', type=str, nargs='?', default="", choices=list_of_subs,
                  help="Sub call for the mediaobject. On default the mediaobject itself is returned, but you can also opt for one of these choices")
client.add_argument('-s', "--sort", type=str, default=None, choices={"asc", "desc"},
                  help="sort (only relevant when using sub)")

args = client.parse_args()
print(client.get(args.mid[0], 
                 sub="" if args.sub == "" else "/" + args.sub,
                 sort=args.sort))
