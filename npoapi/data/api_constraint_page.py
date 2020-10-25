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
        metadata=dict(
            name="and",
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    or_value: List["OrType"] = field(
        default_factory=list,
        metadata=dict(
            name="or",
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    type: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    portal: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    section: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    genre: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
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
        metadata=dict(
            name="and",
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    or_value: List[OrType] = field(
        default_factory=list,
        metadata=dict(
            name="or",
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    type: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    portal: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    section: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    genre: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
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
        metadata=dict(
            name="and",
            type="Element"
        )
    )
    or_value: Optional[OrType] = field(
        default=None,
        metadata=dict(
            name="or",
            type="Element"
        )
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    portal: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    section: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    genre: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
