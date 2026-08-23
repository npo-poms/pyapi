# This file is NOT generated
from datetime import datetime

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.bases import Parsed
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

# imports are implicitly used by parser
from npoapi.data import api, media, mediaupdate, page, pageupdate
from npoapi.data.mediaupdate import (
    Location as LocationUpdate,
)


class MyParser(XmlParser):
    def __init__(self):
        super().__init__()

    def start(
        self,
        clazz: type | None,
        queue: list[XmlNode],
        objects: list[Parsed],
        qname: str,
        attrs: dict,
        ns_map: dict,
    ):
        if qname == "{urn:vpro:media:update:2009}location":
            clazz = LocationUpdate
        super().start(clazz, queue, objects, qname, attrs, ns_map)


from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

parse_config = ParserConfig(
    base_url=None,
    process_xinclude=True,
    fail_on_unknown_properties=True,
    fail_on_unknown_attributes=True,
    fail_on_converter_warnings=True,
)
context = XmlContext()
parser = XmlParser(context=context, config=parse_config)
config = SerializerConfig(pretty_print=False)
serializer = XmlSerializer(config=config, context=context)

NS_MAP = {
    "update": mediaupdate.__NAMESPACE__,
    "pageupdate": pageupdate.__NAMESPACE__,
    "media": media.__NAMESPACE__,
    "pages": page.__NAMESPACE__,
    "api": api.__NAMESPACE__,
}


def prefix(namespace: str):
    for k, v in NS_MAP.items():
        if v == namespace:
            return k
    return None


def from_string(source: str):
    return parser.from_string(source)


def from_bytes(source: bytes, clazz: type | None = None):
    return parser.from_bytes(source, clazz)


def to_xml(node: object):
    return serializer.render(node, ns_map=NS_MAP)


def children_from_any(source: AnyElement, qname: str):
    return list(filter(lambda a: a.qname == qname, source.children))


def to_xml_data_time(input: datetime | str | XmlDateTime) -> XmlDateTime | None:
    if type is None:
        return None
    if type(input) == XmlDateTime:
        return input
    if type(input) == str:
        return XmlDateTime.from_string(input)
    if type(input) == datetime:
        return XmlDateTime.from_datetime(input)
    raise ValueError(f"Cannot convert {input} to XmlDateTime")
