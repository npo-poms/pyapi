import datetime
import http
import os
import urllib.request
from typing import Union

import ijson

from npoapi.npoapi import NpoApi


class Media(NpoApi):
    def get(
        self, mid, sub="", sort=None, accept=None, properties=None, limit=None, offset=None, profile=None, stream=False
    ) -> Union[None, http.client.HTTPResponse, str]:
        if isinstance(properties, list):
            properties = ",".join(properties)

        return self.request_or_stream(
            "/api/media/" + urllib.request.quote(mid, safe="") + sub,
            params={"sort": sort, "properties": properties, "max": limit, "offset": offset, "profile": profile},
            accept=accept,
            stream=stream,
        )

    def multiple(self, mids, accept=None, properties=None, profile=None) -> str:
        if os.path.isfile(mids):
            return self.request(
                "/api/media/multiple", data=mids, params={"properties": properties, "profile": profile}, accept=accept
            )
        else:
            return self.request(
                "/api/media/multiple", params={"ids": mids, "properties": properties, "profile": profile}, accept=accept
            )

    def list(self) -> str:
        return self.request("/api/media")

    def search(
        self,
        form="{}",
        sort="asc",
        offset: int = 0,
        limit: int = 240,
        profile: str = None,
        properties: str = None,
        accept: str = None,
        sub="descendants",
        mid=None,
    ) -> str:
        if isinstance(properties, list):
            properties = ",".join(properties)

        if mid is None:
            return self.request(
                "/api/media",
                data=form,
                accept=accept,
                params={"profile": profile, "sort": sort, "offset": offset, "max": limit, "properties": properties},
            )
        else:
            if sub is None:
                raise Exception("Should give sub when having mid")
            return self.request(
                "/api/media/" + urllib.request.quote(mid) + "/" + sub,
                data=form,
                accept=accept,
                params={"profile": profile, "sort": sort, "offset": offset, "max": limit, "properties": properties},
            )

    def changes(
        self, profile=None, limit=10, since=None, properties=None, deletes="ID_ONLY", tail=None
    ) -> Union[None, ijson.items]:
        return ijson.items(
            self.changes_raw(
                stream=True,
                profile=profile,
                limit=limit,
                since=since,
                properties=properties,
                deletes=deletes,
                tail=tail,
            ),
            "changes.item",
        )

    def changes_raw(
        self,
        profile=None,
        order="ASC",
        stream=False,
        limit=None,
        since: Union[str, int, datetime.datetime] = None,
        since_mid=None,
        force_oldstyle=False,
        properties=None,
        deletes="ID_ONLY",
        tail=None,
        reason_filter="",
    ) -> Union[None, http.client.HTTPResponse, str]:
        if isinstance(properties, list):
            properties = ",".join(properties)
        sinceLong = None
        sinceDate = None
        if tail is None:
            tail = "ALWAYS"
        if not since is None:
            if isinstance(since, datetime.datetime):
                sinceDate = str(since).replace(" ", "T")
            elif type(since) == int:
                sinceDate = str(since)
            elif type(since) == float:
                sinceDate = str(int(since))
            elif not force_oldstyle and type(since) == str and (not since.isdigit() or int(since) > 946681200000):
                sinceDate = since
            else:
                sinceLong = since

        publishedSince = (sinceDate + (("," + str(since_mid)) if since_mid else "")) if sinceDate else None
        self.logger.debug("publishedSince: (%s, %s)" % (publishedSince, sinceLong))
        params = {
            "profile": profile,
            "order": order,
            "max": limit,
            "since": sinceLong,
            "publishedSince": publishedSince,
            "properties": properties,
            "deletes": deletes,
            "tail": tail,
            "reasonFilter": reason_filter,
        }
        if stream:
            return self.stream("/api/media/changes", params=params)
        else:
            return self.request("/api/media/changes", params=params)

    def redirects(self) -> str:
        return self.request("/api/media/redirects")

    def iterate_raw(
        self, form=None, profile=None, stream=True, limit=1000, timeout=None, properties=None
    ) -> Union[None, http.client.HTTPResponse, str]:
        if not form:
            form = "{}"
        if isinstance(properties, list):
            properties = ",".join(properties)
        if stream:
            return self.stream(
                "/api/media/iterate",
                data=form,
                params={"profile": profile, "max": limit, "properties": properties},
                timeout=timeout,
            )
        else:
            return self.request(
                "/api/media/iterate", data=form, params={"profile": profile, "max": limit, "properties": properties}
            )

    def __str__(self) -> str:
        return super.__str__(self) + " (media)"
