#!/usr/bin/env python3
"""
  Simple client to get the changes feed from the NPO Frontend API
"""
import json
import time
from datetime import datetime

import json_stream

from npoapi import Media
from io import TextIOWrapper
from sys import stdout


def media_follow_changes():
    client = Media().command_line_client("Get changes feed from the NPO Frontend API", exclude_arguments={"accept"})
    client.add_argument('profile', type=str, nargs='?', help='Profile')
    client.add_argument("-s", "--since", type=str, default=None)
    client.add_argument("--sleep", type=int, default=5)
    client.add_argument("--deletes", type=str, default="ID_ONLY")
    client.add_argument('-p', "--properties", type=str, default=None,
                        help="properties filtering")

    args = client.parse_args()

    since = args.since
    if since is None:
        since = datetime.now().isoformat()
        client.logger.info("No since given, using %s" % since)

    while True:
        client.logger.info("since: %s" % since)
        response = TextIOWrapper(client.changes_raw(
               profile=args.profile,
               since=since,
               properties=args.properties,
               deletes=args.deletes,
               stream=True), encoding="UTF-8")

        data = json_stream.load(response)
        changes = data['changes']
        for change in changes.persistent():
            c = json_stream.to_standard_types(change)
            since = str(c['publishDate'])
            stdout.write(json.dumps(c))
            stdout.write("\n")
            stdout.flush()

        response.close()
        time.sleep(args.sleep)

    client.exit()


if __name__ == "__main__":
    media_follow_changes()
