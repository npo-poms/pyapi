#!/usr/bin/env python3
"""
Get a media object directly from an S3 bucket (poms-prod-input or poms-acc-input), bypassing the API.

Credentials are read from S3_ACCESS_KEY, S3_SECRET_ACCESS_KEY, and S3_REGION environment variables
or from the standard creds.properties file.
"""

import sys

from npoapi.media_s3 import MediaS3
from npoapi.utils import MID_HELP


def media_s3():
    client = MediaS3()
    client.command_line_client(description="Get a media object from S3, bypassing the API.")

    client.add_argument("mid", type=str, nargs="*", help=MID_HELP)
    client.add_argument(
        "-f", "--format",
        type=str,
        choices=["json", "xml"],
        default="json",
        help="Format to retrieve (default: json)",
    )
    client.add_argument(
        "-l", "--list",
        action="store_true",
        help="List the MIDs in the bucket instead of getting objects by MID",
    )
    client.add_argument(
        "-s", "--modified-since",
        type=str,
        default=None,
        metavar="TIMESTAMP",
        help="Only consider objects modified after this ISO-8601 date or datetime "
             "(e.g. 2026-08-01 or 2026-08-01T12:00:00+02:00). Naive values are UTC. "
             "Combines with --list, or filters the given MIDs.",
    )
    args = client.parse_args()

    if args.list:
        if args.mid:
            client.argument_parser.error("--list takes no MID arguments")
        for mid, obj in client.list_keys(
            fmt=args.format, modified_since=args.modified_since
        ):
            print(f"{obj['LastModified'].isoformat()}\t{mid}")
        return

    if not args.mid:
        client.argument_parser.error("give at least one MID, or --list")

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
