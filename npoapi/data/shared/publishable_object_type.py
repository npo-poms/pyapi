from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .workflow_enum_type import WorkflowEnumType

__NAMESPACE__ = "urn:vpro:shared:2009"


@dataclass
class PublishableObjectType:
    class Meta:
        name = "publishableObjectType"

    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publishDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    creationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
