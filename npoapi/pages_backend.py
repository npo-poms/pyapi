from npoapi.basic_backend import BasicBackend


class PagesBackend(BasicBackend):
    __author__ = "Michiel Meeuwissen"
    def __init__(self, env=None, email: str = None, debug=False, accept=None):
        """

        """
        super().__init__(env, email, debug, accept)

    def env(self, e):
        super().env(e)
        if e == "prod":
            self.url = "http://publish.pages.omroep.nl/"
        elif e == None or e == "test":
            self.url = "http://publish-test.pages.omroep.nl/"
        elif e == "dev":
            self.url = "http://publish-dev.pages.omroep.nl/"
        elif e == "localhost":
            self.url = "http://localhost:8068/"
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



