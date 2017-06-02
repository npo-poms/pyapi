# ./npoapi/xml/media.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:aaac8a39e00bcd1804b49bf5b5b8b83fb686b430
# Generated 2017-06-02 17:13:48.878989 by PyXB version 1.2.5 using Python 3.5.0.final.0
# Namespace urn:vpro:media:2009 [xmlns:media]

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
import pyxb.binding.xml_
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:media:2009', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_shared = _ImportedBinding_npoapi_xml_shared.Namespace
_Namespace_shared.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {urn:vpro:media:2009}mediaTypeEnum
class mediaTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 113, 2)
    _Documentation = None
mediaTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=mediaTypeEnum)
mediaTypeEnum.MEDIA = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='MEDIA', tag='MEDIA')
mediaTypeEnum.STRAND = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='STRAND', tag='STRAND')
mediaTypeEnum.ALBUM = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='ALBUM', tag='ALBUM')
mediaTypeEnum.PLAYLIST = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='PLAYLIST', tag='PLAYLIST')
mediaTypeEnum.ARCHIVE = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='ARCHIVE', tag='ARCHIVE')
mediaTypeEnum.UG_ARCHIVE = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='UG ARCHIVE', tag='UG_ARCHIVE')
mediaTypeEnum.SEASON = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='SEASON', tag='SEASON')
mediaTypeEnum.SERIES = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='SERIES', tag='SERIES')
mediaTypeEnum.UMBRELLA = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='UMBRELLA', tag='UMBRELLA')
mediaTypeEnum.BROADCAST = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='BROADCAST', tag='BROADCAST')
mediaTypeEnum.MOVIE = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='MOVIE', tag='MOVIE')
mediaTypeEnum.TRAILER = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='TRAILER', tag='TRAILER')
mediaTypeEnum.CLIP = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='CLIP', tag='CLIP')
mediaTypeEnum.STRAND_ = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='STRAND', tag='STRAND_')
mediaTypeEnum.TRACK = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='TRACK', tag='TRACK')
mediaTypeEnum.SEGMENT = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='SEGMENT', tag='SEGMENT')
mediaTypeEnum.VISUALRADIO = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='VISUALRADIO', tag='VISUALRADIO')
mediaTypeEnum.PROMO = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='PROMO', tag='PROMO')
mediaTypeEnum.RECORDING = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='RECORDING', tag='RECORDING')
mediaTypeEnum.COLLECTION = mediaTypeEnum._CF_enumeration.addEnumeration(unicode_value='COLLECTION', tag='COLLECTION')
mediaTypeEnum._InitializeFacetMap(mediaTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'mediaTypeEnum', mediaTypeEnum)
_module_typeBindings.mediaTypeEnum = mediaTypeEnum

# Atomic simple type: {urn:vpro:media:2009}groupTypeEnum
class groupTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'groupTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 138, 2)
    _Documentation = None
groupTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=groupTypeEnum)
groupTypeEnum.STRAND = groupTypeEnum._CF_enumeration.addEnumeration(unicode_value='STRAND', tag='STRAND')
groupTypeEnum.ALBUM = groupTypeEnum._CF_enumeration.addEnumeration(unicode_value='ALBUM', tag='ALBUM')
groupTypeEnum.PLAYLIST = groupTypeEnum._CF_enumeration.addEnumeration(unicode_value='PLAYLIST', tag='PLAYLIST')
groupTypeEnum.ARCHIVE = groupTypeEnum._CF_enumeration.addEnumeration(unicode_value='ARCHIVE', tag='ARCHIVE')
groupTypeEnum.COLLECTION = groupTypeEnum._CF_enumeration.addEnumeration(unicode_value='COLLECTION', tag='COLLECTION')
groupTypeEnum.SEASON = groupTypeEnum._CF_enumeration.addEnumeration(unicode_value='SEASON', tag='SEASON')
groupTypeEnum.SERIES = groupTypeEnum._CF_enumeration.addEnumeration(unicode_value='SERIES', tag='SERIES')
groupTypeEnum.UMBRELLA = groupTypeEnum._CF_enumeration.addEnumeration(unicode_value='UMBRELLA', tag='UMBRELLA')
groupTypeEnum._InitializeFacetMap(groupTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'groupTypeEnum', groupTypeEnum)
_module_typeBindings.groupTypeEnum = groupTypeEnum

# Atomic simple type: {urn:vpro:media:2009}programTypeEnum
class programTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'programTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 151, 2)
    _Documentation = None
programTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=programTypeEnum)
programTypeEnum.BROADCAST = programTypeEnum._CF_enumeration.addEnumeration(unicode_value='BROADCAST', tag='BROADCAST')
programTypeEnum.MOVIE = programTypeEnum._CF_enumeration.addEnumeration(unicode_value='MOVIE', tag='MOVIE')
programTypeEnum.TRAILER = programTypeEnum._CF_enumeration.addEnumeration(unicode_value='TRAILER', tag='TRAILER')
programTypeEnum.CLIP = programTypeEnum._CF_enumeration.addEnumeration(unicode_value='CLIP', tag='CLIP')
programTypeEnum.STRAND = programTypeEnum._CF_enumeration.addEnumeration(unicode_value='STRAND', tag='STRAND')
programTypeEnum.TRACK = programTypeEnum._CF_enumeration.addEnumeration(unicode_value='TRACK', tag='TRACK')
programTypeEnum.VISUALRADIO = programTypeEnum._CF_enumeration.addEnumeration(unicode_value='VISUALRADIO', tag='VISUALRADIO')
programTypeEnum.PROMO = programTypeEnum._CF_enumeration.addEnumeration(unicode_value='PROMO', tag='PROMO')
programTypeEnum.RECORDING = programTypeEnum._CF_enumeration.addEnumeration(unicode_value='RECORDING', tag='RECORDING')
programTypeEnum._InitializeFacetMap(programTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'programTypeEnum', programTypeEnum)
_module_typeBindings.programTypeEnum = programTypeEnum

# Atomic simple type: {urn:vpro:media:2009}segmentTypeEnum
class segmentTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'segmentTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 165, 2)
    _Documentation = None
segmentTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=segmentTypeEnum)
segmentTypeEnum.SEGMENT = segmentTypeEnum._CF_enumeration.addEnumeration(unicode_value='SEGMENT', tag='SEGMENT')
segmentTypeEnum._InitializeFacetMap(segmentTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'segmentTypeEnum', segmentTypeEnum)
_module_typeBindings.segmentTypeEnum = segmentTypeEnum

# Atomic simple type: {urn:vpro:media:2009}workflowTypeEnum
class workflowTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workflowTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 171, 2)
    _Documentation = None
workflowTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=workflowTypeEnum)
workflowTypeEnum.PUBLISHED = workflowTypeEnum._CF_enumeration.addEnumeration(unicode_value='PUBLISHED', tag='PUBLISHED')
workflowTypeEnum.REVOKED = workflowTypeEnum._CF_enumeration.addEnumeration(unicode_value='REVOKED', tag='REVOKED')
workflowTypeEnum.FOR_REPUBLICATION = workflowTypeEnum._CF_enumeration.addEnumeration(unicode_value='FOR REPUBLICATION', tag='FOR_REPUBLICATION')
workflowTypeEnum.FOR_PUBLICATION = workflowTypeEnum._CF_enumeration.addEnumeration(unicode_value='FOR PUBLICATION', tag='FOR_PUBLICATION')
workflowTypeEnum.DELETED = workflowTypeEnum._CF_enumeration.addEnumeration(unicode_value='DELETED', tag='DELETED')
workflowTypeEnum.PARENT_REVOKED = workflowTypeEnum._CF_enumeration.addEnumeration(unicode_value='PARENT REVOKED', tag='PARENT_REVOKED')
workflowTypeEnum._InitializeFacetMap(workflowTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'workflowTypeEnum', workflowTypeEnum)
_module_typeBindings.workflowTypeEnum = workflowTypeEnum

# Atomic simple type: {urn:vpro:media:2009}cridType
class cridType (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cridType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 308, 2)
    _Documentation = None
cridType._CF_pattern = pyxb.binding.facets.CF_pattern()
cridType._CF_pattern.addPattern(pattern='(c|C)(r|R)(i|I)(d|D)://.*/.*')
cridType._InitializeFacetMap(cridType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cridType', cridType)
_module_typeBindings.cridType = cridType

# Atomic simple type: {urn:vpro:media:2009}platformTypeEnum
class platformTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'platformTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 314, 2)
    _Documentation = None
platformTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=platformTypeEnum)
platformTypeEnum.INTERNETVOD = platformTypeEnum._CF_enumeration.addEnumeration(unicode_value='INTERNETVOD', tag='INTERNETVOD')
platformTypeEnum.TVVOD = platformTypeEnum._CF_enumeration.addEnumeration(unicode_value='TVVOD', tag='TVVOD')
platformTypeEnum.PLUSVOD = platformTypeEnum._CF_enumeration.addEnumeration(unicode_value='PLUSVOD', tag='PLUSVOD')
platformTypeEnum.NPOPLUSVOD = platformTypeEnum._CF_enumeration.addEnumeration(unicode_value='NPOPLUSVOD', tag='NPOPLUSVOD')
platformTypeEnum._InitializeFacetMap(platformTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'platformTypeEnum', platformTypeEnum)
_module_typeBindings.platformTypeEnum = platformTypeEnum

# Atomic simple type: {urn:vpro:media:2009}textualTypeEnum
class textualTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'textualTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 352, 2)
    _Documentation = None
textualTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=textualTypeEnum)
textualTypeEnum.MAIN = textualTypeEnum._CF_enumeration.addEnumeration(unicode_value='MAIN', tag='MAIN')
textualTypeEnum.SHORT = textualTypeEnum._CF_enumeration.addEnumeration(unicode_value='SHORT', tag='SHORT')
textualTypeEnum.SUB = textualTypeEnum._CF_enumeration.addEnumeration(unicode_value='SUB', tag='SUB')
textualTypeEnum.KICKER = textualTypeEnum._CF_enumeration.addEnumeration(unicode_value='KICKER', tag='KICKER')
textualTypeEnum.ORIGINAL = textualTypeEnum._CF_enumeration.addEnumeration(unicode_value='ORIGINAL', tag='ORIGINAL')
textualTypeEnum.EPISODE = textualTypeEnum._CF_enumeration.addEnumeration(unicode_value='EPISODE', tag='EPISODE')
textualTypeEnum.WORK = textualTypeEnum._CF_enumeration.addEnumeration(unicode_value='WORK', tag='WORK')
textualTypeEnum.LEXICO = textualTypeEnum._CF_enumeration.addEnumeration(unicode_value='LEXICO', tag='LEXICO')
textualTypeEnum.ABBREVIATION = textualTypeEnum._CF_enumeration.addEnumeration(unicode_value='ABBREVIATION', tag='ABBREVIATION')
textualTypeEnum._InitializeFacetMap(textualTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'textualTypeEnum', textualTypeEnum)
_module_typeBindings.textualTypeEnum = textualTypeEnum

# Atomic simple type: {urn:vpro:media:2009}avTypeEnum
class avTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'avTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 366, 2)
    _Documentation = None
avTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=avTypeEnum)
avTypeEnum.AUDIO = avTypeEnum._CF_enumeration.addEnumeration(unicode_value='AUDIO', tag='AUDIO')
avTypeEnum.VIDEO = avTypeEnum._CF_enumeration.addEnumeration(unicode_value='VIDEO', tag='VIDEO')
avTypeEnum.MIXED = avTypeEnum._CF_enumeration.addEnumeration(unicode_value='MIXED', tag='MIXED')
avTypeEnum._InitializeFacetMap(avTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'avTypeEnum', avTypeEnum)
_module_typeBindings.avTypeEnum = avTypeEnum

# Atomic simple type: {urn:vpro:media:2009}avFileFormatEnum
class avFileFormatEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'avFileFormatEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 411, 2)
    _Documentation = None
avFileFormatEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=avFileFormatEnum)
avFileFormatEnum.MP3 = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='MP3', tag='MP3')
avFileFormatEnum.RA = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='RA', tag='RA')
avFileFormatEnum.RM = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='RM', tag='RM')
avFileFormatEnum.MP4 = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='MP4', tag='MP4')
avFileFormatEnum.WVC1 = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='WVC1', tag='WVC1')
avFileFormatEnum.WM = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='WM', tag='WM')
avFileFormatEnum.RAM = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='RAM', tag='RAM')
avFileFormatEnum.WMP = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='WMP', tag='WMP')
avFileFormatEnum.HTML = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='HTML', tag='HTML')
avFileFormatEnum.M4A = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='M4A', tag='M4A')
avFileFormatEnum.M4V = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='M4V', tag='M4V')
avFileFormatEnum.DGPP = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='DGPP', tag='DGPP')
avFileFormatEnum.FLV = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='FLV', tag='FLV')
avFileFormatEnum.HASP = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='HASP', tag='HASP')
avFileFormatEnum.MPEG2 = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='MPEG2', tag='MPEG2')
avFileFormatEnum.H264 = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='H264', tag='H264')
avFileFormatEnum.UNKNOWN = avFileFormatEnum._CF_enumeration.addEnumeration(unicode_value='UNKNOWN', tag='UNKNOWN')
avFileFormatEnum._InitializeFacetMap(avFileFormatEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'avFileFormatEnum', avFileFormatEnum)
_module_typeBindings.avFileFormatEnum = avFileFormatEnum

# Atomic simple type: {urn:vpro:media:2009}colorType
class colorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'colorType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 443, 2)
    _Documentation = None
colorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=colorType)
colorType.COLOR = colorType._CF_enumeration.addEnumeration(unicode_value='COLOR', tag='COLOR')
colorType.BLACK_AND_WHITE = colorType._CF_enumeration.addEnumeration(unicode_value='BLACK AND WHITE', tag='BLACK_AND_WHITE')
colorType.BLACK_AND_WHITE_AND_COLOR = colorType._CF_enumeration.addEnumeration(unicode_value='BLACK AND WHITE AND COLOR', tag='BLACK_AND_WHITE_AND_COLOR')
colorType.COLORIZED = colorType._CF_enumeration.addEnumeration(unicode_value='COLORIZED', tag='COLORIZED')
colorType._InitializeFacetMap(colorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'colorType', colorType)
_module_typeBindings.colorType = colorType

# Atomic simple type: {urn:vpro:media:2009}aspectRatioEnum
class aspectRatioEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'aspectRatioEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 452, 2)
    _Documentation = None
aspectRatioEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=aspectRatioEnum)
aspectRatioEnum.n43 = aspectRatioEnum._CF_enumeration.addEnumeration(unicode_value='4:3', tag='n43')
aspectRatioEnum.n169 = aspectRatioEnum._CF_enumeration.addEnumeration(unicode_value='16:9', tag='n169')
aspectRatioEnum._InitializeFacetMap(aspectRatioEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'aspectRatioEnum', aspectRatioEnum)
_module_typeBindings.aspectRatioEnum = aspectRatioEnum

# Atomic simple type: {urn:vpro:media:2009}roleType
class roleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'roleType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 482, 2)
    _Documentation = None
roleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=roleType)
roleType.DIRECTOR = roleType._CF_enumeration.addEnumeration(unicode_value='DIRECTOR', tag='DIRECTOR')
roleType.CHIEF_EDITOR = roleType._CF_enumeration.addEnumeration(unicode_value='CHIEF_EDITOR', tag='CHIEF_EDITOR')
roleType.EDITOR = roleType._CF_enumeration.addEnumeration(unicode_value='EDITOR', tag='EDITOR')
roleType.PRESENTER = roleType._CF_enumeration.addEnumeration(unicode_value='PRESENTER', tag='PRESENTER')
roleType.INTERVIEWER = roleType._CF_enumeration.addEnumeration(unicode_value='INTERVIEWER', tag='INTERVIEWER')
roleType.PRODUCER = roleType._CF_enumeration.addEnumeration(unicode_value='PRODUCER', tag='PRODUCER')
roleType.RESEARCH = roleType._CF_enumeration.addEnumeration(unicode_value='RESEARCH', tag='RESEARCH')
roleType.GUEST = roleType._CF_enumeration.addEnumeration(unicode_value='GUEST', tag='GUEST')
roleType.REPORTER = roleType._CF_enumeration.addEnumeration(unicode_value='REPORTER', tag='REPORTER')
roleType.ACTOR = roleType._CF_enumeration.addEnumeration(unicode_value='ACTOR', tag='ACTOR')
roleType.COMMENTATOR = roleType._CF_enumeration.addEnumeration(unicode_value='COMMENTATOR', tag='COMMENTATOR')
roleType.SCRIPTWRITER = roleType._CF_enumeration.addEnumeration(unicode_value='SCRIPTWRITER', tag='SCRIPTWRITER')
roleType.COMPOSER = roleType._CF_enumeration.addEnumeration(unicode_value='COMPOSER', tag='COMPOSER')
roleType.UNDEFINED = roleType._CF_enumeration.addEnumeration(unicode_value='UNDEFINED', tag='UNDEFINED')
roleType._InitializeFacetMap(roleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'roleType', roleType)
_module_typeBindings.roleType = roleType

# Atomic simple type: {urn:vpro:media:2009}license
class license (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'license')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 538, 2)
    _Documentation = None
