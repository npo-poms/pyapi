#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint. This version accepts explicit key, secret origins.
"""
from npoapi import Media
import argparse

ARGS = argparse.ArgumentParser(
    description="Get an media object from the NPO Frontend API using provided credentials. This lets you easily check whether new credentials do work"

)
ARGS.add_argument('apikey', type=str, nargs=1, help='key')
ARGS.add_argument('apisecret', type=str, nargs=1, help='secret')
ARGS.add_argument('origin', type=str, nargs=1, help='origin')
ARGS.add_argument('mid', type=str, nargs='?', help='mid', default="WO_NCRV_026201")

args = ARGS.parse_args()
client = Media(key=args.apikey[0], secret=args.apisecret[0], origin=args.origin[0]).read_environmental_variables()
mid = args.mid

print(client.get(mid))
