#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Frontend API media endpoint
"""
from npoapi import Media

from npoapi.utils import resolve_mid, MID_HELP


def media_get():
    client = Media().command_line_client(description="Get an media object from the NPO Frontend API")
    list_of_subs = ["descendants", "members", "episodes", "related", ""]
    client.add_argument('mid', type=str, nargs=1, help=MID_HELP)
    client.add_argument('sub', type=str, nargs='?', default="", choices=list_of_subs,
                      help="Sub call for the mediaobject. On default the mediaobject itself is returned, but you can also opt for one of these choices")
    client.add_argument('-s', "--sort", type=str, default=None, choices={"asc", "desc"},
                        help="sort (only relevant when using sub)")
    client.add_argument('-M', "--multiple", action='store_true',
                        help="""
    Use the 'multiple' call. This will result not one media object, but a list.
    If the argument is a comma separated list of mids or a file (e.g. ~/github/npo-poms/api/examples/media/get-multiple.json). If it is a file, the POST call is done.
    Sub calls and the sort option are ignored.
    """)
    client.add_argument('-p', "--properties", type=str, default=None,
                        help="properties filtering")
    client.add_argument('-m', "--max", type=int, default=None,
                        help="max (only relevant when using sub)")
    client.add_argument('-o', "--offset", type=int, default=None,
                        help="offset (only relevant when using sub)")
    client.add_argument('-P', "--profile", type=str, default=None,
                        help="profile filtering")

    args = client.parse_args()

    mid = resolve_mid(args.mid[0])


    if args.multiple:
        print(client.multiple(mid, properties=args.properties, profile=args.profile))
    else:
        print(client.get(mid,
                         sub="" if args.sub == "" else "/" + args.sub,
                         properties=args.properties,
                         sort=args.sort,
                         limit=args.max,
                         offset=args.offset,
                         profile=args.profile

        ))

    client.exit()


if __name__ == "__main__":
    media_get()
