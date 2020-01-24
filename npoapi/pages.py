from npoapi.npoapi import NpoApi


class Pages(NpoApi):

    __author__ = "Michiel Meeuwissen"

    def get(self, url) -> str:
        return self.request("/api/pages/multiple", params={"ids": url})

    def search(self, form="{}", sort="asc", offset=0, limit=240, profile=None, accept=None) -> str:
        return self.request("/api/pages", data=form, accept=accept, params={"sort": sort, "offset": offset, "max": limit, "profile": profile})

    def iterate(self, form="{}", profile=None, offset=0, limit=None) -> str:
        import ijson
        stream = self.stream("/api/pages/iterate", data=form, accept="application/json", params={"profile": profile, "offset": offset, "max": limit})
        if not stream is None:
            return ijson.items(stream, "pages.item")
        else:
            return None
