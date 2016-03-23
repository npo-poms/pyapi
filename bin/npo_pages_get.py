#!/usr/bin/env python3
"""
  Simple client to get an page from the NPO Frontend API pages endpoint
"""
from npoapi import Pages
client = Pages().command_line_client(description="Get a page from the NPO Frontend API")
client.ARGS.add_argument('url', type=str, nargs=1, help='The url  of the object to get')
args = client.parse_args()
print(client.get(args.url[0]))
