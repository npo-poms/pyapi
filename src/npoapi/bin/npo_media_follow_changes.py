#!/usr/bin/env python3
"""
  Simple client to get the changes feed from the NPO Frontend API
"""
from npoapi import Media
from io import TextIOWrapper
from sys import stdout


def media_follow_changes():
    client = Media().command_line_client("Get changes feed from the NPO Frontend API", exclude_arguments={"accept"})
    client.add_argument('profile', type=str, nargs='?', help='Profile')
    client.add_argument("-s", "--since", type=str, default=None)
    client.add_argument("--no_check_profile", action="store_true")
    client.add_argument("--deletes", type=str, default="ID_ONLY")
    client.add_argument('-p', "--properties", type=str, default=None,
                        help="properties filtering")
    
    args = client.parse_args()
    
    since=""
    while True:
        response = TextIOWrapper(client.changes_raw(
               profile=args.profile,
               since=args.since,
               properties=args.properties,
               check_profile=not args.no_check_profile,
               deletes=args.deletes,
               stream=True), encoding="UTF-8")
    
        while True:
            buffer = response.read(1024)
            if len(buffer) == 0:
                break
            stdout.write(buffer)
            stdout.flush()
    
        response.close()
    
    client.exit()
