# ./npoapi/xml/mediaupdate.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2751238d63e5454a5dc65ff574f334ca7496c03f
# Generated 2017-06-02 17:13:48.883107 by PyXB version 1.2.5 using Python 3.5.0.final.0
# Namespace urn:vpro:media:update:2009

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:116f7218-47a6-11e7-9adf-3c075445667b')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import npoapi.xml.shared as _ImportedBinding_npoapi_xml_shared
import pyxb.binding.datatypes
import npoapi.xml.media as _ImportedBinding_npoapi_xml_media

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:media:update:2009', create_if_missing=True)
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


# Atomic simple type: {urn:vpro:media:update:2009}mediaRefType
class mediaRefType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaRefType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 197, 2)
    _Documentation = None
mediaRefType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
mediaRefType._InitializeFacetMap(mediaRefType._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'mediaRefType', mediaRefType)
_module_typeBindings.mediaRefType = mediaRefType

# Atomic simple type: {urn:vpro:media:update:2009}imageLocationUrnType
class imageLocationUrnType (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageLocationUrnType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 300, 2)
    _Documentation = None
imageLocationUrnType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1024))
imageLocationUrnType._InitializeFacetMap(imageLocationUrnType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'imageLocationUrnType', imageLocationUrnType)
_module_typeBindings.imageLocationUrnType = imageLocationUrnType

# Atomic simple type: {urn:vpro:media:update:2009}imageUrnType
class imageUrnType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageUrnType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 306, 2)
    _Documentation = None
imageUrnType._CF_pattern = pyxb.binding.facets.CF_pattern()
imageUrnType._CF_pattern.addPattern(pattern='urn:vpro[\\.:]image:[0-9]+')
imageUrnType._InitializeFacetMap(imageUrnType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'imageUrnType', imageUrnType)
_module_typeBindings.imageUrnType = imageUrnType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 409, 8)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.ASC = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ASC', tag='ASC')
STD_ANON.DESC = STD_ANON._CF_enumeration.addEnumeration(unicode_value='DESC', tag='DESC')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {urn:vpro:media:update:2009}tagUpdateType
class tagUpdateType (_ImportedBinding_npoapi_xml_media.baseTextType):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tagUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 67, 2)
    _Documentation = None
tagUpdateType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'tagUpdateType', tagUpdateType)
_module_typeBindings.tagUpdateType = tagUpdateType

# Atomic simple type: {urn:vpro:media:update:2009}genreUpdateType
class genreUpdateType (_ImportedBinding_npoapi_xml_media.genreIdType):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genreUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 71, 2)
    _Documentation = None
genreUpdateType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'genreUpdateType', genreUpdateType)
_module_typeBindings.genreUpdateType = genreUpdateType

# Complex type {urn:vpro:media:update:2009}avAtributeUpdateType with content type ELEMENT_ONLY
class avAtributeUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}avAtributeUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'avAtributeUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}bitrate uses Python identifier bitrate
    __bitrate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bitrate'), 'bitrate', '__urnvpromediaupdate2009_avAtributeUpdateType_urnvpromediaupdate2009bitrate', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 35, 6), )

    
    bitrate = property(__bitrate.value, __bitrate.set, None, None)

    
    # Element {urn:vpro:media:update:2009}avFileFormat uses Python identifier avFileFormat
    __avFileFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), 'avFileFormat', '__urnvpromediaupdate2009_avAtributeUpdateType_urnvpromediaupdate2009avFileFormat', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 36, 6), )

    
    avFileFormat = property(__avFileFormat.value, __avFileFormat.set, None, None)

    
    # Element {urn:vpro:media:update:2009}videoAttributes uses Python identifier videoAttributes
    __videoAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'videoAttributes'), 'videoAttributes', '__urnvpromediaupdate2009_avAtributeUpdateType_urnvpromediaupdate2009videoAttributes', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 37, 6), )

    
    videoAttributes = property(__videoAttributes.value, __videoAttributes.set, None, None)

    
    # Element {urn:vpro:media:update:2009}audioAttributes uses Python identifier audioAttributes
    __audioAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'audioAttributes'), 'audioAttributes', '__urnvpromediaupdate2009_avAtributeUpdateType_urnvpromediaupdate2009audioAttributes', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 38, 6), )

    
    audioAttributes = property(__audioAttributes.value, __audioAttributes.set, None, None)

    _ElementMap.update({
        __bitrate.name() : __bitrate,
        __avFileFormat.name() : __avFileFormat,
        __videoAttributes.name() : __videoAttributes,
        __audioAttributes.name() : __audioAttributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.avAtributeUpdateType = avAtributeUpdateType
Namespace.addCategoryObject('typeBinding', 'avAtributeUpdateType', avAtributeUpdateType)


# Complex type {urn:vpro:media:update:2009}videoAttributesUpdateType with content type ELEMENT_ONLY
class videoAttributesUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}videoAttributesUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'videoAttributesUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 42, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}aspectRatio uses Python identifier aspectRatio
    __aspectRatio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aspectRatio'), 'aspectRatio', '__urnvpromediaupdate2009_videoAttributesUpdateType_urnvpromediaupdate2009aspectRatio', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 44, 6), )

    
    aspectRatio = property(__aspectRatio.value, __aspectRatio.set, None, None)

    
    # Element {urn:vpro:media:update:2009}color uses Python identifier color
    __color = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'color'), 'color', '__urnvpromediaupdate2009_videoAttributesUpdateType_urnvpromediaupdate2009color', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 45, 6), )

    
    color = property(__color.value, __color.set, None, None)

    
    # Element {urn:vpro:media:update:2009}coding uses Python identifier coding
    __coding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coding'), 'coding', '__urnvpromediaupdate2009_videoAttributesUpdateType_urnvpromediaupdate2009coding', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 46, 6), )

    
    coding = property(__coding.value, __coding.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__urnvpromediaupdate2009_videoAttributesUpdateType_width', pyxb.binding.datatypes.int)
    __width._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 48, 4)
    __width._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 48, 4)
    
    width = property(__width.value, __width.set, None, None)

    
    # Attribute height uses Python identifier height
    __height = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__urnvpromediaupdate2009_videoAttributesUpdateType_height', pyxb.binding.datatypes.int)
    __height._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 49, 4)
    __height._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 49, 4)
    
    height = property(__height.value, __height.set, None, None)

    _ElementMap.update({
        __aspectRatio.name() : __aspectRatio,
        __color.name() : __color,
        __coding.name() : __coding
    })
    _AttributeMap.update({
        __width.name() : __width,
        __height.name() : __height
    })
_module_typeBindings.videoAttributesUpdateType = videoAttributesUpdateType
Namespace.addCategoryObject('typeBinding', 'videoAttributesUpdateType', videoAttributesUpdateType)


