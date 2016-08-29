from npoapi.npoapi import NpoApi
import urllib.request
import os


class Media(NpoApi):
    def get(self, mid, sub="", sort=None, accept=None, properties=None, limit=None):
        return self.request("/api/media/" + urllib.request.quote(mid, safe='') + sub, params={"sort": sort, "properties": properties, "max": limit}, accept=accept)

    def multiple(self, mids, accept=None):
        if os.path.isfile(mids):
            return self.request("/api/media/multiple", data=mids, params={}, accept=accept)
        else:
            return self.request("/api/media/multiple", params={"ids": mids}, accept=accept)

    def list(self):
        return self.request("/api/media")

    def search(self, form="{}", sort="asc", offset=0, limit=240, properties=None, accept=None, sub=None, mid=None):
        if mid is None:
            return self.request("/api/media", data=form, accept=accept,
                                params={"sort": sort, "offset": offset, "max": limit, "properties": properties})
        else:
            return self.request("/api/media/" + urllib.request.quote(mid) + "/" + sub, data=form, accept=accept,
                                params={"sort": sort, "offset": offset, "max": limit, "properties": properties})


    def changes(self, profile=None, order="ASC", stream=False, limit=10, since=None, forceOldStyle=False):
        sinceLong = None
        sinceDate = None
        if not since is None:
            if not forceOldStyle and (not since.isdigit() or int(since) > 946681200000):
                sinceDate = since
            else:
                sinceLong = since
        if stream:
            return self.stream("/api/media/changes", params={"profile": profile, "order": order, "max": limit, "since": sinceLong, "publishedSince": sinceDate})
        else:
            return self.request("/api/media/changes", params={"profile": profile, "order": order, "max": limit, "since": sinceLong, "publishedSince": sinceDate})

    def iterate(self, form=None, profile=None, stream=True, limit=100):
        if not form:
            form = "{}"
        if stream:
            return self.stream("/api/media/iterate", data=form,
                               params={"profile": profile, "max": limit})
        else:

            return self.request("/api/media/iterate", data=form,
                                params={"profile": profile, "max": limit})
