from npoapi.npoapi import NpoApi


class Pages(NpoApi):
    def get(self, url):
        return self.request("/api/pages/multiple", params={"ids": url})

    def search(self, form="{}", sort="asc", offset=0, limit=240):
        return self.request("/api/pages", data=form, params={"sort": sort, "offset": offset, "max": limit})
