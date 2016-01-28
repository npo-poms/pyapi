#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint
"""
from npoapi import Schedule
import argparse

ARGS = argparse.ArgumentParser(
    description="Get schedule from the NPO Frontend API",
    epilog=Schedule.EPILOG
)
ARGS.add_argument('guideDay', type=str, nargs='?', help='The day to get')

args = ARGS.parse_args()
client = Schedule().command_line_client()

print(client.get(guideDay=args.guideDay))
