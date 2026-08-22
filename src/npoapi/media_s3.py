import datetime
import logging
import os
from typing import Optional, Union

import boto3
import botocore
from botocore.exceptions import ClientError

from npoapi.base import NpoApiBase


BUCKETS = {
    "prod": "poms-prd-input",
    "acc": "poms-acc-input",
    "test": "poms-tst-input"
}

DateLike = Union[str, datetime.datetime, datetime.date]


def _as_utc(value: Optional[DateLike]) -> Optional[datetime.datetime]:
    """Coerce an ISO-8601 string, date or datetime into an aware UTC datetime.

    S3 reports LastModified as a timezone-aware datetime, so naive input is
    assumed to be UTC rather than raising on the comparison.
    """
    if value is None:
        return None
    if isinstance(value, str):
        parsed = datetime.datetime.fromisoformat(value.replace("Z", "+00:00"))
    elif isinstance(value, datetime.datetime):
        parsed = value
    elif isinstance(value, datetime.date):
        parsed = datetime.datetime.combine(value, datetime.time.min)
    else:
        raise TypeError(f"cannot interpret {value!r} as a date")
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=datetime.timezone.utc)
    return parsed.astimezone(datetime.timezone.utc)


def _read_creds_properties(env: str) -> dict:
    """Read key=value pairs from the standard creds.properties file, honouring .env suffixes."""
    for path in NpoApiBase.get_configfiles():
        if os.path.isfile(path):
            raw = {}
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        raw[k.strip()] = v.strip().strip('"')
            # start with un-suffixed values, then let env-specific ones override
            props = {k: v for k, v in raw.items() if "." not in k}
            for k, v in raw.items():
                parts = k.rsplit(".", 1)
                if len(parts) == 2 and parts[1] == env:
                    props[parts[0]] = v
            return props
    return {}


class MediaS3:
    """Reads media objects from the S3 bucket for a given environment, bypassing the API."""

    __author__ = "Michiel Meeuwissen"

    def __init__(
        self,
        env: str = "prod",
        access_key: Optional[str] = None,
        secret_access_key: Optional[str] = None,
        region: Optional[str] = None,
        max_pool_connections: int = 25,
    ):
        if env not in BUCKETS:
            raise ValueError(f"env must be one of {list(BUCKETS)}, got {env!r}")
        self.env = env
        self.bucket = BUCKETS[env]
        self.logger = logging.getLogger(__name__)
        props = _read_creds_properties(env)

        def resolve(arg, key):
            return arg or os.environ.get(key) or props.get(key)

        self._client = boto3.client(
            "s3",
            aws_access_key_id=resolve(access_key, "S3_ACCESS_KEY"),
            aws_secret_access_key=resolve(secret_access_key, "S3_SECRET_ACCESS_KEY"),
            region_name=resolve(region, "S3_REGION"),
            config=botocore.client.Config(max_pool_connections=max_pool_connections)
        )

    def _get_raw(
        self,
        mid: str,
        fmt: str = "json",
        modified_since: Optional[DateLike] = None,
    ) -> Optional[str]:
        key = f"media/{fmt}/{mid}.{fmt}"
        kwargs = {"Bucket": self.bucket, "Key": key}
        since = _as_utc(modified_since)
        if since is not None:
            # GetObject, unlike the listing calls, filters on the timestamp
            # server-side and answers 304 when the object is older.
            kwargs["IfModifiedSince"] = since
        try:
            response = self._client.get_object(**kwargs)
            return response["Body"].read().decode("utf-8")
        except ClientError as e:
            if e.response["Error"]["Code"] in ("NoSuchKey", "404", "NotModified", "304"):
                return None
            raise

    def get(
        self,
        mid: str,
        fmt: str = "json",
        modified_since: Optional[DateLike] = None,
    ) -> Optional[str]:
        """Return the raw JSON or XML string for a media object.

        Returns None if the object does not exist, or — when *modified_since*
        is given — if it was not modified after that moment.
        """
        return self._get_raw(mid, fmt, modified_since=modified_since)

    def list_keys(
        self,
        fmt: str = "json",
        modified_since: Optional[DateLike] = None,
        modified_before: Optional[DateLike] = None,
    ):
        """Yield (mid, s3_object) for every object under media/<fmt>/.

        The second element is the raw S3 listing entry, so it carries
        LastModified, Size and ETag.

        S3 records LastModified for every object and returns it in the listing,
        but it cannot filter on it: the prefix is always listed in key order,
        never in date order, so *modified_since* (exclusive) and
        *modified_before* (exclusive) are applied here, client-side. The number
        of LIST requests is therefore unaffected by the filter — only the
        objects yielded are.
        """
        since = _as_utc(modified_since)
        before = _as_utc(modified_before)
        prefix = f"media/{fmt}/"
        paginator = self._client.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=self.bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                mid = obj["Key"].removeprefix(prefix).removesuffix(f".{fmt}")
                if not mid:
                    continue
                last_modified = obj["LastModified"]
                if since is not None and last_modified <= since:
                    continue
                if before is not None and last_modified >= before:
                    continue
                yield mid, obj

    def list_mids(
        self,
        fmt: str = "json",
        modified_since: Optional[DateLike] = None,
        modified_before: Optional[DateLike] = None,
    ):
        """Yield all MIDs stored under media/<fmt>/ in the bucket, one page at a time."""
        for mid, _obj in self.list_keys(
            fmt=fmt, modified_since=modified_since, modified_before=modified_before
        ):
            yield mid

    def list_objects(
        self,
        fmt: str = "json",
        fetch_content: bool = True,
        modified_since: Optional[DateLike] = None,
        modified_before: Optional[DateLike] = None,
    ):
        """Yield (mid, content) tuples for all objects under media/<fmt>/.

        When *fetch_content* is True (default) the raw string content of each
        object is fetched and returned as the second element of the tuple.
        When False, the second element is None, making this equivalent to
        iterating keys only (as list_mids does).

        The timestamp filter is applied to the listing entry, before the
        content is fetched, so filtered-out objects cost no GET request.
        """
        for mid, _obj in self.list_keys(
            fmt=fmt, modified_since=modified_since, modified_before=modified_before
        ):
            yield mid, (self._get_raw(mid, fmt) if fetch_content else None)

    def get_object(
        self,
        mid: str,
        fmt: str = "xml",
        binding=None,
        modified_since: Optional[DateLike] = None,
    ):
        """Return a deserialized media object (xsdata), or None if not found
        (or not modified after *modified_since*)."""
        from npoapi.base import DEFAULT_BINDING
        raw = self._get_raw(mid, fmt, modified_since=modified_since)
        if raw is None:
            return None
        return _deserialize(raw, fmt, binding or DEFAULT_BINDING)


def _deserialize(raw: str, fmt: str, binding):
    from npoapi.base import Binding
    from npoapi.data import MediaUpdateType
    if binding == Binding.XSDATA:
        if fmt == "json":
            from xsdata.formats.dataclass.parsers import JsonParser
            return JsonParser().from_string(raw, MediaUpdateType)
        else:
            from xsdata.formats.dataclass.parsers import XmlParser
            return XmlParser().from_string(raw, MediaUpdateType)
    raise ValueError(f"Unsupported binding: {binding}")
