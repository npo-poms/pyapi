#!/usr/bin/env python3
"""
Simple client to search media in the  NPO Frontend API
"""

import json
import os

from npoapi import Schedule


def schedule_search():
    client = Schedule().command_line_client(description="Search from the NPO Frontend API")
    client.add_argument(
        "form",
        type=str,
        nargs=1,
        help="The search form. This may be a json string, or the name of a file containing it",
    )
    client.add_argument("-m", "--max", type=int, default="240")
    client.add_argument("-o", "--offset", type=int, default=0)
    client.add_argument("-p", "--properties", type=str, default=None, help="properties filtering")
    client.add_argument("-P", "--profile", type=str, default=None, help="profile filtering")

    args = client.parse_args()
    form = args.form[0]

    if not os.path.isfile(form) and not form.startswith("{") and not form.startswith("<"):
        form = '{"searches": {"text": %s}}' % json.dumps(form)

    print(
        client.search(
            form, sort="asc", limit=args.max, offset=args.offset, properties=args.properties, profile=args.profile
        )
    )
    client.exit()