# Complex type {urn:vpro:media:update:2009}audioAttributesUpdateType with content type ELEMENT_ONLY
class audioAttributesUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}audioAttributesUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'audioAttributesUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 52, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}channels uses Python identifier channels
    __channels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'channels'), 'channels', '__urnvpromediaupdate2009_audioAttributesUpdateType_urnvpromediaupdate2009channels', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 54, 6), )

    
    channels = property(__channels.value, __channels.set, None, None)

    
    # Element {urn:vpro:media:update:2009}coding uses Python identifier coding
    __coding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coding'), 'coding', '__urnvpromediaupdate2009_audioAttributesUpdateType_urnvpromediaupdate2009coding', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 55, 6), )

    
    coding = property(__coding.value, __coding.set, None, None)

    _ElementMap.update({
        __channels.name() : __channels,
        __coding.name() : __coding
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.audioAttributesUpdateType = audioAttributesUpdateType
Namespace.addCategoryObject('typeBinding', 'audioAttributesUpdateType', audioAttributesUpdateType)


# Complex type {urn:vpro:media:update:2009}creditsUpdateType with content type ELEMENT_ONLY
class creditsUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}creditsUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'creditsUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 84, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__urnvpromediaupdate2009_creditsUpdateType_urnvpromediaupdate2009person', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 86, 6), )

    
    person = property(__person.value, __person.set, None, None)

    _ElementMap.update({
        __person.name() : __person
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.creditsUpdateType = creditsUpdateType
Namespace.addCategoryObject('typeBinding', 'creditsUpdateType', creditsUpdateType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 124, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__urnvpromediaupdate2009_CTD_ANON_urnvpromediaupdate2009location', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 126, 12), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 131, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}scheduleEvent uses Python identifier scheduleEvent
    __scheduleEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), 'scheduleEvent', '__urnvpromediaupdate2009_CTD_ANON__urnvpromediaupdate2009scheduleEvent', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 133, 12), )

    
    scheduleEvent = property(__scheduleEvent.value, __scheduleEvent.set, None, None)

    _ElementMap.update({
        __scheduleEvent.name() : __scheduleEvent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 140, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'image'), 'image', '__urnvpromediaupdate2009_CTD_ANON_2_urnvpromediaupdate2009image', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 142, 12), )

    
    image = property(__image.value, __image.set, None, None)

    _ElementMap.update({
        __image.name() : __image
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {urn:vpro:media:update:2009}bulkUpdateType with content type ELEMENT_ONLY
class bulkUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}bulkUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bulkUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 158, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}titles uses Python identifier titles
    __titles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'titles'), 'titles', '__urnvpromediaupdate2009_bulkUpdateType_urnvpromediaupdate2009titles', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 160, 6), )

    
    titles = property(__titles.value, __titles.set, None, None)

    
    # Element {urn:vpro:media:update:2009}descriptions uses Python identifier descriptions
    __descriptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descriptions'), 'descriptions', '__urnvpromediaupdate2009_bulkUpdateType_urnvpromediaupdate2009descriptions', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 161, 6), )

    
    descriptions = property(__descriptions.value, __descriptions.set, None, None)

    _ElementMap.update({
        __titles.name() : __titles,
        __descriptions.name() : __descriptions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.bulkUpdateType = bulkUpdateType
Namespace.addCategoryObject('typeBinding', 'bulkUpdateType', bulkUpdateType)


# Complex type {urn:vpro:media:update:2009}portalRestrictionUpdateType with content type SIMPLE
class portalRestrictionUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}portalRestrictionUpdateType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'portalRestrictionUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 173, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__urnvpromediaupdate2009_portalRestrictionUpdateType_start', pyxb.binding.datatypes.dateTime)
    __start._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 286, 4)
    __start._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 286, 4)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute stop uses Python identifier stop
    __stop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__urnvpromediaupdate2009_portalRestrictionUpdateType_stop', pyxb.binding.datatypes.dateTime)
    __stop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 287, 4)
    __stop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 287, 4)
    
    stop = property(__stop.value, __stop.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __start.name() : __start,
        __stop.name() : __stop
    })
_module_typeBindings.portalRestrictionUpdateType = portalRestrictionUpdateType
Namespace.addCategoryObject('typeBinding', 'portalRestrictionUpdateType', portalRestrictionUpdateType)


# Complex type {urn:vpro:media:update:2009}locationUpdateType with content type ELEMENT_ONLY
class locationUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}locationUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 214, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}programUrl uses Python identifier programUrl
    __programUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), 'programUrl', '__urnvpromediaupdate2009_locationUpdateType_urnvpromediaupdate2009programUrl', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 216, 6), )

    
    programUrl = property(__programUrl.value, __programUrl.set, None, None)

    
    # Element {urn:vpro:media:update:2009}avAttributes uses Python identifier avAttributes
    __avAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), 'avAttributes', '__urnvpromediaupdate2009_locationUpdateType_urnvpromediaupdate2009avAttributes', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 217, 6), )

    
    avAttributes = property(__avAttributes.value, __avAttributes.set, None, None)

    
    # Element {urn:vpro:media:update:2009}offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'offset'), 'offset', '__urnvpromediaupdate2009_locationUpdateType_urnvpromediaupdate2009offset', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 218, 6), )

    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Element {urn:vpro:media:update:2009}duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__urnvpromediaupdate2009_locationUpdateType_urnvpromediaupdate2009duration', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 219, 6), )

    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvpromediaupdate2009_locationUpdateType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 221, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 221, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvpromediaupdate2009_locationUpdateType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 222, 4)
    __publishStop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 222, 4)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvpromediaupdate2009_locationUpdateType_urn', pyxb.binding.datatypes.anyURI)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 223, 4)
    __urn._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 223, 4)
    
    urn = property(__urn.value, __urn.set, None, None)

    _ElementMap.update({
        __programUrl.name() : __programUrl,
        __avAttributes.name() : __avAttributes,
        __offset.name() : __offset,
        __duration.name() : __duration
    })
    _AttributeMap.update({
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop,
        __urn.name() : __urn
    })
_module_typeBindings.locationUpdateType = locationUpdateType
Namespace.addCategoryObject('typeBinding', 'locationUpdateType', locationUpdateType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 231, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpromediaupdate2009_CTD_ANON_3_urnvpromediaupdate2009title', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 233, 12), )

    
    title = property(__title.value, __title.set, None, None)

    _ElementMap.update({
        __title.name() : __title
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 238, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvpromediaupdate2009_CTD_ANON_4_urnvpromediaupdate2009description', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 240, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {urn:vpro:media:update:2009}imageDataType with content type ELEMENT_ONLY
class imageDataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}imageDataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageDataType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 286, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'data'), 'data', '__urnvpromediaupdate2009_imageDataType_urnvpromediaupdate2009data', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 288, 6), )

    
    data = property(__data.value, __data.set, None, None)

    _ElementMap.update({
        __data.name() : __data
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.imageDataType = imageDataType
Namespace.addCategoryObject('typeBinding', 'imageDataType', imageDataType)


# Complex type {urn:vpro:media:update:2009}imageLocationType with content type ELEMENT_ONLY
class imageLocationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}imageLocationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageLocationType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 293, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'url'), 'url', '__urnvpromediaupdate2009_imageLocationType_urnvpromediaupdate2009url', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 295, 6), )

    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        __url.name() : __url
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.imageLocationType = imageLocationType
Namespace.addCategoryObject('typeBinding', 'imageLocationType', imageLocationType)


# Complex type {urn:vpro:media:update:2009}assetType with content type ELEMENT_ONLY
class assetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}assetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'assetType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 312, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}assetData uses Python identifier assetData
    __assetData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'assetData'), 'assetData', '__urnvpromediaupdate2009_assetType_urnvpromediaupdate2009assetData', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 314, 6), )

    
    assetData = property(__assetData.value, __assetData.set, None, None)

    
    # Element {urn:vpro:media:update:2009}assetLocation uses Python identifier assetLocation
    __assetLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'assetLocation'), 'assetLocation', '__urnvpromediaupdate2009_assetType_urnvpromediaupdate2009assetLocation', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 315, 6), )

    
    assetLocation = property(__assetLocation.value, __assetLocation.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvpromediaupdate2009_assetType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 317, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 317, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvpromediaupdate2009_assetType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 318, 4)
    __publishStop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 318, 4)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    _ElementMap.update({
        __assetData.name() : __assetData,
        __assetLocation.name() : __assetLocation
    })
    _AttributeMap.update({
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop
    })
_module_typeBindings.assetType = assetType
Namespace.addCategoryObject('typeBinding', 'assetType', assetType)


