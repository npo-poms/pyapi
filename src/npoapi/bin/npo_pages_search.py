#!/usr/bin/env python3
"""
Simple client to search media in the  NPO Frontend API
"""

import json

from npoapi import Pages
from npoapi.utils import looks_like_form


def pages_search():
    client = Pages().command_line_client(description="Search from the NPO Frontend API")
    client.add_argument(
        "form",
        type=str,
        nargs=1,
        help="The search form. This may be a json string, or the name of a file containing it. It can also be XML, or a string to search on",
    )
    client.add_argument("-s", "--sort", type=str, default=None, choices={"asc", "desc"})
    client.add_argument("-m", "--max", type=int, default="240")
    client.add_argument("-o", "--offset", type=int, default=0)
    client.add_argument(
        "--mids",
        action="store_true",
        help="Interpret the form argument as a list of mids. Search pages with these mids embedded",
    )
    client.add_argument("--urlprefix", action="store_true", help="")
    client.add_argument("-P", "--profile", type=str, default=None, help="profile filtering")
    client.add_argument("-p", "--properties", type=str, default=None, help="properties filtering")

    args = client.parse_args()

    form = args.form[0]
    if not looks_like_form(form):
        if args.mids:
            form = '{"mediaForm": { "searches": {"mediaIds": %s}}}' % (json.dumps(form.split(",")))
        else:
            form = '{"searches": {"text": %s}}' % json.dumps(form)

    print(
        client.search(
            form, sort=args.sort, limit=args.max, offset=args.offset, profile=args.profile, properties=args.properties
        )
    )
    client.exit()
