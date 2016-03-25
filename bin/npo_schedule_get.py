#!/usr/bin/env python3
"""
  Simple client to get a schedule from the NPO Frontend API2
"""
from npoapi import Schedule

client = Schedule().command_line_client("Get schedule from the NPO Frontend API")
client.add_argument('guideDay', type=str, nargs='?', help='The day to get')
args = client.parse_args()

print(client.get(guideDay=args.guideDay))