# Complex type {urn:vpro:media:update:2009}assetDataType with content type ELEMENT_ONLY
class assetDataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}assetDataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'assetDataType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 321, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'data'), 'data', '__urnvpromediaupdate2009_assetDataType_urnvpromediaupdate2009data', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 323, 6), )

    
    data = property(__data.value, __data.set, None, None)

    _ElementMap.update({
        __data.name() : __data
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.assetDataType = assetDataType
Namespace.addCategoryObject('typeBinding', 'assetDataType', assetDataType)


# Complex type {urn:vpro:media:update:2009}assetLocationType with content type ELEMENT_ONLY
class assetLocationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}assetLocationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'assetLocationType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 328, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'url'), 'url', '__urnvpromediaupdate2009_assetLocationType_urnvpromediaupdate2009url', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 330, 6), )

    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        __url.name() : __url
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.assetLocationType = assetLocationType
Namespace.addCategoryObject('typeBinding', 'assetLocationType', assetLocationType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
                Optional list of program segments. A segment is a part of a program that can be visually shown on the
                timeline of a player. A segment always has a start time indicating the start of the segment relative to
                the parent program. A segment can have the same fields as other media objects, like titles, descriptions,
                images, locations, etc.

                The standard scenario when playing a segment is to load a location of the parent media object and
                to use the start time as an offset to start playing the segment. However, it is also possible for a
                segment to have its own locations. This makes it possible to for instance have a podcast of a weekly
                segment in a radio show without providing the complete radio program it is a part of.

                Rules:
                - Start time is required
                - If duration is not set the player should play until the end of the program
                - Removing a program also deletes its segments
              """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 365, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}segment uses Python identifier segment
    __segment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'segment'), 'segment', '__urnvpromediaupdate2009_CTD_ANON_5_urnvpromediaupdate2009segment', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 19, 2), )

    
    segment = property(__segment.value, __segment.set, None, None)

    _ElementMap.update({
        __segment.name() : __segment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type {urn:vpro:media:update:2009}memberUpdateType with content type ELEMENT_ONLY
class memberUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}memberUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'memberUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 388, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__urnvpromediaupdate2009_memberUpdateType_position', pyxb.binding.datatypes.integer)
    __position._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 395, 4)
    __position._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 395, 4)
    
    position = property(__position.value, __position.set, None, None)

    
    # Attribute highlighted uses Python identifier highlighted
    __highlighted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'highlighted'), 'highlighted', '__urnvpromediaupdate2009_memberUpdateType_highlighted', pyxb.binding.datatypes.boolean)
    __highlighted._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 396, 4)
    __highlighted._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 396, 4)
    
    highlighted = property(__highlighted.value, __highlighted.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __position.name() : __position,
        __highlighted.name() : __highlighted
    })
_module_typeBindings.memberUpdateType = memberUpdateType
Namespace.addCategoryObject('typeBinding', 'memberUpdateType', memberUpdateType)


# Complex type {urn:vpro:media:update:2009}moveActionType with content type ELEMENT_ONLY
class moveActionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}moveActionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'moveActionType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 419, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}from uses Python identifier from_
    __from = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'from'), 'from_', '__urnvpromediaupdate2009_moveActionType_urnvpromediaupdate2009from', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 421, 6), )

    
    from_ = property(__from.value, __from.set, None, None)

    
    # Element {urn:vpro:media:update:2009}to uses Python identifier to
    __to = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'to'), 'to', '__urnvpromediaupdate2009_moveActionType_urnvpromediaupdate2009to', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 422, 6), )

    
    to = property(__to.value, __to.set, None, None)

    _ElementMap.update({
        __from.name() : __from,
        __to.name() : __to
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.moveActionType = moveActionType
Namespace.addCategoryObject('typeBinding', 'moveActionType', moveActionType)


# Complex type {urn:vpro:media:update:2009}descriptionUpdateType with content type SIMPLE
class descriptionUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}descriptionUpdateType with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_npoapi_xml_media.unboundedTextType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'descriptionUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 59, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding_npoapi_xml_media.unboundedTextType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediaupdate2009_descriptionUpdateType_type', _ImportedBinding_npoapi_xml_media.textualTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 62, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 62, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.descriptionUpdateType = descriptionUpdateType
Namespace.addCategoryObject('typeBinding', 'descriptionUpdateType', descriptionUpdateType)


# Complex type {urn:vpro:media:update:2009}personUpdateType with content type ELEMENT_ONLY
class personUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}personUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'personUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 76, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}givenName uses Python identifier givenName
    __givenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'givenName'), 'givenName', '__urnvpromediaupdate2009_personUpdateType_urnvpromediaupdate2009givenName', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 78, 6), )

    
    givenName = property(__givenName.value, __givenName.set, None, None)

    
    # Element {urn:vpro:media:update:2009}familyName uses Python identifier familyName
    __familyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'familyName'), 'familyName', '__urnvpromediaupdate2009_personUpdateType_urnvpromediaupdate2009familyName', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 79, 6), )

    
    familyName = property(__familyName.value, __familyName.set, None, None)

    
    # Attribute role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__urnvpromediaupdate2009_personUpdateType_role', _ImportedBinding_npoapi_xml_media.roleType, required=True)
    __role._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 81, 4)
    __role._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 81, 4)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __givenName.name() : __givenName,
        __familyName.name() : __familyName
    })
    _AttributeMap.update({
        __role.name() : __role
    })
_module_typeBindings.personUpdateType = personUpdateType
Namespace.addCategoryObject('typeBinding', 'personUpdateType', personUpdateType)


# Complex type {urn:vpro:media:update:2009}mediaUpdateType with content type ELEMENT_ONLY
class mediaUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}mediaUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 101, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}crid uses Python identifier crid
    __crid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'crid'), 'crid', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009crid', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6), )

    
    crid = property(__crid.value, __crid.set, None, None)

    
    # Element {urn:vpro:media:update:2009}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009broadcaster', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 104, 6), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Element {urn:vpro:media:update:2009}portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portal'), 'portal', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009portal', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6), )

    
    portal = property(__portal.value, __portal.set, None, None)

    
    # Element {urn:vpro:media:update:2009}exclusive uses Python identifier exclusive
    __exclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), 'exclusive', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009exclusive', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6), )

    
    exclusive = property(__exclusive.value, __exclusive.set, None, None)

    
    # Element {urn:vpro:media:update:2009}region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'region'), 'region', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009region', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6), )

    
    region = property(__region.value, __region.set, None, None)

    
    # Element {urn:vpro:media:update:2009}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009title', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 109, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:media:update:2009}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009description', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:media:update:2009}tag uses Python identifier tag
    __tag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tag'), 'tag', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009tag', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6), )

    
    tag = property(__tag.value, __tag.set, None, None)

    
    # Element {urn:vpro:media:update:2009}genre uses Python identifier genre
    __genre = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genre'), 'genre', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009genre', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6), )

    
    genre = property(__genre.value, __genre.set, None, None)

    
    # Element {urn:vpro:media:update:2009}avAttributes uses Python identifier avAttributes
    __avAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), 'avAttributes', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009avAttributes', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6), )

    
    avAttributes = property(__avAttributes.value, __avAttributes.set, None, None)

    
    # Element {urn:vpro:media:update:2009}releaseYear uses Python identifier releaseYear
    __releaseYear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'releaseYear'), 'releaseYear', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009releaseYear', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6), )

    
    releaseYear = property(__releaseYear.value, __releaseYear.set, None, None)

    
    # Element {urn:vpro:media:update:2009}duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009duration', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6), )

    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Element {urn:vpro:media:update:2009}credits uses Python identifier credits
    __credits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'credits'), 'credits', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009credits', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6), )

    
    credits = property(__credits.value, __credits.set, None, None)

    
    # Element {urn:vpro:media:update:2009}memberOf uses Python identifier memberOf
    __memberOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), 'memberOf', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009memberOf', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6), )

    
    memberOf = property(__memberOf.value, __memberOf.set, None, None)

    
    # Element {urn:vpro:media:update:2009}ageRating uses Python identifier ageRating
    __ageRating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ageRating'), 'ageRating', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009ageRating', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6), )

    
    ageRating = property(__ageRating.value, __ageRating.set, None, None)

    
    # Element {urn:vpro:media:update:2009}contentRating uses Python identifier contentRating
    __contentRating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contentRating'), 'contentRating', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009contentRating', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6), )

    
    contentRating = property(__contentRating.value, __contentRating.set, None, None)

    
    # Element {urn:vpro:media:update:2009}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009email', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6), )

    
    email = property(__email.value, __email.set, None, None)

    
    # Element {urn:vpro:media:update:2009}website uses Python identifier website
    __website = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'website'), 'website', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009website', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6), )

    
    website = property(__website.value, __website.set, None, None)

    
    # Element {urn:vpro:media:update:2009}locations uses Python identifier locations
    __locations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'locations'), 'locations', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009locations', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6), )

    
    locations = property(__locations.value, __locations.set, None, None)

    
    # Element {urn:vpro:media:update:2009}scheduleEvents uses Python identifier scheduleEvents
    __scheduleEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents'), 'scheduleEvents', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009scheduleEvents', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6), )

    
    scheduleEvents = property(__scheduleEvents.value, __scheduleEvents.set, None, None)

    
    # Element {urn:vpro:media:update:2009}relation uses Python identifier relation
    __relation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relation'), 'relation', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009relation', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6), )

    
    relation = property(__relation.value, __relation.set, None, None)

    
    # Element {urn:vpro:media:update:2009}images uses Python identifier images
    __images = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'images'), 'images', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009images', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6), )

    
    images = property(__images.value, __images.set, None, None)

    
    # Element {urn:vpro:media:update:2009}asset uses Python identifier asset
    __asset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'asset'), 'asset', '__urnvpromediaupdate2009_mediaUpdateType_urnvpromediaupdate2009asset', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6), )

    
    asset = property(__asset.value, __asset.set, None, None)

    
    # Attribute avType uses Python identifier avType
    __avType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avType'), 'avType', '__urnvpromediaupdate2009_mediaUpdateType_avType', _ImportedBinding_npoapi_xml_media.avTypeEnum, required=True)
    __avType._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 148, 4)
    __avType._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 148, 4)
    
    avType = property(__avType.value, __avType.set, None, None)

    
    # Attribute deleted uses Python identifier deleted
    __deleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deleted'), 'deleted', '__urnvpromediaupdate2009_mediaUpdateType_deleted', pyxb.binding.datatypes.boolean)
    __deleted._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 149, 4)
    __deleted._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 149, 4)
    
    deleted = property(__deleted.value, __deleted.set, None, None)

    
    # Attribute embeddable uses Python identifier embeddable
    __embeddable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'embeddable'), 'embeddable', '__urnvpromediaupdate2009_mediaUpdateType_embeddable', pyxb.binding.datatypes.boolean, unicode_default='true')
    __embeddable._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 150, 4)
    __embeddable._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 150, 4)
    
    embeddable = property(__embeddable.value, __embeddable.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvpromediaupdate2009_mediaUpdateType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 151, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 151, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvpromediaupdate2009_mediaUpdateType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 152, 4)
    __publishStop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 152, 4)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    
    # Attribute mid uses Python identifier mid
    __mid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mid'), 'mid', '__urnvpromediaupdate2009_mediaUpdateType_mid', _ImportedBinding_npoapi_xml_media.midType)
    __mid._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 153, 4)
    __mid._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 153, 4)
    
    mid = property(__mid.value, __mid.set, None, None)

    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvpromediaupdate2009_mediaUpdateType_urn', pyxb.binding.datatypes.anyURI)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 154, 4)
    __urn._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 154, 4)
    
    urn = property(__urn.value, __urn.set, None, None)

    
    # Attribute ordered uses Python identifier ordered
    __ordered = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ordered'), 'ordered', '__urnvpromediaupdate2009_mediaUpdateType_ordered', pyxb.binding.datatypes.boolean)
    __ordered._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 155, 4)
    __ordered._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 155, 4)
    
    ordered = property(__ordered.value, __ordered.set, None, None)

    _ElementMap.update({
        __crid.name() : __crid,
        __broadcaster.name() : __broadcaster,
        __portal.name() : __portal,
        __exclusive.name() : __exclusive,
        __region.name() : __region,
        __title.name() : __title,
        __description.name() : __description,
        __tag.name() : __tag,
        __genre.name() : __genre,
        __avAttributes.name() : __avAttributes,
        __releaseYear.name() : __releaseYear,
        __duration.name() : __duration,
        __credits.name() : __credits,
        __memberOf.name() : __memberOf,
        __ageRating.name() : __ageRating,
        __contentRating.name() : __contentRating,
        __email.name() : __email,
        __website.name() : __website,
        __locations.name() : __locations,
        __scheduleEvents.name() : __scheduleEvents,
        __relation.name() : __relation,
        __images.name() : __images,
        __asset.name() : __asset
    })
    _AttributeMap.update({
        __avType.name() : __avType,
        __deleted.name() : __deleted,
        __embeddable.name() : __embeddable,
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop,
        __mid.name() : __mid,
        __urn.name() : __urn,
        __ordered.name() : __ordered
    })
_module_typeBindings.mediaUpdateType = mediaUpdateType
Namespace.addCategoryObject('typeBinding', 'mediaUpdateType', mediaUpdateType)


# Complex type {urn:vpro:media:update:2009}midAndTypeType with content type ELEMENT_ONLY
class midAndTypeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}midAndTypeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'midAndTypeType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 165, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}crid uses Python identifier crid
    __crid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'crid'), 'crid', '__urnvpromediaupdate2009_midAndTypeType_urnvpromediaupdate2009crid', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 167, 6), )

    
    crid = property(__crid.value, __crid.set, None, None)

    
    # Attribute mid uses Python identifier mid
    __mid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mid'), 'mid', '__urnvpromediaupdate2009_midAndTypeType_mid', pyxb.binding.datatypes.string)
    __mid._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 169, 4)
    __mid._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 169, 4)
    
    mid = property(__mid.value, __mid.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediaupdate2009_midAndTypeType_type', _ImportedBinding_npoapi_xml_media.mediaTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 170, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 170, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __crid.name() : __crid
    })
    _AttributeMap.update({
        __mid.name() : __mid,
        __type.name() : __type
    })
_module_typeBindings.midAndTypeType = midAndTypeType
Namespace.addCategoryObject('typeBinding', 'midAndTypeType', midAndTypeType)


# Complex type {urn:vpro:media:update:2009}geoRestrictionUpdateType with content type SIMPLE
class geoRestrictionUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}geoRestrictionUpdateType with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_npoapi_xml_media.geoRestrictionEnum
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geoRestrictionUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 181, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding_npoapi_xml_media.geoRestrictionEnum
    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__urnvpromediaupdate2009_geoRestrictionUpdateType_start', pyxb.binding.datatypes.dateTime)
    __start._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 286, 4)
    __start._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 286, 4)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute stop uses Python identifier stop
    __stop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__urnvpromediaupdate2009_geoRestrictionUpdateType_stop', pyxb.binding.datatypes.dateTime)
    __stop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 287, 4)
    __stop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 287, 4)
    
    stop = property(__stop.value, __stop.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __start.name() : __start,
        __stop.name() : __stop
    })
_module_typeBindings.geoRestrictionUpdateType = geoRestrictionUpdateType
Namespace.addCategoryObject('typeBinding', 'geoRestrictionUpdateType', geoRestrictionUpdateType)


# Complex type {urn:vpro:media:update:2009}titleUpdateType with content type SIMPLE
class titleUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}titleUpdateType with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_npoapi_xml_media.baseTextType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'titleUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 189, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding_npoapi_xml_media.baseTextType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediaupdate2009_titleUpdateType_type', _ImportedBinding_npoapi_xml_media.textualTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 192, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 192, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.titleUpdateType = titleUpdateType
Namespace.addCategoryObject('typeBinding', 'titleUpdateType', titleUpdateType)


# Complex type {urn:vpro:media:update:2009}memberRefUpdateType with content type SIMPLE
class memberRefUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}memberRefUpdateType with content type SIMPLE"""
    _TypeDefinition = mediaRefType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'memberRefUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 205, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is mediaRefType
    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__urnvpromediaupdate2009_memberRefUpdateType_position', pyxb.binding.datatypes.int)
    __position._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 208, 8)
    __position._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 208, 8)
    
    position = property(__position.value, __position.set, None, None)

    
    # Attribute highlighted uses Python identifier highlighted
    __highlighted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'highlighted'), 'highlighted', '__urnvpromediaupdate2009_memberRefUpdateType_highlighted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __highlighted._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 209, 8)
    __highlighted._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 209, 8)
    
    highlighted = property(__highlighted.value, __highlighted.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __position.name() : __position,
        __highlighted.name() : __highlighted
    })
