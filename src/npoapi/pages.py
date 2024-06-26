import http
from typing import Union

import ijson

from npoapi.npoapi import NpoApi


class Pages(NpoApi):
    __author__ = "Michiel Meeuwissen"

    def get(self, url) -> str:
        return self.request("/api/pages/multiple", params={"ids": url})

    def search(
        self,
        form="{}",
        sort="asc",
        offset=0,
        limit=240,
        profile: str = None,
        accept: str = None,
        properties: str = None,
    ) -> str:
        """
        Performs a search on the pages api
        """
        return self.request(
            "/api/pages",
            data=form,
            accept=accept,
            params={"sort": sort, "offset": offset, "max": limit, "profile": profile, "properties": properties},
        )

    def iterate(self, form="{}", profile=None, limit=None) -> Union[None, ijson.items]:
        """
        Returns a stream of ijson objects
        """
        stream = self.iterate_raw(form=form, profile=profile, limit=limit)
        if not stream is None:
            return ijson.items(stream, "pages.item")
        else:
            return None

    def iterate_raw(
        self, form="{}", profile=None, limit=1000, stream=True, timeout=None, properties=None
    ) -> Union[None, http.client.HTTPResponse, str]:
        if not form:
            form = "{}"
        if isinstance(properties, list):
            properties = ",".join(properties)
        if stream:
            return self.stream(
                "/api/pages/iterate",
                data=form,
                params={"profile": profile, "max": limit, "properties": properties},
                timeout=timeout,
            )
        else:
            return self.request(
                "/api/pages/iterate", data=form, params={"profile": profile, "max": limit, "properties": properties}
            )
