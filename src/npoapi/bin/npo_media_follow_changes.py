#!/usr/bin/env python3
"""
  Simple client to get the changes feed from the NPO Frontend API
"""
import http
import json
import logging
import os
import time
from datetime import datetime
from sys import stdout
from typing import final, Final

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
        self.client.add_argument("--raw", action='store_true', help="No attempts to stream and handle big results. Everything should fit in memory. Simpler, but less efficient.")
        self.client.add_argument("--reasonFilter", type=str, default="")
        self.client.add_argument("--change_to_string", type=str, help="dict to string for change. E.g. 'change.get('id', '') + title(change). Or 'CONCISE' for a default concise string.")

        self.args = self.client.parse_args()

        since = self.args.since
        self.since_file = None
        if since is None:
            since = "./since." + self.client.actualenv
            self.client.logger.info("No since given, using %s" % os.path.abspath(since))
        if since.startswith(".") or os.path.exists(since):
            self.since_file = since
            # default
            since = str(int(datetime.now().timestamp() * 1000))

        if self.since_file and os.path.exists(self.since_file):
            self.since = json.loads(open(self.since_file, "r").read().strip())
            self.client.logger.info("Using since %s from %s" % (self.since, self.since_file))
        else:
            self.since = {
            }
            if since.isdigit():
                self.since['timestamp'] = int(since)
            else:
                self.since['timestamp'] = int(datetime.fromisoformat(since).timestamp() * 1000) - 60000
            self.since['mid'] = None
            self.safe_since()
        self.check_grow = False
        if self.args.change_to_string == "CONCISE":
            self.change_to_string_function = "timestamp_to_string(change.get('publishDate')) + ':' + change.get('id', '') + ':' + title(change) + ':' + reasons(change)"
            self.client.logger.info("Using to string: %s" % self.change_to_string_function)
        else:
            self.change_to_string_function = self.args.change_to_string


    def change_to_string(self, change):
        if self.args.change_to_string:
            def timestamp_to_string(timestamp):
                return self.timestamp_to_string(timestamp)
            def title(change):
                return self.title(change)
            def reasons(change):
                ar = change.get('reasons', [])
                if len(ar) == 0:
                    self.client.debug("No reasons in %s" % change)
                    return "<no reasons>"
                return ",".join(list(map(lambda r:  r['value'], ar)))
            return str(eval(self.change_to_string_function))
        else:
            return json.dumps(change)

    def title(self, change):
        """
        helpful in change_to_string
        """
        tail = change.get("tail", False)
        if tail:
            return "TAIL"
        delete = change.get("delete", False)
        if delete:
            return "DELETE"
        media = change.get('media')

        if media:
            return media['titles'][0]['value']
        else:
            return "<no media>"

    def timestamp_to_string(self, timestamp):
        return datetime.fromtimestamp(timestamp/1000).isoformat()

    def set_since(self, timestamp, mid):
        self.since['timestamp'] = timestamp
        self.since['mid'] = mid
        self.safe_since()

    def safe_since(self):
        if self.since_file:
            open(self.since_file, "w").write(json.dumps(self.since))


    def one_call_raw(self):
        response = self.client.changes_raw(
            profile=self.args.profile,
            since=self.since['timestamp'],
            since_mid = self.since['mid'],
            properties=self.args.properties,
            deletes=self.args.deletes,
            reason_filter=self.args.reasonFilter,
            stream=False)
        changes = json.loads(response)['changes']
        last_change = changes[-1]

        self.set_since(last_change['publishDate'], last_change['id'])
        for change in changes:
            is_tail = change.get('tail', False)
            if not is_tail or self.args.tail:
                stdout.write(self.change_to_string(change) + "\n")

    def one_call(self):
        response = self.client.changes_raw(
            profile=self.args.profile,
            since=self.since['timestamp'],
            since_mid = self.since['mid'],
            properties=self.args.properties,
            deletes=self.args.deletes,
            reason_filter=self.args.reasonFilter,
            stream=True)

        if response is None:
            self.client.logger.debug("No response")
            return
        if response.status != 200:
            self.client.logger.error("Error %d" % response.status)
            return
        data = json_stream.load(response)
        changes = data['changes']
        new_since = None
        count = 0
        for lazy_change in changes:
            count += 1
            c = json_stream.to_standard_types(lazy_change)
            new_since = c.get('publishDate')
            self.set_since(new_since, c.get('id', None))
            if not new_since:
                logging.error("No publishDate in %s" % c)
                break
            is_tail = c.get('tail', False)
            if not is_tail or self.args.tail:
                stdout.write(self.change_to_string(c) + "\n")
            stdout.flush()
        if count == 0:
            raise Exception("No changes received!")
        if new_since is None:
            raise Exception("No tail received?")
        if self.check_grow and new_since < self.since['timestamp']:
            raise Exception("Since doesn't grow (%s < %s)" % (new_since, self.since))
        self.check_grow = True
        changes.read_all()
        response.close()

    def follow_changes(self):
        self.client.logger.info("Watching %s " % (self.client.url))
        while True:
            try:
                self.client.logger.debug("since: %s,%s (%s)" % (self.since, self.since['timestamp'], self.timestamp_to_string(self.since['timestamp'])))
                if self.args.raw:
                    self.one_call_raw()
                else:
                    self.one_call()
                time.sleep(self.args.sleep)
            except KeyboardInterrupt:
                self.client.logger.info("interrupted")
                break
            except Exception as e:
                self.client.logger.warn("Exception %s" % str(e))

        self.client.exit()


def media_follow_changes():
    FollowChanges().follow_changes()


if __name__ == "__main__":
    media_follow_changes()
