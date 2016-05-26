# ./npoapi/xml/api_constraint_media.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c4e4314e58c54eb763331b986f51d7c6d2480f27
# Generated 2016-05-26 14:08:02.457183 by PyXB version 1.2.4 using Python 3.5.0.final.0
# Namespace urn:vpro:api:constraint:media:2013 [xmlns:media]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:7d827ad8-233a-11e6-881c-3c075445667b')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import npoapi.xml.api_constraint as _ImportedBinding_npoapi_xml_api_constraint

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:api:constraint:media:2013', create_if_missing=True)
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


# Atomic simple type: {urn:vpro:api:constraint:media:2013}avTypeConstraintType
class avTypeConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'avTypeConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 122, 2)
    _Documentation = None
avTypeConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'avTypeConstraintType', avTypeConstraintType)

# Atomic simple type: {urn:vpro:api:constraint:media:2013}avFileFormatConstraintType
class avFileFormatConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'avFileFormatConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 126, 2)
    _Documentation = None
avFileFormatConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'avFileFormatConstraintType', avFileFormatConstraintType)

# Atomic simple type: {urn:vpro:api:constraint:media:2013}avFileExtensionConstraintType
class avFileExtensionConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'avFileExtensionConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 130, 2)
    _Documentation = None
avFileExtensionConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'avFileExtensionConstraintType', avFileExtensionConstraintType)

# Atomic simple type: {urn:vpro:api:constraint:media:2013}descendantOfConstraintType
class descendantOfConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'descendantOfConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 142, 2)
    _Documentation = None
descendantOfConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'descendantOfConstraintType', descendantOfConstraintType)

# Atomic simple type: {urn:vpro:api:constraint:media:2013}broadcasterConstraintType
class broadcasterConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'broadcasterConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 146, 2)
    _Documentation = None
broadcasterConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'broadcasterConstraintType', broadcasterConstraintType)

# Atomic simple type: {urn:vpro:api:constraint:media:2013}typeConstraintType
class typeConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 163, 2)
    _Documentation = None
typeConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'typeConstraintType', typeConstraintType)

# Atomic simple type: {urn:vpro:api:constraint:media:2013}channelConstraintType
class channelConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'channelConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 167, 2)
    _Documentation = None
channelConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'channelConstraintType', channelConstraintType)

# Atomic simple type: {urn:vpro:api:constraint:media:2013}portalConstraintType
class portalConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'portalConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 181, 2)
    _Documentation = None
portalConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'portalConstraintType', portalConstraintType)

# Atomic simple type: {urn:vpro:api:constraint:media:2013}portalRestrictionConstraintType
class portalRestrictionConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'portalRestrictionConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 189, 2)
    _Documentation = None
portalRestrictionConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'portalRestrictionConstraintType', portalRestrictionConstraintType)

# Atomic simple type: {urn:vpro:api:constraint:media:2013}geoRestrictionConstraintType
class geoRestrictionConstraintType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geoRestrictionConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 197, 2)
    _Documentation = None
geoRestrictionConstraintType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'geoRestrictionConstraintType', geoRestrictionConstraintType)

