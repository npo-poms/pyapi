#!/usr/bin/env python3
"""
  Simple client to get the changes feed from the NPO Frontend API
"""
import json
import logging
import time
from datetime import datetime
from sys import stdout

import json_stream

from npoapi import Media


class FollowChanges:
    def __init__(self):
        self.client = Media().command_line_client("Get changes feed from the NPO Frontend API", exclude_arguments={"accept"})
        self.client.add_argument('profile', type=str, nargs='?', help='Profile')
        self.client.add_argument("-s", "--since", type=str, default=None)
        self.client.add_argument("--sleep", type=int, default=5)
        self.client.add_argument("--deletes", type=str, default="ID_ONLY")
        self.client.add_argument("--tail", action='store_true')
        self.client.add_argument('-p', "--properties", type=str, default=None,
                        help="properties filtering")
        self.client.add_argument("--raw", action='store_true', description="No attempts to stream and handle big results. Everything should fit in memory. Simpler, but less efficient.")
        self.client.add_argument("--reasonFilter", type=str, default="")

        self.args = self.client.parse_args()

        self.since = self.args.since
        if self.since is None:
            self.since = datetime.now().isoformat()
        self.client.logger.info("No since given, using %s" % self.since)

        self.sinceAsEpoch = int(datetime.fromisoformat(self.since).timestamp() * 1000) - 60000

    def one_call_raw(self):
        response = self.client.changes_raw(
            profile=self.args.profile,
            since=self.sinceAsEpoch,
            properties=self.args.properties,
            deletes=self.args.deletes,
            reason_filter=self.args.reasonFilter,
            stream=False)
        self.sinceAsEpoch = json.loads(response)['changes'][0]['publishDate']
        stdout.write(response)

    def one_call(self):
        response = self.client.changes_raw(
            profile=self.args.profile,
            since=self.sinceAsEpoch,
            properties=self.args.properties,
            deletes=self.args.deletes,
            reason_filter=self.args.reasonFilter,
            stream=True)

        if response.status != 200:
            logging.error("Error %d" % response.status)
            return
        data = json_stream.load(response)
        changes = data['changes']
        newsince = None
        count = 0
        for change in changes:
            count += 1
            c = json_stream.to_standard_types(change)
            newsince = c.get('publishDate')
            if not newsince:
                logging.error("No publishDate in %s" % c)
                break
            tail = c.get('tail', False)
            if not tail or self.args.tail:
                stdout.write(json.dumps(c))
                stdout.write("\n")
            stdout.flush()
        if count == 0:
            raise Exception("No changes received!")
        if newsince is None:
            raise Exception("No tail received?")
        if newsince <= self.sinceAsEpoch:
            raise Exception("Since doesn't grow")
        self.sinceAsEpoch = newsince
        changes.read_all()
        response.close()
        time.sleep(self.args.sleep)

    def follow_changes(self):
        try:
            while True:
                self.client.logger.info("since: %s (%s)" % (self.sinceAsEpoch, datetime.fromtimestamp(self.sinceAsEpoch/1000).isoformat()))
                if self.args.raw:
                    self.one_call_raw()
                else:
                    self.one_call()
        except KeyboardInterrupt:
            self.client.logger.info("interrupted")

        self.client.exit()


def media_follow_changes():
    FollowChanges().follow_changes()


if __name__ == "__main__":
    media_follow_changes()
