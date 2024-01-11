from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class Names:
    class Meta:
        name = "names"

    familyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    givenName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class NewPersonType:
    class Meta:
        name = "newPersonType"

    givenName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    familyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


class Scheme(Enum):
    PERSON = "person"
    GEOGRAPHICNAME = "geographicname"
    TOPIC = "topic"
    TOPICBANDG = "topicbandg"
    CLASSIFICATION = "classification"
    MAKER = "maker"
    GENRE = "genre"
    NAME = "name"
    GENREFILMMUSEUM = "genrefilmmuseum"


class Status(Enum):
    CANDIDATE = "candidate"
    APPROVED = "approved"
    REDIRECTED = "redirected"
    NOT_COMPLIANT = "not_compliant"
    REJECTED = "rejected"
    OBSOLETE = "obsolete"
    DELETED = "deleted"


@dataclass(slots=True)
class ClassificationType:
    class Meta:
        name = "classificationType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class GenreFilmMuseumType:
    class Meta:
        name = "genreFilmMuseumType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class GenreType:
    class Meta:
        name = "genreType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class GeographicNameType:
    class Meta:
        name = "geographicNameType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class MakerType:
    class Meta:
        name = "makerType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class NameType:
    class Meta:
        name = "nameType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class NewConceptType:
    class Meta:
        name = "newConceptType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    objectType: Optional[Scheme] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class NewPerson(NewPersonType):
    class Meta:
        name = "newPerson"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class PersonType:
    class Meta:
        name = "personType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    givenName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    familyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    knownAs: List[Names] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class TopicType:
    class Meta:
        name = "topicType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class TopicbandgType:
    class Meta:
        name = "topicbandgType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        },
    )


@dataclass(slots=True)
class Classification(ClassificationType):
    class Meta:
        name = "classification"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class Genre(GenreType):
    class Meta:
        name = "genre"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class GenreFilmMuseum(GenreFilmMuseumType):
    class Meta:
        name = "genreFilmMuseum"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class GeographicName(GeographicNameType):
    class Meta:
        name = "geographicName"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class Maker(MakerType):
    class Meta:
        name = "maker"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class Name(NameType):
    class Meta:
        name = "name"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class NewConcept(NewConceptType):
    class Meta:
        name = "newConcept"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class Person(PersonType):
    class Meta:
        name = "person"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class Topic(TopicType):
    class Meta:
        name = "topic"
        namespace = "urn:vpro:gtaa:2017"


@dataclass(slots=True)
class Topicbandg(TopicbandgType):
    class Meta:
        name = "topicbandg"
        namespace = "urn:vpro:gtaa:2017"
