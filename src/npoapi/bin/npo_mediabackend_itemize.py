#!/usr/bin/env python3
"""
Simple client to get an object from the NPO Backend API media endpoint
"""

from npoapi import MediaBackend

from npoapi.data.mediaupdate import Itemize


def mediabackend_itemize():
    client = MediaBackend().command_line_client(description="Upload and transcode a file")
    client.add_argument("mid", type=str, help="The mid")
    client.add_argument("start", type=str, help="start")
    client.add_argument("stop", type=str, help="stop")

    args = client.parse_args()
    mid, start, stop = args.mid, args.start, args.stop
    itemize = Itemize()
    itemize.mid = mid
    itemize.start = start
    itemize.stop = stop
    response = client.itemize(mid, itemize)
    print(response)


if __name__ == "__main__":
    mediabackend_itemize()
