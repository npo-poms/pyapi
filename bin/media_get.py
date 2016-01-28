#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint
"""
from npoapi.npoapi import Media
import argparse

ARGS = argparse.ArgumentParser(
    description="Get an media object from the NPO Frontend API",
    epilog="""
DEBUG=true and ENV=<dev|test|prod> environment variables are recognized.
Credentials are read from a config file. If such a file does not exist it will offer to create one.
"""
)
ARGS.add_argument('mid', type=str, nargs=1, help='The mid  of the object to get')

args = ARGS.parse_args()
client = Media().configured_login(read_environment=True, create_config_file=True)

print(client.get(args.mid[0]))
