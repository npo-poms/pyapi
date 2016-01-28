#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint
"""
import npoapi.npoapi
from npoapi import Media
import argparse

ARGS = argparse.ArgumentParser(
    description="Get an media object from the NPO Frontend API",
    epilog=npoapi.npoapi.EPILOG
)
ARGS.add_argument('profile', type=str, nargs='?', help='Profile')

args = ARGS.parse_args()
client = Media().configured_login(read_environment=True, create_config_file=True)

print(client.changes(profile=args.profile))
