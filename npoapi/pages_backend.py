from npoapi.basic_backend import BasicBackend


class PagesBackend(BasicBackend):
    __author__ = "Michiel Meeuwissen"

    def __init__(self, env=None, email: str = None, debug=False, accept=None):
        """

        """
        super().__init__(env, email, debug, accept)
        self.authorizationHeader = None
        self.thesaurusUser = None
        self.thesaurusSecret = None


    def env(self, e):
        super().env(e)
        if e == "prod":
            self.url = "https://publish.pages.omroep.nl/"
        elif e == None or e == "test":
            self.url = "https://publish-test.pages.omroep.nl/"
        elif e == "dev":
            self.url = "https://publish-dev.pages.omroep.nl/"
        elif e == "localhost":
            self.url = "http://localhost:8069/"
        else:
            self.url = e
        return self

    def post(self, update):
        return self.post_to("api/pages/updates", update, accept="text/plain")

    def delete(self, url):
        return self.delete_from("api/pages/updates", url=url, accept="application/json")

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