# Complex type {urn:vpro:api:constraint:media:2013}filter with content type ELEMENT_ONLY
class filter_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}filter with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'filter')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:constraint:media:2013}and uses Python identifier and_
    __and = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'and'), 'and_', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013and', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 11, 8), )

    
    and_ = property(__and.value, __and.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}or uses Python identifier or_
    __or = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'or'), 'or_', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013or', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 12, 8), )

    
    or_ = property(__or.value, __or.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}not uses Python identifier not_
    __not = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'not'), 'not_', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013not', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 13, 8), )

    
    not_ = property(__not.value, __not.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avType uses Python identifier avType
    __avType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avType'), 'avType', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013avType', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 14, 8), )

    
    avType = property(__avType.value, __avType.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avFileFormat uses Python identifier avFileFormat
    __avFileFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), 'avFileFormat', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013avFileFormat', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 15, 8), )

    
    avFileFormat = property(__avFileFormat.value, __avFileFormat.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avFileExtension uses Python identifier avFileExtension
    __avFileExtension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension'), 'avFileExtension', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013avFileExtension', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 16, 8), )

    
    avFileExtension = property(__avFileExtension.value, __avFileExtension.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}programUrl uses Python identifier programUrl
    __programUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), 'programUrl', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013programUrl', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 17, 8), )

    
    programUrl = property(__programUrl.value, __programUrl.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}descendantOf uses Python identifier descendantOf
    __descendantOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), 'descendantOf', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013descendantOf', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 18, 8), )

    
    descendantOf = property(__descendantOf.value, __descendantOf.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013broadcaster', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 19, 8), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasImage uses Python identifier hasImage
    __hasImage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasImage'), 'hasImage', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013hasImage', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 20, 8), )

    
    hasImage = property(__hasImage.value, __hasImage.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasLocation uses Python identifier hasLocation
    __hasLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasLocation'), 'hasLocation', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013hasLocation', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 21, 8), )

    
    hasLocation = property(__hasLocation.value, __hasLocation.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasPrediction uses Python identifier hasPrediction
    __hasPrediction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction'), 'hasPrediction', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013hasPrediction', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 22, 8), )

    
    hasPrediction = property(__hasPrediction.value, __hasPrediction.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013type', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 23, 8), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}channel uses Python identifier channel
    __channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'channel'), 'channel', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013channel', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 24, 8), )

    
    channel = property(__channel.value, __channel.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}scheduleEvent uses Python identifier scheduleEvent
    __scheduleEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), 'scheduleEvent', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013scheduleEvent', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 25, 8), )

    
    scheduleEvent = property(__scheduleEvent.value, __scheduleEvent.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasPortal uses Python identifier hasPortal
    __hasPortal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasPortal'), 'hasPortal', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013hasPortal', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 26, 8), )

    
    hasPortal = property(__hasPortal.value, __hasPortal.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portal'), 'portal', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013portal', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 27, 8), )

    
    portal = property(__portal.value, __portal.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}isExclusive uses Python identifier isExclusive
    __isExclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isExclusive'), 'isExclusive', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013isExclusive', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 30, 8), )

    
    isExclusive = property(__isExclusive.value, __isExclusive.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}exclusive uses Python identifier exclusive
    __exclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), 'exclusive', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013exclusive', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 31, 8), )

    
    exclusive = property(__exclusive.value, __exclusive.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasGeoRestriction uses Python identifier hasGeoRestriction
    __hasGeoRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction'), 'hasGeoRestriction', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013hasGeoRestriction', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 32, 8), )

    
    hasGeoRestriction = property(__hasGeoRestriction.value, __hasGeoRestriction.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}geoRestriction uses Python identifier geoRestriction
    __geoRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction'), 'geoRestriction', '__urnvproapiconstraintmedia2013_filter__urnvproapiconstraintmedia2013geoRestriction', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 33, 8), )

    
    geoRestriction = property(__geoRestriction.value, __geoRestriction.set, None, None)

    _ElementMap.update({
        __and.name() : __and,
        __or.name() : __or,
        __not.name() : __not,
        __avType.name() : __avType,
        __avFileFormat.name() : __avFileFormat,
        __avFileExtension.name() : __avFileExtension,
        __programUrl.name() : __programUrl,
        __descendantOf.name() : __descendantOf,
        __broadcaster.name() : __broadcaster,
        __hasImage.name() : __hasImage,
        __hasLocation.name() : __hasLocation,
        __hasPrediction.name() : __hasPrediction,
        __type.name() : __type,
        __channel.name() : __channel,
        __scheduleEvent.name() : __scheduleEvent,
        __hasPortal.name() : __hasPortal,
        __portal.name() : __portal,
        __isExclusive.name() : __isExclusive,
        __exclusive.name() : __exclusive,
        __hasGeoRestriction.name() : __hasGeoRestriction,
        __geoRestriction.name() : __geoRestriction
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'filter', filter_)


# Complex type {urn:vpro:api:constraint:media:2013}and with content type ELEMENT_ONLY
class and_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}and with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'and')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 38, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:constraint:media:2013}and uses Python identifier and_
    __and = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'and'), 'and_', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013and', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 41, 8), )

    
    and_ = property(__and.value, __and.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}or uses Python identifier or_
    __or = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'or'), 'or_', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013or', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 42, 8), )

    
    or_ = property(__or.value, __or.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}not uses Python identifier not_
    __not = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'not'), 'not_', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013not', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 43, 8), )

    
    not_ = property(__not.value, __not.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avType uses Python identifier avType
    __avType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avType'), 'avType', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013avType', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 44, 8), )

    
    avType = property(__avType.value, __avType.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avFileFormat uses Python identifier avFileFormat
    __avFileFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), 'avFileFormat', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013avFileFormat', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 45, 8), )

    
    avFileFormat = property(__avFileFormat.value, __avFileFormat.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avFileExtension uses Python identifier avFileExtension
    __avFileExtension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension'), 'avFileExtension', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013avFileExtension', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 46, 8), )

    
    avFileExtension = property(__avFileExtension.value, __avFileExtension.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}programUrl uses Python identifier programUrl
    __programUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), 'programUrl', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013programUrl', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 47, 8), )

    
    programUrl = property(__programUrl.value, __programUrl.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}descendantOf uses Python identifier descendantOf
    __descendantOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), 'descendantOf', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013descendantOf', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 48, 8), )

    
    descendantOf = property(__descendantOf.value, __descendantOf.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013broadcaster', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 49, 8), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasImage uses Python identifier hasImage
    __hasImage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasImage'), 'hasImage', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013hasImage', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 50, 8), )

    
    hasImage = property(__hasImage.value, __hasImage.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasLocation uses Python identifier hasLocation
    __hasLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasLocation'), 'hasLocation', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013hasLocation', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 51, 8), )

    
    hasLocation = property(__hasLocation.value, __hasLocation.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasPrediction uses Python identifier hasPrediction
    __hasPrediction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction'), 'hasPrediction', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013hasPrediction', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 52, 8), )

    
    hasPrediction = property(__hasPrediction.value, __hasPrediction.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013type', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 53, 8), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}channel uses Python identifier channel
    __channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'channel'), 'channel', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013channel', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 54, 8), )

    
    channel = property(__channel.value, __channel.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}scheduleEvent uses Python identifier scheduleEvent
    __scheduleEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), 'scheduleEvent', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013scheduleEvent', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 55, 8), )

    
    scheduleEvent = property(__scheduleEvent.value, __scheduleEvent.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasPortal uses Python identifier hasPortal
    __hasPortal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasPortal'), 'hasPortal', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013hasPortal', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 56, 8), )

    
    hasPortal = property(__hasPortal.value, __hasPortal.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portal'), 'portal', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013portal', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 57, 8), )

    
    portal = property(__portal.value, __portal.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}isExclusive uses Python identifier isExclusive
    __isExclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isExclusive'), 'isExclusive', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013isExclusive', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 58, 8), )

    
    isExclusive = property(__isExclusive.value, __isExclusive.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}exclusive uses Python identifier exclusive
    __exclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), 'exclusive', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013exclusive', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 59, 8), )

    
    exclusive = property(__exclusive.value, __exclusive.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasGeoRestriction uses Python identifier hasGeoRestriction
    __hasGeoRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction'), 'hasGeoRestriction', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013hasGeoRestriction', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 60, 8), )

    
    hasGeoRestriction = property(__hasGeoRestriction.value, __hasGeoRestriction.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}geoRestriction uses Python identifier geoRestriction
    __geoRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction'), 'geoRestriction', '__urnvproapiconstraintmedia2013_and__urnvproapiconstraintmedia2013geoRestriction', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 61, 8), )

    
    geoRestriction = property(__geoRestriction.value, __geoRestriction.set, None, None)

    _ElementMap.update({
        __and.name() : __and,
        __or.name() : __or,
        __not.name() : __not,
        __avType.name() : __avType,
        __avFileFormat.name() : __avFileFormat,
        __avFileExtension.name() : __avFileExtension,
        __programUrl.name() : __programUrl,
        __descendantOf.name() : __descendantOf,
        __broadcaster.name() : __broadcaster,
        __hasImage.name() : __hasImage,
        __hasLocation.name() : __hasLocation,
        __hasPrediction.name() : __hasPrediction,
        __type.name() : __type,
        __channel.name() : __channel,
        __scheduleEvent.name() : __scheduleEvent,
        __hasPortal.name() : __hasPortal,
        __portal.name() : __portal,
        __isExclusive.name() : __isExclusive,
        __exclusive.name() : __exclusive,
        __hasGeoRestriction.name() : __hasGeoRestriction,
        __geoRestriction.name() : __geoRestriction
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'and', and_)


# Complex type {urn:vpro:api:constraint:media:2013}or with content type ELEMENT_ONLY
class or_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}or with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'or')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 66, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:constraint:media:2013}and uses Python identifier and_
    __and = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'and'), 'and_', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013and', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 69, 8), )

    
    and_ = property(__and.value, __and.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}or uses Python identifier or_
    __or = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'or'), 'or_', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013or', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 70, 8), )

    
    or_ = property(__or.value, __or.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}not uses Python identifier not_
    __not = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'not'), 'not_', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013not', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 71, 8), )

    
    not_ = property(__not.value, __not.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avType uses Python identifier avType
    __avType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avType'), 'avType', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013avType', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 72, 8), )

    
    avType = property(__avType.value, __avType.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avFileFormat uses Python identifier avFileFormat
    __avFileFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), 'avFileFormat', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013avFileFormat', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 73, 8), )

    
    avFileFormat = property(__avFileFormat.value, __avFileFormat.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avFileExtension uses Python identifier avFileExtension
    __avFileExtension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension'), 'avFileExtension', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013avFileExtension', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 74, 8), )

    
    avFileExtension = property(__avFileExtension.value, __avFileExtension.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}programUrl uses Python identifier programUrl
    __programUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), 'programUrl', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013programUrl', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 75, 8), )

    
    programUrl = property(__programUrl.value, __programUrl.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}descendantOf uses Python identifier descendantOf
    __descendantOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), 'descendantOf', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013descendantOf', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 76, 8), )

    
    descendantOf = property(__descendantOf.value, __descendantOf.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013broadcaster', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 77, 8), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasImage uses Python identifier hasImage
    __hasImage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasImage'), 'hasImage', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013hasImage', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 78, 8), )

    
    hasImage = property(__hasImage.value, __hasImage.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasLocation uses Python identifier hasLocation
    __hasLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasLocation'), 'hasLocation', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013hasLocation', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 79, 8), )

    
    hasLocation = property(__hasLocation.value, __hasLocation.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasPrediction uses Python identifier hasPrediction
    __hasPrediction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction'), 'hasPrediction', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013hasPrediction', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 80, 8), )

    
    hasPrediction = property(__hasPrediction.value, __hasPrediction.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013type', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 81, 8), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}channel uses Python identifier channel
    __channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'channel'), 'channel', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013channel', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 82, 8), )

    
    channel = property(__channel.value, __channel.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}scheduleEvent uses Python identifier scheduleEvent
    __scheduleEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), 'scheduleEvent', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013scheduleEvent', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 83, 8), )

    
    scheduleEvent = property(__scheduleEvent.value, __scheduleEvent.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasPortal uses Python identifier hasPortal
    __hasPortal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasPortal'), 'hasPortal', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013hasPortal', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 84, 8), )

    
    hasPortal = property(__hasPortal.value, __hasPortal.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portal'), 'portal', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013portal', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 85, 8), )

    
    portal = property(__portal.value, __portal.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}isExclusive uses Python identifier isExclusive
    __isExclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isExclusive'), 'isExclusive', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013isExclusive', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 86, 8), )

    
    isExclusive = property(__isExclusive.value, __isExclusive.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}exclusive uses Python identifier exclusive
    __exclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), 'exclusive', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013exclusive', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 87, 8), )

    
    exclusive = property(__exclusive.value, __exclusive.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasGeoRestriction uses Python identifier hasGeoRestriction
    __hasGeoRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction'), 'hasGeoRestriction', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013hasGeoRestriction', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 88, 8), )

    
    hasGeoRestriction = property(__hasGeoRestriction.value, __hasGeoRestriction.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}geoRestriction uses Python identifier geoRestriction
    __geoRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction'), 'geoRestriction', '__urnvproapiconstraintmedia2013_or__urnvproapiconstraintmedia2013geoRestriction', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 89, 8), )

    
    geoRestriction = property(__geoRestriction.value, __geoRestriction.set, None, None)

    _ElementMap.update({
        __and.name() : __and,
        __or.name() : __or,
        __not.name() : __not,
        __avType.name() : __avType,
        __avFileFormat.name() : __avFileFormat,
        __avFileExtension.name() : __avFileExtension,
        __programUrl.name() : __programUrl,
        __descendantOf.name() : __descendantOf,
        __broadcaster.name() : __broadcaster,
        __hasImage.name() : __hasImage,
        __hasLocation.name() : __hasLocation,
        __hasPrediction.name() : __hasPrediction,
        __type.name() : __type,
        __channel.name() : __channel,
        __scheduleEvent.name() : __scheduleEvent,
        __hasPortal.name() : __hasPortal,
        __portal.name() : __portal,
        __isExclusive.name() : __isExclusive,
        __exclusive.name() : __exclusive,
        __hasGeoRestriction.name() : __hasGeoRestriction,
        __geoRestriction.name() : __geoRestriction
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'or', or_)


# Complex type {urn:vpro:api:constraint:media:2013}not with content type ELEMENT_ONLY
class not_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}not with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'not')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 94, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:constraint:media:2013}and uses Python identifier and_
    __and = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'and'), 'and_', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013and', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 97, 8), )

    
    and_ = property(__and.value, __and.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}or uses Python identifier or_
    __or = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'or'), 'or_', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013or', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 98, 8), )

    
    or_ = property(__or.value, __or.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}not uses Python identifier not_
    __not = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'not'), 'not_', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013not', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 99, 8), )

    
    not_ = property(__not.value, __not.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avType uses Python identifier avType
    __avType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avType'), 'avType', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013avType', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 100, 8), )

    
    avType = property(__avType.value, __avType.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avFileFormat uses Python identifier avFileFormat
    __avFileFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), 'avFileFormat', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013avFileFormat', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 101, 8), )

    
    avFileFormat = property(__avFileFormat.value, __avFileFormat.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}avFileExtension uses Python identifier avFileExtension
    __avFileExtension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension'), 'avFileExtension', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013avFileExtension', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 102, 8), )

    
    avFileExtension = property(__avFileExtension.value, __avFileExtension.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}programUrl uses Python identifier programUrl
    __programUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), 'programUrl', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013programUrl', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 103, 8), )

    
    programUrl = property(__programUrl.value, __programUrl.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}descendantOf uses Python identifier descendantOf
    __descendantOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), 'descendantOf', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013descendantOf', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 104, 8), )

    
    descendantOf = property(__descendantOf.value, __descendantOf.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013broadcaster', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 105, 8), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasImage uses Python identifier hasImage
    __hasImage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasImage'), 'hasImage', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013hasImage', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 106, 8), )

    
    hasImage = property(__hasImage.value, __hasImage.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasLocation uses Python identifier hasLocation
    __hasLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasLocation'), 'hasLocation', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013hasLocation', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 107, 8), )

    
    hasLocation = property(__hasLocation.value, __hasLocation.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasPrediction uses Python identifier hasPrediction
    __hasPrediction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction'), 'hasPrediction', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013hasPrediction', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 108, 8), )

    
    hasPrediction = property(__hasPrediction.value, __hasPrediction.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013type', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 109, 8), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}channel uses Python identifier channel
    __channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'channel'), 'channel', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013channel', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 110, 8), )

    
    channel = property(__channel.value, __channel.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}scheduleEvent uses Python identifier scheduleEvent
    __scheduleEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), 'scheduleEvent', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013scheduleEvent', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 111, 8), )

    
    scheduleEvent = property(__scheduleEvent.value, __scheduleEvent.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasPortal uses Python identifier hasPortal
    __hasPortal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasPortal'), 'hasPortal', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013hasPortal', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 112, 8), )

    
    hasPortal = property(__hasPortal.value, __hasPortal.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portal'), 'portal', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013portal', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 113, 8), )

    
    portal = property(__portal.value, __portal.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}isExclusive uses Python identifier isExclusive
    __isExclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isExclusive'), 'isExclusive', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013isExclusive', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 114, 8), )

    
    isExclusive = property(__isExclusive.value, __isExclusive.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}exclusive uses Python identifier exclusive
    __exclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), 'exclusive', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013exclusive', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 115, 8), )

    
    exclusive = property(__exclusive.value, __exclusive.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}hasGeoRestriction uses Python identifier hasGeoRestriction
    __hasGeoRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction'), 'hasGeoRestriction', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013hasGeoRestriction', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 116, 8), )

    
    hasGeoRestriction = property(__hasGeoRestriction.value, __hasGeoRestriction.set, None, None)

    
    # Element {urn:vpro:api:constraint:media:2013}geoRestriction uses Python identifier geoRestriction
    __geoRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction'), 'geoRestriction', '__urnvproapiconstraintmedia2013_not__urnvproapiconstraintmedia2013geoRestriction', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 117, 8), )

    
    geoRestriction = property(__geoRestriction.value, __geoRestriction.set, None, None)

    _ElementMap.update({
        __and.name() : __and,
        __or.name() : __or,
        __not.name() : __not,
        __avType.name() : __avType,
        __avFileFormat.name() : __avFileFormat,
        __avFileExtension.name() : __avFileExtension,
        __programUrl.name() : __programUrl,
        __descendantOf.name() : __descendantOf,
        __broadcaster.name() : __broadcaster,
        __hasImage.name() : __hasImage,
        __hasLocation.name() : __hasLocation,
        __hasPrediction.name() : __hasPrediction,
        __type.name() : __type,
        __channel.name() : __channel,
        __scheduleEvent.name() : __scheduleEvent,
        __hasPortal.name() : __hasPortal,
        __portal.name() : __portal,
        __isExclusive.name() : __isExclusive,
        __exclusive.name() : __exclusive,
        __hasGeoRestriction.name() : __hasGeoRestriction,
        __geoRestriction.name() : __geoRestriction
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'not', not_)


# Complex type {urn:vpro:api:constraint:media:2013}programUrlConstraintType with content type SIMPLE
class programUrlConstraintType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}programUrlConstraintType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'programUrlConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 134, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute exact uses Python identifier exact
    __exact = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'exact'), 'exact', '__urnvproapiconstraintmedia2013_programUrlConstraintType_exact', pyxb.binding.datatypes.boolean)
    __exact._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 137, 8)
    __exact._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 137, 8)
    
    exact = property(__exact.value, __exact.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __exact.name() : __exact
    })
