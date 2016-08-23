from npoapi.npoapi import NpoApi


class Pages(NpoApi):
    def get(self, url) -> str:
        return self.request("/api/pages/multiple", params={"ids": url})

    def search(self, form="{}", sort="asc", offset=0, limit=240, profile=None, accept=None) -> str:
        return self.request("/api/pages", data=form, accept=accept, params={"sort": sort, "offset": offset, "max": limit, "profile": profile})
