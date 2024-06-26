#!/usr/bin/env python3
"""
Simple client to get an object from the NPO Frontend API media endpoint. This version accepts explicit key, secret origins.
"""

from npoapi.media import Media


def check_credentials():
    client = Media().command_line_client(
        description="Get an media object from the NPO Frontend API using provided credentials. This lets you easily "
        "check whether new credentials do work"
    )

    client.add_argument("apikey", type=str, nargs=1, help="key")
    client.add_argument("apisecret", type=str, nargs=1, help="secret")
    client.add_argument("origin", type=str, nargs=1, help="origin")
    client.add_argument("mid", type=str, nargs="?", help="mid", default="WO_NCRV_026201")

    args = client.parse_args()

    client.login(args.apikey[0], args.apisecret[0], args.origin[0])

    mid = args.mid

    print(client.get(mid))
    client.exit()


if __name__ == "__main__":
    check_credentials()
