#!/usr/bin/env python3
"""
  Simple client to get the changes feed from the NPO Frontend API
"""
from datetime import datetime, time
from io import TextIOWrapper
from sys import stdout
from isoduration import parse_duration
import pytz

from npoapi import Media
    
def media_changes():    
    client = Media().command_line_client("Get changes feed from the NPO Frontend API", exclude_arguments={"accept"})
    client.add_argument('profile', type=str, nargs='?', help='Profile')
    client.add_argument("-s", "--since", type=str, default=None, help="The since date. As millis since epoch, ISO date format, or ISO duration format (which will substracted from the current time)")
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
    since = args.since
    if since and since.startswith("P"):
        duration = parse_duration(since)
        since = datetime.now().astimezone() - duration
        
        client.logger.info("Parsed duration " + str(duration) + " to " + str(since))

        
    response = TextIOWrapper(client.changes_raw(
        profile=args.profile,
        since=since,
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

if __name__ == "__main__":
    media_changes()