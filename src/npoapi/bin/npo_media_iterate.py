#!/usr/bin/env python3
"""
  Simple client to search media in the  NPO Frontend API
"""
from http.client import IncompleteRead

from npoapi import Media
import sys
import os


def media_iterate():
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

    args = client.parse_args()
    form = args.form

    response = client.iterate_raw(form=form, profile=args.profile, limit=None if args.max == -1 else args.max, timeout=100, properties=args.properties)

    buffer = bytearray("-" * buffer_size, "ascii")
    total_count = 0
    while not response.closed:
        if  args.progress:
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
    if args.progress:
        sys.stderr.write("\n%d byte written\n" % total_count)
    client.exit()


if __name__ == "__main__":
    media_iterate()