license._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=license)
license.COPYRIGHTED = license._CF_enumeration.addEnumeration(unicode_value='COPYRIGHTED', tag='COPYRIGHTED')
license.PUBLIC_DOMAIN = license._CF_enumeration.addEnumeration(unicode_value='PUBLIC_DOMAIN', tag='PUBLIC_DOMAIN')
license.CC_BY = license._CF_enumeration.addEnumeration(unicode_value='CC_BY', tag='CC_BY')
license.CC_BY_SA = license._CF_enumeration.addEnumeration(unicode_value='CC_BY_SA', tag='CC_BY_SA')
license.CC_BY_ND = license._CF_enumeration.addEnumeration(unicode_value='CC_BY_ND', tag='CC_BY_ND')
license.CC_BY_NC = license._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC', tag='CC_BY_NC')
license.CC_BY_NC_SA = license._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_SA', tag='CC_BY_NC_SA')
license.CC_BY_NC_ND = license._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_ND', tag='CC_BY_NC_ND')
license._InitializeFacetMap(license._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'license', license)
_module_typeBindings.license = license

# Atomic simple type: {urn:vpro:media:2009}websiteType
class websiteType (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'websiteType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 557, 2)
    _Documentation = None
websiteType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
websiteType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
websiteType._InitializeFacetMap(websiteType._CF_minLength,
   websiteType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'websiteType', websiteType)
_module_typeBindings.websiteType = websiteType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 568, 10)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.ACCOUNT = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ACCOUNT', tag='ACCOUNT')
STD_ANON.HASHTAG = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HASHTAG', tag='HASHTAG')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {urn:vpro:media:2009}scheduleEventTypeEnum
class scheduleEventTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleEventTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 646, 2)
    _Documentation = None
scheduleEventTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=scheduleEventTypeEnum)
scheduleEventTypeEnum.STRAND = scheduleEventTypeEnum._CF_enumeration.addEnumeration(unicode_value='STRAND', tag='STRAND')
scheduleEventTypeEnum._InitializeFacetMap(scheduleEventTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'scheduleEventTypeEnum', scheduleEventTypeEnum)
_module_typeBindings.scheduleEventTypeEnum = scheduleEventTypeEnum

# Atomic simple type: {urn:vpro:media:2009}predictionStateEnum
class predictionStateEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'predictionStateEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 652, 2)
    _Documentation = None
predictionStateEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=predictionStateEnum)
predictionStateEnum.ANNOUNCED = predictionStateEnum._CF_enumeration.addEnumeration(unicode_value='ANNOUNCED', tag='ANNOUNCED')
predictionStateEnum.REALIZED = predictionStateEnum._CF_enumeration.addEnumeration(unicode_value='REALIZED', tag='REALIZED')
predictionStateEnum.REVOKED = predictionStateEnum._CF_enumeration.addEnumeration(unicode_value='REVOKED', tag='REVOKED')
predictionStateEnum._InitializeFacetMap(predictionStateEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'predictionStateEnum', predictionStateEnum)
_module_typeBindings.predictionStateEnum = predictionStateEnum

# Atomic simple type: {urn:vpro:media:2009}locationTypeEnum
class locationTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 691, 2)
    _Documentation = None
locationTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=locationTypeEnum)
locationTypeEnum.INTERNAL = locationTypeEnum._CF_enumeration.addEnumeration(unicode_value='INTERNAL', tag='INTERNAL')
locationTypeEnum.EXTERNAL = locationTypeEnum._CF_enumeration.addEnumeration(unicode_value='EXTERNAL', tag='EXTERNAL')
locationTypeEnum.UNKNOWN = locationTypeEnum._CF_enumeration.addEnumeration(unicode_value='UNKNOWN', tag='UNKNOWN')
locationTypeEnum._InitializeFacetMap(locationTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'locationTypeEnum', locationTypeEnum)
_module_typeBindings.locationTypeEnum = locationTypeEnum

# Atomic simple type: {urn:vpro:media:2009}midType
class midType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'midType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 760, 2)
    _Documentation = None
midType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
midType._CF_pattern = pyxb.binding.facets.CF_pattern()
midType._CF_pattern.addPattern(pattern='[ \\.a-zA-Z0-9_-]+')
midType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
midType._InitializeFacetMap(midType._CF_minLength,
   midType._CF_pattern,
   midType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'midType', midType)
_module_typeBindings.midType = midType

# Atomic simple type: {urn:vpro:media:2009}organizationIdType
class organizationIdType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'organizationIdType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 768, 2)
    _Documentation = None
organizationIdType._CF_pattern = pyxb.binding.facets.CF_pattern()
organizationIdType._CF_pattern.addPattern(pattern='[A-Z0-9_-]{2,}')
organizationIdType._InitializeFacetMap(organizationIdType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'organizationIdType', organizationIdType)
_module_typeBindings.organizationIdType = organizationIdType

# Atomic simple type: {urn:vpro:media:2009}relationTypeType
class relationTypeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relationTypeType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 774, 2)
    _Documentation = None
relationTypeType._CF_pattern = pyxb.binding.facets.CF_pattern()
relationTypeType._CF_pattern.addPattern(pattern='[A-Z0-9_-]{4,}')
relationTypeType._InitializeFacetMap(relationTypeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'relationTypeType', relationTypeType)
_module_typeBindings.relationTypeType = relationTypeType

# Atomic simple type: {urn:vpro:media:2009}baseTextType
class baseTextType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'baseTextType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 780, 2)
    _Documentation = None
baseTextType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
baseTextType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
baseTextType._InitializeFacetMap(baseTextType._CF_minLength,
   baseTextType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'baseTextType', baseTextType)
_module_typeBindings.baseTextType = baseTextType

# Atomic simple type: {urn:vpro:media:2009}unrequiredBaseTextType
class unrequiredBaseTextType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unrequiredBaseTextType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 787, 2)
    _Documentation = None
unrequiredBaseTextType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
unrequiredBaseTextType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
unrequiredBaseTextType._InitializeFacetMap(unrequiredBaseTextType._CF_minLength,
   unrequiredBaseTextType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'unrequiredBaseTextType', unrequiredBaseTextType)
_module_typeBindings.unrequiredBaseTextType = unrequiredBaseTextType

# Atomic simple type: {urn:vpro:media:2009}unboundedTextType
class unboundedTextType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unboundedTextType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 794, 2)
    _Documentation = None
unboundedTextType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
unboundedTextType._InitializeFacetMap(unboundedTextType._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'unboundedTextType', unboundedTextType)
_module_typeBindings.unboundedTextType = unboundedTextType

# Atomic simple type: {urn:vpro:media:2009}termType
class termType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'termType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 807, 2)
    _Documentation = None
termType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'termType', termType)
_module_typeBindings.termType = termType

# Atomic simple type: {urn:vpro:media:2009}genreIdType
class genreIdType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genreIdType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 811, 2)
    _Documentation = None
genreIdType._CF_pattern = pyxb.binding.facets.CF_pattern()
genreIdType._CF_pattern.addPattern(pattern='3(\\.[0-9]+)+')
genreIdType._InitializeFacetMap(genreIdType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'genreIdType', genreIdType)
_module_typeBindings.genreIdType = genreIdType

# Atomic simple type: {urn:vpro:media:2009}geoRestrictionEnum
class geoRestrictionEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geoRestrictionEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 823, 2)
    _Documentation = None
geoRestrictionEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=geoRestrictionEnum)
geoRestrictionEnum.NL = geoRestrictionEnum._CF_enumeration.addEnumeration(unicode_value='NL', tag='NL')
geoRestrictionEnum.BENELUX = geoRestrictionEnum._CF_enumeration.addEnumeration(unicode_value='BENELUX', tag='BENELUX')
geoRestrictionEnum._InitializeFacetMap(geoRestrictionEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'geoRestrictionEnum', geoRestrictionEnum)
_module_typeBindings.geoRestrictionEnum = geoRestrictionEnum

# Atomic simple type: {urn:vpro:media:2009}contentRatingType
class contentRatingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contentRatingType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 842, 2)
    _Documentation = None
contentRatingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=contentRatingType)
contentRatingType.DISCRIMINATIE = contentRatingType._CF_enumeration.addEnumeration(unicode_value='DISCRIMINATIE', tag='DISCRIMINATIE')
contentRatingType.GROF_TAALGEBRUIK = contentRatingType._CF_enumeration.addEnumeration(unicode_value='GROF_TAALGEBRUIK', tag='GROF_TAALGEBRUIK')
contentRatingType.ANGST = contentRatingType._CF_enumeration.addEnumeration(unicode_value='ANGST', tag='ANGST')
contentRatingType.GEWELD = contentRatingType._CF_enumeration.addEnumeration(unicode_value='GEWELD', tag='GEWELD')
contentRatingType.SEKS = contentRatingType._CF_enumeration.addEnumeration(unicode_value='SEKS', tag='SEKS')
contentRatingType.DRUGS_EN_ALCOHOL = contentRatingType._CF_enumeration.addEnumeration(unicode_value='DRUGS_EN_ALCOHOL', tag='DRUGS_EN_ALCOHOL')
contentRatingType._InitializeFacetMap(contentRatingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'contentRatingType', contentRatingType)
_module_typeBindings.contentRatingType = contentRatingType

# Atomic simple type: {urn:vpro:media:2009}ageRatingType
class ageRatingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ageRatingType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 889, 2)
    _Documentation = None
ageRatingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=ageRatingType)
ageRatingType.n6 = ageRatingType._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
ageRatingType.n9 = ageRatingType._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
ageRatingType.n12 = ageRatingType._CF_enumeration.addEnumeration(unicode_value='12', tag='n12')
ageRatingType.n16 = ageRatingType._CF_enumeration.addEnumeration(unicode_value='16', tag='n16')
ageRatingType.ALL = ageRatingType._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
ageRatingType._InitializeFacetMap(ageRatingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ageRatingType', ageRatingType)
_module_typeBindings.ageRatingType = ageRatingType

# Atomic simple type: {urn:vpro:media:2009}countryCodeType
class countryCodeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'countryCodeType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 937, 2)
    _Documentation = None
countryCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
countryCodeType._CF_pattern.addPattern(pattern='(\\w){2,4}')
countryCodeType._InitializeFacetMap(countryCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'countryCodeType', countryCodeType)
_module_typeBindings.countryCodeType = countryCodeType

# Atomic simple type: {urn:vpro:media:2009}languageCodeType
class languageCodeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'languageCodeType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 957, 2)
    _Documentation = None
languageCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
languageCodeType._CF_pattern.addPattern(pattern='(\\w){2,4}')
languageCodeType._InitializeFacetMap(languageCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'languageCodeType', languageCodeType)
_module_typeBindings.languageCodeType = languageCodeType

# Atomic simple type: {urn:vpro:media:2009}channelEnum
class channelEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'channelEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 969, 2)
    _Documentation = None
channelEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=channelEnum)
channelEnum.NED1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='NED1', tag='NED1')
channelEnum.NED2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='NED2', tag='NED2')
channelEnum.NED3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='NED3', tag='NED3')
channelEnum.RTL4 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RTL4', tag='RTL4')
channelEnum.RTL5 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RTL5', tag='RTL5')
channelEnum.SBS6 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SBS6', tag='SBS6')
channelEnum.RTL7 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RTL7', tag='RTL7')
channelEnum.VERO = channelEnum._CF_enumeration.addEnumeration(unicode_value='VERO', tag='VERO')
channelEnum.NET5 = channelEnum._CF_enumeration.addEnumeration(unicode_value='NET5', tag='NET5')
channelEnum.RTL8 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RTL8', tag='RTL8')
channelEnum.REGI = channelEnum._CF_enumeration.addEnumeration(unicode_value='REGI', tag='REGI')
channelEnum.OFRY = channelEnum._CF_enumeration.addEnumeration(unicode_value='OFRY', tag='OFRY')
channelEnum.NOOR = channelEnum._CF_enumeration.addEnumeration(unicode_value='NOOR', tag='NOOR')
channelEnum.RTVD = channelEnum._CF_enumeration.addEnumeration(unicode_value='RTVD', tag='RTVD')
channelEnum.OOST = channelEnum._CF_enumeration.addEnumeration(unicode_value='OOST', tag='OOST')
channelEnum.GELD = channelEnum._CF_enumeration.addEnumeration(unicode_value='GELD', tag='GELD')
channelEnum.FLEV = channelEnum._CF_enumeration.addEnumeration(unicode_value='FLEV', tag='FLEV')
channelEnum.BRAB = channelEnum._CF_enumeration.addEnumeration(unicode_value='BRAB', tag='BRAB')
channelEnum.REGU = channelEnum._CF_enumeration.addEnumeration(unicode_value='REGU', tag='REGU')
channelEnum.NORH = channelEnum._CF_enumeration.addEnumeration(unicode_value='NORH', tag='NORH')
channelEnum.WEST = channelEnum._CF_enumeration.addEnumeration(unicode_value='WEST', tag='WEST')
channelEnum.RIJN = channelEnum._CF_enumeration.addEnumeration(unicode_value='RIJN', tag='RIJN')
channelEnum.L1TV = channelEnum._CF_enumeration.addEnumeration(unicode_value='L1TV', tag='L1TV')
channelEnum.OZEE = channelEnum._CF_enumeration.addEnumeration(unicode_value='OZEE', tag='OZEE')
channelEnum.AT5 = channelEnum._CF_enumeration.addEnumeration(unicode_value='AT5_', tag='AT5')
channelEnum.RNN7 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RNN7', tag='RNN7')
channelEnum.BVNT = channelEnum._CF_enumeration.addEnumeration(unicode_value='BVNT', tag='BVNT')
channelEnum.EEN = channelEnum._CF_enumeration.addEnumeration(unicode_value='EEN_', tag='EEN')
channelEnum.KETN = channelEnum._CF_enumeration.addEnumeration(unicode_value='KETN', tag='KETN')
channelEnum.VTM = channelEnum._CF_enumeration.addEnumeration(unicode_value='VTM_', tag='VTM')
channelEnum.KA2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='KA2_', tag='KA2')
channelEnum.VT4 = channelEnum._CF_enumeration.addEnumeration(unicode_value='VT4_', tag='VT4')
channelEnum.LUNE = channelEnum._CF_enumeration.addEnumeration(unicode_value='LUNE', tag='LUNE')
channelEnum.LDUE = channelEnum._CF_enumeration.addEnumeration(unicode_value='LDUE', tag='LDUE')
channelEnum.RTBF = channelEnum._CF_enumeration.addEnumeration(unicode_value='RTBF', tag='RTBF')
channelEnum.ARD = channelEnum._CF_enumeration.addEnumeration(unicode_value='ARD_', tag='ARD')
channelEnum.ZDF = channelEnum._CF_enumeration.addEnumeration(unicode_value='ZDF_', tag='ZDF')
channelEnum.WDR = channelEnum._CF_enumeration.addEnumeration(unicode_value='WDR_', tag='WDR')
channelEnum.N_3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='N_3_', tag='N_3')
channelEnum.SUDW = channelEnum._CF_enumeration.addEnumeration(unicode_value='SUDW', tag='SUDW')
channelEnum.SWF = channelEnum._CF_enumeration.addEnumeration(unicode_value='SWF_', tag='SWF')
channelEnum.RTL = channelEnum._CF_enumeration.addEnumeration(unicode_value='RTL_', tag='RTL')
channelEnum.SAT1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SAT1', tag='SAT1')
channelEnum.PRO7 = channelEnum._CF_enumeration.addEnumeration(unicode_value='PRO7', tag='PRO7')
channelEnum.n3SAT = channelEnum._CF_enumeration.addEnumeration(unicode_value='3SAT', tag='n3SAT')
channelEnum.KABE = channelEnum._CF_enumeration.addEnumeration(unicode_value='KABE', tag='KABE')
channelEnum.ARTE = channelEnum._CF_enumeration.addEnumeration(unicode_value='ARTE', tag='ARTE')
channelEnum.T5ME = channelEnum._CF_enumeration.addEnumeration(unicode_value='T5ME', tag='T5ME')
channelEnum.FRA2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FRA2', tag='FRA2')
channelEnum.FRA3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FRA3', tag='FRA3')
channelEnum.BBC1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBC1', tag='BBC1')
channelEnum.BBC2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBC2', tag='BBC2')
channelEnum.BBTH = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBTH', tag='BBTH')
channelEnum.BBTC = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBTC', tag='BBTC')
channelEnum.BBCF = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBCF', tag='BBCF')
channelEnum.BBFC = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBFC', tag='BBFC')
channelEnum.BBCP = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBCP', tag='BBCP')
channelEnum.TRTI = channelEnum._CF_enumeration.addEnumeration(unicode_value='TRTI', tag='TRTI')
channelEnum.SHOW = channelEnum._CF_enumeration.addEnumeration(unicode_value='SHOW', tag='SHOW')
channelEnum.LIGT = channelEnum._CF_enumeration.addEnumeration(unicode_value='LIGT', tag='LIGT')
channelEnum.TURK = channelEnum._CF_enumeration.addEnumeration(unicode_value='TURK', tag='TURK')
channelEnum.ATVT = channelEnum._CF_enumeration.addEnumeration(unicode_value='ATVT', tag='ATVT')
channelEnum.FOXT = channelEnum._CF_enumeration.addEnumeration(unicode_value='FOXT', tag='FOXT')
channelEnum.HABN = channelEnum._CF_enumeration.addEnumeration(unicode_value='HABN', tag='HABN')
channelEnum.STTV = channelEnum._CF_enumeration.addEnumeration(unicode_value='STTV', tag='STTV')
channelEnum.RRTM = channelEnum._CF_enumeration.addEnumeration(unicode_value='RRTM', tag='RRTM')
channelEnum.RMBC = channelEnum._CF_enumeration.addEnumeration(unicode_value='RMBC', tag='RMBC')
channelEnum.RART = channelEnum._CF_enumeration.addEnumeration(unicode_value='RART', tag='RART')
channelEnum.ARTM = channelEnum._CF_enumeration.addEnumeration(unicode_value='ARTM', tag='ARTM')
channelEnum.TVBS = channelEnum._CF_enumeration.addEnumeration(unicode_value='TVBS', tag='TVBS')
channelEnum.ASIA = channelEnum._CF_enumeration.addEnumeration(unicode_value='ASIA', tag='ASIA')
channelEnum.TIVI = channelEnum._CF_enumeration.addEnumeration(unicode_value='TIVI', tag='TIVI')
channelEnum.B4UM = channelEnum._CF_enumeration.addEnumeration(unicode_value='B4UM', tag='B4UM')
channelEnum.PCNE = channelEnum._CF_enumeration.addEnumeration(unicode_value='PCNE', tag='PCNE')
channelEnum.PATN = channelEnum._CF_enumeration.addEnumeration(unicode_value='PATN', tag='PATN')
channelEnum.ZEET = channelEnum._CF_enumeration.addEnumeration(unicode_value='ZEET', tag='ZEET')
channelEnum.ZEEC = channelEnum._CF_enumeration.addEnumeration(unicode_value='ZEEC', tag='ZEEC')
channelEnum.TVE = channelEnum._CF_enumeration.addEnumeration(unicode_value='TVE_', tag='TVE')
channelEnum.RAI = channelEnum._CF_enumeration.addEnumeration(unicode_value='RAI_', tag='RAI')
channelEnum.RAID = channelEnum._CF_enumeration.addEnumeration(unicode_value='RAID', tag='RAID')
channelEnum.RAIT = channelEnum._CF_enumeration.addEnumeration(unicode_value='RAIT', tag='RAIT')
channelEnum.TEVE = channelEnum._CF_enumeration.addEnumeration(unicode_value='TEVE', tag='TEVE')
channelEnum.ERTS = channelEnum._CF_enumeration.addEnumeration(unicode_value='ERTS', tag='ERTS')
channelEnum.STV = channelEnum._CF_enumeration.addEnumeration(unicode_value='STV_', tag='STV')
channelEnum.NTV = channelEnum._CF_enumeration.addEnumeration(unicode_value='NTV_', tag='NTV')
channelEnum.TVPO = channelEnum._CF_enumeration.addEnumeration(unicode_value='TVPO', tag='TVPO')
channelEnum.NOSJ = channelEnum._CF_enumeration.addEnumeration(unicode_value='NOSJ', tag='NOSJ')
channelEnum.CULT = channelEnum._CF_enumeration.addEnumeration(unicode_value='CULT', tag='CULT')
channelEnum.n101 = channelEnum._CF_enumeration.addEnumeration(unicode_value='101_', tag='n101')
channelEnum.PO24 = channelEnum._CF_enumeration.addEnumeration(unicode_value='PO24', tag='PO24')
channelEnum.HILV = channelEnum._CF_enumeration.addEnumeration(unicode_value='HILV', tag='HILV')
channelEnum.HOLL = channelEnum._CF_enumeration.addEnumeration(unicode_value='HOLL', tag='HOLL')
channelEnum.GESC = channelEnum._CF_enumeration.addEnumeration(unicode_value='GESC', tag='GESC')
channelEnum.STER = channelEnum._CF_enumeration.addEnumeration(unicode_value='STER', tag='STER')
channelEnum.NCRV = channelEnum._CF_enumeration.addEnumeration(unicode_value='NCRV', tag='NCRV')
channelEnum.OPVO = channelEnum._CF_enumeration.addEnumeration(unicode_value='OPVO', tag='OPVO')
channelEnum.CONS = channelEnum._CF_enumeration.addEnumeration(unicode_value='CONS', tag='CONS')
channelEnum.HUMO = channelEnum._CF_enumeration.addEnumeration(unicode_value='HUMO', tag='HUMO')
channelEnum.ENTE = channelEnum._CF_enumeration.addEnumeration(unicode_value='ENTE', tag='ENTE')
channelEnum.FASH = channelEnum._CF_enumeration.addEnumeration(unicode_value='FASH', tag='FASH')
channelEnum.COMC = channelEnum._CF_enumeration.addEnumeration(unicode_value='COMC', tag='COMC')
channelEnum.TBN = channelEnum._CF_enumeration.addEnumeration(unicode_value='TBN_', tag='TBN')
channelEnum.DISC = channelEnum._CF_enumeration.addEnumeration(unicode_value='DISC', tag='DISC')
channelEnum.ZONE = channelEnum._CF_enumeration.addEnumeration(unicode_value='ZONE', tag='ZONE')
channelEnum.ANPL = channelEnum._CF_enumeration.addEnumeration(unicode_value='ANPL', tag='ANPL')
channelEnum.CLUB = channelEnum._CF_enumeration.addEnumeration(unicode_value='CLUB', tag='CLUB')
channelEnum.NAGE = channelEnum._CF_enumeration.addEnumeration(unicode_value='NAGE', tag='NAGE')
channelEnum.TRAC = channelEnum._CF_enumeration.addEnumeration(unicode_value='TRAC', tag='TRAC')
channelEnum.NGHD = channelEnum._CF_enumeration.addEnumeration(unicode_value='NGHD', tag='NGHD')
channelEnum.WILD = channelEnum._CF_enumeration.addEnumeration(unicode_value='WILD', tag='WILD')
channelEnum.GARU = channelEnum._CF_enumeration.addEnumeration(unicode_value='GARU', tag='GARU')
channelEnum.ZAZA = channelEnum._CF_enumeration.addEnumeration(unicode_value='ZAZA', tag='ZAZA')
channelEnum.FAM7 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FAM7', tag='FAM7')
channelEnum.DTAL = channelEnum._CF_enumeration.addEnumeration(unicode_value='DTAL', tag='DTAL')
channelEnum.SCIE = channelEnum._CF_enumeration.addEnumeration(unicode_value='SCIE', tag='SCIE')
channelEnum.CIVI = channelEnum._CF_enumeration.addEnumeration(unicode_value='CIVI', tag='CIVI')
channelEnum.DIHD = channelEnum._CF_enumeration.addEnumeration(unicode_value='DIHD', tag='DIHD')
channelEnum.HIST = channelEnum._CF_enumeration.addEnumeration(unicode_value='HIST', tag='HIST')
channelEnum.TRAV = channelEnum._CF_enumeration.addEnumeration(unicode_value='TRAV', tag='TRAV')
channelEnum.HETG = channelEnum._CF_enumeration.addEnumeration(unicode_value='HETG', tag='HETG')
channelEnum.GOED = channelEnum._CF_enumeration.addEnumeration(unicode_value='GOED', tag='GOED')
channelEnum.BABY = channelEnum._CF_enumeration.addEnumeration(unicode_value='BABY', tag='BABY')
channelEnum.DH1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='DH1_', tag='DH1')
channelEnum.LITV = channelEnum._CF_enumeration.addEnumeration(unicode_value='LITV', tag='LITV')
channelEnum.LIVE = channelEnum._CF_enumeration.addEnumeration(unicode_value='LIVE', tag='LIVE')
channelEnum.STAR = channelEnum._CF_enumeration.addEnumeration(unicode_value='STAR', tag='STAR')
channelEnum.WEER = channelEnum._CF_enumeration.addEnumeration(unicode_value='WEER', tag='WEER')
channelEnum.REAL = channelEnum._CF_enumeration.addEnumeration(unicode_value='REAL', tag='REAL')
channelEnum.SCIF = channelEnum._CF_enumeration.addEnumeration(unicode_value='SCIF', tag='SCIF')
channelEnum.n13ST = channelEnum._CF_enumeration.addEnumeration(unicode_value='13ST', tag='n13ST')
channelEnum.CARC = channelEnum._CF_enumeration.addEnumeration(unicode_value='CARC', tag='CARC')
channelEnum.NOSN = channelEnum._CF_enumeration.addEnumeration(unicode_value='NOSN', tag='NOSN')
channelEnum.HISH = channelEnum._CF_enumeration.addEnumeration(unicode_value='HISH', tag='HISH')
channelEnum.BRHD = channelEnum._CF_enumeration.addEnumeration(unicode_value='BRHD', tag='BRHD')
channelEnum.FANT = channelEnum._CF_enumeration.addEnumeration(unicode_value='FANT', tag='FANT')
channelEnum.RACW = channelEnum._CF_enumeration.addEnumeration(unicode_value='RACW', tag='RACW')
channelEnum.COMF = channelEnum._CF_enumeration.addEnumeration(unicode_value='COMF', tag='COMF')
channelEnum.POKE = channelEnum._CF_enumeration.addEnumeration(unicode_value='POKE', tag='POKE')
channelEnum.MNET = channelEnum._CF_enumeration.addEnumeration(unicode_value='MNET', tag='MNET')
channelEnum.VOOM = channelEnum._CF_enumeration.addEnumeration(unicode_value='VOOM', tag='VOOM')
channelEnum.ZONH = channelEnum._CF_enumeration.addEnumeration(unicode_value='ZONH', tag='ZONH')
channelEnum.KPN1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='KPN1', tag='KPN1')
channelEnum.KPN2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='KPN2', tag='KPN2')
channelEnum.KPN3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='KPN3', tag='KPN3')
channelEnum.KPN4 = channelEnum._CF_enumeration.addEnumeration(unicode_value='KPN4', tag='KPN4')
channelEnum.ZIZO = channelEnum._CF_enumeration.addEnumeration(unicode_value='ZIZO', tag='ZIZO')
channelEnum.DVB1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='DVB1', tag='DVB1')
channelEnum.DVB2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='DVB2', tag='DVB2')
channelEnum.DVB3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='DVB3', tag='DVB3')
channelEnum.NICK = channelEnum._CF_enumeration.addEnumeration(unicode_value='NICK', tag='NICK')
channelEnum.NIJN = channelEnum._CF_enumeration.addEnumeration(unicode_value='NIJN', tag='NIJN')
channelEnum.NIKT = channelEnum._CF_enumeration.addEnumeration(unicode_value='NIKT', tag='NIKT')
channelEnum.NIKH = channelEnum._CF_enumeration.addEnumeration(unicode_value='NIKH', tag='NIKH')
channelEnum.CART = channelEnum._CF_enumeration.addEnumeration(unicode_value='CART', tag='CART')
channelEnum.BOOM = channelEnum._CF_enumeration.addEnumeration(unicode_value='BOOM', tag='BOOM')
channelEnum.CNN = channelEnum._CF_enumeration.addEnumeration(unicode_value='CNN_', tag='CNN')
channelEnum.BBCW = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBCW', tag='BBCW')
channelEnum.EURN = channelEnum._CF_enumeration.addEnumeration(unicode_value='EURN', tag='EURN')
channelEnum.SKNE = channelEnum._CF_enumeration.addEnumeration(unicode_value='SKNE', tag='SKNE')
channelEnum.BLOO = channelEnum._CF_enumeration.addEnumeration(unicode_value='BLOO', tag='BLOO')
channelEnum.CNBC = channelEnum._CF_enumeration.addEnumeration(unicode_value='CNBC', tag='CNBC')
channelEnum.PALJ = channelEnum._CF_enumeration.addEnumeration(unicode_value='PALJ', tag='PALJ')
channelEnum.ALJA = channelEnum._CF_enumeration.addEnumeration(unicode_value='ALJA', tag='ALJA')
channelEnum.FOXN = channelEnum._CF_enumeration.addEnumeration(unicode_value='FOXN', tag='FOXN')
channelEnum.MTV = channelEnum._CF_enumeration.addEnumeration(unicode_value='MTV_', tag='MTV')
channelEnum.MTV2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='MTV2', tag='MTV2')
channelEnum.HITS = channelEnum._CF_enumeration.addEnumeration(unicode_value='HITS', tag='HITS')
channelEnum.BASE = channelEnum._CF_enumeration.addEnumeration(unicode_value='BASE', tag='BASE')
channelEnum.MTVB = channelEnum._CF_enumeration.addEnumeration(unicode_value='MTVB', tag='MTVB')
channelEnum.TMF = channelEnum._CF_enumeration.addEnumeration(unicode_value='TMF_', tag='TMF')
channelEnum.TMFN = channelEnum._CF_enumeration.addEnumeration(unicode_value='TMFN', tag='TMFN')
channelEnum.TMFP = channelEnum._CF_enumeration.addEnumeration(unicode_value='TMFP', tag='TMFP')
channelEnum.TMFY = channelEnum._CF_enumeration.addEnumeration(unicode_value='TMFY', tag='TMFY')
channelEnum.TVOR = channelEnum._CF_enumeration.addEnumeration(unicode_value='TVOR', tag='TVOR')
channelEnum.VH1E = channelEnum._CF_enumeration.addEnumeration(unicode_value='VH1E', tag='VH1E')
channelEnum.VH1C = channelEnum._CF_enumeration.addEnumeration(unicode_value='VH1C', tag='VH1C')
channelEnum.PERC = channelEnum._CF_enumeration.addEnumeration(unicode_value='PERC', tag='PERC')
channelEnum.MEZZ = channelEnum._CF_enumeration.addEnumeration(unicode_value='MEZZ', tag='MEZZ')
channelEnum.EURO = channelEnum._CF_enumeration.addEnumeration(unicode_value='EURO', tag='EURO')
channelEnum.EUR2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='EUR2', tag='EUR2')
channelEnum.EXTR = channelEnum._CF_enumeration.addEnumeration(unicode_value='EXTR', tag='EXTR')
channelEnum.MOTO = channelEnum._CF_enumeration.addEnumeration(unicode_value='MOTO', tag='MOTO')
channelEnum.SAIL = channelEnum._CF_enumeration.addEnumeration(unicode_value='SAIL', tag='SAIL')
channelEnum.ESPN = channelEnum._CF_enumeration.addEnumeration(unicode_value='ESPN', tag='ESPN')
channelEnum.NASE = channelEnum._CF_enumeration.addEnumeration(unicode_value='NASE', tag='NASE')
channelEnum.SP11 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SP11', tag='SP11')
channelEnum.SP12 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SP12', tag='SP12')
channelEnum.SP13 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SP13', tag='SP13')
channelEnum.SP14 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SP14', tag='SP14')
channelEnum.SP15 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SP15', tag='SP15')
channelEnum.SP16 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SP16', tag='SP16')
channelEnum.SP17 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SP17', tag='SP17')
channelEnum.SP18 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SP18', tag='SP18')
channelEnum.S1HD = channelEnum._CF_enumeration.addEnumeration(unicode_value='S1HD', tag='S1HD')
channelEnum.FIL1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FIL1', tag='FIL1')
channelEnum.FIL2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FIL2', tag='FIL2')
channelEnum.FIL3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FIL3', tag='FIL3')
channelEnum.FL11 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FL11', tag='FL11')
channelEnum.FL1P = channelEnum._CF_enumeration.addEnumeration(unicode_value='FL1P', tag='FL1P')
channelEnum.FL12 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FL12', tag='FL12')
channelEnum.FL13 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FL13', tag='FL13')
channelEnum.FLHD = channelEnum._CF_enumeration.addEnumeration(unicode_value='FLHD', tag='FLHD')
channelEnum.MGMM = channelEnum._CF_enumeration.addEnumeration(unicode_value='MGMM', tag='MGMM')
channelEnum.TCM = channelEnum._CF_enumeration.addEnumeration(unicode_value='TCM_', tag='TCM')
channelEnum.HALL = channelEnum._CF_enumeration.addEnumeration(unicode_value='HALL', tag='HALL')
channelEnum.ACNW = channelEnum._CF_enumeration.addEnumeration(unicode_value='ACNW', tag='ACNW')
channelEnum.RHUS = channelEnum._CF_enumeration.addEnumeration(unicode_value='RHUS', tag='RHUS')
channelEnum.PLAY = channelEnum._CF_enumeration.addEnumeration(unicode_value='PLAY', tag='PLAY')
channelEnum.ADUL = channelEnum._CF_enumeration.addEnumeration(unicode_value='ADUL', tag='ADUL')
channelEnum.PSPI = channelEnum._CF_enumeration.addEnumeration(unicode_value='PSPI', tag='PSPI')
channelEnum.HUST = channelEnum._CF_enumeration.addEnumeration(unicode_value='HUST', tag='HUST')
channelEnum.OXMO = channelEnum._CF_enumeration.addEnumeration(unicode_value='OXMO', tag='OXMO')
channelEnum.XM24 = channelEnum._CF_enumeration.addEnumeration(unicode_value='XM24', tag='XM24')
channelEnum.OU24 = channelEnum._CF_enumeration.addEnumeration(unicode_value='OU24', tag='OU24')
channelEnum.RAD1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RAD1', tag='RAD1')
channelEnum.RAD2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RAD2', tag='RAD2')
channelEnum.RAD3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RAD3', tag='RAD3')
channelEnum.RAD4 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RAD4', tag='RAD4')
channelEnum.RAD5 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RAD5', tag='RAD5')
channelEnum.RAD6 = channelEnum._CF_enumeration.addEnumeration(unicode_value='RAD6', tag='RAD6')
channelEnum.REGR = channelEnum._CF_enumeration.addEnumeration(unicode_value='REGR', tag='REGR')
channelEnum.RFRY = channelEnum._CF_enumeration.addEnumeration(unicode_value='RFRY', tag='RFRY')
channelEnum.RNOO = channelEnum._CF_enumeration.addEnumeration(unicode_value='RNOO', tag='RNOO')
channelEnum.RTVD_ = channelEnum._CF_enumeration.addEnumeration(unicode_value='RTVD', tag='RTVD_')
channelEnum.ROST = channelEnum._CF_enumeration.addEnumeration(unicode_value='ROST', tag='ROST')
channelEnum.RGEL = channelEnum._CF_enumeration.addEnumeration(unicode_value='RGEL', tag='RGEL')
channelEnum.RFLE = channelEnum._CF_enumeration.addEnumeration(unicode_value='RFLE', tag='RFLE')
channelEnum.RBRA = channelEnum._CF_enumeration.addEnumeration(unicode_value='RBRA', tag='RBRA')
channelEnum.RUTR = channelEnum._CF_enumeration.addEnumeration(unicode_value='RUTR', tag='RUTR')
channelEnum.RNOH = channelEnum._CF_enumeration.addEnumeration(unicode_value='RNOH', tag='RNOH')
channelEnum.RWST = channelEnum._CF_enumeration.addEnumeration(unicode_value='RWST', tag='RWST')
channelEnum.RRIJ = channelEnum._CF_enumeration.addEnumeration(unicode_value='RRIJ', tag='RRIJ')
channelEnum.LRAD = channelEnum._CF_enumeration.addEnumeration(unicode_value='LRAD', tag='LRAD')
channelEnum.RZEE = channelEnum._CF_enumeration.addEnumeration(unicode_value='RZEE', tag='RZEE')
channelEnum.COMM = channelEnum._CF_enumeration.addEnumeration(unicode_value='COMM', tag='COMM')
channelEnum.RVER = channelEnum._CF_enumeration.addEnumeration(unicode_value='RVER', tag='RVER')
channelEnum.SLAM = channelEnum._CF_enumeration.addEnumeration(unicode_value='SLAM', tag='SLAM')
channelEnum.SKYR = channelEnum._CF_enumeration.addEnumeration(unicode_value='SKYR', tag='SKYR')
channelEnum.BNRN = channelEnum._CF_enumeration.addEnumeration(unicode_value='BNRN', tag='BNRN')
channelEnum.KINK = channelEnum._CF_enumeration.addEnumeration(unicode_value='KINK', tag='KINK')
channelEnum.PCAZ = channelEnum._CF_enumeration.addEnumeration(unicode_value='PCAZ', tag='PCAZ')
channelEnum.QMUS = channelEnum._CF_enumeration.addEnumeration(unicode_value='QMUS', tag='QMUS')
channelEnum.R538 = channelEnum._CF_enumeration.addEnumeration(unicode_value='R538', tag='R538')
channelEnum.GOLD = channelEnum._CF_enumeration.addEnumeration(unicode_value='GOLD', tag='GOLD')
channelEnum.ARRO = channelEnum._CF_enumeration.addEnumeration(unicode_value='ARRO', tag='ARRO')
channelEnum.FUNX = channelEnum._CF_enumeration.addEnumeration(unicode_value='FUNX', tag='FUNX')
channelEnum.CLAS = channelEnum._CF_enumeration.addEnumeration(unicode_value='CLAS', tag='CLAS')
channelEnum.BEL1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='BEL1', tag='BEL1')
channelEnum.BEL2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='BEL2', tag='BEL2')
channelEnum.KLAR = channelEnum._CF_enumeration.addEnumeration(unicode_value='KLAR', tag='KLAR')
channelEnum.BBR1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBR1', tag='BBR1')
channelEnum.BBR2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBR2', tag='BBR2')
channelEnum.BBR3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBR3', tag='BBR3')
channelEnum.BBR4 = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBR4', tag='BBR4')
channelEnum.BBWS = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBWS', tag='BBWS')
channelEnum.BBCX = channelEnum._CF_enumeration.addEnumeration(unicode_value='BBCX', tag='BBCX')
channelEnum.NDR3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='NDR3', tag='NDR3')
channelEnum.WDR4 = channelEnum._CF_enumeration.addEnumeration(unicode_value='WDR4', tag='WDR4')
channelEnum.WDR3 = channelEnum._CF_enumeration.addEnumeration(unicode_value='WDR3', tag='WDR3')
channelEnum.DIG1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='DIG1', tag='DIG1')
channelEnum.DIG2 = channelEnum._CF_enumeration.addEnumeration(unicode_value='DIG2', tag='DIG2')
channelEnum.D24K = channelEnum._CF_enumeration.addEnumeration(unicode_value='D24K', tag='D24K')
channelEnum.H1NL = channelEnum._CF_enumeration.addEnumeration(unicode_value='H1NL', tag='H1NL')
channelEnum.SYFY = channelEnum._CF_enumeration.addEnumeration(unicode_value='SYFY', tag='SYFY')
channelEnum.SBS9 = channelEnum._CF_enumeration.addEnumeration(unicode_value='SBS9', tag='SBS9')
channelEnum.DIXD = channelEnum._CF_enumeration.addEnumeration(unicode_value='DIXD', tag='DIXD')
channelEnum.BRNL = channelEnum._CF_enumeration.addEnumeration(unicode_value='BRNL', tag='BRNL')
channelEnum.FOXL = channelEnum._CF_enumeration.addEnumeration(unicode_value='FOXL', tag='FOXL')
channelEnum.TLC = channelEnum._CF_enumeration.addEnumeration(unicode_value='TLC_', tag='TLC')
channelEnum.BCFS = channelEnum._CF_enumeration.addEnumeration(unicode_value='BCFS', tag='BCFS')
channelEnum.AMC = channelEnum._CF_enumeration.addEnumeration(unicode_value='AMC_', tag='AMC')
channelEnum.FLM1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='FLM1', tag='FLM1')
channelEnum.ZGS1 = channelEnum._CF_enumeration.addEnumeration(unicode_value='ZGS1', tag='ZGS1')
channelEnum.BRTZ = channelEnum._CF_enumeration.addEnumeration(unicode_value='BRTZ', tag='BRTZ')
channelEnum._InitializeFacetMap(channelEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'channelEnum', channelEnum)
_module_typeBindings.channelEnum = channelEnum

