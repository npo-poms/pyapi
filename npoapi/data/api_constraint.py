from enum import Enum

__NAMESPACE__ = "urn:vpro:api:constraint:2014"


class OperatorType(Enum):
    """
    :cvar LT:
    :cvar GT:
    :cvar EQ:
    :cvar LTE:
    :cvar GTE:
    """
    LT = "LT"
    GT = "GT"
    EQ = "EQ"
    LTE = "LTE"
    GTE = "GTE"
