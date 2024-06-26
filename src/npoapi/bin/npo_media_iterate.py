#!/usr/bin/env python3
"""
Simple client to search media in the  NPO Frontend API
"""

import os
import sys
from http.client import IncompleteRead
from typing import Callable

import json_stream

from npoapi import Media


class MediaIterate:
    @staticmethod
    def raw_to_stdout(response, progress: bool, buffer_size: int):
        buffer = bytearray("-" * buffer_size, "ascii")
        total_count = 0
        while not response.closed:
            if progress:
                sys.stderr.write(".")
                sys.stderr.flush()
            try:
                number_of_bytes_read = response.readinto(buffer)
            except IncompleteRead as e:
                number_of_bytes_read = len(e.partial)

            os.write(sys.stdout.fileno(), buffer[0:number_of_bytes_read])
            sys.stdout.flush()
            total_count += number_of_bytes_read
            if number_of_bytes_read < buffer_size:
                response.close()
                break
        if progress:
            sys.stderr.write("\n%d byte written\n" % total_count)

    @staticmethod
    def stream_to_stdout(response, progress: bool, buffer_size: int, object_to_string: Callable[[dict, int], str]):
        data = json_stream.load(response)
        mediaobjects = data["mediaobjects"]
        count = 0
        for lazy_mediaobject in mediaobjects:
            count += 1
            mo = json_stream.to_standard_types(lazy_mediaobject)
            sys.stdout.write(object_to_string(mo, count) + "\n")
            sys.stdout.flush()
        response.close()

    magical_values = {
        "LINE": "lambda mo: str(mo)",
        "MID": "lambda mo, count: str(count) + ':' + str(mo['mid'])",
        "TITLE": "lambda mo, count: str(count) + ':' + str(mo['mid']) + mo['titles'][0]['value']",
    }

    def media_iterate(self):
        buffer_size = 10000
        client = Media().command_line_client(
            description="Iterate the NPO Frontend API. This is the adviced way to download all data or all data relevant to you (via profile and/or form arguments).",
            exclude_arguments={"accept"},
        )
        client.add_argument(
            "profile",
            type=str,
            nargs="?",
            help="The profile to search within. Can be empty string to not use a profile",
        )
        client.add_argument(
            "form",
            type=str,
            nargs="?",
            help="The search form. This may be a json string, or the name of a file containing it",
        )
        client.add_argument(
            "-m",
            "--max",
            type=int,
            default="100",
            help="On default the size is maximized to 100, but unlike with other API calls you can set this max value arbitrary large. -1 means no maximum",
        )
        client.add_argument(
            "--progress",
            action="store_true",
            help="If set, some progress indication will be written to stderr (a dot for every %s bytes)" % buffer_size,
        )
        client.add_argument("-p", "--properties", type=str, default=None, help="properties filtering")
        client.add_argument(
            "--object_to_string",
            type=str,
            default=None,
            help="""
        A lambda receiving a dict and a count. Should produce a string. E.g. lambda mo: mo.get('mid', '').

        A few magical values are supported:
        %s
          """
            % ("\n".join(list(map(lambda item: item[0] + ":" + item[1], self.magical_values.items())))),
        )

        args = client.parse_args()
        form = args.form

        response = client.iterate_raw(
            form=form,
            profile=args.profile,
            limit=None if args.max == -1 else args.max,
            timeout=100,
            properties=args.properties,
        )

        if args.object_to_string:
            object_to_string = args.object_to_string
            if object_to_string in self.magical_values:
                object_to_string = self.magical_values[object_to_string]

            try:
                to_string = eval(object_to_string)
            except NameError as e:
                to_string = lambda mo, count: eval(object_to_string)
            if not callable(to_string):
                to_string = lambda mo, count: eval(object_to_string)

            if to_string.__code__.co_argcount < 2:
                l = lambda mo, count: to_string(mo)
            else:
                l = to_string
            self.stream_to_stdout(response, args.progress, buffer_size, l)
        else:
            self.raw_to_stdout(response, args.progress, buffer_size)

        client.exit()


def media_iterate():
    MediaIterate().media_iterate()


if __name__ == "__main__":
    media_iterate()