Namespace.addCategoryObject('typeBinding', 'programUrlConstraintType', programUrlConstraintType)


# Complex type {urn:vpro:api:constraint:media:2013}hasImageConstraintType with content type EMPTY
class hasImageConstraintType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}hasImageConstraintType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'hasImageConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 150, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'hasImageConstraintType', hasImageConstraintType)


# Complex type {urn:vpro:api:constraint:media:2013}hasLocationConstraintType with content type EMPTY
class hasLocationConstraintType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}hasLocationConstraintType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'hasLocationConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 154, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute platform uses Python identifier platform
    __platform = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'platform'), 'platform', '__urnvproapiconstraintmedia2013_hasLocationConstraintType_platform', pyxb.binding.datatypes.string)
    __platform._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 156, 4)
    __platform._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 156, 4)
    
    platform = property(__platform.value, __platform.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __platform.name() : __platform
    })
Namespace.addCategoryObject('typeBinding', 'hasLocationConstraintType', hasLocationConstraintType)


# Complex type {urn:vpro:api:constraint:media:2013}hasPredictionConstraintType with content type EMPTY
class hasPredictionConstraintType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}hasPredictionConstraintType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'hasPredictionConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 159, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'hasPredictionConstraintType', hasPredictionConstraintType)


# Complex type {urn:vpro:api:constraint:media:2013}hasPortalConstraintType with content type EMPTY
class hasPortalConstraintType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}hasPortalConstraintType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'hasPortalConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 177, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'hasPortalConstraintType', hasPortalConstraintType)


