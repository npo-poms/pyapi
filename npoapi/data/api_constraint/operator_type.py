from enum import Enum

__NAMESPACE__ = "urn:vpro:api:constraint:2014"


class OperatorType(Enum):
    LT = "LT"
    GT = "GT"
    EQ = "EQ"
    LTE = "LTE"
    GTE = "GTE"
