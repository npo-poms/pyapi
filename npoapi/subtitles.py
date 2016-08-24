import urllib.request

from npoapi.npoapi import NpoApi


class Subtitles(NpoApi):
    def __init__(self, key: str = None, secret: str = None, env: str = None, origin: str = None, debug: bool = False, accept: str = "text/vtt"):
        """
        Instantiates a client to the NPO Frontend API
        """
        super().__init__(env=env, debug=debug, accept=accept)
        self.key, self.secret, self.origin = key, secret, origin

    def accept_choices(self):
        return {"vtt": "text/vtt", "srt": "text/srt", "ebu": "text/ebu-tt"}


    def get(self, mid, language):
        return self.request("/api/subtitles/" + urllib.request.quote(mid, safe='') + "/"
                            + urllib.request.quote(language, safe='')) 

    def search(self, form="{}", sort="asc", offset=0, limit=240, accept=None):
        return self.request("/api/subtitles", data=form, accept=accept, params={"sort": sort, "offset": offset, "max": limit})
