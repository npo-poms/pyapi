#!/usr/bin/env python3
"""
Simple client to post thesaurus updates to npo backend api.
"""

from npoapi import PagesBackend
from npoapi.data import NewPerson


def thesaurus():
    client = PagesBackend().command_line_client(description="Submit thesaurus object")
    client.add_argument("xml", type=str, nargs="?", help="The xml to post")
    client.add_argument("--given_name", type=str, default=None, help="Override given name")
    client.add_argument("--family_name", type=str, default=None, help="Override family name")

    args = client.parse_args()

    data = None
    if args.xml:
        data = args.xml[0]
    update = None

    if data:
        update = client.to_object_or_none(data)
    else:
        pass
        # TODO
        # update = NewPersonRequest()
        ##update.person = NewPerson()

    if args.given_name:
        update.person.givenName = args.given_name
    if args.family_name:
        update.person.familyName = args.family_name

    response = client.post_person(update)
    client.logger.info("%s", str(response))

    client.exit()


if __name__ == "__main__":
    thesaurus()
