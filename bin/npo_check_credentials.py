#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint
"""
from npoapi import Media
import argparse

ARGS = argparse.ArgumentParser(
    description="Get an media object from the NPO Frontend API",
    epilog=Media.EPILOG
)
ARGS.add_argument('apikey', type=str, nargs=1, help='key')
ARGS.add_argument('apisecret', type=str, nargs=1, help='secret')
ARGS.add_argument('origin', type=str, nargs=1, help='origin')

args = ARGS.parse_args()
client = Media(key=args.apikey[0], secret=args.apisecret[0], origin=args.origin[0]).read_environmental_variables()

print(client.get("WO_NCRV_026201"))