_module_typeBindings.memberRefUpdateType = memberRefUpdateType
Namespace.addCategoryObject('typeBinding', 'memberRefUpdateType', memberRefUpdateType)


# Complex type {urn:vpro:media:update:2009}scheduleEventUpdateType with content type ELEMENT_ONLY
class scheduleEventUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}scheduleEventUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleEventUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 226, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'start'), 'start', '__urnvpromediaupdate2009_scheduleEventUpdateType_urnvpromediaupdate2009start', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 228, 6), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element {urn:vpro:media:update:2009}duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__urnvpromediaupdate2009_scheduleEventUpdateType_urnvpromediaupdate2009duration', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 229, 6), )

    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Element {urn:vpro:media:update:2009}titles uses Python identifier titles
    __titles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'titles'), 'titles', '__urnvpromediaupdate2009_scheduleEventUpdateType_urnvpromediaupdate2009titles', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 230, 6), )

    
    titles = property(__titles.value, __titles.set, None, None)

    
    # Element {urn:vpro:media:update:2009}descriptions uses Python identifier descriptions
    __descriptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descriptions'), 'descriptions', '__urnvpromediaupdate2009_scheduleEventUpdateType_urnvpromediaupdate2009descriptions', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 237, 6), )

    
    descriptions = property(__descriptions.value, __descriptions.set, None, None)

    
    # Attribute channel uses Python identifier channel
    __channel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'channel'), 'channel', '__urnvpromediaupdate2009_scheduleEventUpdateType_channel', _ImportedBinding_npoapi_xml_media.channelEnum, required=True)
    __channel._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 246, 4)
    __channel._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 246, 4)
    
    channel = property(__channel.value, __channel.set, None, None)

    
    # Attribute net uses Python identifier net
    __net = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'net'), 'net', '__urnvpromediaupdate2009_scheduleEventUpdateType_net', pyxb.binding.datatypes.string)
    __net._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 247, 4)
    __net._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 247, 4)
    
    net = property(__net.value, __net.set, None, None)

    _ElementMap.update({
        __start.name() : __start,
        __duration.name() : __duration,
        __titles.name() : __titles,
        __descriptions.name() : __descriptions
    })
    _AttributeMap.update({
        __channel.name() : __channel,
        __net.name() : __net
    })
