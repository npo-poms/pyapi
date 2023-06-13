# This file is NOT generated
from datetime import datetime
from typing import Union, Optional, Type, List, Dict

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.bases import Parsed
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.models.datatype import XmlDateTime
from xsdata.formats.dataclass.parsers import XmlParser, UserXmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


# imports are implicitly used by parser
import npoapi
from npoapi.data.media import Group, Program, Segment, LocationType
from npoapi.data.mediaupdate import Group as GroupUpdate, Program as ProgramUpdate, Segment as SegmentUpdate, \
    Location as LocationUpdate, Image as ImageUpdate
from npoapi.data.pageupdate import Page as PageUpdate
from npoapi.data.api import MediaForm, PagesForm
from npoapi.data import api, page, media, mediaupdate, pageupdate

class MyParser(XmlParser):
    def __init__(self):
        super().__init__()
        
    
    def start(
        self,
        clazz: Optional[Type],
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
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

NS_MAP={
    "update": mediaupdate.__NAMESPACE__,
    "pageupdate": pageupdate.__NAMESPACE__,
    "media": media.__NAMESPACE__,
    "pages": page.__NAMESPACE__,
    "api": api.__NAMESPACE__,
    }
    
def prefix(namespace:str):
    for k,v in NS_MAP.items():
        if v == namespace:
            return k
    return None

def from_string(source: str):
    return parser.from_string(source)

def from_bytes(source: bytes):
    return parser.from_bytes(source)

def to_xml(node: object):
    return serializer.render(node, ns_map=NS_MAP)


def from_any(source: AnyElement):
    for i in parser.context.xsi_cache.items():
        if i[0] == source.qname:
            source.qname = None
            source.text = None
            namespace = i[1][0].Meta.namespace
            name = i[1][0].Meta.name
            pref = prefix(namespace)
            
            return from_string(to_xml(source).replace("AnyElement",  pref + ":" + name))

    raise ValueError("Cannot convert AnyElement to dataclass")
        
def children_from_any(source: AnyElement, qname: str):
     return  list(filter(lambda a: a.qname == qname, source.children))
        

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

