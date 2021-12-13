from dataclasses import dataclass
from .media_result_type import MediaResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaResult(MediaResultType):
    class Meta:
        name = "mediaResult"
        namespace = "urn:vpro:api:2013"
