# ./npoapi/xml/media_search.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c9f1e5fb53f06c35ed1f8bfb94927ecdc3fc6078
# Generated 2016-08-24 12:53:35.859385 by PyXB version 1.2.4 using Python 3.5.0.final.0
# Namespace urn:vpro:media:search:2012

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ff62ef9e-69e8-11e6-b94f-60fb42f0af34')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import npoapi.xml.shared as _ImportedBinding_npoapi_xml_shared
import npoapi.xml.media as _ImportedBinding_npoapi_xml_media

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:media:search:2012', create_if_missing=True)
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 70, 8)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.integer(0), value_datatype=STD_ANON)
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 77, 8)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.integer(0), value_datatype=STD_ANON_)
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 85, 8)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_2)
STD_ANON_2.ASC = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='ASC', tag='ASC')
STD_ANON_2.DESC = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='DESC', tag='DESC')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 122, 6)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_3)
STD_ANON_3.ASC = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ASC', tag='ASC')
STD_ANON_3.DESC = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='DESC', tag='DESC')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Complex type {urn:vpro:media:search:2012}mediaFormType with content type ELEMENT_ONLY
class mediaFormType (pyxb.binding.basis.complexTypeDefinition):
    """

      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaFormType')
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 16, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:search:2012}pager uses Python identifier pager
    __pager = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pager'), 'pager', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012pager', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 23, 6), )

    
    pager = property(__pager.value, __pager.set, None, None)

    
    # Element {urn:vpro:media:search:2012}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012broadcaster', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 24, 6), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Element {urn:vpro:media:search:2012}portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portal'), 'portal', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012portal', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 25, 6), )

    
    portal = property(__portal.value, __portal.set, None, None)

    
    # Element {urn:vpro:media:search:2012}text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'text'), 'text', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012text', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 30, 6), )

    
    text = property(__text.value, __text.set, None, None)

    
    # Element {urn:vpro:media:search:2012}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012title', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 31, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:media:search:2012}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012type', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 42, 6), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {urn:vpro:media:search:2012}releaseYear uses Python identifier releaseYear
    __releaseYear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'releaseYear'), 'releaseYear', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012releaseYear', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 43, 6), )

    
    releaseYear = property(__releaseYear.value, __releaseYear.set, None, None)

    
    # Element {urn:vpro:media:search:2012}relation uses Python identifier relation
    __relation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relation'), 'relation', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012relation', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 44, 6), )

    
    relation = property(__relation.value, __relation.set, None, None)

    
    # Element {urn:vpro:media:search:2012}noBroadcast uses Python identifier noBroadcast
    __noBroadcast = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'noBroadcast'), 'noBroadcast', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012noBroadcast', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 45, 6), )

    
    noBroadcast = property(__noBroadcast.value, __noBroadcast.set, None, None)

    
    # Element {urn:vpro:media:search:2012}hasLocations uses Python identifier hasLocations
    __hasLocations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasLocations'), 'hasLocations', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012hasLocations', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 46, 6), )

    
    hasLocations = property(__hasLocations.value, __hasLocations.set, None, None)

    
    # Element {urn:vpro:media:search:2012}noPlaylist uses Python identifier noPlaylist
    __noPlaylist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'noPlaylist'), 'noPlaylist', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012noPlaylist', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 47, 6), )

    
    noPlaylist = property(__noPlaylist.value, __noPlaylist.set, None, None)

    
    # Element {urn:vpro:media:search:2012}sortRange uses Python identifier sortRange
    __sortRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortRange'), 'sortRange', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012sortRange', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 48, 6), )

    
    sortRange = property(__sortRange.value, __sortRange.set, None, None)

    
    # Element {urn:vpro:media:search:2012}eventRange uses Python identifier eventRange
    __eventRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eventRange'), 'eventRange', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012eventRange', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 49, 6), )

    
    eventRange = property(__eventRange.value, __eventRange.set, None, None)

    
    # Element {urn:vpro:media:search:2012}channel uses Python identifier channel
    __channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'channel'), 'channel', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012channel', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 50, 6), )

    
    channel = property(__channel.value, __channel.set, None, None)

    
    # Element {urn:vpro:media:search:2012}createdBy uses Python identifier createdBy
    __createdBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'createdBy'), 'createdBy', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012createdBy', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 51, 6), )

    
    createdBy = property(__createdBy.value, __createdBy.set, None, None)

    
    # Element {urn:vpro:media:search:2012}creationRange uses Python identifier creationRange
    __creationRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creationRange'), 'creationRange', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012creationRange', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 52, 6), )

    
    creationRange = property(__creationRange.value, __creationRange.set, None, None)

    
    # Element {urn:vpro:media:search:2012}lastModifiedBy uses Python identifier lastModifiedBy
    __lastModifiedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastModifiedBy'), 'lastModifiedBy', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012lastModifiedBy', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 53, 6), )

    
    lastModifiedBy = property(__lastModifiedBy.value, __lastModifiedBy.set, None, None)

    
    # Element {urn:vpro:media:search:2012}lastModifiedRange uses Python identifier lastModifiedRange
    __lastModifiedRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastModifiedRange'), 'lastModifiedRange', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012lastModifiedRange', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 54, 6), )

    
    lastModifiedRange = property(__lastModifiedRange.value, __lastModifiedRange.set, None, None)

    
    # Element {urn:vpro:media:search:2012}tag uses Python identifier tag
    __tag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tag'), 'tag', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012tag', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 55, 6), )

    
    tag = property(__tag.value, __tag.set, None, None)

    
    # Element {urn:vpro:media:search:2012}avType uses Python identifier avType
    __avType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avType'), 'avType', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012avType', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 56, 6), )

    
    avType = property(__avType.value, __avType.set, None, None)

    
    # Element {urn:vpro:media:search:2012}notAnEpisode uses Python identifier notAnEpisode
    __notAnEpisode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notAnEpisode'), 'notAnEpisode', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012notAnEpisode', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 57, 6), )

    
    notAnEpisode = property(__notAnEpisode.value, __notAnEpisode.set, None, None)

    
    # Element {urn:vpro:media:search:2012}findDeleted uses Python identifier findDeleted
    __findDeleted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'findDeleted'), 'findDeleted', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012findDeleted', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 58, 6), )

    
    findDeleted = property(__findDeleted.value, __findDeleted.set, None, None)

    
    # Element {urn:vpro:media:search:2012}excludedMid uses Python identifier excludedMid
    __excludedMid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'excludedMid'), 'excludedMid', '__urnvpromediasearch2012_mediaFormType_urnvpromediasearch2012excludedMid', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 59, 6), )

    
    excludedMid = property(__excludedMid.value, __excludedMid.set, None, None)

    _ElementMap.update({
        __pager.name() : __pager,
        __broadcaster.name() : __broadcaster,
        __portal.name() : __portal,
        __text.name() : __text,
        __title.name() : __title,
        __type.name() : __type,
        __releaseYear.name() : __releaseYear,
        __relation.name() : __relation,
        __noBroadcast.name() : __noBroadcast,
        __hasLocations.name() : __hasLocations,
        __noPlaylist.name() : __noPlaylist,
        __sortRange.name() : __sortRange,
        __eventRange.name() : __eventRange,
        __channel.name() : __channel,
        __createdBy.name() : __createdBy,
        __creationRange.name() : __creationRange,
        __lastModifiedBy.name() : __lastModifiedBy,
        __lastModifiedRange.name() : __lastModifiedRange,
        __tag.name() : __tag,
        __avType.name() : __avType,
        __notAnEpisode.name() : __notAnEpisode,
        __findDeleted.name() : __findDeleted,
        __excludedMid.name() : __excludedMid
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaFormType', mediaFormType)


# Complex type {urn:vpro:media:search:2012}pagerType with content type ELEMENT_ONLY
class pagerType (pyxb.binding.basis.complexTypeDefinition):
    """
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pagerType')
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 63, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:search:2012}offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'offset'), 'offset', '__urnvpromediasearch2012_pagerType_urnvpromediasearch2012offset', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 69, 6), )

    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Element {urn:vpro:media:search:2012}max uses Python identifier max
    __max = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'max'), 'max', '__urnvpromediasearch2012_pagerType_urnvpromediasearch2012max', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 76, 6), )

    
    max = property(__max.value, __max.set, None, None)

    
    # Element {urn:vpro:media:search:2012}sort uses Python identifier sort
    __sort = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sort'), 'sort', '__urnvpromediasearch2012_pagerType_urnvpromediasearch2012sort', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 83, 6), )

    
    sort = property(__sort.value, __sort.set, None, None)

    
    # Element {urn:vpro:media:search:2012}order uses Python identifier order
    __order = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'order'), 'order', '__urnvpromediasearch2012_pagerType_urnvpromediasearch2012order', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 84, 6), )

    
    order = property(__order.value, __order.set, None, None)

    _ElementMap.update({
        __offset.name() : __offset,
        __max.name() : __max,
        __sort.name() : __sort,
        __order.name() : __order
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pagerType', pagerType)


# Complex type {urn:vpro:media:search:2012}dateRangeType with content type ELEMENT_ONLY
class dateRangeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:search:2012}dateRangeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateRangeType')
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 105, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:search:2012}start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'start'), 'start', '__urnvpromediasearch2012_dateRangeType_urnvpromediasearch2012start', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 107, 6), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element {urn:vpro:media:search:2012}stop uses Python identifier stop
    __stop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stop'), 'stop', '__urnvpromediasearch2012_dateRangeType_urnvpromediasearch2012stop', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 108, 6), )

    
    stop = property(__stop.value, __stop.set, None, None)

    _ElementMap.update({
        __start.name() : __start,
        __stop.name() : __stop
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'dateRangeType', dateRangeType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 32, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediasearch2012_CTD_ANON_type', _ImportedBinding_npoapi_xml_media.textualTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 35, 14)
    __type._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 35, 14)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner'), 'owner', '__urnvpromediasearch2012_CTD_ANON_owner', _ImportedBinding_npoapi_xml_shared.ownerTypeEnum)
    __owner._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 36, 14)
    __owner._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 36, 14)
    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Attribute tokenized uses Python identifier tokenized
    __tokenized = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tokenized'), 'tokenized', '__urnvpromediasearch2012_CTD_ANON_tokenized', pyxb.binding.datatypes.boolean, unicode_default='false')
    __tokenized._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 37, 14)
    __tokenized._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 37, 14)
    
    tokenized = property(__tokenized.value, __tokenized.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __owner.name() : __owner,
        __tokenized.name() : __tokenized
    })



