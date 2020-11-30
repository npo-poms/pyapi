from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:vpro:api:constraint:page:2013"


@dataclass
class OrType:
    """
    :ivar and_value:
    :ivar or_value:
    :ivar broadcaster:
    :ivar type:
    :ivar portal:
    :ivar section:
    :ivar genre:
    """
    class Meta:
        name = "or"

    and_value: List["AndType"] = field(
        default_factory=list,
        metadata={
            "name": "and",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    or_value: List["OrType"] = field(
        default_factory=list,
        metadata={
            "name": "or",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    type: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    portal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    section: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )


@dataclass
class AndType:
    """
    :ivar and_value:
    :ivar or_value:
    :ivar broadcaster:
    :ivar type:
    :ivar portal:
    :ivar section:
    :ivar genre:
    """
    class Meta:
        name = "and"

    and_value: List["AndType"] = field(
        default_factory=list,
        metadata={
            "name": "and",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    or_value: List[OrType] = field(
        default_factory=list,
        metadata={
            "name": "or",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    type: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    portal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    section: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )
    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
            "sequential": True,
        }
    )


@dataclass
class Filter:
    """
    :ivar and_value:
    :ivar or_value:
    :ivar broadcaster:
    :ivar type:
    :ivar portal:
    :ivar section:
    :ivar genre:
    """
    class Meta:
        name = "filter"
        namespace = "urn:vpro:api:constraint:page:2013"

    and_value: Optional[AndType] = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
        }
    )
    or_value: Optional[OrType] = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    portal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    section: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    genre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
