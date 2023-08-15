#!/usr/bin/env python3
"""
  Simple client to get an object from the NPO Backend API media endpoint. You can also call the DELETE endpoint.
"""
from npoapi import MediaBackend

from npoapi.utils import resolve_mid, MID_HELP


def mediabackend_get():
    client = MediaBackend().command_line_client(description="Get an media object from the NPO Backend API", exclude_arguments=["accept"])
    
    list_of_subs = ["members", "episodes", "images", "locations", "full", "subtitles", "memberOfs", "episodeOfs", "predictions", "predictions/INTERNETVOD", "predictions/TVVOD", "predictions/PLUSVOD", ""]
    
    client.add_argument('mid', type=str, nargs=1, help=MID_HELP)
    client.add_argument('sub', type=str, nargs='?', default="", choices=list_of_subs,
                        help="Sub call for the mediaobject. On default the mediaobject itself is returned, but you can also opt for one of these choices")
    
    client.add_argument('-p', '--process',  type=str, help="""python code to postprocess. E.g. "update.duration='PT5M'""""")
    
    client.add_argument('--nofollowMerges',   action='store_true',  help="""implicitely follow merges""")
    client.add_argument('--deletes',   action='store_true',  help="""find deleted objects too""")
    client.add_argument('-D', '--delete', action='store_true',
                        help="""The mid is deleted""")
    
    client.add_argument('-F', '--full', action='store_true', help="""full xml version""")
    
    args = client.parse_args()
    process = args.process
    sub=args.sub
    mid = resolve_mid(args.mid[0])
    
    def get():
        nonlocal sub
        if sub == "subtitles":
            return client.subtitles(mid)
        elif sub == 'members' or sub == 'episodes':
            return client.members_or_episodes(mid, sub, full=args.full, follow_merges=not args.nofollowMerges, deletes=args.deletes)
        else:
            if args.full and sub == "":
                sub = "full"
            return client.get_sub(mid, sub, follow_merges=not args.nofollowMerges, deletes=args.deletes)
    
    
    if not args.delete or process:
        result = get()
    else:
        result = None
    
    if args.delete:
        client.delete(resolve_mid(mid))
    
    if type(result) == list:
        strings = map(lambda o:
                      o.toprettyxml(), result)
        for s in strings:
            print(s)
    elif result is not None:
        if process is None:
            print(client.pretty_xml(result))
        else:
            from npoapi.xml import poms
            update = poms.CreateFromDocument(result)
            exec(process)
            print(update.toDOM().toprettyxml(indent="  "))
    
    
    client.exit()
    

if __name__ == "__main__":
    mediabackend_get()

