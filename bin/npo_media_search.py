#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint
"""
from npoapi import Media
client = Media().command_line_client(description="Search from the NPO Frontend API")

client.ARGS.add_argument('form', type=str, nargs=1, help='Form')
client.ARGS.add_argument('-s', "--sort", type=str, default=None, choices={"asc", "desc"},
                         help="sort (only relevant when using sub)")
client.ARGS.add_argument('-m', "--max", type=int, default=240)
client.ARGS.add_argument('-o', "--offset", type=int, default=0)
args = client.parse_args()
print(client.search(args.form[0], sort=args.sort, max_=args.max, offset=args.offset))