# Complex type {urn:vpro:media:search:2012}relationFormType with content type SIMPLE
class relationFormType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:search:2012}relationFormType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relationFormType')
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 95, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromediasearch2012_relationFormType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 98, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 98, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'broadcaster'), 'broadcaster', '__urnvpromediasearch2012_relationFormType_broadcaster', _ImportedBinding_npoapi_xml_media.organizationIdType)
    __broadcaster._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 99, 8)
    __broadcaster._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 99, 8)
    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Attribute uriRef uses Python identifier uriRef
    __uriRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uriRef'), 'uriRef', '__urnvpromediasearch2012_relationFormType_uriRef', pyxb.binding.datatypes.string)
    __uriRef._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 100, 8)
    __uriRef._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 100, 8)
    
    uriRef = property(__uriRef.value, __uriRef.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __broadcaster.name() : __broadcaster,
        __uriRef.name() : __uriRef
    })
Namespace.addCategoryObject('typeBinding', 'relationFormType', relationFormType)


# Complex type {urn:vpro:media:search:2012}mediaListResultType with content type ELEMENT_ONLY
class mediaListResultType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:search:2012}mediaListResultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaListResultType')
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 112, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:search:2012}item uses Python identifier item
    __item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'item'), 'item', '__urnvpromediasearch2012_mediaListResultType_urnvpromediasearch2012item', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 114, 6), )

    
    item = property(__item.value, __item.set, None, None)

    
    # Attribute totalCount uses Python identifier totalCount
    __totalCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'totalCount'), 'totalCount', '__urnvpromediasearch2012_mediaListResultType_totalCount', pyxb.binding.datatypes.long)
    __totalCount._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 116, 4)
    __totalCount._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 116, 4)
    
    totalCount = property(__totalCount.value, __totalCount.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offset'), 'offset', '__urnvpromediasearch2012_mediaListResultType_offset', pyxb.binding.datatypes.long)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 117, 4)
    __offset._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 117, 4)
    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__urnvpromediasearch2012_mediaListResultType_max', pyxb.binding.datatypes.integer)
    __max._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 118, 4)
    __max._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 118, 4)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__urnvpromediasearch2012_mediaListResultType_size', pyxb.binding.datatypes.integer)
    __size._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 119, 4)
    __size._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 119, 4)
    
    size = property(__size.value, __size.set, None, None)

    
    # Attribute sort uses Python identifier sort
    __sort = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sort'), 'sort', '__urnvpromediasearch2012_mediaListResultType_sort', pyxb.binding.datatypes.string)
    __sort._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 120, 4)
    __sort._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 120, 4)
    
    sort = property(__sort.value, __sort.set, None, None)

    
    # Attribute order uses Python identifier order
    __order = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'order'), 'order', '__urnvpromediasearch2012_mediaListResultType_order', STD_ANON_3)
    __order._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 121, 4)
    __order._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 121, 4)
    
    order = property(__order.value, __order.set, None, None)

    _ElementMap.update({
        __item.name() : __item
    })
    _AttributeMap.update({
        __totalCount.name() : __totalCount,
        __offset.name() : __offset,
        __max.name() : __max,
        __size.name() : __size,
        __sort.name() : __sort,
        __order.name() : __order
    })
