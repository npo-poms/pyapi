#!/usr/bin/env python3
"""
  Simple client to search media in the  NPO Frontend API
"""

import json

from npoapi import Media
from npoapi.utils import looks_like_form


def media_search():
    client = Media()\
        .command_line_client(description="Search from the NPO Frontend API")
    list_of_subs = ["descendants", "members", "episodes", "related", ""]
    client.add_argument('form', type=str, nargs=1, help='The search form. This may be a json string, or the name of a file containing it. If -, read from stdin')
    client.add_argument('mid', type=str, nargs='?', default=None,
                        help="Mid for use with 'sub'")
    client.add_argument('sub', type=str, nargs='?', default="", choices=list_of_subs,
                        help="Sub call for the mediaobject. On default the mediaobject itself is returned, but you can also opt for one of these choices")
    client.add_argument('-s', "--sort", type=str, default=None, choices={"asc", "desc"})
    client.add_argument('-m', "--max", type=int, default="240")
    client.add_argument('-o', "--offset", type=int, default=0)
    client.add_argument('-f', "--fuzzy", action='store_true')
    client.add_argument('-p', "--properties", type=str, default=None,
                        help="properties filtering")
    client.add_argument('-P', "--profile", type=str, default=None,
                        help="profile filtering")

    args = client.parse_args()
    mid = args.mid
    sub = args.sub
    form = args.form[0]

    if not looks_like_form(form):
        form = "{\"searches\": {\"text\": {\"value\": %s, \"fuzziness\": \"%s\" }}}" % (json.dumps(form), "AUTO" if args.fuzzy else "")
        client.logger.debug("Posting " + form)

    print(client.search(form, sort=args.sort, limit=args.max, offset=args.offset, properties=args.properties, mid=mid, sub=sub, profile=args.profile))
    client.exit()


if __name__ == "__main__":
    media_search()