# Complex type {urn:vpro:media:2009}mediaTableType with content type ELEMENT_ONLY
class mediaTableType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}mediaTableType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaTableType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 53, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}schedule uses Python identifier schedule
    __schedule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'schedule'), 'schedule', '__urnvpromedia2009_mediaTableType_urnvpromedia2009schedule', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 45, 2), )

    
    schedule = property(__schedule.value, __schedule.set, None, "\n        Programs of type 'BROADCAST' can contain schedule events. A schedule indicates on which channel and at what time the program is broadcast. A schedule is a container which contains the schedule events of different programs, for a certain period of time.\n      ")

    
    # Element {urn:vpro:media:2009}programTable uses Python identifier programTable
    __programTable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'programTable'), 'programTable', '__urnvpromedia2009_mediaTableType_urnvpromedia2009programTable', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 55, 6), )

    
    programTable = property(__programTable.value, __programTable.set, None, 'A table with all program objects in this container')

    
    # Element {urn:vpro:media:2009}groupTable uses Python identifier groupTable
    __groupTable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'groupTable'), 'groupTable', '__urnvpromedia2009_mediaTableType_urnvpromedia2009groupTable', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 60, 6), )

    
    groupTable = property(__groupTable.value, __groupTable.set, None, 'A table with all group objects in this container')

    
    # Element {urn:vpro:media:2009}locationTable uses Python identifier locationTable
    __locationTable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'locationTable'), 'locationTable', '__urnvpromedia2009_mediaTableType_urnvpromedia2009locationTable', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 65, 6), )

    
    locationTable = property(__locationTable.value, __locationTable.set, None, None)

    
    # Attribute publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publisher'), 'publisher', '__urnvpromedia2009_mediaTableType_publisher', pyxb.binding.datatypes.string)
    __publisher._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 72, 4)
    __publisher._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 72, 4)
    
    publisher = property(__publisher.value, __publisher.set, None, None)

    
    # Attribute publicationTime uses Python identifier publicationTime
    __publicationTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publicationTime'), 'publicationTime', '__urnvpromedia2009_mediaTableType_publicationTime', pyxb.binding.datatypes.dateTime)
    __publicationTime._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 73, 4)
    __publicationTime._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 73, 4)
    
    publicationTime = property(__publicationTime.value, __publicationTime.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__urnvpromedia2009_mediaTableType_version', pyxb.binding.datatypes.short)
    __version._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 74, 4)
    __version._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 74, 4)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __schedule.name() : __schedule,
        __programTable.name() : __programTable,
        __groupTable.name() : __groupTable,
        __locationTable.name() : __locationTable
    })
    _AttributeMap.update({
        __publisher.name() : __publisher,
        __publicationTime.name() : __publicationTime,
        __version.name() : __version
    })
_module_typeBindings.mediaTableType = mediaTableType
Namespace.addCategoryObject('typeBinding', 'mediaTableType', mediaTableType)


# Complex type {urn:vpro:media:2009}programTableType with content type ELEMENT_ONLY
class programTableType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}programTableType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'programTableType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 77, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}program uses Python identifier program
    __program = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'program'), 'program', '__urnvpromedia2009_programTableType_urnvpromedia2009program', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 24, 2), )

    
    program = property(__program.value, __program.set, None, '\n        This is the most used entity in POMS. It represents e.g. one broadcast program or one web-only clip. It represent a standalone entity which a consumer can view or listen to.\n      ')

    _ElementMap.update({
        __program.name() : __program
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.programTableType = programTableType
Namespace.addCategoryObject('typeBinding', 'programTableType', programTableType)


# Complex type {urn:vpro:media:2009}portalRestrictionType with content type SIMPLE
class portalRestrictionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}portalRestrictionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'portalRestrictionType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 290, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__urnvpromedia2009_portalRestrictionType_start', pyxb.binding.datatypes.dateTime)
    __start._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 286, 4)
    __start._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 286, 4)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute stop uses Python identifier stop
    __stop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__urnvpromedia2009_portalRestrictionType_stop', pyxb.binding.datatypes.dateTime)
    __stop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 287, 4)
    __stop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 287, 4)
    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Attribute portalId uses Python identifier portalId
    __portalId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'portalId'), 'portalId', '__urnvpromedia2009_portalRestrictionType_portalId', pyxb.binding.datatypes.string)
    __portalId._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 293, 8)
    __portalId._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 293, 8)
    
    portalId = property(__portalId.value, __portalId.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __start.name() : __start,
        __stop.name() : __stop,
        __portalId.name() : __portalId
    })
_module_typeBindings.portalRestrictionType = portalRestrictionType
Namespace.addCategoryObject('typeBinding', 'portalRestrictionType', portalRestrictionType)


# Complex type {urn:vpro:media:2009}tagType with content type SIMPLE
class tagType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}tagType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tagType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 331, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__urnvpromedia2009_tagType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 334, 8)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.tagType = tagType
Namespace.addCategoryObject('typeBinding', 'tagType', tagType)


# Complex type {urn:vpro:media:2009}broadcasterType with content type ELEMENT_ONLY
class broadcasterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}broadcasterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'broadcasterType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 374, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvpromedia2009_broadcasterType_urnvpromedia2009broadcaster', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 376, 6), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    _ElementMap.update({
        __broadcaster.name() : __broadcaster
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.broadcasterType = broadcasterType
Namespace.addCategoryObject('typeBinding', 'broadcasterType', broadcasterType)


# Complex type {urn:vpro:media:2009}portalsType with content type ELEMENT_ONLY
class portalsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}portalsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'portalsType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 388, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portal'), 'portal', '__urnvpromedia2009_portalsType_urnvpromedia2009portal', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 390, 6), )

    
    portal = property(__portal.value, __portal.set, None, None)

    _ElementMap.update({
        __portal.name() : __portal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.portalsType = portalsType
Namespace.addCategoryObject('typeBinding', 'portalsType', portalsType)


# Complex type {urn:vpro:media:2009}repeatType with content type SIMPLE
class repeatType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}repeatType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'repeatType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 394, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute isRerun uses Python identifier isRerun
    __isRerun = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isRerun'), 'isRerun', '__urnvpromedia2009_repeatType_isRerun', pyxb.binding.datatypes.boolean, required=True)
    __isRerun._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 397, 8)
    __isRerun._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 397, 8)
    
    isRerun = property(__isRerun.value, __isRerun.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __isRerun.name() : __isRerun
    })
_module_typeBindings.repeatType = repeatType
Namespace.addCategoryObject('typeBinding', 'repeatType', repeatType)


# Complex type {urn:vpro:media:2009}avAttributesType with content type ELEMENT_ONLY
class avAttributesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}avAttributesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'avAttributesType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 402, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}bitrate uses Python identifier bitrate
    __bitrate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bitrate'), 'bitrate', '__urnvpromedia2009_avAttributesType_urnvpromedia2009bitrate', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 404, 6), )

    
    bitrate = property(__bitrate.value, __bitrate.set, None, None)

    
    # Element {urn:vpro:media:2009}avFileFormat uses Python identifier avFileFormat
    __avFileFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), 'avFileFormat', '__urnvpromedia2009_avAttributesType_urnvpromedia2009avFileFormat', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 405, 6), )

    
    avFileFormat = property(__avFileFormat.value, __avFileFormat.set, None, None)

    
    # Element {urn:vpro:media:2009}videoAttributes uses Python identifier videoAttributes
    __videoAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'videoAttributes'), 'videoAttributes', '__urnvpromedia2009_avAttributesType_urnvpromedia2009videoAttributes', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 406, 6), )

    
    videoAttributes = property(__videoAttributes.value, __videoAttributes.set, None, None)

    
    # Element {urn:vpro:media:2009}audioAttributes uses Python identifier audioAttributes
    __audioAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'audioAttributes'), 'audioAttributes', '__urnvpromedia2009_avAttributesType_urnvpromedia2009audioAttributes', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 407, 6), )

    
    audioAttributes = property(__audioAttributes.value, __audioAttributes.set, None, None)

    _ElementMap.update({
        __bitrate.name() : __bitrate,
        __avFileFormat.name() : __avFileFormat,
        __videoAttributes.name() : __videoAttributes,
        __audioAttributes.name() : __audioAttributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.avAttributesType = avAttributesType
Namespace.addCategoryObject('typeBinding', 'avAttributesType', avAttributesType)


# Complex type {urn:vpro:media:2009}videoAttributesType with content type ELEMENT_ONLY
class videoAttributesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}videoAttributesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'videoAttributesType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 433, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}color uses Python identifier color
    __color = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'color'), 'color', '__urnvpromedia2009_videoAttributesType_urnvpromedia2009color', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 435, 6), )

    
    color = property(__color.value, __color.set, None, None)

    
    # Element {urn:vpro:media:2009}videoCoding uses Python identifier videoCoding
    __videoCoding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'videoCoding'), 'videoCoding', '__urnvpromedia2009_videoAttributesType_urnvpromedia2009videoCoding', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 436, 6), )

    
    videoCoding = property(__videoCoding.value, __videoCoding.set, None, None)

    
    # Element {urn:vpro:media:2009}aspectRatio uses Python identifier aspectRatio
    __aspectRatio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aspectRatio'), 'aspectRatio', '__urnvpromedia2009_videoAttributesType_urnvpromedia2009aspectRatio', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 437, 6), )

    
    aspectRatio = property(__aspectRatio.value, __aspectRatio.set, None, None)

    
    # Attribute height uses Python identifier height
    __height = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__urnvpromedia2009_videoAttributesType_height', pyxb.binding.datatypes.short)
    __height._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 439, 4)
    __height._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 439, 4)
    
    height = property(__height.value, __height.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__urnvpromedia2009_videoAttributesType_width', pyxb.binding.datatypes.short)
    __width._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 440, 4)
    __width._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 440, 4)
    
    width = property(__width.value, __width.set, None, None)

    _ElementMap.update({
        __color.name() : __color,
        __videoCoding.name() : __videoCoding,
        __aspectRatio.name() : __aspectRatio
    })
    _AttributeMap.update({
        __height.name() : __height,
        __width.name() : __width
    })
_module_typeBindings.videoAttributesType = videoAttributesType
Namespace.addCategoryObject('typeBinding', 'videoAttributesType', videoAttributesType)