Namespace.addCategoryObject('typeBinding', 'mediaListResultType', mediaListResultType)


# Complex type {urn:vpro:media:search:2012}publishableListItem with content type EMPTY
class publishableListItem (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:search:2012}publishableListItem with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'publishableListItem')
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 162, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__urnvpromediasearch2012_publishableListItem_id', pyxb.binding.datatypes.long)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 164, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 164, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvpromediasearch2012_publishableListItem_urn', pyxb.binding.datatypes.string)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 165, 4)
    __urn._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 165, 4)
    
    urn = property(__urn.value, __urn.set, None, None)

    
    # Attribute workflow uses Python identifier workflow
    __workflow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'workflow'), 'workflow', '__urnvpromediasearch2012_publishableListItem_workflow', _ImportedBinding_npoapi_xml_shared.workflowEnumType)
    __workflow._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 166, 4)
    __workflow._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 166, 4)
    
    workflow = property(__workflow.value, __workflow.set, None, None)

    
    # Attribute deleted uses Python identifier deleted
    __deleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deleted'), 'deleted', '__urnvpromediasearch2012_publishableListItem_deleted', pyxb.binding.datatypes.boolean)
    __deleted._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 167, 4)
    __deleted._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 167, 4)
    
    deleted = property(__deleted.value, __deleted.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __urn.name() : __urn,
        __workflow.name() : __workflow,
        __deleted.name() : __deleted
    })