# Complex type {urn:vpro:api:constraint:media:2013}hasPortalRestrictionConstraintType with content type EMPTY
class hasPortalRestrictionConstraintType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}hasPortalRestrictionConstraintType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'hasPortalRestrictionConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 185, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'hasPortalRestrictionConstraintType', hasPortalRestrictionConstraintType)


# Complex type {urn:vpro:api:constraint:media:2013}hasGeoRestrictionConstraintType with content type EMPTY
class hasGeoRestrictionConstraintType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}hasGeoRestrictionConstraintType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestrictionConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 193, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'hasGeoRestrictionConstraintType', hasGeoRestrictionConstraintType)


# Complex type {urn:vpro:api:constraint:media:2013}scheduleEventType with content type EMPTY
class scheduleEventType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:media:2013}scheduleEventType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleEventType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 171, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__urnvproapiconstraintmedia2013_scheduleEventType_date', pyxb.binding.datatypes.string)
    __date._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 173, 4)
    __date._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 173, 4)
    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute operator uses Python identifier operator
    __operator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'operator'), 'operator', '__urnvproapiconstraintmedia2013_scheduleEventType_operator', _ImportedBinding_npoapi_xml_api_constraint.operatorType)
    __operator._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 174, 4)
    __operator._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 174, 4)
    
    operator = property(__operator.value, __operator.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __date.name() : __date,
        __operator.name() : __operator
    })
