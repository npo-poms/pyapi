#!/usr/bin/env python3
"""
  Simple client to get an page from the NPO Frontend API pages endpoint
"""
from npoapi import Pages


def pages_list():
    client = Pages().command_line_client(description="Get a pages from the NPO Frontend API")
    client.add_argument('max', type=int)

    args = client.parse_args()

    print(client.list(max = args.max))
    client.exit()


if __name__ == "__main__":
    pages_list()
