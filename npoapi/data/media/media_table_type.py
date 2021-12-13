from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .group_table_type import GroupTableType
from .location_table_type import LocationTableType
from .program_table_type import ProgramTableType
from .schedule import Schedule

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class MediaTableType:
    """
    :ivar program_table: A table with all program objects in this container
    :ivar group_table: A table with all group objects in this container
    :ivar location_table:
    :ivar schedule: A table with all schedule information in this container
    :ivar publisher:
    :ivar publication_time:
    :ivar version:
    """
    class Meta:
        name = "mediaTableType"

    program_table: Optional[ProgramTableType] = field(
        default=None,
        metadata={
            "name": "programTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    group_table: Optional[GroupTableType] = field(
        default=None,
        metadata={
            "name": "groupTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    location_table: Optional[LocationTableType] = field(
        default=None,
        metadata={
            "name": "locationTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    schedule: Optional[Schedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    publisher: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publication_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
