# ./npoapi/xml/subtitles.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f5e9c7dba985d37f434a2bc6acd18425aef883c8
# Generated 2018-02-07 21:23:46.336403 by PyXB version 1.2.6 using Python 3.5.2.final.0
# Namespace urn:vpro:media:subtitles:2009

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c6e76098-0c44-11e8-810c-6a0002581300')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.xml_
import npoapi.xml.shared as _ImportedBinding_npoapi_xml_shared
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:media:subtitles:2009', create_if_missing=True)
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


# Atomic simple type: {urn:vpro:media:subtitles:2009}subtitlesFormatEnum
class subtitlesFormatEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subtitlesFormatEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 31, 2)
    _Documentation = None
subtitlesFormatEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=subtitlesFormatEnum, enum_prefix=None)
subtitlesFormatEnum.WEBVTT = subtitlesFormatEnum._CF_enumeration.addEnumeration(unicode_value='WEBVTT', tag='WEBVTT')
subtitlesFormatEnum.TT888 = subtitlesFormatEnum._CF_enumeration.addEnumeration(unicode_value='TT888', tag='TT888')
subtitlesFormatEnum.EBU = subtitlesFormatEnum._CF_enumeration.addEnumeration(unicode_value='EBU', tag='EBU')
subtitlesFormatEnum.SRT = subtitlesFormatEnum._CF_enumeration.addEnumeration(unicode_value='SRT', tag='SRT')
subtitlesFormatEnum._InitializeFacetMap(subtitlesFormatEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'subtitlesFormatEnum', subtitlesFormatEnum)
_module_typeBindings.subtitlesFormatEnum = subtitlesFormatEnum

# Complex type {urn:vpro:media:subtitles:2009}subtitlesType with content type ELEMENT_ONLY
class subtitlesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:subtitles:2009}subtitlesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subtitlesType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 9, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:subtitles:2009}content uses Python identifier content_
    __content = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'content'), 'content_', '__urnvpromediasubtitles2009_subtitlesType_urnvpromediasubtitles2009content', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 11, 6), )

    
    content_ = property(__content.value, __content.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__urnvpromediasubtitles2009_subtitlesType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 18, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute mid uses Python identifier mid
    __mid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mid'), 'mid', '__urnvpromediasubtitles2009_subtitlesType_mid', pyxb.binding.datatypes.string, required=True)
    __mid._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 13, 4)
    __mid._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 13, 4)
    
    mid = property(__mid.value, __mid.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offset'), 'offset', '__urnvpromediasubtitles2009_subtitlesType_offset', pyxb.binding.datatypes.duration)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 14, 4)
    __offset._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 14, 4)
    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__urnvpromediasubtitles2009_subtitlesType_creationDate', pyxb.binding.datatypes.dateTime)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 15, 4)
    __creationDate._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 15, 4)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Attribute lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastModified'), 'lastModified', '__urnvpromediasubtitles2009_subtitlesType_lastModified', pyxb.binding.datatypes.dateTime)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 16, 4)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 16, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediasubtitles2009_subtitlesType_type', _ImportedBinding_npoapi_xml_shared.subtitlesTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 17, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 17, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute cueCount uses Python identifier cueCount
    __cueCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cueCount'), 'cueCount', '__urnvpromediasubtitles2009_subtitlesType_cueCount', pyxb.binding.datatypes.int)
    __cueCount._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 19, 4)
    __cueCount._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 19, 4)
    
    cueCount = property(__cueCount.value, __cueCount.set, None, None)

    _ElementMap.update({
        __content.name() : __content
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __mid.name() : __mid,
        __offset.name() : __offset,
        __creationDate.name() : __creationDate,
        __lastModified.name() : __lastModified,
        __type.name() : __type,
        __cueCount.name() : __cueCount
    })
_module_typeBindings.subtitlesType = subtitlesType
Namespace.addCategoryObject('typeBinding', 'subtitlesType', subtitlesType)


# Complex type {urn:vpro:media:subtitles:2009}subtitlesContentType with content type SIMPLE
class subtitlesContentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:subtitles:2009}subtitlesContentType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subtitlesContentType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 22, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.base64Binary
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__urnvpromediasubtitles2009_subtitlesContentType_format', _module_typeBindings.subtitlesFormatEnum)
    __format._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 25, 8)
    __format._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 25, 8)
    
    format = property(__format.value, __format.set, None, None)

    
    # Attribute charset uses Python identifier charset
    __charset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'charset'), 'charset', '__urnvpromediasubtitles2009_subtitlesContentType_charset', pyxb.binding.datatypes.string)
    __charset._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 26, 8)
    __charset._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 26, 8)
    
    charset = property(__charset.value, __charset.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format,
        __charset.name() : __charset
    })
_module_typeBindings.subtitlesContentType = subtitlesContentType
Namespace.addCategoryObject('typeBinding', 'subtitlesContentType', subtitlesContentType)


subtitles = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subtitles'), subtitlesType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 7, 2))
Namespace.addCategoryObject('elementBinding', subtitles.name().localName(), subtitles)



subtitlesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'content'), subtitlesContentType, scope=subtitlesType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 11, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(subtitlesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'content')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:media:subtitles:2009', 11, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
subtitlesType._Automaton = _BuildAutomaton()