# Complex type {urn:vpro:media:2009}audioAttributesType with content type ELEMENT_ONLY
class audioAttributesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}audioAttributesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'audioAttributesType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 459, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}numberOfChannels uses Python identifier numberOfChannels
    __numberOfChannels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'numberOfChannels'), 'numberOfChannels', '__urnvpromedia2009_audioAttributesType_urnvpromedia2009numberOfChannels', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 461, 6), )

    
    numberOfChannels = property(__numberOfChannels.value, __numberOfChannels.set, None, None)

    
    # Element {urn:vpro:media:2009}audioCoding uses Python identifier audioCoding
    __audioCoding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'audioCoding'), 'audioCoding', '__urnvpromedia2009_audioAttributesType_urnvpromedia2009audioCoding', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 462, 6), )

    
    audioCoding = property(__audioCoding.value, __audioCoding.set, None, None)

    
    # Element {urn:vpro:media:2009}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'language'), 'language', '__urnvpromedia2009_audioAttributesType_urnvpromedia2009language', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 463, 6), )

    
    language = property(__language.value, __language.set, None, None)

    _ElementMap.update({
        __numberOfChannels.name() : __numberOfChannels,
        __audioCoding.name() : __audioCoding,
        __language.name() : __language
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.audioAttributesType = audioAttributesType
Namespace.addCategoryObject('typeBinding', 'audioAttributesType', audioAttributesType)


# Complex type {urn:vpro:media:2009}creditsType with content type ELEMENT_ONLY
class creditsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}creditsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'creditsType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 467, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__urnvpromedia2009_creditsType_urnvpromedia2009person', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 469, 6), )

    
    person = property(__person.value, __person.set, None, None)

    _ElementMap.update({
        __person.name() : __person
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.creditsType = creditsType
Namespace.addCategoryObject('typeBinding', 'creditsType', creditsType)


# Complex type {urn:vpro:media:2009}segmentsType with content type ELEMENT_ONLY
class segmentsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}segmentsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'segmentsType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 501, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}segment uses Python identifier segment
    __segment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'segment'), 'segment', '__urnvpromedia2009_segmentsType_urnvpromedia2009segment', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 503, 6), )

    
    segment = property(__segment.value, __segment.set, None, None)

    _ElementMap.update({
        __segment.name() : __segment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.segmentsType = segmentsType
Namespace.addCategoryObject('typeBinding', 'segmentsType', segmentsType)


# Complex type {urn:vpro:media:2009}imagesType with content type ELEMENT_ONLY
class imagesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}imagesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imagesType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 532, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:shared:2009}image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_shared, 'image'), 'image', '__urnvpromedia2009_imagesType_urnvproshared2009image', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 7, 2), )

    
    image = property(__image.value, __image.set, None, None)

    _ElementMap.update({
        __image.name() : __image
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.imagesType = imagesType
Namespace.addCategoryObject('typeBinding', 'imagesType', imagesType)


# Complex type {urn:vpro:media:2009}groupTableType with content type ELEMENT_ONLY
class groupTableType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}groupTableType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'groupTableType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 551, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'group'), 'group', '__urnvpromedia2009_groupTableType_urnvpromedia2009group', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 31, 2), )

    
    group = property(__group.value, __group.set, None, '\n        A groups collects a number of programs and/or other groups. Examples: season, series, playlist and album.\n      ')

    _ElementMap.update({
        __group.name() : __group
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.groupTableType = groupTableType
Namespace.addCategoryObject('typeBinding', 'groupTableType', groupTableType)


# Complex type {urn:vpro:media:2009}locationTableType with content type ELEMENT_ONLY
class locationTableType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}locationTableType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationTableType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 579, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__urnvpromedia2009_locationTableType_urnvpromedia2009location', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 581, 6), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element {urn:vpro:media:2009}scheduleEvent uses Python identifier scheduleEvent
    __scheduleEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), 'scheduleEvent', '__urnvpromedia2009_locationTableType_urnvpromedia2009scheduleEvent', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 582, 6), )

    
    scheduleEvent = property(__scheduleEvent.value, __scheduleEvent.set, None, None)

    _ElementMap.update({
        __location.name() : __location,
        __scheduleEvent.name() : __scheduleEvent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.locationTableType = locationTableType
Namespace.addCategoryObject('typeBinding', 'locationTableType', locationTableType)


# Complex type {urn:vpro:media:2009}scheduleEventsType with content type ELEMENT_ONLY
class scheduleEventsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}scheduleEventsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleEventsType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 596, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}scheduleEvent uses Python identifier scheduleEvent
    __scheduleEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), 'scheduleEvent', '__urnvpromedia2009_scheduleEventsType_urnvpromedia2009scheduleEvent', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 598, 6), )

    
    scheduleEvent = property(__scheduleEvent.value, __scheduleEvent.set, None, None)

    _ElementMap.update({
        __scheduleEvent.name() : __scheduleEvent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.scheduleEventsType = scheduleEventsType
Namespace.addCategoryObject('typeBinding', 'scheduleEventsType', scheduleEventsType)


# Complex type {urn:vpro:media:2009}locationsType with content type ELEMENT_ONLY
class locationsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}locationsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationsType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 670, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__urnvpromedia2009_locationsType_urnvpromedia2009location', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 672, 6), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.locationsType = locationsType
Namespace.addCategoryObject('typeBinding', 'locationsType', locationsType)


# Complex type {urn:vpro:media:2009}availableSubtitleType with content type EMPTY
class availableSubtitleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}availableSubtitleType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'availableSubtitleType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 699, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'language'), 'language', '__urnvpromedia2009_availableSubtitleType_language', pyxb.binding.datatypes.string)
    __language._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 701, 4)
    __language._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 701, 4)
    
    language = property(__language.value, __language.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_availableSubtitleType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 702, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 702, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __language.name() : __language,
        __type.name() : __type
    })
_module_typeBindings.availableSubtitleType = availableSubtitleType
Namespace.addCategoryObject('typeBinding', 'availableSubtitleType', availableSubtitleType)


