#!/usr/bin/env python3
"""
Get a media object directly from an S3 bucket (poms-prod-input or poms-acc-input), bypassing the API.

Credentials are read from S3_ACCESS_KEY, S3_SECRET_ACCESS_KEY, and S3_REGION environment variables
or from the standard creds.properties file.
"""

import argparse
import sys

from npoapi.media_s3 import MediaS3
from npoapi.utils import MID_HELP


def media_s3():
    parser = argparse.ArgumentParser(
        description="Get a media object from S3, bypassing the API."
    )
    parser.add_argument(
        "-e", "--env",
        type=str,
        choices=["prod", "acc"],
        default="prod",
        help="Environment / bucket to use: prod=poms-prod-input, acc=poms-acc-input (default: prod)",
    )
    parser.add_argument("mid", type=str, nargs="+", help=MID_HELP)
    parser.add_argument(
        "-f", "--format",
        type=str,
        choices=["json", "xml"],
        default="json",
        help="Format to retrieve (default: json)",
    )
    args = parser.parse_args()

    client = MediaS3(env=args.env)

    for mid in args.mid:
        result = client.get(mid, fmt=args.format)
        if result is None:
            print(f"Not found: {mid}", file=sys.stderr)
        else:
            print(result)


if __name__ == "__main__":
    media_s3()
