#!/usr/bin/env python3
"""
Simple client to get a schedule from the NPO Frontend API2
"""

from npoapi import Schedule


def schedule_get():
    client = Schedule().command_line_client("Get schedule from the NPO Frontend API")
    client.add_argument("guideDay", type=str, nargs="?", help="The day to get")
    client.add_argument("channel", type=str, nargs="?", help="For channel to get")
    client.add_argument("-s", "--sort", type=str, default=None, choices={"asc", "desc"})
    client.add_argument("-m", "--max", type=int, default="240")
    client.add_argument("-o", "--offset", type=int, default=0)
    client.add_argument("-p", "--properties", type=str, default=None, help="properties filtering")
    args = client.parse_args()

    print(
        client.get(
            guideDay=args.guideDay,
            channel=args.channel,
            sort=args.sort,
            limit=args.max,
            offset=args.offset,
            properties=args.properties,
        )
    )
    client.exit()
