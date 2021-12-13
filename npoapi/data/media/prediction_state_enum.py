from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class PredictionStateEnum(Enum):
    """
    :cvar NOT_ANNOUNCED: This value is not exposed, it can be present in the database though.
    :cvar ANNOUNCED:
    :cvar REALIZED:
    :cvar REVOKED:
    """
    NOT_ANNOUNCED = "NOT_ANNOUNCED"
    ANNOUNCED = "ANNOUNCED"
    REALIZED = "REALIZED"
    REVOKED = "REVOKED"
