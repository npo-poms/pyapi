from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class ClassificationType:
    class Meta:
        name = "classificationType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    lastModified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class GenreType:
    class Meta:
        name = "genreType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    lastModified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class GeographicNameType:
    class Meta:
        name = "geographicNameType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    lastModified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class MakerType:
    class Meta:
        name = "makerType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    lastModified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class NameType:
    class Meta:
        name = "nameType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    lastModified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class Names:
    class Meta:
        name = "names"

    familyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    givenName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class TopicType:
    class Meta:
        name = "topicType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    lastModified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


@dataclass
class TopicbandgType:
    class Meta:
        name = "topicbandgType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    lastModified: Optional[str] = field(
        default=None,
        metadata={
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
class PersonType:
    class Meta:
        name = "personType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    givenName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    familyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    knownAs: List[Names] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    lastModified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )


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


@dataclass
class Person(PersonType):
    class Meta:
        name = "person"
        namespace = "urn:vpro:gtaa:2017"
