from enum import Enum

__NAMESPACE__ = "urn:vpro:shared:2009"


class WorkflowEnumType(Enum):
    """These are the possible values of several 'workflow' fields.

    These serve administrative purposes only. In the Frontent API you should only encounter 'PUBLISHED'.

    :cvar FOR_PUBLICATION:
    :cvar FOR_REPUBLICATION:
    :cvar PUBLISHED:
    :cvar PARENT_REVOKED:
    :cvar REVOKED:
    :cvar FOR_DELETION:
    :cvar DELETED:
    :cvar MERGED:
    :cvar IGNORE: This means that the object is ignored for workflow changes. This is mainly usefull during
        testing.
    """
    FOR_PUBLICATION = "FOR PUBLICATION"
    FOR_REPUBLICATION = "FOR REPUBLICATION"
    PUBLISHED = "PUBLISHED"
    PARENT_REVOKED = "PARENT REVOKED"
    REVOKED = "REVOKED"
    FOR_DELETION = "FOR DELETION"
    DELETED = "DELETED"
    MERGED = "MERGED"
    IGNORE = "IGNORE"
