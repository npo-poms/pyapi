#!/usr/bin/env python3
"""
  Simple client to search media in the  NPO Frontend API
"""
from http.client import IncompleteRead

from npoapi import Pages
import sys
import os
import json_stream



def pages_iterate():
    client = Pages()\
        .command_line_client(description="Iterate the NPO Frontend API. This is the adviced way to download all data or all data relevant to you (via profile and/or form arguments).", exclude_arguments= {"accept"})
    client.add_argument('profile', type=str, nargs='?',
                        help='The profile to search within. Can be empty string to not use a profile')
    client.add_argument('form', type=str, nargs='?',
                        help='The search form. This may be a json string, or the name of a file containing it')
    client.add_argument('-m', "--max", type=int, default="100", help="On default the size is maximized to 100, but unlike with other API calls you can set this max value arbitrary large.")
    client.add_argument("--progress", action='store_true', help="If set to true, some progress indication will be written to stderr")
    client.add_argument('-p', "--properties", type=str, default=None,   help="properties filtering")
    client.add_argument("--object_to_string", type=str, default="CONCISE", help="dict to string for change. E.g. 'change.get('id', '') + title(change). Or 'CONCISE' for a default concise string.")
    client.add_argument("--output_size", type=int, default=None,   help="If this is used, the 'output' parameter must contain a '%d', and every file will contain an array with this many media objects. Defaults to 1000 if output contains a '%d'")

    args = client.parse_args()
    form = args.form
    if not form:
        form = """{
          "sort" : {
              "creationDate" : "ASC"
        }}
        """

    response = client.iterate_raw(profile=args.profile, form=form, limit=args.max, properties=args.properties, timeout=100)

    if args.output:
        if  "%d" in args.output:
            if args.output_size:
                output_size = args.output_size
            else:
                output_size = 1000


        output = args.output % 0
        output_count = 0
        output_file = open(output, "w")
        output_file.write("[")

    buffer_size = 1000
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