# Complex type {urn:vpro:media:2009}baseMediaType with content type ELEMENT_ONLY
class baseMediaType (pyxb.binding.basis.complexTypeDefinition):
    """
        This is the abstract base entity for programs, groups and segments. Actually these objects are very similar and share most properties.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'baseMediaType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 182, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}crid uses Python identifier crid
    __crid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'crid'), 'crid', '__urnvpromedia2009_baseMediaType_urnvpromedia2009crid', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6), )

    
    crid = property(__crid.value, __crid.set, None, '\n            A crid (content reference identifier) is a reference to an entity in another system. E.g. a crid like\n            crid://broadcast.radiobox2/335793 refers to a broadcast with id 335793 in Radiobox. A crid must be a valid\n            URI starting with "crid://". Crids must be unique, but they can be made up freely. It is a good idea to use\n            a logical structure which can easily be associated with another system. Any POMS object can have zero or\n            more crids. They can refer to different systems, but a POMS object could also actually represent more than\n            one entity in a remote system.\n          ')

    
    # Element {urn:vpro:media:2009}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvpromedia2009_baseMediaType_urnvpromedia2009broadcaster', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 201, 6), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, '\n            One or more broadcasters can be the owner of a POMS media object. This information is meta information about the object, but it is also used\n            for assigning write access to the object in the POMS backend to employees of these given broadcasting companies.\n          ')

    
    # Element {urn:vpro:media:2009}portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portal'), 'portal', '__urnvpromedia2009_baseMediaType_urnvpromedia2009portal', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6), )

    
    portal = property(__portal.value, __portal.set, None, "\n            Optionally 'portals' can be assigned to a media object. Portals are also 'owners', and employees can also work for a certain portal.\n            This is because some portal are shared by several broadcasting companies.\n          ")

    
    # Element {urn:vpro:media:2009}exclusive uses Python identifier exclusive
    __exclusive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), 'exclusive', '__urnvpromedia2009_baseMediaType_urnvpromedia2009exclusive', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6), )

    
    exclusive = property(__exclusive.value, __exclusive.set, None, "\n            Besides having portals, which mainly indicates where the object originates, a media object can also be assigned 'portal restrictions'.\n            If a media object has any portal restrictions the media object may only be shown on these portals.\n          ")

    
    # Element {urn:vpro:media:2009}region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'region'), 'region', '__urnvpromedia2009_baseMediaType_urnvpromedia2009region', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6), )

    
    region = property(__region.value, __region.set, None, "\n            Media with a geo restriction can only be played in the indicated region (NL, BENELUX, WORLD). This\n            restriction doesn't apply to the metadata of the media object. It only applies to the actual playable content.\n          ")

    
    # Element {urn:vpro:media:2009}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpromedia2009_baseMediaType_urnvpromedia2009title', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 233, 6), )

    
    title = property(__title.value, __title.set, None, '\n            A media object has one or more titles. All titles have a type (MAIN, SUB etc.) and an owner (BROADCASTER, MIS etc.).\n            The combination of type and owner is always unique for a particular media object, so a media object cannot\n            have multiple titles of the same type and owner. Titles are sorted in order of the textualTypeEnum and the in order\n            of ownerTypeEnum when published, so the first title in a published document will be a title owned by BROADCASTER of type\n            MAIN, if that title exists.\n          ')

    
    # Element {urn:vpro:media:2009}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvpromedia2009_baseMediaType_urnvpromedia2009description', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6), )

    
    description = property(__description.value, __description.set, None, '\n            Optional descriptions for the media object. Descriptions have an owner and a type, and are ordered just like titles.\n          ')

    
    # Element {urn:vpro:media:2009}genre uses Python identifier genre
    __genre = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genre'), 'genre', '__urnvpromedia2009_baseMediaType_urnvpromedia2009genre', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6), )

    
    genre = property(__genre.value, __genre.set, None, None)

    
    # Element {urn:vpro:media:2009}tag uses Python identifier tag
    __tag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tag'), 'tag', '__urnvpromedia2009_baseMediaType_urnvpromedia2009tag', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6), )

    
    tag = property(__tag.value, __tag.set, None, None)

    
    # Element {urn:vpro:media:2009}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__urnvpromedia2009_baseMediaType_urnvpromedia2009source', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {urn:vpro:media:2009}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'country'), 'country', '__urnvpromedia2009_baseMediaType_urnvpromedia2009country', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {urn:vpro:media:2009}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'language'), 'language', '__urnvpromedia2009_baseMediaType_urnvpromedia2009language', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {urn:vpro:media:2009}availableSubtitles uses Python identifier availableSubtitles
    __availableSubtitles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'availableSubtitles'), 'availableSubtitles', '__urnvpromedia2009_baseMediaType_urnvpromedia2009availableSubtitles', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6), )

    
    availableSubtitles = property(__availableSubtitles.value, __availableSubtitles.set, None, None)

    
    # Element {urn:vpro:media:2009}avAttributes uses Python identifier avAttributes
    __avAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), 'avAttributes', '__urnvpromedia2009_baseMediaType_urnvpromedia2009avAttributes', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6), )

    
    avAttributes = property(__avAttributes.value, __avAttributes.set, None, None)

    
    # Element {urn:vpro:media:2009}releaseYear uses Python identifier releaseYear
    __releaseYear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'releaseYear'), 'releaseYear', '__urnvpromedia2009_baseMediaType_urnvpromedia2009releaseYear', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6), )

    
    releaseYear = property(__releaseYear.value, __releaseYear.set, None, None)

    
    # Element {urn:vpro:media:2009}duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__urnvpromedia2009_baseMediaType_urnvpromedia2009duration', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6), )

    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Element {urn:vpro:media:2009}credits uses Python identifier credits
    __credits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'credits'), 'credits', '__urnvpromedia2009_baseMediaType_urnvpromedia2009credits', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6), )

    
    credits = property(__credits.value, __credits.set, None, None)

    
    # Element {urn:vpro:media:2009}award uses Python identifier award
    __award = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'award'), 'award', '__urnvpromedia2009_baseMediaType_urnvpromedia2009award', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6), )

    
    award = property(__award.value, __award.set, None, None)

    
    # Element {urn:vpro:media:2009}descendantOf uses Python identifier descendantOf
    __descendantOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), 'descendantOf', '__urnvpromedia2009_baseMediaType_urnvpromedia2009descendantOf', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6), )

    
    descendantOf = property(__descendantOf.value, __descendantOf.set, None, None)

    
    # Element {urn:vpro:media:2009}memberOf uses Python identifier memberOf
    __memberOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), 'memberOf', '__urnvpromedia2009_baseMediaType_urnvpromedia2009memberOf', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6), )

    
    memberOf = property(__memberOf.value, __memberOf.set, None, None)

    
    # Element {urn:vpro:media:2009}ageRating uses Python identifier ageRating
    __ageRating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ageRating'), 'ageRating', '__urnvpromedia2009_baseMediaType_urnvpromedia2009ageRating', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6), )

    
    ageRating = property(__ageRating.value, __ageRating.set, None, None)

    
    # Element {urn:vpro:media:2009}contentRating uses Python identifier contentRating
    __contentRating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contentRating'), 'contentRating', '__urnvpromedia2009_baseMediaType_urnvpromedia2009contentRating', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6), )

    
    contentRating = property(__contentRating.value, __contentRating.set, None, None)

    
    # Element {urn:vpro:media:2009}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__urnvpromedia2009_baseMediaType_urnvpromedia2009email', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6), )

    
    email = property(__email.value, __email.set, None, None)

    
    # Element {urn:vpro:media:2009}website uses Python identifier website
    __website = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'website'), 'website', '__urnvpromedia2009_baseMediaType_urnvpromedia2009website', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6), )

    
    website = property(__website.value, __website.set, None, None)

    
    # Element {urn:vpro:media:2009}twitter uses Python identifier twitter
    __twitter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'twitter'), 'twitter', '__urnvpromedia2009_baseMediaType_urnvpromedia2009twitter', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6), )

    
    twitter = property(__twitter.value, __twitter.set, None, None)

    
    # Element {urn:vpro:media:2009}teletext uses Python identifier teletext
    __teletext = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'teletext'), 'teletext', '__urnvpromedia2009_baseMediaType_urnvpromedia2009teletext', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6), )

    
    teletext = property(__teletext.value, __teletext.set, None, None)

    
    # Element {urn:vpro:media:2009}prediction uses Python identifier prediction
    __prediction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prediction'), 'prediction', '__urnvpromedia2009_baseMediaType_urnvpromedia2009prediction', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6), )

    
    prediction = property(__prediction.value, __prediction.set, None, None)

    
    # Element {urn:vpro:media:2009}locations uses Python identifier locations
    __locations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'locations'), 'locations', '__urnvpromedia2009_baseMediaType_urnvpromedia2009locations', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6), )

    
    locations = property(__locations.value, __locations.set, None, None)

    
    # Element {urn:vpro:media:2009}scheduleEvents uses Python identifier scheduleEvents
    __scheduleEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents'), 'scheduleEvents', '__urnvpromedia2009_baseMediaType_urnvpromedia2009scheduleEvents', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6), )

    
    scheduleEvents = property(__scheduleEvents.value, __scheduleEvents.set, None, None)

    
    # Element {urn:vpro:media:2009}relation uses Python identifier relation
    __relation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relation'), 'relation', '__urnvpromedia2009_baseMediaType_urnvpromedia2009relation', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6), )

    
    relation = property(__relation.value, __relation.set, None, None)

    
    # Element {urn:vpro:media:2009}images uses Python identifier images
    __images = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'images'), 'images', '__urnvpromedia2009_baseMediaType_urnvpromedia2009images', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6), )

    
    images = property(__images.value, __images.set, None, None)

    
    # Attribute mid uses Python identifier mid
    __mid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mid'), 'mid', '__urnvpromedia2009_baseMediaType_mid', _module_typeBindings.midType)
    __mid._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 276, 4)
    __mid._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 276, 4)
    
    mid = property(__mid.value, __mid.set, None, None)

    
    # Attribute avType uses Python identifier avType
    __avType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avType'), 'avType', '__urnvpromedia2009_baseMediaType_avType', _module_typeBindings.avTypeEnum, required=True)
    __avType._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 277, 4)
    __avType._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 277, 4)
    
    avType = property(__avType.value, __avType.set, None, None)

    
    # Attribute sortDate uses Python identifier sortDate
    __sortDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sortDate'), 'sortDate', '__urnvpromedia2009_baseMediaType_sortDate', pyxb.binding.datatypes.dateTime)
    __sortDate._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 278, 4)
    __sortDate._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 278, 4)
    
    sortDate = property(__sortDate.value, __sortDate.set, None, None)

    
    # Attribute embeddable uses Python identifier embeddable
    __embeddable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'embeddable'), 'embeddable', '__urnvpromedia2009_baseMediaType_embeddable', pyxb.binding.datatypes.boolean, unicode_default='true')
    __embeddable._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 279, 4)
    __embeddable._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 279, 4)
    
    embeddable = property(__embeddable.value, __embeddable.set, None, None)

    
    # Attribute hasSubtitles uses Python identifier hasSubtitles
    __hasSubtitles = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hasSubtitles'), 'hasSubtitles', '__urnvpromedia2009_baseMediaType_hasSubtitles', pyxb.binding.datatypes.boolean, unicode_default='false')
    __hasSubtitles._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 280, 4)
    __hasSubtitles._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 280, 4)
    
    hasSubtitles = property(__hasSubtitles.value, __hasSubtitles.set, None, None)

    
    # Attribute mergedTo uses Python identifier mergedTo
    __mergedTo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mergedTo'), 'mergedTo', '__urnvpromedia2009_baseMediaType_mergedTo', _module_typeBindings.midType)
    __mergedTo._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 282, 4)
    __mergedTo._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 282, 4)
    
    mergedTo = property(__mergedTo.value, __mergedTo.set, None, None)

    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvpromedia2009_baseMediaType_urn', pyxb.binding.datatypes.anyURI)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 10, 4)
    __urn._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 10, 4)
    
    urn = property(__urn.value, __urn.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvpromedia2009_baseMediaType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 11, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 11, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvpromedia2009_baseMediaType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 12, 4)
    __publishStop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 12, 4)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    
    # Attribute publishDate uses Python identifier publishDate
    __publishDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishDate'), 'publishDate', '__urnvpromedia2009_baseMediaType_publishDate', pyxb.binding.datatypes.dateTime)
    __publishDate._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 13, 4)
    __publishDate._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 13, 4)
    
    publishDate = property(__publishDate.value, __publishDate.set, None, None)

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__urnvpromedia2009_baseMediaType_creationDate', pyxb.binding.datatypes.dateTime)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 14, 4)
    __creationDate._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 14, 4)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Attribute lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastModified'), 'lastModified', '__urnvpromedia2009_baseMediaType_lastModified', pyxb.binding.datatypes.dateTime)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 15, 4)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 15, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute workflow uses Python identifier workflow
    __workflow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'workflow'), 'workflow', '__urnvpromedia2009_baseMediaType_workflow', _ImportedBinding_npoapi_xml_shared.workflowEnumType)
    __workflow._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 16, 4)
    __workflow._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 16, 4)
    
    workflow = property(__workflow.value, __workflow.set, None, None)

    _ElementMap.update({
        __crid.name() : __crid,
        __broadcaster.name() : __broadcaster,
        __portal.name() : __portal,
        __exclusive.name() : __exclusive,
        __region.name() : __region,
        __title.name() : __title,
        __description.name() : __description,
        __genre.name() : __genre,
        __tag.name() : __tag,
        __source.name() : __source,
        __country.name() : __country,
        __language.name() : __language,
        __availableSubtitles.name() : __availableSubtitles,
        __avAttributes.name() : __avAttributes,
        __releaseYear.name() : __releaseYear,
        __duration.name() : __duration,
        __credits.name() : __credits,
        __award.name() : __award,
        __descendantOf.name() : __descendantOf,
        __memberOf.name() : __memberOf,
        __ageRating.name() : __ageRating,
        __contentRating.name() : __contentRating,
        __email.name() : __email,
        __website.name() : __website,
        __twitter.name() : __twitter,
        __teletext.name() : __teletext,
        __prediction.name() : __prediction,
        __locations.name() : __locations,
        __scheduleEvents.name() : __scheduleEvents,
        __relation.name() : __relation,
        __images.name() : __images
    })
    _AttributeMap.update({
        __mid.name() : __mid,
        __avType.name() : __avType,
        __sortDate.name() : __sortDate,
        __embeddable.name() : __embeddable,
        __hasSubtitles.name() : __hasSubtitles,
        __mergedTo.name() : __mergedTo,
        __urn.name() : __urn,
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop,
        __publishDate.name() : __publishDate,
        __creationDate.name() : __creationDate,
        __lastModified.name() : __lastModified,
        __workflow.name() : __workflow
    })
_module_typeBindings.baseMediaType = baseMediaType
Namespace.addCategoryObject('typeBinding', 'baseMediaType', baseMediaType)


# Complex type {urn:vpro:media:2009}geoRestrictionType with content type SIMPLE
class geoRestrictionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}geoRestrictionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geoRestrictionType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 299, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__urnvpromedia2009_geoRestrictionType_start', pyxb.binding.datatypes.dateTime)
    __start._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 286, 4)
    __start._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 286, 4)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute stop uses Python identifier stop
    __stop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__urnvpromedia2009_geoRestrictionType_stop', pyxb.binding.datatypes.dateTime)
    __stop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 287, 4)
    __stop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 287, 4)
    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Attribute regionId uses Python identifier regionId
    __regionId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'regionId'), 'regionId', '__urnvpromedia2009_geoRestrictionType_regionId', _module_typeBindings.geoRestrictionEnum)
    __regionId._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 302, 8)
    __regionId._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 302, 8)
    
    regionId = property(__regionId.value, __regionId.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __start.name() : __start,
        __stop.name() : __stop,
        __regionId.name() : __regionId
    })
_module_typeBindings.geoRestrictionType = geoRestrictionType
Namespace.addCategoryObject('typeBinding', 'geoRestrictionType', geoRestrictionType)


# Complex type {urn:vpro:media:2009}titleType with content type SIMPLE
class titleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}titleType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'titleType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 323, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_titleType_type', _module_typeBindings.textualTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 348, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 348, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner'), 'owner', '__urnvpromedia2009_titleType_owner', _ImportedBinding_npoapi_xml_shared.ownerTypeEnum, required=True)
    __owner._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 349, 4)
    __owner._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 349, 4)
    
    owner = property(__owner.value, __owner.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __owner.name() : __owner
    })
_module_typeBindings.titleType = titleType
Namespace.addCategoryObject('typeBinding', 'titleType', titleType)


# Complex type {urn:vpro:media:2009}descriptionType with content type SIMPLE
class descriptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}descriptionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'descriptionType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 339, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_descriptionType_type', _module_typeBindings.textualTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 348, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 348, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner'), 'owner', '__urnvpromedia2009_descriptionType_owner', _ImportedBinding_npoapi_xml_shared.ownerTypeEnum, required=True)
    __owner._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 349, 4)
    __owner._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 349, 4)
    
    owner = property(__owner.value, __owner.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __owner.name() : __owner
    })
_module_typeBindings.descriptionType = descriptionType
Namespace.addCategoryObject('typeBinding', 'descriptionType', descriptionType)


# Complex type {urn:vpro:media:2009}organizationType with content type SIMPLE
class organizationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}organizationType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'organizationType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 380, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__urnvpromedia2009_organizationType_id', _module_typeBindings.organizationIdType)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 383, 8)
    __id._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 383, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.organizationType = organizationType
Namespace.addCategoryObject('typeBinding', 'organizationType', organizationType)


# Complex type {urn:vpro:media:2009}personType with content type ELEMENT_ONLY
class personType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}personType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'personType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 473, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}givenName uses Python identifier givenName
    __givenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'givenName'), 'givenName', '__urnvpromedia2009_personType_urnvpromedia2009givenName', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 475, 6), )

    
    givenName = property(__givenName.value, __givenName.set, None, None)

    
    # Element {urn:vpro:media:2009}familyName uses Python identifier familyName
    __familyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'familyName'), 'familyName', '__urnvpromedia2009_personType_urnvpromedia2009familyName', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 476, 6), )

    
    familyName = property(__familyName.value, __familyName.set, None, None)

    
    # Attribute role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__urnvpromedia2009_personType_role', _module_typeBindings.roleType, required=True)
    __role._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 478, 4)
    __role._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 478, 4)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute gtaaUri uses Python identifier gtaaUri
    __gtaaUri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gtaaUri'), 'gtaaUri', '__urnvpromedia2009_personType_gtaaUri', pyxb.binding.datatypes.string)
    __gtaaUri._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 479, 4)
    __gtaaUri._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 479, 4)
    
    gtaaUri = property(__gtaaUri.value, __gtaaUri.set, None, None)

    _ElementMap.update({
        __givenName.name() : __givenName,
        __familyName.name() : __familyName
    })
    _AttributeMap.update({
        __role.name() : __role,
        __gtaaUri.name() : __gtaaUri
    })
_module_typeBindings.personType = personType
Namespace.addCategoryObject('typeBinding', 'personType', personType)


# Complex type {urn:vpro:media:2009}relationType with content type SIMPLE
class relationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}relationType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relationType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 521, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_relationType_type', _module_typeBindings.relationTypeType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 524, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 524, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'broadcaster'), 'broadcaster', '__urnvpromedia2009_relationType_broadcaster', pyxb.binding.datatypes.string, required=True)
    __broadcaster._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 525, 8)
    __broadcaster._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 525, 8)
    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Attribute uriRef uses Python identifier uriRef
    __uriRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uriRef'), 'uriRef', '__urnvpromedia2009_relationType_uriRef', pyxb.binding.datatypes.anyURI)
    __uriRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 526, 8)
    __uriRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 526, 8)
    
    uriRef = property(__uriRef.value, __uriRef.set, None, None)

    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvpromedia2009_relationType_urn', pyxb.binding.datatypes.anyURI)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 527, 8)
    __urn._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 527, 8)
    
    urn = property(__urn.value, __urn.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __broadcaster.name() : __broadcaster,
        __uriRef.name() : __uriRef,
        __urn.name() : __urn
    })
_module_typeBindings.relationType = relationType
Namespace.addCategoryObject('typeBinding', 'relationType', relationType)


# Complex type {urn:vpro:media:2009}twitterType with content type SIMPLE
class twitterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}twitterType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'twitterType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 564, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_twitterType_type', _module_typeBindings.STD_ANON)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 567, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 567, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.twitterType = twitterType
Namespace.addCategoryObject('typeBinding', 'twitterType', twitterType)


# Complex type {urn:vpro:media:2009}scheduleType with content type ELEMENT_ONLY
class scheduleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}scheduleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 586, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}scheduleEvent uses Python identifier scheduleEvent
    __scheduleEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), 'scheduleEvent', '__urnvpromedia2009_scheduleType_urnvpromedia2009scheduleEvent', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 588, 6), )

    
    scheduleEvent = property(__scheduleEvent.value, __scheduleEvent.set, None, None)

    
    # Attribute channel uses Python identifier channel
    __channel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'channel'), 'channel', '__urnvpromedia2009_scheduleType_channel', _module_typeBindings.channelEnum)
    __channel._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 590, 4)
    __channel._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 590, 4)
    
    channel = property(__channel.value, __channel.set, None, None)

    
    # Attribute net uses Python identifier net
    __net = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'net'), 'net', '__urnvpromedia2009_scheduleType_net', pyxb.binding.datatypes.string)
    __net._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 591, 4)
    __net._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 591, 4)
    
    net = property(__net.value, __net.set, None, None)

    
    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__urnvpromedia2009_scheduleType_date', pyxb.binding.datatypes.date)
    __date._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 592, 4)
    __date._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 592, 4)
    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute releaseVersion uses Python identifier releaseVersion
    __releaseVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'releaseVersion'), 'releaseVersion', '__urnvpromedia2009_scheduleType_releaseVersion', pyxb.binding.datatypes.short)
    __releaseVersion._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 593, 4)
    __releaseVersion._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 593, 4)
    
    releaseVersion = property(__releaseVersion.value, __releaseVersion.set, None, None)

    _ElementMap.update({
        __scheduleEvent.name() : __scheduleEvent
    })
    _AttributeMap.update({
        __channel.name() : __channel,
        __net.name() : __net,
        __date.name() : __date,
        __releaseVersion.name() : __releaseVersion
    })
_module_typeBindings.scheduleType = scheduleType
Namespace.addCategoryObject('typeBinding', 'scheduleType', scheduleType)


# Complex type {urn:vpro:media:2009}scheduleEventType with content type ELEMENT_ONLY
class scheduleEventType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}scheduleEventType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleEventType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 602, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009title', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 604, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:media:2009}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009description', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 605, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:media:2009}repeat uses Python identifier repeat
    __repeat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'repeat'), 'repeat', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009repeat', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 606, 6), )

    
    repeat = property(__repeat.value, __repeat.set, None, None)

    
    # Element {urn:vpro:media:2009}memberOf uses Python identifier memberOf
    __memberOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), 'memberOf', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009memberOf', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 607, 6), )

    
    memberOf = property(__memberOf.value, __memberOf.set, None, None)

    
    # Element {urn:vpro:media:2009}avAttributes uses Python identifier avAttributes
    __avAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), 'avAttributes', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009avAttributes', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 608, 6), )

    
    avAttributes = property(__avAttributes.value, __avAttributes.set, None, None)

    
    # Element {urn:vpro:media:2009}textSubtitles uses Python identifier textSubtitles
    __textSubtitles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'textSubtitles'), 'textSubtitles', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009textSubtitles', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 609, 6), )

    
    textSubtitles = property(__textSubtitles.value, __textSubtitles.set, None, None)

    
    # Element {urn:vpro:media:2009}textPage uses Python identifier textPage
    __textPage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'textPage'), 'textPage', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009textPage', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 610, 6), )

    
    textPage = property(__textPage.value, __textPage.set, None, None)

    
    # Element {urn:vpro:media:2009}guideDay uses Python identifier guideDay
    __guideDay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'guideDay'), 'guideDay', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009guideDay', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 611, 6), )

    
    guideDay = property(__guideDay.value, __guideDay.set, None, None)

    
    # Element {urn:vpro:media:2009}start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'start'), 'start', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009start', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 612, 6), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element {urn:vpro:media:2009}offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'offset'), 'offset', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009offset', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 613, 6), )

    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Element {urn:vpro:media:2009}duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009duration', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 614, 6), )

    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Element {urn:vpro:media:2009}poProgID uses Python identifier poProgID
    __poProgID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'poProgID'), 'poProgID', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009poProgID', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 615, 6), )

    
    poProgID = property(__poProgID.value, __poProgID.set, None, None)

    
    # Element {urn:vpro:media:2009}primaryLifestyle uses Python identifier primaryLifestyle
    __primaryLifestyle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'primaryLifestyle'), 'primaryLifestyle', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009primaryLifestyle', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 616, 6), )

    
    primaryLifestyle = property(__primaryLifestyle.value, __primaryLifestyle.set, None, None)

    
    # Element {urn:vpro:media:2009}secondaryLifestyle uses Python identifier secondaryLifestyle
    __secondaryLifestyle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'secondaryLifestyle'), 'secondaryLifestyle', '__urnvpromedia2009_scheduleEventType_urnvpromedia2009secondaryLifestyle', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 617, 6), )

    
    secondaryLifestyle = property(__secondaryLifestyle.value, __secondaryLifestyle.set, None, None)

    
    # Attribute imi uses Python identifier imi
    __imi = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'imi'), 'imi', '__urnvpromedia2009_scheduleEventType_imi', pyxb.binding.datatypes.string)
    __imi._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 619, 4)
    __imi._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 619, 4)
    
    imi = property(__imi.value, __imi.set, None, None)

    
    # Attribute channel uses Python identifier channel
    __channel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'channel'), 'channel', '__urnvpromedia2009_scheduleEventType_channel', _module_typeBindings.channelEnum)
    __channel._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 620, 4)
    __channel._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 620, 4)
    
    channel = property(__channel.value, __channel.set, None, None)

    
    # Attribute net uses Python identifier net
    __net = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'net'), 'net', '__urnvpromedia2009_scheduleEventType_net', pyxb.binding.datatypes.string)
    __net._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 621, 4)
    __net._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 621, 4)
    
    net = property(__net.value, __net.set, None, None)

    
    # Attribute guideDay uses Python identifier guideDay_
    __guideDay_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'guideDay'), 'guideDay_', '__urnvpromedia2009_scheduleEventType_guideDay', pyxb.binding.datatypes.date)
    __guideDay_._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 622, 4)
    __guideDay_._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 622, 4)
    
    guideDay_ = property(__guideDay_.value, __guideDay_.set, None, None)

    
    # Attribute midRef uses Python identifier midRef
    __midRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'midRef'), 'midRef', '__urnvpromedia2009_scheduleEventType_midRef', _module_typeBindings.midType, required=True)
    __midRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 623, 4)
    __midRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 623, 4)
    
    midRef = property(__midRef.value, __midRef.set, None, None)

    
    # Attribute urnRef uses Python identifier urnRef
    __urnRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urnRef'), 'urnRef', '__urnvpromedia2009_scheduleEventType_urnRef', pyxb.binding.datatypes.anyURI, required=True)
    __urnRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 624, 4)
    __urnRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 624, 4)
    
    urnRef = property(__urnRef.value, __urnRef.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_scheduleEventType_type', _module_typeBindings.scheduleEventTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 625, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 625, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __repeat.name() : __repeat,
        __memberOf.name() : __memberOf,
        __avAttributes.name() : __avAttributes,
        __textSubtitles.name() : __textSubtitles,
        __textPage.name() : __textPage,
        __guideDay.name() : __guideDay,
        __start.name() : __start,
        __offset.name() : __offset,
        __duration.name() : __duration,
        __poProgID.name() : __poProgID,
        __primaryLifestyle.name() : __primaryLifestyle,
        __secondaryLifestyle.name() : __secondaryLifestyle
    })
    _AttributeMap.update({
        __imi.name() : __imi,
        __channel.name() : __channel,
        __net.name() : __net,
        __guideDay_.name() : __guideDay_,
        __midRef.name() : __midRef,
        __urnRef.name() : __urnRef,
        __type.name() : __type
    })
_module_typeBindings.scheduleEventType = scheduleEventType
Namespace.addCategoryObject('typeBinding', 'scheduleEventType', scheduleEventType)


# Complex type {urn:vpro:media:2009}scheduleEventTitle with content type SIMPLE
class scheduleEventTitle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}scheduleEventTitle with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleEventTitle')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 628, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner'), 'owner', '__urnvpromedia2009_scheduleEventTitle_owner', _ImportedBinding_npoapi_xml_shared.ownerTypeEnum, required=True)
    __owner._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 631, 8)
    __owner._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 631, 8)
    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_scheduleEventTitle_type', _module_typeBindings.textualTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 632, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 632, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __owner.name() : __owner,
        __type.name() : __type
    })
_module_typeBindings.scheduleEventTitle = scheduleEventTitle
Namespace.addCategoryObject('typeBinding', 'scheduleEventTitle', scheduleEventTitle)


# Complex type {urn:vpro:media:2009}scheduleEventDescription with content type SIMPLE
class scheduleEventDescription (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}scheduleEventDescription with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleEventDescription')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 637, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner'), 'owner', '__urnvpromedia2009_scheduleEventDescription_owner', _ImportedBinding_npoapi_xml_shared.ownerTypeEnum, required=True)
    __owner._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 640, 8)
    __owner._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 640, 8)
    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_scheduleEventDescription_type', _module_typeBindings.textualTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 641, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 641, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __owner.name() : __owner,
        __type.name() : __type
    })
_module_typeBindings.scheduleEventDescription = scheduleEventDescription
Namespace.addCategoryObject('typeBinding', 'scheduleEventDescription', scheduleEventDescription)


# Complex type {urn:vpro:media:2009}predictionType with content type SIMPLE
class predictionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}predictionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'predictionType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 660, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute state uses Python identifier state
    __state = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'state'), 'state', '__urnvpromedia2009_predictionType_state', _module_typeBindings.predictionStateEnum)
    __state._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 663, 8)
    __state._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 663, 8)
    
    state = property(__state.value, __state.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvpromedia2009_predictionType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 664, 8)
    __publishStart._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 664, 8)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvpromedia2009_predictionType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 665, 8)
    __publishStop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 665, 8)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __state.name() : __state,
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop
    })
_module_typeBindings.predictionType = predictionType
Namespace.addCategoryObject('typeBinding', 'predictionType', predictionType)


# Complex type {urn:vpro:media:2009}locationType with content type ELEMENT_ONLY
class locationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}locationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 676, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}broadcasters uses Python identifier broadcasters
    __broadcasters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), 'broadcasters', '__urnvpromedia2009_locationType_urnvpromedia2009broadcasters', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 678, 6), )

    
    broadcasters = property(__broadcasters.value, __broadcasters.set, None, None)

    
    # Element {urn:vpro:media:2009}programUrl uses Python identifier programUrl
    __programUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), 'programUrl', '__urnvpromedia2009_locationType_urnvpromedia2009programUrl', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 679, 6), )

    
    programUrl = property(__programUrl.value, __programUrl.set, None, None)

    
    # Element {urn:vpro:media:2009}avAttributes uses Python identifier avAttributes
    __avAttributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), 'avAttributes', '__urnvpromedia2009_locationType_urnvpromedia2009avAttributes', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 680, 6), )

    
    avAttributes = property(__avAttributes.value, __avAttributes.set, None, None)

    
    # Element {urn:vpro:media:2009}subtitles uses Python identifier subtitles
    __subtitles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subtitles'), 'subtitles', '__urnvpromedia2009_locationType_urnvpromedia2009subtitles', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 681, 6), )

    
    subtitles = property(__subtitles.value, __subtitles.set, None, None)

    
    # Element {urn:vpro:media:2009}offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'offset'), 'offset', '__urnvpromedia2009_locationType_urnvpromedia2009offset', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 682, 6), )

    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Element {urn:vpro:media:2009}duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__urnvpromedia2009_locationType_urnvpromedia2009duration', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 683, 6), )

    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_locationType_type', _module_typeBindings.locationTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 685, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 685, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute platform uses Python identifier platform
    __platform = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'platform'), 'platform', '__urnvpromedia2009_locationType_platform', _module_typeBindings.platformTypeEnum)
    __platform._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 686, 4)
    __platform._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 686, 4)
    
    platform = property(__platform.value, __platform.set, None, None)

    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner'), 'owner', '__urnvpromedia2009_locationType_owner', _ImportedBinding_npoapi_xml_shared.ownerTypeEnum, required=True)
    __owner._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 687, 4)
    __owner._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 687, 4)
    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvpromedia2009_locationType_urn', pyxb.binding.datatypes.anyURI)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 10, 4)
    __urn._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 10, 4)
    
    urn = property(__urn.value, __urn.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvpromedia2009_locationType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 11, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 11, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvpromedia2009_locationType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 12, 4)
    __publishStop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 12, 4)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    
    # Attribute publishDate uses Python identifier publishDate
    __publishDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishDate'), 'publishDate', '__urnvpromedia2009_locationType_publishDate', pyxb.binding.datatypes.dateTime)
    __publishDate._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 13, 4)
    __publishDate._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 13, 4)
    
    publishDate = property(__publishDate.value, __publishDate.set, None, None)

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__urnvpromedia2009_locationType_creationDate', pyxb.binding.datatypes.dateTime)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 14, 4)
    __creationDate._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 14, 4)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Attribute lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastModified'), 'lastModified', '__urnvpromedia2009_locationType_lastModified', pyxb.binding.datatypes.dateTime)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 15, 4)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 15, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute workflow uses Python identifier workflow
    __workflow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'workflow'), 'workflow', '__urnvpromedia2009_locationType_workflow', _ImportedBinding_npoapi_xml_shared.workflowEnumType)
    __workflow._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 16, 4)
    __workflow._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 16, 4)
    
    workflow = property(__workflow.value, __workflow.set, None, None)

    _ElementMap.update({
        __broadcasters.name() : __broadcasters,
        __programUrl.name() : __programUrl,
        __avAttributes.name() : __avAttributes,
        __subtitles.name() : __subtitles,
        __offset.name() : __offset,
        __duration.name() : __duration
    })
    _AttributeMap.update({
        __type.name() : __type,
        __platform.name() : __platform,
        __owner.name() : __owner,
        __urn.name() : __urn,
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop,
        __publishDate.name() : __publishDate,
        __creationDate.name() : __creationDate,
        __lastModified.name() : __lastModified,
        __workflow.name() : __workflow
    })
_module_typeBindings.locationType = locationType
Namespace.addCategoryObject('typeBinding', 'locationType', locationType)


# Complex type {urn:vpro:media:2009}descendantRefType with content type EMPTY
class descendantRefType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}descendantRefType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'descendantRefType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 718, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute midRef uses Python identifier midRef
    __midRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'midRef'), 'midRef', '__urnvpromedia2009_descendantRefType_midRef', _module_typeBindings.midType)
    __midRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 719, 4)
    __midRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 719, 4)
    
    midRef = property(__midRef.value, __midRef.set, None, None)

    
    # Attribute urnRef uses Python identifier urnRef
    __urnRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urnRef'), 'urnRef', '__urnvpromedia2009_descendantRefType_urnRef', pyxb.binding.datatypes.anyURI)
    __urnRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 720, 4)
    __urnRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 720, 4)
    
    urnRef = property(__urnRef.value, __urnRef.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_descendantRefType_type', _module_typeBindings.mediaTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 721, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 721, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __midRef.name() : __midRef,
        __urnRef.name() : __urnRef,
        __type.name() : __type
    })
_module_typeBindings.descendantRefType = descendantRefType
Namespace.addCategoryObject('typeBinding', 'descendantRefType', descendantRefType)


# Complex type {urn:vpro:media:2009}memberRefType with content type EMPTY
class memberRefType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}memberRefType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'memberRefType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 727, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute midRef uses Python identifier midRef
    __midRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'midRef'), 'midRef', '__urnvpromedia2009_memberRefType_midRef', _module_typeBindings.midType)
    __midRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 728, 4)
    __midRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 728, 4)
    
    midRef = property(__midRef.value, __midRef.set, None, '\n          Reference to the MID of the parent of this object.\n        ')

    
    # Attribute urnRef uses Python identifier urnRef
    __urnRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urnRef'), 'urnRef', '__urnvpromedia2009_memberRefType_urnRef', pyxb.binding.datatypes.anyURI)
    __urnRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 735, 4)
    __urnRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 735, 4)
    
    urnRef = property(__urnRef.value, __urnRef.set, None, "\n          Reference to the URN of the parent of this object. URN's are no longer actively used, but the attribute is\n          still available for backwards compatibility.\n        ")

    
    # Attribute cridRef uses Python identifier cridRef
    __cridRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cridRef'), 'cridRef', '__urnvpromedia2009_memberRefType_cridRef', pyxb.binding.datatypes.anyURI)
    __cridRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 743, 4)
    __cridRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 743, 4)
    
    cridRef = property(__cridRef.value, __cridRef.set, None, '\n          Reference to a crid of the parent of this object. This is only used for imports from systems that cannot\n          supply a MID or URN. POMS does not export or publish parent crids.\n        ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_memberRefType_type', _module_typeBindings.mediaTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 751, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 751, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__urnvpromedia2009_memberRefType_index', pyxb.binding.datatypes.positiveInteger)
    __index._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 752, 4)
    __index._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 752, 4)
    
    index = property(__index.value, __index.set, None, None)

    
    # Attribute highlighted uses Python identifier highlighted
    __highlighted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'highlighted'), 'highlighted', '__urnvpromedia2009_memberRefType_highlighted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __highlighted._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 753, 4)
    __highlighted._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 753, 4)
    
    highlighted = property(__highlighted.value, __highlighted.set, None, None)

    
    # Attribute added uses Python identifier added
    __added = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'added'), 'added', '__urnvpromedia2009_memberRefType_added', pyxb.binding.datatypes.dateTime)
    __added._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 754, 4)
    __added._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 754, 4)
    
    added = property(__added.value, __added.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __midRef.name() : __midRef,
        __urnRef.name() : __urnRef,
        __cridRef.name() : __cridRef,
        __type.name() : __type,
        __index.name() : __index,
        __highlighted.name() : __highlighted,
        __added.name() : __added
    })
_module_typeBindings.memberRefType = memberRefType
Namespace.addCategoryObject('typeBinding', 'memberRefType', memberRefType)


# Complex type {urn:vpro:media:2009}genreType with content type ELEMENT_ONLY
class genreType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}genreType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genreType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 800, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:media:2009}term uses Python identifier term
    __term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'term'), 'term', '__urnvpromedia2009_genreType_urnvpromedia2009term', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 802, 6), )

    
    term = property(__term.value, __term.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__urnvpromedia2009_genreType_id', _module_typeBindings.genreIdType, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 804, 4)
    __id._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 804, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __term.name() : __term
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.genreType = genreType
Namespace.addCategoryObject('typeBinding', 'genreType', genreType)


# Complex type {urn:vpro:media:2009}countryType with content type SIMPLE
class countryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}countryType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'countryType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 929, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__urnvpromedia2009_countryType_code', _module_typeBindings.countryCodeType)
    __code._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 932, 8)
    __code._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 932, 8)
    
    code = property(__code.value, __code.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code
    })
_module_typeBindings.countryType = countryType
Namespace.addCategoryObject('typeBinding', 'countryType', countryType)


# Complex type {urn:vpro:media:2009}languageType with content type SIMPLE
class languageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:media:2009}languageType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'languageType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 949, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__urnvpromedia2009_languageType_code', _module_typeBindings.languageCodeType)
    __code._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 952, 8)
    __code._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 952, 8)
    
    code = property(__code.value, __code.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code
    })
_module_typeBindings.languageType = languageType
Namespace.addCategoryObject('typeBinding', 'languageType', languageType)


# Complex type {urn:vpro:media:2009}programType with content type ELEMENT_ONLY
class programType (baseMediaType):
    """Complex type {urn:vpro:media:2009}programType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'programType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 83, 2)
    _ElementMap = baseMediaType._ElementMap.copy()
    _AttributeMap = baseMediaType._AttributeMap.copy()
    # Base type is baseMediaType
    
    # Element {urn:vpro:media:2009}episodeOf uses Python identifier episodeOf
    __episodeOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), 'episodeOf', '__urnvpromedia2009_programType_urnvpromedia2009episodeOf', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 87, 10), )

    
    episodeOf = property(__episodeOf.value, __episodeOf.set, None, "\n                A program (only if its type is 'BROADCAST') can be an episode of a group of type 'SERIES' or 'SEASON'.\n              ")

    
    # Element {urn:vpro:media:2009}segments uses Python identifier segments
    __segments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'segments'), 'segments', '__urnvpromedia2009_programType_urnvpromedia2009segments', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 94, 10), )

    
    segments = property(__segments.value, __segments.set, None, None)

    
    # Element crid ({urn:vpro:media:2009}crid) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element broadcaster ({urn:vpro:media:2009}broadcaster) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element portal ({urn:vpro:media:2009}portal) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element exclusive ({urn:vpro:media:2009}exclusive) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element region ({urn:vpro:media:2009}region) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element title ({urn:vpro:media:2009}title) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element description ({urn:vpro:media:2009}description) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element genre ({urn:vpro:media:2009}genre) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element tag ({urn:vpro:media:2009}tag) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element source ({urn:vpro:media:2009}source) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element country ({urn:vpro:media:2009}country) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element language ({urn:vpro:media:2009}language) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element availableSubtitles ({urn:vpro:media:2009}availableSubtitles) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element avAttributes ({urn:vpro:media:2009}avAttributes) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element releaseYear ({urn:vpro:media:2009}releaseYear) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element duration ({urn:vpro:media:2009}duration) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element credits ({urn:vpro:media:2009}credits) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element award ({urn:vpro:media:2009}award) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element descendantOf ({urn:vpro:media:2009}descendantOf) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element memberOf ({urn:vpro:media:2009}memberOf) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element ageRating ({urn:vpro:media:2009}ageRating) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element contentRating ({urn:vpro:media:2009}contentRating) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element email ({urn:vpro:media:2009}email) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element website ({urn:vpro:media:2009}website) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element twitter ({urn:vpro:media:2009}twitter) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element teletext ({urn:vpro:media:2009}teletext) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element prediction ({urn:vpro:media:2009}prediction) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element locations ({urn:vpro:media:2009}locations) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element scheduleEvents ({urn:vpro:media:2009}scheduleEvents) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element relation ({urn:vpro:media:2009}relation) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element images ({urn:vpro:media:2009}images) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_programType_type', _module_typeBindings.programTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 102, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 102, 8)
    
    type = property(__type.value, __type.set, None, '\n              The type of this program (e.g. BROADCAST, TRACK, CLIP)\n            ')

    
    # Attribute mid inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute avType inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute sortDate inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute embeddable inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute hasSubtitles inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute mergedTo inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute urn inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute publishStart inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute publishStop inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute publishDate inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute creationDate inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute lastModified inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute workflow inherited from {urn:vpro:media:2009}baseMediaType
    _ElementMap.update({
        __episodeOf.name() : __episodeOf,
        __segments.name() : __segments
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.programType = programType
Namespace.addCategoryObject('typeBinding', 'programType', programType)


# Complex type {urn:vpro:media:2009}segmentType with content type ELEMENT_ONLY
class segmentType (baseMediaType):
    """Complex type {urn:vpro:media:2009}segmentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'segmentType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 507, 2)
    _ElementMap = baseMediaType._ElementMap.copy()
    _AttributeMap = baseMediaType._AttributeMap.copy()
    # Base type is baseMediaType
    
    # Element crid ({urn:vpro:media:2009}crid) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element broadcaster ({urn:vpro:media:2009}broadcaster) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element portal ({urn:vpro:media:2009}portal) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element exclusive ({urn:vpro:media:2009}exclusive) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element region ({urn:vpro:media:2009}region) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element title ({urn:vpro:media:2009}title) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element description ({urn:vpro:media:2009}description) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element genre ({urn:vpro:media:2009}genre) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element tag ({urn:vpro:media:2009}tag) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element source ({urn:vpro:media:2009}source) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element country ({urn:vpro:media:2009}country) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element language ({urn:vpro:media:2009}language) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element availableSubtitles ({urn:vpro:media:2009}availableSubtitles) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element avAttributes ({urn:vpro:media:2009}avAttributes) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element releaseYear ({urn:vpro:media:2009}releaseYear) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element duration ({urn:vpro:media:2009}duration) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element credits ({urn:vpro:media:2009}credits) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element award ({urn:vpro:media:2009}award) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element descendantOf ({urn:vpro:media:2009}descendantOf) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element memberOf ({urn:vpro:media:2009}memberOf) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element ageRating ({urn:vpro:media:2009}ageRating) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element contentRating ({urn:vpro:media:2009}contentRating) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element email ({urn:vpro:media:2009}email) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element website ({urn:vpro:media:2009}website) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element twitter ({urn:vpro:media:2009}twitter) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element teletext ({urn:vpro:media:2009}teletext) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element prediction ({urn:vpro:media:2009}prediction) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element locations ({urn:vpro:media:2009}locations) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element scheduleEvents ({urn:vpro:media:2009}scheduleEvents) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element relation ({urn:vpro:media:2009}relation) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element images ({urn:vpro:media:2009}images) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element {urn:vpro:media:2009}start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'start'), 'start', '__urnvpromedia2009_segmentType_urnvpromedia2009start', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 511, 10), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute mid inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute avType inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute sortDate inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute embeddable inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute hasSubtitles inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute mergedTo inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute midRef uses Python identifier midRef
    __midRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'midRef'), 'midRef', '__urnvpromedia2009_segmentType_midRef', _module_typeBindings.midType, required=True)
    __midRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 513, 8)
    __midRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 513, 8)
    
    midRef = property(__midRef.value, __midRef.set, None, None)

    
    # Attribute urnRef uses Python identifier urnRef
    __urnRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urnRef'), 'urnRef', '__urnvpromedia2009_segmentType_urnRef', pyxb.binding.datatypes.anyURI, required=True)
    __urnRef._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 514, 8)
    __urnRef._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 514, 8)
    
    urnRef = property(__urnRef.value, __urnRef.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_segmentType_type', _module_typeBindings.segmentTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 515, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 515, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute urn inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute publishStart inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute publishStop inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute publishDate inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute creationDate inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute lastModified inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute workflow inherited from {urn:vpro:media:2009}baseMediaType
    _ElementMap.update({
        __start.name() : __start
    })
    _AttributeMap.update({
        __midRef.name() : __midRef,
        __urnRef.name() : __urnRef,
        __type.name() : __type
    })
_module_typeBindings.segmentType = segmentType
Namespace.addCategoryObject('typeBinding', 'segmentType', segmentType)


# Complex type {urn:vpro:media:2009}groupType with content type ELEMENT_ONLY
class groupType (baseMediaType):
    """Complex type {urn:vpro:media:2009}groupType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'groupType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 705, 2)
    _ElementMap = baseMediaType._ElementMap.copy()
    _AttributeMap = baseMediaType._AttributeMap.copy()
    # Base type is baseMediaType
    
    # Element crid ({urn:vpro:media:2009}crid) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element broadcaster ({urn:vpro:media:2009}broadcaster) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element portal ({urn:vpro:media:2009}portal) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element exclusive ({urn:vpro:media:2009}exclusive) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element region ({urn:vpro:media:2009}region) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element title ({urn:vpro:media:2009}title) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element description ({urn:vpro:media:2009}description) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element genre ({urn:vpro:media:2009}genre) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element tag ({urn:vpro:media:2009}tag) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element source ({urn:vpro:media:2009}source) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element country ({urn:vpro:media:2009}country) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element language ({urn:vpro:media:2009}language) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element availableSubtitles ({urn:vpro:media:2009}availableSubtitles) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element avAttributes ({urn:vpro:media:2009}avAttributes) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element releaseYear ({urn:vpro:media:2009}releaseYear) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element duration ({urn:vpro:media:2009}duration) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element credits ({urn:vpro:media:2009}credits) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element award ({urn:vpro:media:2009}award) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element descendantOf ({urn:vpro:media:2009}descendantOf) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element memberOf ({urn:vpro:media:2009}memberOf) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element ageRating ({urn:vpro:media:2009}ageRating) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element contentRating ({urn:vpro:media:2009}contentRating) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element email ({urn:vpro:media:2009}email) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element website ({urn:vpro:media:2009}website) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element twitter ({urn:vpro:media:2009}twitter) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element teletext ({urn:vpro:media:2009}teletext) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element prediction ({urn:vpro:media:2009}prediction) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element locations ({urn:vpro:media:2009}locations) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element scheduleEvents ({urn:vpro:media:2009}scheduleEvents) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element relation ({urn:vpro:media:2009}relation) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element images ({urn:vpro:media:2009}images) inherited from {urn:vpro:media:2009}baseMediaType
    
    # Element {urn:vpro:media:2009}poSeriesID uses Python identifier poSeriesID
    __poSeriesID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'poSeriesID'), 'poSeriesID', '__urnvpromedia2009_groupType_urnvpromedia2009poSeriesID', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 709, 10), )

    
    poSeriesID = property(__poSeriesID.value, __poSeriesID.set, None, None)

    
    # Attribute mid inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute avType inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute sortDate inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute embeddable inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute hasSubtitles inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute mergedTo inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute isOrdered uses Python identifier isOrdered
    __isOrdered = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isOrdered'), 'isOrdered', '__urnvpromedia2009_groupType_isOrdered', pyxb.binding.datatypes.boolean, required=True)
    __isOrdered._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 711, 8)
    __isOrdered._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 711, 8)
    
    isOrdered = property(__isOrdered.value, __isOrdered.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpromedia2009_groupType_type', _module_typeBindings.groupTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 712, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 712, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute defaultElement uses Python identifier defaultElement
    __defaultElement = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'defaultElement'), 'defaultElement', '__urnvpromedia2009_groupType_defaultElement', pyxb.binding.datatypes.long)
    __defaultElement._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 713, 8)
    __defaultElement._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 713, 8)
    
    defaultElement = property(__defaultElement.value, __defaultElement.set, None, None)

    
    # Attribute urn inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute publishStart inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute publishStop inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute publishDate inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute creationDate inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute lastModified inherited from {urn:vpro:media:2009}baseMediaType
    
    # Attribute workflow inherited from {urn:vpro:media:2009}baseMediaType
    _ElementMap.update({
        __poSeriesID.name() : __poSeriesID
    })
    _AttributeMap.update({
        __isOrdered.name() : __isOrdered,
        __type.name() : __type,
        __defaultElement.name() : __defaultElement
    })
