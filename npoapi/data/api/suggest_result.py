from dataclasses import dataclass
from .suggest_result_type import SuggestResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class SuggestResult(SuggestResultType):
    class Meta:
        name = "suggestResult"
        namespace = "urn:vpro:api:2013"
