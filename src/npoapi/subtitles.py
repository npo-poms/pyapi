import urllib.request
from typing import Optional

from npoapi.npoapi import NpoApi


class Subtitles(NpoApi):
    def __init__(
        self,
        key: str = None,
        secret: str = None,
        env: str = None,
        origin: str = None,
        debug: bool = False,
        accept: str = "text/vtt",
    ):
        """
        Instantiates a client to the NPO Frontend API
        """
        super().__init__(env=env, debug=debug, accept=accept)
        self.key, self.secret, self.origin = key, secret, origin

    def accept_choices(self):
        return {"vtt": "text/vtt", "srt": "text/srt", "ebu": "application/ebu-stl", "tt888": "text/tt888"}

    def get(self, mid, language, subtitle_type="CAPTION", ignore_not_found=True) -> Optional[str]:
        """Returns subtitles for giving mid, or None of not found"""
        return self.request(
            "/api/subtitles/"
            + urllib.request.quote(mid, safe="")
            + "/"
            + urllib.request.quote(language, safe="")
            + "/"
            + subtitle_type,
            ignore_not_found=ignore_not_found,
        )

    def search(self, form="{}", sort="asc", offset=0, limit=240, accept="application/json"):
        return self.request(
            "/api/subtitles", data=form, accept=accept, params={"sort": sort, "offset": offset, "max": limit}
        )

    def accept(self, arg="text/vtt"):
        super().accept(arg)
        return self