_module_typeBindings.groupType = groupType
Namespace.addCategoryObject('typeBinding', 'groupType', groupType)


mediaInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaInformation'), mediaTableType, documentation='\n        Base element only used when programs, groups and schedule information need to be bundled in one XML. E.g. when distributing to cable companies.\n      ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 17, 2))
Namespace.addCategoryObject('elementBinding', mediaInformation.name().localName(), mediaInformation)

schedule = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'schedule'), scheduleType, documentation="\n        Programs of type 'BROADCAST' can contain schedule events. A schedule indicates on which channel and at what time the program is broadcast. A schedule is a container which contains the schedule events of different programs, for a certain period of time.\n      ", location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 45, 2))
Namespace.addCategoryObject('elementBinding', schedule.name().localName(), schedule)

program = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'program'), programType, documentation='\n        This is the most used entity in POMS. It represents e.g. one broadcast program or one web-only clip. It represent a standalone entity which a consumer can view or listen to.\n      ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 24, 2))
Namespace.addCategoryObject('elementBinding', program.name().localName(), program)

group = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'group'), groupType, documentation='\n        A groups collects a number of programs and/or other groups. Examples: season, series, playlist and album.\n      ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 31, 2))
Namespace.addCategoryObject('elementBinding', group.name().localName(), group)

