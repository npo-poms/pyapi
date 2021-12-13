from dataclasses import dataclass
from .error_type import ErrorType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class Error(ErrorType):
    class Meta:
        name = "error"
        namespace = "urn:vpro:api:2013"
