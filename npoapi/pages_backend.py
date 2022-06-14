from typing import Optional

from npoapi.basic_backend import BasicBackend

import json


class PagesBackend(BasicBackend):

    __author__ = "Michiel Meeuwissen"

    def __init__(self, env=None, email: str = None, debug=False, accept=None):
        """
        Instantiates a client to the NPO Pages Publisher API
        """
        super().__init__("Pages Backend", env, email, debug, accept)
        self.env(env)
        self.authorizationHeader = None
        self.thesaurusUser = None
        self.thesaurusSecret = None

    def env(self, e):
        super().env(e)
        if e == "prod":
            self.url = "https://publish.pages.omroep.nl/"
        elif e == "prod_new":
            self.url = "https://publish-os.pages.omroep.nl/"
        elif e is None or e == "test":
            self.url = "https://publish-test.pages.omroep.nl/"
        elif e == "test_new":
            self.url = "https://publish-test-os.pages.omroep.nl/"
        elif e == "acc":
            self.url = "https://publish-acc.pages.omroep.nl/"
        elif e == "localhost":
            self.url = "http://localhost:8069/"
        else:
            if e is None:
                self.logger("Using url for implicit environment % ", self.actualenv)
                self.env(self.actualenv)
            else:
                self.url = e
        return self

    def post(self, update):
        return self.post_to("api/pages/updates", update, accept="text/plain", include_errors=False)

    def delete(self, url, batch: bool = False) -> Optional[dict]:
        result = self.delete_from("api/pages/updates", url=url, batch=batch, accept="application/json", include_errors=False)
        if result is None:
            return None
        else:
            return json.loads(result)

    def get(self, url):
        return self.get_from("api/pages/updates", url=url)

    def get_users(self):
        return ["pages_user", "user"]

    def post_person(self, new_person):
        import jwt
        import datetime
        new_person.jws = jwt.encode(
            {'subject': 'GTAAPerson',
            "usr": "",
            "iat": datetime.datetime.now(),
            "iss": self.get_setting("thesaurus_user", "Your Thesaurus user")
            },
            self.get_setting("thesaurus_secret", "Your Thesaurus secret"),
            algorithm='HS256'
        ).decode("utf-8")
        return self.post_to("api/thesaurus/person", new_person)

    def __str__(self):
        return "pages backend api for " + str(self.url)



