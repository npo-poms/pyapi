# ./npoapi/xml/api_constraint.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:16fe21f7d82c570c380b0c8dc2a83f6f2249d3d1
# Generated 2020-10-20 09:07:11.803132 by PyXB version 1.2.6 using Python 3.7.2.final.0
# Namespace urn:vpro:api:constraint:2014 [xmlns:constraint]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d7b16146-12a2-11eb-a4bf-9801a7ae4ad1')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:api:constraint:2014', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {urn:vpro:api:constraint:2014}operatorType
class operatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'operatorType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 3, 2)
    _Documentation = None
operatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=operatorType, enum_prefix=None)
operatorType.LT = operatorType._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
operatorType.GT = operatorType._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
operatorType.EQ = operatorType._CF_enumeration.addEnumeration(unicode_value='EQ', tag='EQ')
operatorType.LTE = operatorType._CF_enumeration.addEnumeration(unicode_value='LTE', tag='LTE')
operatorType.GTE = operatorType._CF_enumeration.addEnumeration(unicode_value='GTE', tag='GTE')
operatorType._InitializeFacetMap(operatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'operatorType', operatorType)
_module_typeBindings.operatorType = operatorType
