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


    def create_config(self):
        """
        """
        super().create_config()
        self.create_thesaurus_config()
        return self

    def create_thesaurus_config(self, settings, ):
        settings['thesaurus_user'] = input("Your Thesaurus user?: ")
        settings['thesaurus_secret'] = input("Your Thesaurus secret?: ")


    def read_settings(self):
        """
        """
        super().read_settings()
        settings = self.settings
        if not ('thesaurus_user' in settings):
            self.logger.info("No thesaurus accounts found in settings")
            self.create_thesaurus_config(settings)
            self._write_settings(settings)
        self.thesaurusUser = settings['thesaurus_user']
        self.thesaurusSecret = settings['thesaurus_secret']
        return

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
        return self.delete_from("api/pages/updates", url=url)

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
            "iss": self.thesaurusUser},
            self.thesaurusSecret,
            algorithm='HS256'
        ).decode("utf-8")
        return self.post_to("api/thesaurus/person", new_person)



