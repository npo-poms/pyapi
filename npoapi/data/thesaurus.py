from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Names:
    """
    :ivar family_name:
    :ivar given_name:
    """
    class Meta:
        name = "names"

    family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


class Status(Enum):
    """
    :cvar CANDIDATE:
    :cvar APPROVED:
    :cvar REDIRECTED:
    :cvar NOT_COMPLIANT:
    :cvar REJECTED:
    :cvar OBSOLETE:
    :cvar DELETED:
    """
    CANDIDATE = "candidate"
    APPROVED = "approved"
    REDIRECTED = "redirected"
    NOT_COMPLIANT = "not_compliant"
    REJECTED = "rejected"
    OBSOLETE = "obsolete"
    DELETED = "deleted"


@dataclass
class ClassificationType:
    """
    :ivar name:
    :ivar scope_note:
    :ivar redirected_from:
    :ivar id:
    :ivar status:
    :ivar last_modified:
    """
    class Meta:
        name = "classificationType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirected_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectedFrom",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class GenreType:
    """
    :ivar name:
    :ivar scope_note:
    :ivar redirected_from:
    :ivar id:
    :ivar status:
    :ivar last_modified:
    """
    class Meta:
        name = "genreType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirected_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectedFrom",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class GeographicNameType:
    """
    :ivar name:
    :ivar scope_note:
    :ivar redirected_from:
    :ivar id:
    :ivar status:
    :ivar last_modified:
    """
    class Meta:
        name = "geographicNameType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirected_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectedFrom",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class MakerType:
    """
    :ivar name:
    :ivar scope_note:
    :ivar redirected_from:
    :ivar id:
    :ivar status:
    :ivar last_modified:
    """
    class Meta:
        name = "makerType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirected_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectedFrom",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class NameType:
    """
    :ivar name:
    :ivar scope_note:
    :ivar redirected_from:
    :ivar id:
    :ivar status:
    :ivar last_modified:
    """
    class Meta:
        name = "nameType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirected_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectedFrom",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class PersonType:
    """
    :ivar name:
    :ivar given_name:
    :ivar family_name:
    :ivar scope_note:
    :ivar known_as:
    :ivar redirected_from:
    :ivar id:
    :ivar status:
    :ivar last_modified:
    """
    class Meta:
        name = "personType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    known_as: List[Names] = field(
        default_factory=list,
        metadata={
            "name": "knownAs",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirected_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectedFrom",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class TopicType:
    """
    :ivar name:
    :ivar scope_note:
    :ivar redirected_from:
    :ivar id:
    :ivar status:
    :ivar last_modified:
    """
    class Meta:
        name = "topicType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirected_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectedFrom",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class TopicbandgType:
    """
    :ivar name:
    :ivar scope_note:
    :ivar redirected_from:
    :ivar id:
    :ivar status:
    :ivar last_modified:
    """
    class Meta:
        name = "topicbandgType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirected_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectedFrom",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class Classification(ClassificationType):
    class Meta:
        name = "classification"
        namespace = "urn:vpro:gtaa:2017"


@dataclass
class Genre(GenreType):
    class Meta:
        name = "genre"
        namespace = "urn:vpro:gtaa:2017"


@dataclass
class GeographicName(GeographicNameType):
    class Meta:
        name = "geographicName"
        namespace = "urn:vpro:gtaa:2017"


@dataclass
class Maker(MakerType):
    class Meta:
        name = "maker"
        namespace = "urn:vpro:gtaa:2017"


@dataclass
class Name(NameType):
    class Meta:
        name = "name"
        namespace = "urn:vpro:gtaa:2017"


@dataclass
class Person(PersonType):
    class Meta:
        name = "person"
        namespace = "urn:vpro:gtaa:2017"


@dataclass
class Topic(TopicType):
    class Meta:
        name = "topic"
        namespace = "urn:vpro:gtaa:2017"


@dataclass
class Topicbandg(TopicbandgType):
    class Meta:
        name = "topicbandg"
        namespace = "urn:vpro:gtaa:2017"
