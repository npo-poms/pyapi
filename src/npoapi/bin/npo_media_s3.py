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
        choices=["prod", "acc", "test"],
        default="prod",
        help="Environment / bucket to use: prod=poms-prod-input, acc=poms-acc-input (default: prod)",
    )
    parser.add_argument("mid", type=str, nargs="*", help=MID_HELP)
    parser.add_argument(
        "-f", "--format",
        type=str,
        choices=["json", "xml"],
        default="json",
        help="Format to retrieve (default: json)",
    )
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List the MIDs in the bucket instead of getting objects by MID",
    )
    parser.add_argument(
        "-s", "--modified-since",
        type=str,
        default=None,
        metavar="TIMESTAMP",
        help="Only consider objects modified after this ISO-8601 date or datetime "
             "(e.g. 2026-08-01 or 2026-08-01T12:00:00+02:00). Naive values are UTC. "
             "Combines with --list, or filters the given MIDs.",
    )
    args = parser.parse_args()

    client = MediaS3(env=args.env)

    if args.list:
        if args.mid:
            parser.error("--list takes no MID arguments")
        for mid, obj in client.list_keys(
            fmt=args.format, modified_since=args.modified_since
        ):
            print(f"{obj['LastModified'].isoformat()}\t{mid}")
        return

    if not args.mid:
        parser.error("give at least one MID, or --list")

    for mid in args.mid:
        result = client.get(mid, fmt=args.format, modified_since=args.modified_since)
        if result is None:
            if args.modified_since:
                print(f"Not found or not modified: {mid}", file=sys.stderr)
            else:
                print(f"Not found: {mid}", file=sys.stderr)
        else:
            print(result)


if __name__ == "__main__":
    media_s3()
