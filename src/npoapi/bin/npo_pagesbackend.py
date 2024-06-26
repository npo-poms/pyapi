#!/usr/bin/env python3
"""
Simple client publish to and delete pages from the NPO pages api. Using the rest interfaces at http://publish.pages.omroep.nl/api/pages/updates/
"""

from npoapi import PagesBackend
from npoapi.base import Binding


def pagesbackend():
    client = PagesBackend().command_line_client(description="Set an page object into  NPO API")
    client.add_argument("xml", type=str, nargs=1, help="The xml to post (or in case of deletes/get it may be an url)")
    client.add_argument(
        "-p",
        "--process",
        type=str,
        help="""python code to postprocess. E.g. "update.embeds.embed[0].midRef ='POMS_S_VPRO_168360'""" "",
    )
    client.add_argument(
        "-D", "--delete", action="store_true", help="""Deletes the page object. You can also only specify an URL"""
    )

    client.add_argument(
        "-B",
        "--batch_delete",
        action="store_true",
        help="""Deletes a batch of page objects. You can also only specify a base-url""",
    )
    client.add_argument(
        "-G", "--get", action="store_true", help="""Get the page object. You can also only specify an URL"""
    )

    args = client.parse_args()
    delete = args.delete or args.batch_delete
    get = args.get
    process = args.process
    data = args.xml[0]

    url = None
    update = None

    if data:
        update = client.to_object_or_none(data, binding=Binding.XSDATA)

    if update:
        if process is not None:
            exec(process)
            client.logger.debug("Execed " + process)
        url = update.url

    if delete or get:
        if update:
            url = update.url
        else:
            url = args.xml[0]

    if delete:
        result = client.delete(url, batch=args.batch_delete)
        print(str(result))
    elif get:
        string = client.get(url)
        print(string)
        update = client.to_object_or_none(string)
    else:
        if not update:
            raise Exception("No xml found")
        client.post(update)

    if update:
        print(url, list(map(lambda e: e.midRef, update.embeds.embed)) if update.embeds else "")
    elif url:
        print(url)

    client.exit()
