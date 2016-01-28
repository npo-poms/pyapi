#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint
"""
from npoapi import Media
import argparse

ARGS = argparse.ArgumentParser(
    description="Get changes feed from the NPO Frontend API",
    epilog=Media.EPILOG
)
ARGS.add_argument('profile', type=str, nargs='?', help='Profile')

args = ARGS.parse_args()
client = Media().configured_login(read_environment=True, create_config_file=True)

print(client.changes(profile=args.profile))
