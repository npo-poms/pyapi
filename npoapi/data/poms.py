# This file is NOT generated
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from npoapi.base import NS_MAP

# imports are implicitely used by parser
from npoapi.data.media import Group, Program, Segment, LocationType
from npoapi.data.mediaupdate import Group as GroupUpdate, Program as ProgramUpdate, Segment as SegmentUpdate
from npoapi.data.pageupdate import Page as PageUpdate

parser = XmlParser()
config = SerializerConfig(pretty_print=False)
serializer = XmlSerializer(config=config)


def from_string(source: str):
    return parser.from_string(source)

def from_bytes(source: bytes):
    return parser.from_bytes(source)


def to_xml(node: object):
    return serializer.render(node, ns_map=NS_MAP)

