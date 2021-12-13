from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class GeoRestrictionEnum(Enum):
    """
    :cvar NL: Media only playable in the Netherlands.
    :cvar BENELUX: Media only playable in the Benelux (Belgium, Netherlands, Luxembourg). This is unused.
    :cvar NLBES: New in 5.6.  Nederland plus BES gemeentes
    :cvar NLALL: New in 5.6. Nederland plus BES gemeentes plus Curacao, St. Maarten en Aruba
    :cvar EU: New in 5.6. EU (incl. BES gemeentes, Curacao, St. Maarten en Aruba)
    :cvar EUROPE: New in 5.6. Europa in breedste zin van het woord
    """
    NL = "NL"
    BENELUX = "BENELUX"
    NLBES = "NLBES"
    NLALL = "NLALL"
    EU = "EU"
    EUROPE = "EUROPE"
