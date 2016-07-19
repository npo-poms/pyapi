from npoapi.npoapi import NpoApi


class Screens(NpoApi):
    def list(self, sort="asc", offset=0, limit=240):
        return self.request("/api/screens", params={"sort": sort, "offset": offset, "max": limit})
