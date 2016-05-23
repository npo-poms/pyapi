# ./npoapi/xml/pages.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:bae47b8c8a50fe304e6e9de618201baa8dfd97c5
# Generated 2016-05-22 14:42:03.599898 by PyXB version 1.2.4 using Python 3.5.0.final.0
# Namespace urn:vpro:pages:2013 [xmlns:page]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:93a4c04c-201a-11e6-986b-60fb42f0af34')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:pages:2013', create_if_missing=True)
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


# Atomic simple type: {urn:vpro:pages:2013}pridType
class pridType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pridType')
    _XSDLocation = pyxb.utils.utility.Location('http://publish.pages.omroep.nl/schema/pages_2013.xsd', 4, 2)
    _Documentation = None
pridType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'pridType', pridType)

# Atomic simple type: {urn:vpro:pages:2013}pageTypeEnum
class pageTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('http://publish.pages.omroep.nl/schema/pages_2013.xsd', 16, 2)
    _Documentation = None
pageTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=pageTypeEnum)
pageTypeEnum.ARTICLE = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='ARTICLE', tag='ARTICLE')
pageTypeEnum.SPECIAL = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='SPECIAL', tag='SPECIAL')
pageTypeEnum.HOME = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='HOME', tag='HOME')
pageTypeEnum.OVERVIEW = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='OVERVIEW', tag='OVERVIEW')
pageTypeEnum.PRODUCT = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='PRODUCT', tag='PRODUCT')
pageTypeEnum.PLAYER = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='PLAYER', tag='PLAYER')
pageTypeEnum.AUDIO = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='AUDIO', tag='AUDIO')
pageTypeEnum.VIDEO = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='VIDEO', tag='VIDEO')
pageTypeEnum.PLAYLIST = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='PLAYLIST', tag='PLAYLIST')
pageTypeEnum.MOVIE = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='MOVIE', tag='MOVIE')
pageTypeEnum.SERIES = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='SERIES', tag='SERIES')
pageTypeEnum.PERSON = pageTypeEnum._CF_enumeration.addEnumeration(unicode_value='PERSON', tag='PERSON')
pageTypeEnum._InitializeFacetMap(pageTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'pageTypeEnum', pageTypeEnum)

# Atomic simple type: {urn:vpro:pages:2013}linkTypeEnum
class linkTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'linkTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('http://publish.pages.omroep.nl/schema/pages_2013.xsd', 33, 2)
    _Documentation = None
linkTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=linkTypeEnum)
linkTypeEnum.TOP_STORY = linkTypeEnum._CF_enumeration.addEnumeration(unicode_value='TOP_STORY', tag='TOP_STORY')
linkTypeEnum._InitializeFacetMap(linkTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'linkTypeEnum', linkTypeEnum)

# Complex type {urn:vpro:pages:2013}sectionType with content type SIMPLE
class sectionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}sectionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sectionType')
    _XSDLocation = pyxb.utils.utility.Location('http://publish.pages.omroep.nl/schema/pages_2013.xsd', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'path'), 'path', '__urnvpropages2013_sectionType_path', pyxb.binding.datatypes.string)
    __path._DeclarationLocation = pyxb.utils.utility.Location('http://publish.pages.omroep.nl/schema/pages_2013.xsd', 11, 8)
    __path._UseLocation = pyxb.utils.utility.Location('http://publish.pages.omroep.nl/schema/pages_2013.xsd', 11, 8)
    
    path = property(__path.value, __path.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __path.name() : __path
    })
Namespace.addCategoryObject('typeBinding', 'sectionType', sectionType)

