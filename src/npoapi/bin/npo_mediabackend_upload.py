#!/usr/bin/env python3
"""
Simple client to get an object from the NPO Backend API media endpoint
"""

from npoapi import MediaBackend

def mediabackend_upload():
    client = MediaBackend().command_line_client(description="Upload and transcode a file")
    client.add_argument("mid", type=str, nargs="?", help="The mid")
    client.add_argument("file", type=str, nargs="?", help="The file")

    args = client.parse_args()
    mid, file = args.mid, args.file

    client.upload(
        mid=mid,
        file=file
    )



if __name__ == "__main__":
    mediabackend_upload()
