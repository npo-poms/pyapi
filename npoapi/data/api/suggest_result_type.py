from dataclasses import dataclass
from .result_type import ResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class SuggestResultType(ResultType):
    class Meta:
        name = "suggestResultType"
