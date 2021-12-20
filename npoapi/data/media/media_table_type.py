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
    :ivar programTable: A table with all program objects in this container
    :ivar groupTable: A table with all group objects in this container
    :ivar locationTable:
    :ivar schedule: A table with all schedule information in this container
    :ivar publisher:
    :ivar publicationTime:
    :ivar version:
    """
    class Meta:
        name = "mediaTableType"

    programTable: Optional[ProgramTableType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    groupTable: Optional[GroupTableType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    locationTable: Optional[LocationTableType] = field(
        default=None,
        metadata={
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
    publicationTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
