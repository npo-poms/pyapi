#!/usr/bin/env python3
"""
  Simple client to search media in the  NPO Frontend API
"""
from http.client import IncompleteRead

import json_stream

from npoapi import Media
import sys
import os

class MediaIterate:

    def raw_to_stdout(self, response, progress: bool, buffer_size: int):
        buffer = bytearray("-" * buffer_size, "ascii")
        total_count = 0
        while not response.closed:
            if  progress:
                sys.stderr.write('.')
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

    def stream_to_stdout(self, response, progress: bool, buffer_size: int, object_to_string: str):
        data = json_stream.load(response)
        mediaobjects = data['mediaobjects']
        count = 0
        for lazy_mediaobject in mediaobjects:
            count += 1
            mo = json_stream.to_standard_types(lazy_mediaobject)
            sys.stdout.write(str(eval(object_to_string)))
            sys.stdout.flush()
        response.close()


    def media_iterate(self):
        buffer_size = 10000
        client = Media()\
            .command_line_client(description="Iterate the NPO Frontend API. This is the adviced way to download all data or all data relevant to you (via profile and/or form arguments).", exclude_arguments= {"accept"})
        client.add_argument('profile', type=str, nargs='?',
                            help='The profile to search within. Can be empty string to not use a profile')
        client.add_argument('form', type=str, nargs='?',
                            help='The search form. This may be a json string, or the name of a file containing it')
        client.add_argument('-m', "--max", type=int, default="100", help="On default the size is maximized to 100, but unlike with other API calls you can set this max value arbitrary large. -1 means no maximum")
        client.add_argument("--progress", action='store_true', help="If set, some progress indication will be written to stderr (a dot for every %s bytes)" % buffer_size)
        client.add_argument('-p', "--properties", type=str, default=None,   help="properties filtering")
        client.add_argument("--object_to_string", type=str, default=None, help="dict to string for change. E.g. mo.get('mid', '') + '\n''. Or 'LINE' for str representation of the entire dict.")


        args = client.parse_args()
        form = args.form

        response = client.iterate_raw(form=form, profile=args.profile, limit=None if args.max == -1 else args.max, timeout=100, properties=args.properties)

        if args.object_to_string:
            object_to_string = args.object_to_string
            if object_to_string == "LINE":
                object_to_string = "str(mo) + '\\n'"
            if object_to_string == "MID":
                object_to_string = "str(mo['mid']) + '\\n'"
            self.stream_to_stdout(response, args.progress, buffer_size, object_to_string)
        else:
            self.raw_to_stdout(response, args.progress, buffer_size)

        client.exit()


def media_iterate():
    MediaIterate().media_iterate()


if __name__ == "__main__":
    media_iterate()