segment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'segment'), segmentType, documentation='\n        A program can contain a number of segments. A segment is an identifiable part of a program.\n      ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 38, 2))
Namespace.addCategoryObject('elementBinding', segment.name().localName(), segment)



mediaTableType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'schedule'), scheduleType, scope=mediaTableType, documentation="\n        Programs of type 'BROADCAST' can contain schedule events. A schedule indicates on which channel and at what time the program is broadcast. A schedule is a container which contains the schedule events of different programs, for a certain period of time.\n      ", location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 45, 2)))

mediaTableType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'programTable'), programTableType, scope=mediaTableType, documentation='A table with all program objects in this container', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 55, 6)))

mediaTableType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'groupTable'), groupTableType, scope=mediaTableType, documentation='A table with all group objects in this container', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 60, 6)))

mediaTableType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locationTable'), locationTableType, scope=mediaTableType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 65, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 55, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 60, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 65, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 66, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaTableType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'programTable')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 55, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaTableType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'groupTable')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 60, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaTableType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locationTable')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 65, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaTableType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'schedule')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 66, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaTableType._Automaton = _BuildAutomaton()




programTableType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'program'), programType, scope=programTableType, documentation='\n        This is the most used entity in POMS. It represents e.g. one broadcast program or one web-only clip. It represent a standalone entity which a consumer can view or listen to.\n      ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 24, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 79, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(programTableType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'program')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 79, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
programTableType._Automaton = _BuildAutomaton_()




broadcasterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), organizationType, scope=broadcasterType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 376, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 376, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(broadcasterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 376, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
broadcasterType._Automaton = _BuildAutomaton_2()




portalsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portal'), organizationType, scope=portalsType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 390, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 390, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(portalsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 390, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
portalsType._Automaton = _BuildAutomaton_3()




avAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bitrate'), pyxb.binding.datatypes.long, scope=avAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 404, 6)))

avAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat'), avFileFormatEnum, scope=avAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 405, 6)))

avAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'videoAttributes'), videoAttributesType, scope=avAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 406, 6)))

avAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audioAttributes'), audioAttributesType, scope=avAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 407, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 404, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 405, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 406, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 407, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(avAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bitrate')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 404, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(avAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avFileFormat')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 405, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(avAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'videoAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 406, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(avAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'audioAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 407, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
avAttributesType._Automaton = _BuildAutomaton_4()




videoAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'color'), colorType, scope=videoAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 435, 6)))

videoAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'videoCoding'), pyxb.binding.datatypes.string, scope=videoAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 436, 6)))

videoAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aspectRatio'), aspectRatioEnum, scope=videoAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 437, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 435, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 436, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 437, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(videoAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'color')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 435, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(videoAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'videoCoding')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 436, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(videoAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aspectRatio')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 437, 6))
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
videoAttributesType._Automaton = _BuildAutomaton_5()




audioAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numberOfChannels'), pyxb.binding.datatypes.short, scope=audioAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 461, 6)))

audioAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audioCoding'), pyxb.binding.datatypes.string, scope=audioAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 462, 6)))

audioAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'language'), pyxb.binding.datatypes.string, scope=audioAttributesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 463, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 461, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 462, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 463, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(audioAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'numberOfChannels')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 461, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(audioAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'audioCoding')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 462, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(audioAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 463, 6))
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
audioAttributesType._Automaton = _BuildAutomaton_6()




creditsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), personType, scope=creditsType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 469, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 469, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(creditsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 469, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
creditsType._Automaton = _BuildAutomaton_7()




segmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'segment'), segmentType, scope=segmentsType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 503, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 503, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(segmentsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'segment')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 503, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
segmentsType._Automaton = _BuildAutomaton_8()




imagesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_shared, 'image'), _ImportedBinding_npoapi_xml_shared.imageType, scope=imagesType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 7, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 534, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(imagesType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_shared, 'image')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 534, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
imagesType._Automaton = _BuildAutomaton_9()




groupTableType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'group'), groupType, scope=groupTableType, documentation='\n        A groups collects a number of programs and/or other groups. Examples: season, series, playlist and album.\n      ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 31, 2)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(groupTableType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'group')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 553, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
groupTableType._Automaton = _BuildAutomaton_10()




locationTableType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), locationType, scope=locationTableType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 581, 6)))

locationTableType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), scheduleEventType, scope=locationTableType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 582, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 581, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 582, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(locationTableType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 581, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(locationTableType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 582, 6))
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
locationTableType._Automaton = _BuildAutomaton_11()




scheduleEventsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), scheduleEventType, scope=scheduleEventsType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 598, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 598, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 598, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
scheduleEventsType._Automaton = _BuildAutomaton_12()




locationsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), locationType, scope=locationsType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 672, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 672, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(locationsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 672, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
locationsType._Automaton = _BuildAutomaton_13()




baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'crid'), pyxb.binding.datatypes.anyURI, scope=baseMediaType, documentation='\n            A crid (content reference identifier) is a reference to an entity in another system. E.g. a crid like\n            crid://broadcast.radiobox2/335793 refers to a broadcast with id 335793 in Radiobox. A crid must be a valid\n            URI starting with "crid://". Crids must be unique, but they can be made up freely. It is a good idea to use\n            a logical structure which can easily be associated with another system. Any POMS object can have zero or\n            more crids. They can refer to different systems, but a POMS object could also actually represent more than\n            one entity in a remote system.\n          ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), organizationType, scope=baseMediaType, documentation='\n            One or more broadcasters can be the owner of a POMS media object. This information is meta information about the object, but it is also used\n            for assigning write access to the object in the POMS backend to employees of these given broadcasting companies.\n          ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 201, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portal'), organizationType, scope=baseMediaType, documentation="\n            Optionally 'portals' can be assigned to a media object. Portals are also 'owners', and employees can also work for a certain portal.\n            This is because some portal are shared by several broadcasting companies.\n          ", location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exclusive'), portalRestrictionType, scope=baseMediaType, documentation="\n            Besides having portals, which mainly indicates where the object originates, a media object can also be assigned 'portal restrictions'.\n            If a media object has any portal restrictions the media object may only be shown on these portals.\n          ", location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'region'), geoRestrictionType, scope=baseMediaType, documentation="\n            Media with a geo restriction can only be played in the indicated region (NL, BENELUX, WORLD). This\n            restriction doesn't apply to the metadata of the media object. It only applies to the actual playable content.\n          ", location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), titleType, scope=baseMediaType, documentation='\n            A media object has one or more titles. All titles have a type (MAIN, SUB etc.) and an owner (BROADCASTER, MIS etc.).\n            The combination of type and owner is always unique for a particular media object, so a media object cannot\n            have multiple titles of the same type and owner. Titles are sorted in order of the textualTypeEnum and the in order\n            of ownerTypeEnum when published, so the first title in a published document will be a title owned by BROADCASTER of type\n            MAIN, if that title exists.\n          ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 233, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), descriptionType, scope=baseMediaType, documentation='\n            Optional descriptions for the media object. Descriptions have an owner and a type, and are ordered just like titles.\n          ', location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genre'), genreType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tag'), tagType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), pyxb.binding.datatypes.string, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'country'), countryType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'language'), languageType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'availableSubtitles'), availableSubtitleType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), avAttributesType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'releaseYear'), pyxb.binding.datatypes.short, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'duration'), pyxb.binding.datatypes.duration, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'credits'), creditsType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'award'), pyxb.binding.datatypes.string, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), descendantRefType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), memberRefType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ageRating'), ageRatingType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contentRating'), contentRatingType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), pyxb.binding.datatypes.anyURI, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'website'), websiteType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'twitter'), twitterType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'teletext'), pyxb.binding.datatypes.short, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prediction'), predictionType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locations'), locationsType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents'), scheduleEventsType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relation'), relationType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6)))

baseMediaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'images'), imagesType, scope=baseMediaType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6))
    counters.add(cc_28)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 201, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 233, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'availableSubtitles')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releaseYear')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'award')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ageRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contentRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'website')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'twitter')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'teletext')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prediction')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(baseMediaType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
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
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, True) ]))
    st_30._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
baseMediaType._Automaton = _BuildAutomaton_14()




personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'givenName'), pyxb.binding.datatypes.string, scope=personType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 475, 6)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'familyName'), pyxb.binding.datatypes.string, scope=personType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 476, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'givenName')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 475, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'familyName')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 476, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
personType._Automaton = _BuildAutomaton_15()




scheduleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent'), scheduleEventType, scope=scheduleType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 588, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(scheduleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvent')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 588, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
scheduleType._Automaton = _BuildAutomaton_16()




scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), scheduleEventTitle, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 604, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), scheduleEventDescription, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 605, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'repeat'), repeatType, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 606, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), pyxb.binding.datatypes.anyURI, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 607, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), avAttributesType, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 608, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'textSubtitles'), pyxb.binding.datatypes.string, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 609, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'textPage'), pyxb.binding.datatypes.string, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 610, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'guideDay'), pyxb.binding.datatypes.date, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 611, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'start'), pyxb.binding.datatypes.dateTime, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 612, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offset'), pyxb.binding.datatypes.duration, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 613, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'duration'), pyxb.binding.datatypes.duration, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 614, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'poProgID'), pyxb.binding.datatypes.string, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 615, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'primaryLifestyle'), pyxb.binding.datatypes.string, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 616, 6)))

scheduleEventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'secondaryLifestyle'), pyxb.binding.datatypes.string, scope=scheduleEventType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 617, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 604, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 605, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 606, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 607, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 608, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 609, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 610, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 613, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 615, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 616, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 617, 6))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 604, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 605, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'repeat')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 606, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 607, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 608, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'textSubtitles')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 609, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'textPage')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 610, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'guideDay')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 611, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'start')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 612, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'offset')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 613, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 614, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'poProgID')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 615, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'primaryLifestyle')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 616, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'secondaryLifestyle')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 617, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
scheduleEventType._Automaton = _BuildAutomaton_17()




locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), broadcasterType, scope=locationType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 678, 6)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'programUrl'), pyxb.binding.datatypes.anyURI, scope=locationType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 679, 6)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avAttributes'), avAttributesType, scope=locationType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 680, 6)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subtitles'), pyxb.binding.datatypes.string, scope=locationType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 681, 6)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offset'), pyxb.binding.datatypes.duration, scope=locationType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 682, 6)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'duration'), pyxb.binding.datatypes.duration, scope=locationType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 683, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 678, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 680, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 681, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 682, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 683, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcasters')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 678, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'programUrl')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 679, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 680, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subtitles')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 681, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'offset')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 682, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 683, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
locationType._Automaton = _BuildAutomaton_18()




genreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'term'), termType, scope=genreType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 802, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 802, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(genreType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'term')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 802, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
genreType._Automaton = _BuildAutomaton_19()




programType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), memberRefType, scope=programType, documentation="\n                A program (only if its type is 'BROADCAST') can be an episode of a group of type 'SERIES' or 'SEASON'.\n              ", location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 87, 10)))

programType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'segments'), segmentsType, scope=programType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 94, 10)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 87, 10))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 94, 10))
    counters.add(cc_30)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 201, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 233, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'availableSubtitles')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releaseYear')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'award')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ageRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contentRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'website')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'twitter')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'teletext')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prediction')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'episodeOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 87, 10))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(programType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'segments')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 94, 10))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
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
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, True) ]))
    st_32._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
programType._Automaton = _BuildAutomaton_20()




segmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'start'), pyxb.binding.datatypes.duration, scope=segmentType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 511, 10)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6))
    counters.add(cc_28)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 201, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 233, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'availableSubtitles')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releaseYear')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'award')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ageRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contentRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'website')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'twitter')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'teletext')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prediction')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(segmentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'start')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 511, 10))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
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
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    st_31._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
segmentType._Automaton = _BuildAutomaton_21()




groupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'poSeriesID'), pyxb.binding.datatypes.string, scope=groupType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 709, 10)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 709, 10))
    counters.add(cc_29)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 189, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 201, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 209, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusive')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 217, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 225, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 233, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 244, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 251, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 252, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 253, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 254, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 255, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'availableSubtitles')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 256, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avAttributes')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 257, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releaseYear')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 258, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 259, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 260, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'award')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 261, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 262, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 263, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ageRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 264, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contentRating')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 265, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 266, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'website')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 267, 6))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'twitter')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 268, 6))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'teletext')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 269, 6))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prediction')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 270, 6))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 271, 6))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 272, 6))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 273, 6))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 274, 6))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(groupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'poSeriesID')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproMedia.xsd', 709, 10))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
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
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
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
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, True) ]))
    st_31._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
groupType._Automaton = _BuildAutomaton_22()

