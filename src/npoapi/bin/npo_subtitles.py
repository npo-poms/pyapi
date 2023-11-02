#!/usr/bin/env python3
"""

"""
from npoapi import Subtitles
import os
import json


def subtitles():
    client = Subtitles().command_line_client(description="Set subtitles")
    client.add_argument('mid|text', type=str, nargs=1, help='The mid for wich subtitles to get. Or form description')
    client.add_argument('-S', '--search', action='store_true',
                        help="""The argument is interpreted as a text to search on""")
    client.add_argument('language', type=str, nargs='?', default="nl", help='Language. Required when getting mid')
    client.add_argument('type', type=str, nargs='?', default="CAPTION", help='', choices={"CAPTION", "TRANSLATION"})

    args = client.parse_args()
    mid_or_text = vars(args)['mid|text'][0]
    language = args.language
    search = args.search

    if search:
        form = mid_or_text
        if not os.path.isfile(form) and not form.startswith("{") and not form.startswith("<"):
            form = "{\"searches\": {\"text\": %s}}" % json.dumps(form)

        print(client.search(form))
    else:
        mid = mid_or_text
        print(client.get(mid, language, subtitle_type=args.type))

    client.exit()


if __name__ == "__main__":
    subtitles()
