#!/usr/bin/env python3
"""
  Simple client to get the changes feed from the NPO Frontend API
"""
from npoapi import Media

client = Media().command_line_client("Get changes feed from the NPO Frontend API")
client.add_argument('profile', type=str, nargs='?', help='Profile')

args = client.parse_args()
print(client.changes(profile=args.profile))
