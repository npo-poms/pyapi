#!/usr/bin/env python3
"""
  Simple client to get the changes feed from the NPO Frontend API
"""
import json
import logging
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
    client.add_argument("--tail", action='store_true')
    client.add_argument('-p', "--properties", type=str, default=None,
                        help="properties filtering")

    args = client.parse_args()

    since = args.since
    if since is None:
        since = datetime.now().isoformat()
        client.logger.info("No since given, using %s" % since)

    sinceAsEpoch = int(datetime.fromisoformat(since).timestamp() * 1000) - 60000

    try:
        while True:
            client.logger.info("since: %s (%s)" % (sinceAsEpoch, datetime.fromtimestamp(sinceAsEpoch/1000).isoformat()))
            response = client.changes_raw(
                   profile=args.profile,
                   since=sinceAsEpoch,
                   properties=args.properties,
                   deletes=args.deletes,
                   stream=True)

            if response.status != 200:
                logging.error("Error %d" % response.status)
                continue
            data = json_stream.load(response)
            changes = data['changes']
            newsince = None
            for change in changes.persistent():
                c = json_stream.to_standard_types(change)
                newsince = c.get('publishDate')
                if not newsince:
                    logging.error("No publishDate in %s" % c)
                    break
                tail = c.get('tail', False)
                if not tail or args.tail:
                    stdout.write(json.dumps(c))
                    stdout.write("\n")
                stdout.flush()
            if newsince is None:
                raise Exception("No tail received?")
            if newsince <= sinceAsEpoch:
                raise Exception("Since doesn't grow")
            sinceAsEpoch = newsince
            changes.read_all()
            response.close()
            time.sleep(args.sleep)
    except KeyboardInterrupt:
        client.logger.info("interrupted")

    client.exit()


if __name__ == "__main__":
    media_follow_changes()
