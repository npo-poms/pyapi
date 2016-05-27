from npoapi.npoapi import NpoApi
import urllib.request
import os


class Media(NpoApi):
    def get(self, mid, sub="", sort=None, accept=None, properties=None, max=None):
        return self.request("/api/media/" + urllib.request.quote(mid, safe='') + sub, params={"sort": sort, "properties": properties, "max": max}, accept=accept)

    def multiple(self, mids, accept=None):
        if os.path.isfile(mids):
            return self.request("/api/media/multiple", data=mids, params={}, accept=accept)
        else:
            return self.request("/api/media/multiple", params={"ids": mids}, accept=accept)

    def list(self):
        return self.request("/api/media")

    def search(self, form="{}", sort="asc", offset=0, max_=240, properties=None, accept=None):
        return self.request("/api/media", data=form, accept=accept, params={"sort": sort, "offset": offset, "max": max_, "properties": properties})

    def changes(self, profile=None, order="ASC", stream=False, max_=10):
        if stream:
            return self.stream("/api/media/changes", params={"profile": profile, "order": order, "max": max_})
        else:
            return self.request("/api/media/changes", params={"profile": profile, "order": order, "max": max_})