_module_typeBindings.scheduleEventUpdateType = scheduleEventUpdateType
Namespace.addCategoryObject('typeBinding', 'scheduleEventUpdateType', scheduleEventUpdateType)


# Complex type {urn:vpro:media:update:2009}relationUpdateType with content type SIMPLE
class relationUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}relationUpdateType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relationUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 250, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediaupdate2009_relationUpdateType_type', _ImportedBinding_npoapi_xml_media.relationTypeType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 253, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 253, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'broadcaster'), 'broadcaster', '__urnvpromediaupdate2009_relationUpdateType_broadcaster', _ImportedBinding_npoapi_xml_media.baseTextType, required=True)
    __broadcaster._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 254, 8)
    __broadcaster._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 254, 8)
    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Attribute uriRef uses Python identifier uriRef
    __uriRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uriRef'), 'uriRef', '__urnvpromediaupdate2009_relationUpdateType_uriRef', pyxb.binding.datatypes.anyURI)
    __uriRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 255, 8)
    __uriRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 255, 8)
    
    uriRef = property(__uriRef.value, __uriRef.set, None, None)

    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvpromediaupdate2009_relationUpdateType_urn', pyxb.binding.datatypes.anyURI)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 256, 8)
    __urn._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 256, 8)
    
    urn = property(__urn.value, __urn.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __broadcaster.name() : __broadcaster,
        __uriRef.name() : __uriRef,
        __urn.name() : __urn
    })
_module_typeBindings.relationUpdateType = relationUpdateType
Namespace.addCategoryObject('typeBinding', 'relationUpdateType', relationUpdateType)


# Complex type {urn:vpro:media:update:2009}imageUpdateType with content type ELEMENT_ONLY
class imageUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:update:2009}imageUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 261, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:update:2009}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009title', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 263, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:media:update:2009}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009description', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 264, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:media:update:2009}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009source', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 265, 6), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {urn:vpro:media:update:2009}sourceName uses Python identifier sourceName
    __sourceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sourceName'), 'sourceName', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009sourceName', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 266, 6), )

    
    sourceName = property(__sourceName.value, __sourceName.set, None, None)

    
    # Element {urn:vpro:media:update:2009}license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'license'), 'license', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009license', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 267, 6), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element {urn:vpro:media:update:2009}width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'width'), 'width', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009width', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 268, 6), )

    
    width = property(__width.value, __width.set, None, None)

    
    # Element {urn:vpro:media:update:2009}height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'height'), 'height', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009height', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 269, 6), )

    
    height = property(__height.value, __height.set, None, None)

    
    # Element {urn:vpro:media:update:2009}credits uses Python identifier credits
    __credits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'credits'), 'credits', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009credits', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 270, 6), )

    
    credits = property(__credits.value, __credits.set, None, None)

    
    # Element {urn:vpro:media:update:2009}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'date'), 'date', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009date', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 271, 6), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Element {urn:vpro:media:update:2009}offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'offset'), 'offset', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009offset', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 272, 6), )

    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Element {urn:vpro:media:update:2009}imageData uses Python identifier imageData
    __imageData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'imageData'), 'imageData', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009imageData', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 274, 8), )

    
    imageData = property(__imageData.value, __imageData.set, None, None)

    
    # Element {urn:vpro:media:update:2009}imageLocation uses Python identifier imageLocation
    __imageLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'imageLocation'), 'imageLocation', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009imageLocation', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 275, 8), )

    
    imageLocation = property(__imageLocation.value, __imageLocation.set, None, None)

    
    # Element {urn:vpro:media:update:2009}urn uses Python identifier urn
    __urn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'urn'), 'urn', '__urnvpromediaupdate2009_imageUpdateType_urnvpromediaupdate2009urn', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 276, 8), )

    
    urn = property(__urn.value, __urn.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediaupdate2009_imageUpdateType_type', _ImportedBinding_npoapi_xml_shared.imageTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 279, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 279, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute urn uses Python identifier urn_
    __urn_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn_', '__urnvpromediaupdate2009_imageUpdateType_urn', pyxb.binding.datatypes.string)
    __urn_._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 280, 4)
    __urn_._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 280, 4)
    
    urn_ = property(__urn_.value, __urn_.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvpromediaupdate2009_imageUpdateType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 281, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 281, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvpromediaupdate2009_imageUpdateType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 282, 4)
    __publishStop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 282, 4)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    
    # Attribute highlighted uses Python identifier highlighted
    __highlighted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'highlighted'), 'highlighted', '__urnvpromediaupdate2009_imageUpdateType_highlighted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __highlighted._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 283, 4)
    __highlighted._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 283, 4)
    
    highlighted = property(__highlighted.value, __highlighted.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __source.name() : __source,
        __sourceName.name() : __sourceName,
        __license.name() : __license,
        __width.name() : __width,
        __height.name() : __height,
        __credits.name() : __credits,
        __date.name() : __date,
        __offset.name() : __offset,
        __imageData.name() : __imageData,
        __imageLocation.name() : __imageLocation,
        __urn.name() : __urn
    })
    _AttributeMap.update({
        __type.name() : __type,
        __urn_.name() : __urn_,
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop,
        __highlighted.name() : __highlighted
    })
