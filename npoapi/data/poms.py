# This file is NOT generated
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


# imports are implicitly used by parser
import npoapi
from npoapi.data.media import Group, Program, Segment, LocationType
from npoapi.data.mediaupdate import Group as GroupUpdate, Program as ProgramUpdate, Segment as SegmentUpdate
from npoapi.data.pageupdate import Page as PageUpdate
from npoapi.data.api import MediaForm, PagesForm
from npoapi.data import api

parser = XmlParser()
config = SerializerConfig(pretty_print=False)
serializer = XmlSerializer(config=config)

# sadly constants in modules (__NAMESPACE__) ar not accessible
NS_MAP={
    "mediaupdate": "urn:vpro:media:update:2009",
    "pageupdate": "urn:vpro:pages:update:2013",
    "media": "urn:vpro:media:2009",
    "pages": "urn:vpro:pages:2013",
    "api": api.__NAMESPACE__,
    }

def from_string(source: str):
    return parser.from_string(source)

def from_bytes(source: bytes):
    return parser.from_bytes(source)


def to_xml(node: object):
    return serializer.render(node, ns_map=NS_MAP)

