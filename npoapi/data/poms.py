# This file is NOT generated
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from npoapi.base import NS_MAP
from npoapi.data.media import Group, Program, Segment, LocationType
from npoapi.data.mediaupdate import Group as GroupUpdate, Program as ProgramUpdate, Segment as SegmentUpdate

parser = XmlParser()
config = SerializerConfig(pretty_print=False)
serializer = XmlSerializer(config=config)


def from_string(node: str):
    return parser.from_string(node)


def to_xml(node: object):
    return serializer.render(node, ns_map=NS_MAP)