_module_typeBindings.imageUpdateType = imageUpdateType
Namespace.addCategoryObject('typeBinding', 'imageUpdateType', imageUpdateType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 400, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offset'), 'offset', '__urnvpromediaupdate2009_CTD_ANON_6_offset', pyxb.binding.datatypes.nonNegativeInteger)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 404, 6)
    __offset._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 404, 6)
    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Attribute totalCount uses Python identifier totalCount
    __totalCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'totalCount'), 'totalCount', '__urnvpromediaupdate2009_CTD_ANON_6_totalCount', pyxb.binding.datatypes.nonNegativeInteger)
    __totalCount._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 405, 6)
    __totalCount._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 405, 6)
    
    totalCount = property(__totalCount.value, __totalCount.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__urnvpromediaupdate2009_CTD_ANON_6_max', pyxb.binding.datatypes.nonNegativeInteger)
    __max._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 406, 6)
    __max._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 406, 6)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__urnvpromediaupdate2009_CTD_ANON_6_size', pyxb.binding.datatypes.nonNegativeInteger)
    __size._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 407, 6)
    __size._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 407, 6)
    
    size = property(__size.value, __size.set, None, None)

    
    # Attribute order uses Python identifier order
    __order = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'order'), 'order', '__urnvpromediaupdate2009_CTD_ANON_6_order', _module_typeBindings.STD_ANON)
    __order._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 408, 6)
    __order._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 408, 6)
    
    order = property(__order.value, __order.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __offset.name() : __offset,
        __totalCount.name() : __totalCount,
        __max.name() : __max,
        __size.name() : __size,
        __order.name() : __order
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type {urn:vpro:media:update:2009}groupUpdateType with content type ELEMENT_ONLY
class groupUpdateType (mediaUpdateType):
    """Complex type {urn:vpro:media:update:2009}groupUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'groupUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 90, 2)
    _ElementMap = mediaUpdateType._ElementMap.copy()
    _AttributeMap = mediaUpdateType._AttributeMap.copy()
    # Base type is mediaUpdateType
    
    # Element {urn:vpro:media:update:2009}poSeriesID uses Python identifier poSeriesID
    __poSeriesID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'poSeriesID'), 'poSeriesID', '__urnvpromediaupdate2009_groupUpdateType_urnvpromediaupdate2009poSeriesID', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 94, 10), )

    
    poSeriesID = property(__poSeriesID.value, __poSeriesID.set, None, None)

    
    # Element crid ({urn:vpro:media:update:2009}crid) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element broadcaster ({urn:vpro:media:update:2009}broadcaster) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element portal ({urn:vpro:media:update:2009}portal) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element exclusive ({urn:vpro:media:update:2009}exclusive) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element region ({urn:vpro:media:update:2009}region) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element title ({urn:vpro:media:update:2009}title) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element description ({urn:vpro:media:update:2009}description) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element tag ({urn:vpro:media:update:2009}tag) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element genre ({urn:vpro:media:update:2009}genre) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element avAttributes ({urn:vpro:media:update:2009}avAttributes) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element releaseYear ({urn:vpro:media:update:2009}releaseYear) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element duration ({urn:vpro:media:update:2009}duration) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element credits ({urn:vpro:media:update:2009}credits) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element memberOf ({urn:vpro:media:update:2009}memberOf) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element ageRating ({urn:vpro:media:update:2009}ageRating) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element contentRating ({urn:vpro:media:update:2009}contentRating) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element email ({urn:vpro:media:update:2009}email) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element website ({urn:vpro:media:update:2009}website) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element locations ({urn:vpro:media:update:2009}locations) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element scheduleEvents ({urn:vpro:media:update:2009}scheduleEvents) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element relation ({urn:vpro:media:update:2009}relation) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element images ({urn:vpro:media:update:2009}images) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element asset ({urn:vpro:media:update:2009}asset) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediaupdate2009_groupUpdateType_type', _ImportedBinding_npoapi_xml_media.groupTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 96, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 96, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute avType inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute deleted inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute embeddable inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute publishStart inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute publishStop inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute mid inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute urn inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute ordered inherited from {urn:vpro:media:update:2009}mediaUpdateType
    _ElementMap.update({
        __poSeriesID.name() : __poSeriesID
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.groupUpdateType = groupUpdateType
Namespace.addCategoryObject('typeBinding', 'groupUpdateType', groupUpdateType)


# Complex type {urn:vpro:media:update:2009}programUpdateType with content type ELEMENT_ONLY
class programUpdateType (mediaUpdateType):
    """Complex type {urn:vpro:media:update:2009}programUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'programUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 334, 2)
    _ElementMap = mediaUpdateType._ElementMap.copy()
    _AttributeMap = mediaUpdateType._AttributeMap.copy()
    # Base type is mediaUpdateType
    
    # Element crid ({urn:vpro:media:update:2009}crid) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element broadcaster ({urn:vpro:media:update:2009}broadcaster) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element portal ({urn:vpro:media:update:2009}portal) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element exclusive ({urn:vpro:media:update:2009}exclusive) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element region ({urn:vpro:media:update:2009}region) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element title ({urn:vpro:media:update:2009}title) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element description ({urn:vpro:media:update:2009}description) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element tag ({urn:vpro:media:update:2009}tag) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element genre ({urn:vpro:media:update:2009}genre) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element avAttributes ({urn:vpro:media:update:2009}avAttributes) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element releaseYear ({urn:vpro:media:update:2009}releaseYear) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element duration ({urn:vpro:media:update:2009}duration) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element credits ({urn:vpro:media:update:2009}credits) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element memberOf ({urn:vpro:media:update:2009}memberOf) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element ageRating ({urn:vpro:media:update:2009}ageRating) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element contentRating ({urn:vpro:media:update:2009}contentRating) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element email ({urn:vpro:media:update:2009}email) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element website ({urn:vpro:media:update:2009}website) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element locations ({urn:vpro:media:update:2009}locations) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element scheduleEvents ({urn:vpro:media:update:2009}scheduleEvents) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element relation ({urn:vpro:media:update:2009}relation) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element images ({urn:vpro:media:update:2009}images) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element asset ({urn:vpro:media:update:2009}asset) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element {urn:vpro:media:update:2009}episodeOf uses Python identifier episodeOf
    __episodeOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), 'episodeOf', '__urnvpromediaupdate2009_programUpdateType_urnvpromediaupdate2009episodeOf', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 338, 10), )

    
    episodeOf = property(__episodeOf.value, __episodeOf.set, None, '\n                episodeOf works similar to memberOf. Important differences: only programs of type CLIP or BROADCAST can\n                be an episode of a group and the group can only be of type SERIES or SEASON.\n              ')

    
    # Element {urn:vpro:media:update:2009}segments uses Python identifier segments
    __segments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'segments'), 'segments', '__urnvpromediaupdate2009_programUpdateType_urnvpromediaupdate2009segments', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 346, 10), )

    
    segments = property(__segments.value, __segments.set, None, '\n                Optional list of program segments. A segment is a part of a program that can be visually shown on the\n                timeline of a player. A segment always has a start time indicating the start of the segment relative to\n                the parent program. A segment can have the same fields as other media objects, like titles, descriptions,\n                images, locations, etc.\n\n                The standard scenario when playing a segment is to load a location of the parent media object and\n                to use the start time as an offset to start playing the segment. However, it is also possible for a\n                segment to have its own locations. This makes it possible to for instance have a podcast of a weekly\n                segment in a radio show without providing the complete radio program it is a part of.\n\n                Rules:\n                - Start time is required\n                - If duration is not set the player should play until the end of the program\n                - Removing a program also deletes its segments\n              ')

    
    # Attribute avType inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute deleted inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute embeddable inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute publishStart inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute publishStop inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute mid inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute urn inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute ordered inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediaupdate2009_programUpdateType_type', _ImportedBinding_npoapi_xml_media.programTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 372, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 372, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __episodeOf.name() : __episodeOf,
        __segments.name() : __segments
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.programUpdateType = programUpdateType
Namespace.addCategoryObject('typeBinding', 'programUpdateType', programUpdateType)


