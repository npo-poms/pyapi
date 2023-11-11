from typing import Optional

from typing_extensions import override

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
        elif e is None or e == "test":
            self.url = "https://publish-test.pages.omroep.nl/"
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

    def post(self, update) -> str:
        return self.post_to("api/pages/updates", update, accept="text/plain", include_errors=False)[0]

    def delete(self, url, batch: bool = False) -> Optional[dict]:
        result, type = self.delete_from("api/pages/updates", url=url, batch=batch, include_errors=False)
        if result is None:
            return None
        elif type == 'application/json':
            return json.loads(result)
        else:
            return result

    def get(self, url) -> str:
        return self.get_from("api/pages/updates", url=url)[0]

    def get_users(self):
        return ["pages_user", "user"]

    def post_person(self, new_person) -> str:
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
        return self.post_to("api/thesaurus/person", new_person)[0]

    @override
    def __str__(self) -> str:
        return super().__str__() + " (pages)"


