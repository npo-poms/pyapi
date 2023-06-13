# This file is NOT generated
from datetime import datetime
from typing import Union, Optional

from xsdata.models.datatype import XmlDateTime
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


# imports are implicitly used by parser
import npoapi
from npoapi.data.media import Group, Program, Segment, LocationType
from npoapi.data.mediaupdate import Group as GroupUpdate, Program as ProgramUpdate, Segment as SegmentUpdate, Location as LocationUpdate, Image as ImageUpdate
from npoapi.data.pageupdate import Page as PageUpdate
from npoapi.data.api import MediaForm, PagesForm
from npoapi.data import api, page, media, mediaupdate, pageupdate

parser = XmlParser()
config = SerializerConfig(pretty_print=False)
serializer = XmlSerializer(config=config)

NS_MAP={
    "update": mediaupdate.__NAMESPACE__,
    "pageupdate": pageupdate.__NAMESPACE__,
    "media": media.__NAMESPACE__,
    "pages": page.__NAMESPACE__,
    "api": api.__NAMESPACE__,
    }

def from_string(source: str):
    return parser.from_string(source)

def from_bytes(source: bytes):
    return parser.from_bytes(source)


def to_xml(node: object):
    return serializer.render(node, ns_map=NS_MAP)

def to_xml_data_time(input: Union[datetime, str, XmlDateTime]) -> Optional[XmlDateTime]:
    if type is None:
        return None
    if type(input) == XmlDateTime:
        return input
    if type(input) == str:
        return XmlDateTime.from_string(input)
    if type(input) == datetime:
        return XmlDateTime.from_datetime(input)
    raise ValueError(f"Cannot convert {input} to XmlDateTime")