Namespace.addCategoryObject('typeBinding', 'scheduleEventType', scheduleEventType)


filter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 6, 2))
Namespace.addCategoryObject('elementBinding', filter.name().localName(), filter)



filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'and'), and_, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 11, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'or'), or_, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 12, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'not'), not_, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 13, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avType'), avTypeConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 14, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), avFileFormatConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 15, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension'), avFileExtensionConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 16, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), programUrlConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 17, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), descendantOfConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 18, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), broadcasterConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 19, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasImage'), hasImageConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 20, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasLocation'), hasLocationConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 21, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction'), hasPredictionConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 22, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), typeConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 23, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'channel'), channelConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 24, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), scheduleEventType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 25, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasPortal'), hasPortalConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 26, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portal'), portalConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 27, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isExclusive'), hasPortalRestrictionConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 30, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), portalRestrictionConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 31, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction'), hasGeoRestrictionConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 32, 8)))

filter_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction'), geoRestrictionConstraintType, scope=filter_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 33, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 10, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'and')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 11, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'or')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 12, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'not')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 13, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avType')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 14, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 15, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 16, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'programUrl')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 17, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 18, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 19, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasImage')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 20, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasLocation')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 21, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 22, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 23, 8))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'channel')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 24, 8))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 25, 8))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasPortal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 26, 8))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 27, 8))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasPortal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 28, 8))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 29, 8))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isExclusive')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 30, 8))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 31, 8))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 32, 8))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(filter_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 33, 8))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_22._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
filter_._Automaton = _BuildAutomaton()




