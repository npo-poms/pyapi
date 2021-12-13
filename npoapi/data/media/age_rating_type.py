from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class AgeRatingType(Enum):
    """
    :cvar VALUE_6: Suitable for people of age 6 and up.
    :cvar VALUE_9: Suitable for people of age 9 and up.
    :cvar VALUE_12: Suitable for people of age 12 and up.
    :cvar VALUE_14: Suitable for people of age 12 and up.
    :cvar VALUE_16: Suitable for people of age 16 and up.
    :cvar VALUE_18: Suitable for people of age 18 and up.
    :cvar ALL: Suitable for people of all ages.
    :cvar NOT_YET_RATED: Not yet rated
    """
    VALUE_6 = "6"
    VALUE_9 = "9"
    VALUE_12 = "12"
    VALUE_14 = "14"
    VALUE_16 = "16"
    VALUE_18 = "18"
    ALL = "ALL"
    NOT_YET_RATED = "NOT_YET_RATED"
