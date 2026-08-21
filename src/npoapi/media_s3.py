import logging
import os
from typing import Optional

import boto3
from botocore.exceptions import ClientError

from npoapi.base import NpoApiBase


BUCKETS = {
    "prod": "poms-prd-input",
    "acc": "poms-acc-input",
}


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
        )

    def _get_raw(self, mid: str, fmt: str = "json") -> Optional[str]:
        key = f"media/{fmt}/{mid}.{fmt}"
        try:
            response = self._client.get_object(Bucket=self.bucket, Key=key)
            return response["Body"].read().decode("utf-8")
        except ClientError as e:
            if e.response["Error"]["Code"] in ("NoSuchKey", "404"):
                return None
            raise

    def get(self, mid: str, fmt: str = "json") -> Optional[str]:
        """Return the raw JSON or XML string for a media object, or None if not found."""
        return self._get_raw(mid, fmt)

    def list_mids(self, fmt: str = "json"):
        """Yield all MIDs stored under media/<fmt>/ in the bucket, one page at a time."""
        for mid, _content in self.list_objects(fmt=fmt, fetch_content=False):
            yield mid

    def list_objects(self, fmt: str = "json", fetch_content: bool = True):
        """Yield (mid, content) tuples for all objects under media/<fmt>/.

        When *fetch_content* is True (default) the raw string content of each
        object is fetched and returned as the second element of the tuple.
        When False, the second element is None, making this equivalent to
        iterating keys only (as list_mids does).
        """
        paginator = self._client.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=self.bucket, Prefix=f"media/{fmt}/"):
            for obj in page.get("Contents", []):
                key = obj["Key"]
                mid = key.removeprefix(f"media/{fmt}/").removesuffix(f".{fmt}")
                if not mid:
                    continue
                if fetch_content:
                    content = self._get_raw(mid, fmt)
                else:
                    content = None
                yield mid, content

    def get_object(self, mid: str, fmt: str = "xml", binding=None):
        """Return a deserialized media object (xsdata), or None if not found."""
        from npoapi.base import DEFAULT_BINDING
        raw = self._get_raw(mid, fmt)
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