and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'and'), and_, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 41, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'or'), or_, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 42, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'not'), not_, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 43, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avType'), avTypeConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 44, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), avFileFormatConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 45, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension'), avFileExtensionConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 46, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), programUrlConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 47, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), descendantOfConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 48, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), broadcasterConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 49, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasImage'), hasImageConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 50, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasLocation'), hasLocationConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 51, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction'), hasPredictionConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 52, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), typeConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 53, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'channel'), channelConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 54, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), scheduleEventType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 55, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasPortal'), hasPortalConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 56, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portal'), portalConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 57, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isExclusive'), hasPortalRestrictionConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 58, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), portalRestrictionConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 59, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction'), hasGeoRestrictionConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 60, 8)))

and_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction'), geoRestrictionConstraintType, scope=and_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 61, 8)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 40, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'and')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 41, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'or')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 42, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'not')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 43, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avType')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 44, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 45, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 46, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'programUrl')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 47, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 48, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 49, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasImage')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 50, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasLocation')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 51, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 52, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 53, 8))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'channel')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 54, 8))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 55, 8))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasPortal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 56, 8))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 57, 8))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isExclusive')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 58, 8))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 59, 8))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 60, 8))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(and_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 61, 8))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
and_._Automaton = _BuildAutomaton_()