Namespace.addCategoryObject('typeBinding', 'publishableListItem', publishableListItem)


# Complex type {urn:vpro:media:search:2012}mediaListItem with content type ELEMENT_ONLY
class mediaListItem (publishableListItem):
    """Complex type {urn:vpro:media:search:2012}mediaListItem with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaListItem')
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 132, 2)
    _ElementMap = publishableListItem._ElementMap.copy()
    _AttributeMap = publishableListItem._AttributeMap.copy()
    # Base type is publishableListItem
    
    # Element {urn:vpro:media:search:2012}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012broadcaster', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 136, 10), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Element {urn:vpro:media:search:2012}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012title', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 137, 10), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:media:search:2012}subTitle uses Python identifier subTitle
    __subTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subTitle'), 'subTitle', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012subTitle', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 138, 10), )

    
    subTitle = property(__subTitle.value, __subTitle.set, None, None)

    
    # Element {urn:vpro:media:search:2012}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012description', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 139, 10), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:media:search:2012}creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creationDate'), 'creationDate', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012creationDate', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 140, 10), )

    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Element {urn:vpro:media:search:2012}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), 'lastModified', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012lastModified', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 141, 10), )

    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Element {urn:vpro:media:search:2012}createdBy uses Python identifier createdBy
    __createdBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'createdBy'), 'createdBy', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012createdBy', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 142, 10), )

    
    createdBy = property(__createdBy.value, __createdBy.set, None, None)

    
    # Element {urn:vpro:media:search:2012}lastModifiedBy uses Python identifier lastModifiedBy
    __lastModifiedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastModifiedBy'), 'lastModifiedBy', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012lastModifiedBy', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 143, 10), )

    
    lastModifiedBy = property(__lastModifiedBy.value, __lastModifiedBy.set, None, None)

    
    # Element {urn:vpro:media:search:2012}sortDate uses Python identifier sortDate
    __sortDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortDate'), 'sortDate', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012sortDate', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 144, 10), )

    
    sortDate = property(__sortDate.value, __sortDate.set, None, None)

    
    # Element {urn:vpro:media:search:2012}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012type', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 145, 10), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {urn:vpro:media:search:2012}publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'publishStart'), 'publishStart', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012publishStart', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 146, 10), )

    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Element {urn:vpro:media:search:2012}publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'publishStop'), 'publishStop', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012publishStop', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 147, 10), )

    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    
    # Element {urn:vpro:media:search:2012}lastPublished uses Python identifier lastPublished
    __lastPublished = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastPublished'), 'lastPublished', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012lastPublished', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 148, 10), )

    
    lastPublished = property(__lastPublished.value, __lastPublished.set, None, None)

    
    # Element {urn:vpro:media:search:2012}firstScheduleEvent uses Python identifier firstScheduleEvent
    __firstScheduleEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstScheduleEvent'), 'firstScheduleEvent', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012firstScheduleEvent', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 149, 10), )

    
    firstScheduleEvent = property(__firstScheduleEvent.value, __firstScheduleEvent.set, None, None)

    
    # Element {urn:vpro:media:search:2012}locations uses Python identifier locations
    __locations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'locations'), 'locations', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012locations', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 150, 10), )

    
    locations = property(__locations.value, __locations.set, None, None)

    
    # Element {urn:vpro:media:search:2012}tag uses Python identifier tag
    __tag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tag'), 'tag', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012tag', True, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 151, 10), )

    
    tag = property(__tag.value, __tag.set, None, None)

    
    # Element {urn:vpro:media:search:2012}image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'image'), 'image', '__urnvpromediasearch2012_mediaListItem_urnvpromediasearch2012image', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 152, 10), )

    
    image = property(__image.value, __image.set, None, None)

    
    # Attribute mid uses Python identifier mid
    __mid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mid'), 'mid', '__urnvpromediasearch2012_mediaListItem_mid', pyxb.binding.datatypes.string)
    __mid._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 154, 8)
    __mid._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 154, 8)
    
    mid = property(__mid.value, __mid.set, None, None)

    
    # Attribute avType uses Python identifier avType
    __avType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avType'), 'avType', '__urnvpromediasearch2012_mediaListItem_avType', _ImportedBinding_npoapi_xml_media.avTypeEnum)
    __avType._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 155, 8)
    __avType._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 155, 8)
    
    avType = property(__avType.value, __avType.set, None, None)

    
    # Attribute mediaType uses Python identifier mediaType
    __mediaType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mediaType'), 'mediaType', '__urnvpromediasearch2012_mediaListItem_mediaType', pyxb.binding.datatypes.string)
    __mediaType._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 156, 8)
    __mediaType._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 156, 8)
    
    mediaType = property(__mediaType.value, __mediaType.set, None, None)

    
    # Attribute episodesLocked uses Python identifier episodesLocked
    __episodesLocked = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'episodesLocked'), 'episodesLocked', '__urnvpromediasearch2012_mediaListItem_episodesLocked', pyxb.binding.datatypes.boolean)
    __episodesLocked._DeclarationLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 157, 8)
    __episodesLocked._UseLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 157, 8)
    
    episodesLocked = property(__episodesLocked.value, __episodesLocked.set, None, None)

    
    # Attribute id inherited from {urn:vpro:media:search:2012}publishableListItem
    
    # Attribute urn inherited from {urn:vpro:media:search:2012}publishableListItem
    
    # Attribute workflow inherited from {urn:vpro:media:search:2012}publishableListItem
    
    # Attribute deleted inherited from {urn:vpro:media:search:2012}publishableListItem
    _ElementMap.update({
        __broadcaster.name() : __broadcaster,
        __title.name() : __title,
        __subTitle.name() : __subTitle,
        __description.name() : __description,
        __creationDate.name() : __creationDate,
        __lastModified.name() : __lastModified,
        __createdBy.name() : __createdBy,
        __lastModifiedBy.name() : __lastModifiedBy,
        __sortDate.name() : __sortDate,
        __type.name() : __type,
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop,
        __lastPublished.name() : __lastPublished,
        __firstScheduleEvent.name() : __firstScheduleEvent,
        __locations.name() : __locations,
        __tag.name() : __tag,
        __image.name() : __image
    })
    _AttributeMap.update({
        __mid.name() : __mid,
        __avType.name() : __avType,
        __mediaType.name() : __mediaType,
        __episodesLocked.name() : __episodesLocked
    })
Namespace.addCategoryObject('typeBinding', 'mediaListItem', mediaListItem)


# Complex type {urn:vpro:media:search:2012}imageListItem with content type EMPTY
class imageListItem (publishableListItem):
    """Complex type {urn:vpro:media:search:2012}imageListItem with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageListItem')
    _XSDLocation = pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 170, 2)
    _ElementMap = publishableListItem._ElementMap.copy()
    _AttributeMap = publishableListItem._AttributeMap.copy()
    # Base type is publishableListItem
    
    # Attribute id inherited from {urn:vpro:media:search:2012}publishableListItem
    
    # Attribute urn inherited from {urn:vpro:media:search:2012}publishableListItem
    
    # Attribute workflow inherited from {urn:vpro:media:search:2012}publishableListItem
    
    # Attribute deleted inherited from {urn:vpro:media:search:2012}publishableListItem
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'imageListItem', imageListItem)


