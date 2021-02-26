import http
from typing import Optional, Union

from npoapi.npoapi import NpoApi
import urllib.request
import os


class Media(NpoApi):
    def get(self, mid, sub="", sort=None, accept=None, properties=None, limit=None, profile=None) -> Optional[str]:
        return self.request("/api/media/" + urllib.request.quote(mid, safe='') + sub,
                            params={"sort": sort, "properties": properties, "max": limit, "profile": profile},
                            accept=accept)

    def multiple(self, mids, accept=None, properties=None, profile=None) -> str:
        if os.path.isfile(mids):
            return self.request("/api/media/multiple", data=mids,
                                params={"properties": properties, "profile": profile}, accept=accept)
        else:
            return self.request("/api/media/multiple",
                                params={"ids": mids, "properties": properties, "profile": profile}, accept=accept)

    def list(self) -> str:
        return self.request("/api/media")

    def search(self, form="{}", sort="asc", offset: int = 0, limit: int = 240, profile: str = None,
               properties: str = None, accept: str = None, sub="descendants", mid=None) -> str:
        if mid is None:
            return self.request("/api/media", data=form, accept=accept,
                                params={"profile": profile, "sort": sort, "offset": offset, "max": limit, "properties": properties})
        else:
            if sub is None:
                raise Exception("Should give sub when having mid")
            return self.request("/api/media/" + urllib.request.quote(mid) + "/" + sub, data=form, accept=accept,
                                params={"profile": profile, "sort": sort, "offset": offset, "max": limit, "properties": properties})

    def changes(self, profile=None, order="ASC", stream=False, limit=10, since=None, force_oldstyle=False, properties=None, check_profile=True, deletes="ID_ONLY") -> Union[None, http.client.HTTPResponse, str]:
        sinceLong = None
        sinceDate = None
        if not since is None:
            if not force_oldstyle and (not since.isdigit() or int(since) > 946681200000):
                sinceDate = since
            else:
                sinceLong = since
        if stream:
            return self.stream("/api/media/changes",
                               params={
                               "profile": profile, "order": order, "max": limit,
                               "since": sinceLong, "publishedSince": sinceDate, "properties": properties,
                               "checkProfile": check_profile, "deletes": deletes
                               }
                )
        else:
            return self.request("/api/media/changes",
                                params={
                                    "profile": profile,
                                    "order": order,
                                    "max": limit,
                                    "since": sinceLong,
                                    "publishedSince": sinceDate,
                                    "properties": properties,
                                    "checkProfile": check_profile, "deletes": deletes
                                }
                )

    def redirects(self) -> str:
        return self.request("/api/media/redirects")

    def iterate(self, form=None, profile=None, stream=True, limit=100, timeout=None, properties=None) -> Union[None, http.client.HTTPResponse, str]:
        if not form:
            form = "{}"
        if stream:
            return self.stream("/api/media/iterate", data=form,
                               params={"profile": profile, "max": limit, "properties": properties}, timeout=timeout)
        else:

            return self.request("/api/media/iterate", data=form,
                                params={"profile": profile, "max": limit, "properties": properties})