or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'and'), and_, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 69, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'or'), or_, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 70, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'not'), not_, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 71, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avType'), avTypeConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 72, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), avFileFormatConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 73, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension'), avFileExtensionConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 74, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), programUrlConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 75, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), descendantOfConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 76, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), broadcasterConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 77, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasImage'), hasImageConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 78, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasLocation'), hasLocationConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 79, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction'), hasPredictionConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 80, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), typeConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 81, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'channel'), channelConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 82, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), scheduleEventType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 83, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasPortal'), hasPortalConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 84, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portal'), portalConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 85, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isExclusive'), hasPortalRestrictionConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 86, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), portalRestrictionConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 87, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction'), hasGeoRestrictionConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 88, 8)))

or_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction'), geoRestrictionConstraintType, scope=or_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 89, 8)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 68, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'and')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 69, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'or')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 70, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'not')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 71, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avType')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 72, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 73, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 74, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'programUrl')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 75, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 76, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 77, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasImage')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 78, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasLocation')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 79, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 80, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 81, 8))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'channel')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 82, 8))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 83, 8))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasPortal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 84, 8))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 85, 8))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isExclusive')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 86, 8))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 87, 8))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 88, 8))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(or_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 89, 8))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
or_._Automaton = _BuildAutomaton_2()