mediaForm = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaForm'), mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 12, 2))
Namespace.addCategoryObject('elementBinding', mediaForm.name().localName(), mediaForm)

list = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'list'), mediaListResultType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 14, 2))
Namespace.addCategoryObject('elementBinding', list.name().localName(), list)



mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pager'), pagerType, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 23, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), pyxb.binding.datatypes.string, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 24, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portal'), pyxb.binding.datatypes.string, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 25, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'text'), pyxb.binding.datatypes.string, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 30, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), CTD_ANON, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 31, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), _ImportedBinding_npoapi_xml_media.mediaTypeEnum, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 42, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'releaseYear'), pyxb.binding.datatypes.short, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 43, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relation'), relationFormType, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 44, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'noBroadcast'), pyxb.binding.datatypes.boolean, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 45, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasLocations'), pyxb.binding.datatypes.boolean, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 46, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'noPlaylist'), pyxb.binding.datatypes.boolean, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 47, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortRange'), dateRangeType, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 48, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eventRange'), dateRangeType, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 49, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'channel'), pyxb.binding.datatypes.string, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 50, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'createdBy'), pyxb.binding.datatypes.string, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 51, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creationRange'), dateRangeType, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 52, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastModifiedBy'), pyxb.binding.datatypes.string, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 53, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastModifiedRange'), dateRangeType, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 54, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tag'), pyxb.binding.datatypes.string, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 55, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avType'), _ImportedBinding_npoapi_xml_media.avTypeEnum, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 56, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notAnEpisode'), pyxb.binding.datatypes.boolean, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 57, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'findDeleted'), pyxb.binding.datatypes.boolean, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 58, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'excludedMid'), pyxb.binding.datatypes.string, scope=mediaFormType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 59, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 24, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 25, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 30, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 31, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 42, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 43, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 44, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 45, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 46, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 47, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 48, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 49, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 50, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 51, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 52, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 53, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 54, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 55, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 56, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 57, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 58, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 59, 6))
    counters.add(cc_21)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pager')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 23, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 25, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'text')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 30, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 31, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 42, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releaseYear')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 43, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 44, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'noBroadcast')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 45, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasLocations')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 46, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'noPlaylist')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 47, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortRange')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 48, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eventRange')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 49, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'channel')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 50, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'createdBy')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 51, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creationRange')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 52, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastModifiedBy')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 53, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastModifiedRange')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 54, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 55, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avType')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 56, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notAnEpisode')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 57, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'findDeleted')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 58, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'excludedMid')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 59, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
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
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
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
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
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
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
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
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
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
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
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
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
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
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, True) ]))
    st_22._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mediaFormType._Automaton = _BuildAutomaton()




pagerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offset'), STD_ANON, scope=pagerType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 69, 6)))

pagerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'max'), STD_ANON_, scope=pagerType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 76, 6)))

pagerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sort'), pyxb.binding.datatypes.string, scope=pagerType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 83, 6)))

pagerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'order'), STD_ANON_2, scope=pagerType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 84, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 69, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 83, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 84, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pagerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'offset')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 69, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(pagerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 76, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pagerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sort')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 83, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pagerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'order')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 84, 6))
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
pagerType._Automaton = _BuildAutomaton_()




dateRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'start'), pyxb.binding.datatypes.dateTime, scope=dateRangeType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 107, 6)))

dateRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stop'), pyxb.binding.datatypes.dateTime, scope=dateRangeType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 108, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 107, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 108, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'start')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 107, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stop')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 108, 6))
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
dateRangeType._Automaton = _BuildAutomaton_2()




mediaListResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'item'), mediaListItem, scope=mediaListResultType, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 114, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 114, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaListResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'item')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 114, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaListResultType._Automaton = _BuildAutomaton_3()




mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), _ImportedBinding_npoapi_xml_media.organizationType, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 136, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), pyxb.binding.datatypes.string, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 137, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subTitle'), pyxb.binding.datatypes.string, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 138, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 139, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creationDate'), pyxb.binding.datatypes.dateTime, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 140, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), pyxb.binding.datatypes.dateTime, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 141, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'createdBy'), pyxb.binding.datatypes.string, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 142, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastModifiedBy'), pyxb.binding.datatypes.string, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 143, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortDate'), pyxb.binding.datatypes.dateTime, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 144, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), _ImportedBinding_npoapi_xml_media.mediaTypeEnum, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 145, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'publishStart'), pyxb.binding.datatypes.dateTime, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 146, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'publishStop'), pyxb.binding.datatypes.dateTime, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 147, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastPublished'), pyxb.binding.datatypes.dateTime, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 148, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstScheduleEvent'), _ImportedBinding_npoapi_xml_media.scheduleEventType, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 149, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locations'), _ImportedBinding_npoapi_xml_media.locationType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 150, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tag'), _ImportedBinding_npoapi_xml_media.tagType, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 151, 10)))

mediaListItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'image'), imageListItem, scope=mediaListItem, location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 152, 10)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 138, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 139, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 141, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 143, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 144, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 146, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 147, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 148, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 149, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 150, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 151, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 152, 10))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 136, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 137, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subTitle')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 138, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 139, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creationDate')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 140, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastModified')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 141, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'createdBy')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 142, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastModifiedBy')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 143, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortDate')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 144, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 145, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'publishStart')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 146, 10))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'publishStop')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 147, 10))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastPublished')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 148, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstScheduleEvent')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 149, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 150, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 151, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(mediaListItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'image')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/search/vproMediaSearch.xsd', 152, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
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
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, True) ]))
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
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, True) ]))
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mediaListItem._Automaton = _BuildAutomaton_4()

