import codecs
import dataclasses
import os
import logging
import re
import sys
from typing import Final, Optional

import pyxb
from npoapi.data.poms import NS_MAP
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from npoapi.base import DEFAULT_BINDING, Binding

logger: Final = logging.getLogger("Npo.Utils")
pattern: Final = re.compile('[a-z0-9]{2,}', re.IGNORECASE)

MIDS = ["WO_VPRO_025057", "WO_NOS_2321514 (not from vpro)", "WO_VPRO_025700 (has locations)", "WO_VPRO_4911154"]


MID_SHORTHANDS = ", ".join(map(lambda e: "M%d: %s" % e, enumerate(MIDS)))
MID_HELP = """The mid of the object to get. You can use the following shorthands %s""" % MID_SHORTHANDS 
MID_SHORTHAND_PATTERN = re.compile("^M[0-9]+$")

def resolve_mid(mid: str) -> str:
    if MID_SHORTHAND_PATTERN.match(mid):
        index = int(mid[1:])
        if index < len(MIDS):
            return MIDS[index].split(" ", 2)[0]
        else:
            raise Exception("No shorthand found %s. Available are %s" % (mid, MID_SHORTHANDS))
    else:
        return mid

def looks_like_form(form: str):
    """
    Checks if the given string looks like a form. E.g. it represents json, xml, a file, or 'stdin'.

    Otherwise, it can e.g. be interpreted as the text for search
    """
    if form.startswith("{") or form.startswith("<"):
        logger.debug("Detected a string that look like either json or xml")
        return True
    if os.path.isfile(form):
        logger.debug("Detected existing file %s" % form)
        return True
    if form.endswith(".json") or form.endswith(".xml"):
        logger.warning("Form %s looks like a file name, but it is not a file." % form)
        return True
    if form == "-":
        logger.debug("Detected explicit stdin")
        return True
    if not pattern.match(form):
        logger.warning("Form does not look like a credible text search. It doesn't look like a file either though")
        return False

    return False


def to_object(data:str, validate=False, binding=DEFAULT_BINDING, clazz=None) -> object:
    """Converts a string to a pyxb or dataclasses object and optionally validates it"""
    if data is None:
        return None
    if binding == Binding.PYXB:
        logger.warning("pyxb is deprecated in to_object")
        if isinstance(data, pyxb.binding.basis.complexTypeDefinition):
            result = data
        else:
            from npoapi.xml import poms
            bytes, contenttype = data_to_bytes(data)
            result = poms.CreateFromDocument(bytes)

        if validate:
            result.validateBinding()
        return result
    else:
        if dataclasses.is_dataclass(data):
            result = data
        else:
            from npoapi.data import poms
            bytes, contenttype = data_to_bytes(data, clazz=clazz)
            result = poms.from_bytes(bytes)
        if validate:
            logger.warning("Find out how to do that")
        return result


def data_to_bytes(data, content_type:str = None, clazz=None) -> [bytearray, str]:
    """
    Given some object representing API data returns it as a bytearray and a content type.
    Recognized are pyxb bindings, a file name, or else a string.
    """
    if data:
        import pyxb
        import xml.dom.minidom
        if data is None:
            logger.warning("Data is none!")
        elif dataclasses.is_dataclass(data):
            serializer = XmlSerializer(config=SerializerConfig(pretty_print = False))
            content_type = "application/xml"
            data = serializer.render(data, ns_map=NS_MAP).encode("utf-8")
        elif isinstance(data, pyxb.binding.basis.complexTypeDefinition):
            logger.warning("pyxb is deprecated!, but incoming object is pyxb object")
            content_type = "application/xml"
            data = data.toxml("utf-8")
        elif isinstance(data, xml.dom.minidom.Document):
            data = data.toxml(encoding="utf-8")
        elif isinstance(data, xml.dom.minidom.Element):
            data = data.toxml(encoding="utf-8")
        elif isinstance(data, str) and isfile(data):
            if content_type is None:
                if data.endswith(".json"):
                    content_type = "application/json"
                elif data.endswith(".xml"):
                    content_type = "application/xml"

            logger.debug("" + data + " is file, reading it in as " + content_type)
            with codecs.open(data, 'r', 'utf-8') as myfile:
                data = myfile.read().encode('utf-8')
                logger.debug("Found data " + data.decode("utf-8"))
        elif isinstance(data, str):
            if data == "-":
                data = sys.stdin.read()
                logger.debug("Slurping data from stdin -> " + data)
            content_type = None
            if data.startswith("{"):
                content_type = "application/json"
            elif data.startswith("<"):
                content_type = "application/xml"
            data = data.encode("utf-8")

    return data, content_type


def isfile(string:str) -> bool:
    try:
        return os.path.isfile(string)
    except:
        return False