not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'and'), and_, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 97, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'or'), or_, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 98, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'not'), not_, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 99, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avType'), avTypeConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 100, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), avFileFormatConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 101, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension'), avFileExtensionConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 102, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), programUrlConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 103, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), descendantOfConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 104, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), broadcasterConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 105, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasImage'), hasImageConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 106, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasLocation'), hasLocationConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 107, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction'), hasPredictionConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 108, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), typeConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 109, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'channel'), channelConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 110, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), scheduleEventType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 111, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasPortal'), hasPortalConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 112, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portal'), portalConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 113, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isExclusive'), hasPortalRestrictionConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 114, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), portalRestrictionConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 115, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction'), hasGeoRestrictionConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 116, 8)))

not_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction'), geoRestrictionConstraintType, scope=not_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 117, 8)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 96, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'and')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 97, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'or')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 98, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'not')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 99, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avType')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 100, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 101, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileExtension')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 102, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'programUrl')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 103, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 104, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 105, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasImage')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 106, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasLocation')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 107, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasPrediction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 108, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 109, 8))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'channel')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 110, 8))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 111, 8))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasPortal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 112, 8))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 113, 8))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isExclusive')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 114, 8))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 115, 8))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasGeoRestriction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 116, 8))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(not_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geoRestriction')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 117, 8))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
not_._Automaton = _BuildAutomaton_3()

