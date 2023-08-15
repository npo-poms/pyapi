#!/usr/bin/env python3
"""
  Simple client to get the changes feed from the NPO Frontend API
"""
from io import TextIOWrapper
from sys import stdout

from npoapi import Media
    
def media_changes():    
    client = Media().command_line_client("Get changes feed from the NPO Frontend API", exclude_arguments={"accept"})
    client.add_argument('profile', type=str, nargs='?', help='Profile')
    client.add_argument("-s", "--since", type=str, default=None)
    client.add_argument('-m', "--max", type=int, default="100", help="The maximal number of changes to return. If not specified 100 will be filled as parameter. If set to -1, no max parameter will be used (which is unbounded).")
    client.add_argument("--backwards", action="store_true")
    client.add_argument("--deletes", type=str, default="ID_ONLY", choices=("ID_ONLY", "EXCLUDE", "INCLUDE"))
    client.add_argument("--order", type=str, default=None, choices=("ASC", "DESC"))
    client.add_argument("--tail", type=str, default=None,  choices=("ALWAYS", "IF_EMPTY", "NEVER"))
    client.add_argument('-p', "--properties", type=str, default=None,
                        help="properties filtering")
    client.add_argument("--reason_filter", type=str, default=None)
    client.add_argument("--buffer_size", type=int, default="1000")
    
    args = client.parse_args()
    response = TextIOWrapper(client.changes_raw(
        profile=args.profile,
        since=args.since,
        limit=None if args.max == -1 else args.max,
        force_oldstyle=args.backwards,
        properties=args.properties,
        deletes=args.deletes,
        tail=args.tail,
        order=args.order,
        stream=True,
        reason_filter=args.reason_filter), encoding="UTF-8")
    
    bufsize=args.buffer_size
    buffer = response.read(bufsize)
    count = 0
    while len(buffer) > 0:
        stdout.write(buffer)
        stdout.flush()
        buffer = response.read(bufsize)
        count += 1
    
    response.close()
    stdout.flush()
    client.exit()
    #time.sleep(300)