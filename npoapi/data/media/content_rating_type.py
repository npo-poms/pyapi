from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class ContentRatingType(Enum):
    """
    :cvar DISCRIMINATIE: Discrimination. Contains depictions, or material which may encourage, discrimination.
    :cvar GROF_TAALGEBRUIK: Coarse language.
    :cvar ANGST: Fear. May be frightening or scary for young children.
    :cvar GEWELD: Violence. Contains depictions of violence.
    :cvar SEKS: Sex. Contains nudity and/or sexual behavior or sexual references.
    :cvar DRUGS_EN_ALCOHOL: Drugs. Refers to or depicts the use of drugs.
    """
    DISCRIMINATIE = "DISCRIMINATIE"
    GROF_TAALGEBRUIK = "GROF_TAALGEBRUIK"
    ANGST = "ANGST"
    GEWELD = "GEWELD"
    SEKS = "SEKS"
    DRUGS_EN_ALCOHOL = "DRUGS_EN_ALCOHOL"
