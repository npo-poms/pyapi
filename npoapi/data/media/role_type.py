from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class RoleType(Enum):
    """
    :cvar DIRECTOR:
    :cvar CHIEF_EDITOR:
    :cvar EDITOR:
    :cvar PRESENTER:
    :cvar INTERVIEWER:
    :cvar PRODUCER:
    :cvar RESEARCH:
    :cvar GUEST:
    :cvar REPORTER:
    :cvar ACTOR:
    :cvar COMMENTATOR:
    :cvar SCRIPTWRITER:
    :cvar COMPOSER:
    :cvar SUBJECT:
    :cvar PARTICIPANT:
    :cvar SIDEKICK: Introduced for MediaConnect sync. This is experimental
    :cvar NEWS_PRESENTER: Introduced for MediaConnect sync. This is experimental
    :cvar ASSISTANT_DIRECTOR:
    :cvar CAMERA:
    :cvar CHOREOGRAPHY:
    :cvar DUBBING:
    :cvar MAKEUP:
    :cvar PRODUCTION_MANAGEMENT:
    :cvar STAGING:
    :cvar STUNT:
    :cvar VISUAL_EFFECTS:
    :cvar UNDEFINED:
    """
    DIRECTOR = "DIRECTOR"
    CHIEF_EDITOR = "CHIEF_EDITOR"
    EDITOR = "EDITOR"
    PRESENTER = "PRESENTER"
    INTERVIEWER = "INTERVIEWER"
    PRODUCER = "PRODUCER"
    RESEARCH = "RESEARCH"
    GUEST = "GUEST"
    REPORTER = "REPORTER"
    ACTOR = "ACTOR"
    COMMENTATOR = "COMMENTATOR"
    SCRIPTWRITER = "SCRIPTWRITER"
    COMPOSER = "COMPOSER"
    SUBJECT = "SUBJECT"
    PARTICIPANT = "PARTICIPANT"
    SIDEKICK = "SIDEKICK"
    NEWS_PRESENTER = "NEWS_PRESENTER"
    ASSISTANT_DIRECTOR = "ASSISTANT_DIRECTOR"
    CAMERA = "CAMERA"
    CHOREOGRAPHY = "CHOREOGRAPHY"
    DUBBING = "DUBBING"
    MAKEUP = "MAKEUP"
    PRODUCTION_MANAGEMENT = "PRODUCTION_MANAGEMENT"
    STAGING = "STAGING"
    STUNT = "STUNT"
    VISUAL_EFFECTS = "VISUAL_EFFECTS"
    UNDEFINED = "UNDEFINED"