# Complex type {urn:vpro:media:update:2009}segmentUpdateType with content type ELEMENT_ONLY
class segmentUpdateType (mediaUpdateType):
    """Complex type {urn:vpro:media:update:2009}segmentUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'segmentUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 377, 2)
    _ElementMap = mediaUpdateType._ElementMap.copy()
    _AttributeMap = mediaUpdateType._AttributeMap.copy()
    # Base type is mediaUpdateType
    
    # Element crid ({urn:vpro:media:update:2009}crid) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element broadcaster ({urn:vpro:media:update:2009}broadcaster) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element portal ({urn:vpro:media:update:2009}portal) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element exclusive ({urn:vpro:media:update:2009}exclusive) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element region ({urn:vpro:media:update:2009}region) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element title ({urn:vpro:media:update:2009}title) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element description ({urn:vpro:media:update:2009}description) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element tag ({urn:vpro:media:update:2009}tag) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element genre ({urn:vpro:media:update:2009}genre) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element avAttributes ({urn:vpro:media:update:2009}avAttributes) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element releaseYear ({urn:vpro:media:update:2009}releaseYear) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element duration ({urn:vpro:media:update:2009}duration) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element credits ({urn:vpro:media:update:2009}credits) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element memberOf ({urn:vpro:media:update:2009}memberOf) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element ageRating ({urn:vpro:media:update:2009}ageRating) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element contentRating ({urn:vpro:media:update:2009}contentRating) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element email ({urn:vpro:media:update:2009}email) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element website ({urn:vpro:media:update:2009}website) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element locations ({urn:vpro:media:update:2009}locations) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element scheduleEvents ({urn:vpro:media:update:2009}scheduleEvents) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element relation ({urn:vpro:media:update:2009}relation) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element images ({urn:vpro:media:update:2009}images) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element asset ({urn:vpro:media:update:2009}asset) inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Element {urn:vpro:media:update:2009}start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'start'), 'start', '__urnvpromediaupdate2009_segmentUpdateType_urnvpromediaupdate2009start', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 381, 10), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute avType inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute deleted inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute embeddable inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute publishStart inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute publishStop inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute mid inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute urn inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute ordered inherited from {urn:vpro:media:update:2009}mediaUpdateType
    
    # Attribute midRef uses Python identifier midRef
    __midRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'midRef'), 'midRef', '__urnvpromediaupdate2009_segmentUpdateType_midRef', pyxb.binding.datatypes.string)
    __midRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 383, 8)
    __midRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 383, 8)
    
    midRef = property(__midRef.value, __midRef.set, None, None)

    _ElementMap.update({
        __start.name() : __start
    })
    _AttributeMap.update({
        __midRef.name() : __midRef
    })
_module_typeBindings.segmentUpdateType = segmentUpdateType
Namespace.addCategoryObject('typeBinding', 'segmentUpdateType', segmentUpdateType)


location = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), locationUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 25, 2))
Namespace.addCategoryObject('elementBinding', location.name().localName(), location)

memberUpdate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'memberUpdate'), memberUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 29, 2))
Namespace.addCategoryObject('elementBinding', memberUpdate.name().localName(), memberUpdate)

move = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'move'), moveActionType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', move.name().localName(), move)

midAndType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'midAndType'), midAndTypeType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 21, 2))
Namespace.addCategoryObject('elementBinding', midAndType.name().localName(), midAndType)

image = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'image'), imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 23, 2))
Namespace.addCategoryObject('elementBinding', image.name().localName(), image)

memberRef = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'memberRef'), memberRefUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 27, 2))
Namespace.addCategoryObject('elementBinding', memberRef.name().localName(), memberRef)

list = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'list'), CTD_ANON_6, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 399, 2))
Namespace.addCategoryObject('elementBinding', list.name().localName(), list)

group = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'group'), groupUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 15, 2))
Namespace.addCategoryObject('elementBinding', group.name().localName(), group)

program = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'program'), programUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 17, 2))
Namespace.addCategoryObject('elementBinding', program.name().localName(), program)

segment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'segment'), segmentUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 19, 2))
Namespace.addCategoryObject('elementBinding', segment.name().localName(), segment)



avAtributeUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bitrate'), pyxb.binding.datatypes.int, scope=avAtributeUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 35, 6)))

avAtributeUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), _ImportedBinding_npoapi_xml_media.avFileFormatEnum, scope=avAtributeUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 36, 6)))

avAtributeUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'videoAttributes'), videoAttributesUpdateType, scope=avAtributeUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 37, 6)))

avAtributeUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audioAttributes'), audioAttributesUpdateType, scope=avAtributeUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 38, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 35, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 37, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 38, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(avAtributeUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bitrate')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(avAtributeUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 36, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(avAtributeUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'videoAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 37, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(avAtributeUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'audioAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 38, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
avAtributeUpdateType._Automaton = _BuildAutomaton()




videoAttributesUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aspectRatio'), _ImportedBinding_npoapi_xml_media.aspectRatioEnum, scope=videoAttributesUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 44, 6)))

videoAttributesUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'color'), _ImportedBinding_npoapi_xml_media.colorType, scope=videoAttributesUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 45, 6)))

videoAttributesUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coding'), _ImportedBinding_npoapi_xml_media.baseTextType, scope=videoAttributesUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 46, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 44, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 45, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 46, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(videoAttributesUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aspectRatio')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 44, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(videoAttributesUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'color')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 45, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(videoAttributesUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coding')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 46, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
videoAttributesUpdateType._Automaton = _BuildAutomaton_()




audioAttributesUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'channels'), pyxb.binding.datatypes.int, scope=audioAttributesUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 54, 6)))

audioAttributesUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coding'), _ImportedBinding_npoapi_xml_media.baseTextType, scope=audioAttributesUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 55, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 54, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 55, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(audioAttributesUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'channels')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 54, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(audioAttributesUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coding')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 55, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
audioAttributesUpdateType._Automaton = _BuildAutomaton_2()




creditsUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), personUpdateType, scope=creditsUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 86, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 86, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(creditsUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 86, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
creditsUpdateType._Automaton = _BuildAutomaton_3()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), locationUpdateType, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 126, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 126, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 126, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_4()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), scheduleEventUpdateType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 133, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 133, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 133, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_5()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'image'), imageUpdateType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 142, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 142, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'image')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 142, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_6()




bulkUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'titles'), titleUpdateType, scope=bulkUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 160, 6)))

bulkUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descriptions'), descriptionUpdateType, scope=bulkUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 161, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(bulkUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'titles')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 160, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(bulkUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descriptions')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 161, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
bulkUpdateType._Automaton = _BuildAutomaton_7()




locationUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), pyxb.binding.datatypes.anyURI, scope=locationUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 216, 6)))

locationUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), avAtributeUpdateType, scope=locationUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 217, 6)))

locationUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offset'), pyxb.binding.datatypes.duration, scope=locationUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 218, 6)))

locationUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'duration'), pyxb.binding.datatypes.duration, scope=locationUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 219, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 218, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 219, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(locationUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'programUrl')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 216, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(locationUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 217, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(locationUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'offset')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 218, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(locationUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 219, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
locationUpdateType._Automaton = _BuildAutomaton_8()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), titleUpdateType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 233, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 233, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 233, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_9()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), descriptionUpdateType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 240, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 240, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 240, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_10()




imageDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'data'), pyxb.binding.datatypes.base64Binary, scope=imageDataType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 288, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 288, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(imageDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'data')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 288, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
imageDataType._Automaton = _BuildAutomaton_11()




imageLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'url'), imageLocationUrnType, scope=imageLocationType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 295, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 295, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(imageLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'url')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 295, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
imageLocationType._Automaton = _BuildAutomaton_12()




assetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'assetData'), assetDataType, scope=assetType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 314, 6)))

assetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'assetLocation'), assetLocationType, scope=assetType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 315, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(assetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'assetData')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 314, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(assetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'assetLocation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 315, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
assetType._Automaton = _BuildAutomaton_13()




assetDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'data'), pyxb.binding.datatypes.base64Binary, scope=assetDataType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 323, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 323, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(assetDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'data')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 323, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
assetDataType._Automaton = _BuildAutomaton_14()




assetLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'url'), pyxb.binding.datatypes.anyURI, scope=assetLocationType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 330, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 330, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(assetLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'url')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 330, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
assetLocationType._Automaton = _BuildAutomaton_15()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'segment'), segmentUpdateType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 19, 2)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 367, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'segment')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 367, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 390, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
memberUpdateType._Automaton = _BuildAutomaton_17()




moveActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'from'), pyxb.binding.datatypes.int, scope=moveActionType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 421, 6)))

moveActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'to'), pyxb.binding.datatypes.int, scope=moveActionType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 422, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(moveActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'from')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 421, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(moveActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'to')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 422, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
moveActionType._Automaton = _BuildAutomaton_18()




personUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'givenName'), pyxb.binding.datatypes.string, scope=personUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 78, 6)))

personUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'familyName'), pyxb.binding.datatypes.string, scope=personUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 79, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'givenName')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 78, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'familyName')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 79, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
personUpdateType._Automaton = _BuildAutomaton_19()




mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'crid'), _ImportedBinding_npoapi_xml_media.cridType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), _ImportedBinding_npoapi_xml_media.organizationIdType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 104, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portal'), _ImportedBinding_npoapi_xml_media.organizationIdType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), portalRestrictionUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'region'), geoRestrictionUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), titleUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 109, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), descriptionUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tag'), tagUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genre'), genreUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), avAtributeUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'releaseYear'), pyxb.binding.datatypes.short, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'duration'), pyxb.binding.datatypes.duration, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'credits'), creditsUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), memberRefUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ageRating'), _ImportedBinding_npoapi_xml_media.ageRatingType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contentRating'), _ImportedBinding_npoapi_xml_media.contentRatingType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), _ImportedBinding_npoapi_xml_media.baseTextType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'website'), _ImportedBinding_npoapi_xml_media.websiteType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locations'), CTD_ANON, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents'), CTD_ANON_, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relation'), relationUpdateType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'images'), CTD_ANON_2, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6)))

mediaUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'asset'), assetType, scope=mediaUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6))
    counters.add(cc_20)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 104, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 109, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releaseYear')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ageRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contentRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'website')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(mediaUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'asset')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    st_22._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mediaUpdateType._Automaton = _BuildAutomaton_20()




midAndTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'crid'), _ImportedBinding_npoapi_xml_media.cridType, scope=midAndTypeType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 167, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 167, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(midAndTypeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 167, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
midAndTypeType._Automaton = _BuildAutomaton_21()




scheduleEventUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'start'), pyxb.binding.datatypes.dateTime, scope=scheduleEventUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 228, 6)))

scheduleEventUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'duration'), pyxb.binding.datatypes.duration, scope=scheduleEventUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 229, 6)))

scheduleEventUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'titles'), CTD_ANON_3, scope=scheduleEventUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 230, 6)))

scheduleEventUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descriptions'), CTD_ANON_4, scope=scheduleEventUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 237, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 230, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 237, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'start')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 228, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(scheduleEventUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 229, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'titles')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 230, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descriptions')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 237, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
scheduleEventUpdateType._Automaton = _BuildAutomaton_22()




imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), _ImportedBinding_npoapi_xml_media.baseTextType, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 263, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 264, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), pyxb.binding.datatypes.string, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 265, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sourceName'), pyxb.binding.datatypes.string, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 266, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'license'), _ImportedBinding_npoapi_xml_shared.licenseEnum, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 267, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'width'), pyxb.binding.datatypes.int, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 268, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height'), pyxb.binding.datatypes.int, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 269, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'credits'), pyxb.binding.datatypes.string, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 270, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'date'), pyxb.binding.datatypes.string, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 271, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offset'), pyxb.binding.datatypes.duration, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 272, 6)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'imageData'), imageDataType, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 274, 8)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'imageLocation'), imageLocationType, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 275, 8)))

imageUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'urn'), imageUrnType, scope=imageUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 276, 8)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 264, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 265, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 266, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 267, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 268, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 269, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 270, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 271, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 272, 6))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 263, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 264, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 265, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sourceName')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 266, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'license')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 267, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'width')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 268, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'height')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 269, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 270, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'date')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 271, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'offset')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 272, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'imageData')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 274, 8))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'imageLocation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 275, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(imageUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'urn')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 276, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
imageUpdateType._Automaton = _BuildAutomaton_23()




def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 402, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_24()




groupUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'poSeriesID'), _ImportedBinding_npoapi_xml_media.baseTextType, scope=groupUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 94, 10)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 94, 10))
    counters.add(cc_21)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 104, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 109, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releaseYear')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ageRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contentRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'website')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'asset')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(groupUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'poSeriesID')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 94, 10))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    st_23._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
groupUpdateType._Automaton = _BuildAutomaton_25()




programUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), memberRefUpdateType, scope=programUpdateType, documentation='\n                episodeOf works similar to memberOf. Important differences: only programs of type CLIP or BROADCAST can\n                be an episode of a group and the group can only be of type SERIES or SEASON.\n              ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 338, 10)))

programUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'segments'), CTD_ANON_5, scope=programUpdateType, documentation='\n                Optional list of program segments. A segment is a part of a program that can be visually shown on the\n                timeline of a player. A segment always has a start time indicating the start of the segment relative to\n                the parent program. A segment can have the same fields as other media objects, like titles, descriptions,\n                images, locations, etc.\n\n                The standard scenario when playing a segment is to load a location of the parent media object and\n                to use the start time as an offset to start playing the segment. However, it is also possible for a\n                segment to have its own locations. This makes it possible to for instance have a podcast of a weekly\n                segment in a radio show without providing the complete radio program it is a part of.\n\n                Rules:\n                - Start time is required\n                - If duration is not set the player should play until the end of the program\n                - Removing a program also deletes its segments\n              ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 346, 10)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 338, 10))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 346, 10))
    counters.add(cc_22)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 104, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 109, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releaseYear')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ageRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contentRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'website')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'asset')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'episodeOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 338, 10))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(programUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'segments')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 346, 10))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    st_24._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
programUpdateType._Automaton = _BuildAutomaton_26()




segmentUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'start'), pyxb.binding.datatypes.duration, scope=segmentUpdateType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 381, 10)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6))
    counters.add(cc_20)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 103, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 104, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 105, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 106, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 108, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 109, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 110, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 111, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 112, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 113, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releaseYear')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 114, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 115, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 116, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 117, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ageRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 118, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contentRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 119, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 121, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'website')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 122, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 123, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 130, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 138, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 139, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'asset')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 146, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(segmentUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'start')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/update/vproMediaUpdate.xsd', 381, 10))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    st_23._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
segmentUpdateType._Automaton = _BuildAutomaton_27()

