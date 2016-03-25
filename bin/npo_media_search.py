#!/usr/bin/env python3
"""
  Simple client to search media in the  NPO Frontend API
"""
from npoapi import Media

client = Media()\
    .command_line_client(description="Search from the NPO Frontend API")
client.add_argument('form', type=str, nargs=1, help='The search form. This may be a json string, or the name of a file containing it')
client.add_argument('-s', "--sort", type=str, default=None, choices={"asc", "desc"})
client.add_argument('-m', "--max", type=int, default="240")
client.add_argument('-o', "--offset", type=int, default=0)

args = client.parse_args()
print(client.search(args.form[0], sort=args.sort, max_=args.max, offset=args.offset))
