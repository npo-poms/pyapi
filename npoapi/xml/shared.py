# ./npoapi/xml/shared.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:aa73b2ec19d0d50df44ac76274274e111838473b
# Generated 2018-01-21 15:19:15.769403 by PyXB version 1.2.6 using Python 3.5.2.final.0
# Namespace urn:vpro:shared:2009 [xmlns:shared]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0daa9cda-feb6-11e7-b006-9801a7ae4ad1')

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
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:shared:2009', create_if_missing=True)
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


# Atomic simple type: {urn:vpro:shared:2009}workflowEnumType
class workflowEnumType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workflowEnumType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 24, 2)
    _Documentation = None
workflowEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=workflowEnumType, enum_prefix=None)
workflowEnumType.DRAFT = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='DRAFT', tag='DRAFT')
workflowEnumType.FOR_APPROVAL = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='FOR APPROVAL', tag='FOR_APPROVAL')
workflowEnumType.REFUSED = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='REFUSED', tag='REFUSED')
workflowEnumType.FOR_PUBLICATION = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='FOR PUBLICATION', tag='FOR_PUBLICATION')
workflowEnumType.FOR_REPUBLICATION = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='FOR REPUBLICATION', tag='FOR_REPUBLICATION')
workflowEnumType.PUBLISHED = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='PUBLISHED', tag='PUBLISHED')
workflowEnumType.PARENT_REVOKED = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='PARENT REVOKED', tag='PARENT_REVOKED')
workflowEnumType.REVOKED = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='REVOKED', tag='REVOKED')
workflowEnumType.FOR_DELETION = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='FOR DELETION', tag='FOR_DELETION')
workflowEnumType.DELETED = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='DELETED', tag='DELETED')
workflowEnumType.MERGED = workflowEnumType._CF_enumeration.addEnumeration(unicode_value='MERGED', tag='MERGED')
workflowEnumType._InitializeFacetMap(workflowEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'workflowEnumType', workflowEnumType)
_module_typeBindings.workflowEnumType = workflowEnumType

# Atomic simple type: {urn:vpro:shared:2009}imageTypeEnum
class imageTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 60, 2)
    _Documentation = None
imageTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=imageTypeEnum, enum_prefix=None)
imageTypeEnum.PICTURE = imageTypeEnum._CF_enumeration.addEnumeration(unicode_value='PICTURE', tag='PICTURE')
imageTypeEnum.PORTRAIT = imageTypeEnum._CF_enumeration.addEnumeration(unicode_value='PORTRAIT', tag='PORTRAIT')
imageTypeEnum.STILL = imageTypeEnum._CF_enumeration.addEnumeration(unicode_value='STILL', tag='STILL')
imageTypeEnum.LOGO = imageTypeEnum._CF_enumeration.addEnumeration(unicode_value='LOGO', tag='LOGO')
imageTypeEnum.ICON = imageTypeEnum._CF_enumeration.addEnumeration(unicode_value='ICON', tag='ICON')
imageTypeEnum.PROMO_LANDSCAPE = imageTypeEnum._CF_enumeration.addEnumeration(unicode_value='PROMO_LANDSCAPE', tag='PROMO_LANDSCAPE')
imageTypeEnum.PROMO_PORTRAIT = imageTypeEnum._CF_enumeration.addEnumeration(unicode_value='PROMO_PORTRAIT', tag='PROMO_PORTRAIT')
imageTypeEnum.BACKGROUND = imageTypeEnum._CF_enumeration.addEnumeration(unicode_value='BACKGROUND', tag='BACKGROUND')
imageTypeEnum._InitializeFacetMap(imageTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'imageTypeEnum', imageTypeEnum)
_module_typeBindings.imageTypeEnum = imageTypeEnum

# Atomic simple type: {urn:vpro:shared:2009}ownerTypeEnum
class ownerTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ownerTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 73, 2)
    _Documentation = None
ownerTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ownerTypeEnum, enum_prefix=None)
ownerTypeEnum.BROADCASTER = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='BROADCASTER', tag='BROADCASTER')
ownerTypeEnum.RADIOBOX = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='RADIOBOX', tag='RADIOBOX')
ownerTypeEnum.NEBO = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='NEBO', tag='NEBO')
ownerTypeEnum.NPO = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='NPO', tag='NPO')
ownerTypeEnum.MIS = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='MIS', tag='MIS')
ownerTypeEnum.CERES = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='CERES', tag='CERES')
ownerTypeEnum.PLUTO = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='PLUTO', tag='PLUTO')
ownerTypeEnum.PROJECTM = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='PROJECTM', tag='PROJECTM')
ownerTypeEnum.WHATS_ON = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='WHATS_ON', tag='WHATS_ON')
ownerTypeEnum.IMMIX = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='IMMIX', tag='IMMIX')
ownerTypeEnum.AUTHORITY = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='AUTHORITY', tag='AUTHORITY')
ownerTypeEnum.BEELDENGELUID = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='BEELDENGELUID', tag='BEELDENGELUID')
ownerTypeEnum._InitializeFacetMap(ownerTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ownerTypeEnum', ownerTypeEnum)
_module_typeBindings.ownerTypeEnum = ownerTypeEnum

# Atomic simple type: {urn:vpro:shared:2009}subtitlesTypeEnum
class subtitlesTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subtitlesTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 91, 2)
    _Documentation = None
subtitlesTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=subtitlesTypeEnum, enum_prefix=None)
subtitlesTypeEnum.CAPTION = subtitlesTypeEnum._CF_enumeration.addEnumeration(unicode_value='CAPTION', tag='CAPTION')
subtitlesTypeEnum.TRANSLATION = subtitlesTypeEnum._CF_enumeration.addEnumeration(unicode_value='TRANSLATION', tag='TRANSLATION')
subtitlesTypeEnum.TRANSCRIPT = subtitlesTypeEnum._CF_enumeration.addEnumeration(unicode_value='TRANSCRIPT', tag='TRANSCRIPT')
subtitlesTypeEnum._InitializeFacetMap(subtitlesTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'subtitlesTypeEnum', subtitlesTypeEnum)
_module_typeBindings.subtitlesTypeEnum = subtitlesTypeEnum

# Atomic simple type: {urn:vpro:shared:2009}licenseEnum
class licenseEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'licenseEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 99, 2)
    _Documentation = None
licenseEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=licenseEnum, enum_prefix=None)
licenseEnum.COPYRIGHTED = licenseEnum._CF_enumeration.addEnumeration(unicode_value='COPYRIGHTED', tag='COPYRIGHTED')
licenseEnum.PUBLIC_DOMAIN = licenseEnum._CF_enumeration.addEnumeration(unicode_value='PUBLIC_DOMAIN', tag='PUBLIC_DOMAIN')
licenseEnum.CC_BY = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY', tag='CC_BY')
licenseEnum.CC_BY_1_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_1_0', tag='CC_BY_1_0')
licenseEnum.CC_BY_2_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_2_0', tag='CC_BY_2_0')
licenseEnum.CC_BY_3_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_3_0', tag='CC_BY_3_0')
licenseEnum.CC_BY_4_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_4_0', tag='CC_BY_4_0')
licenseEnum.CC_BY_SA = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_SA', tag='CC_BY_SA')
licenseEnum.CC_BY_SA_1_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_SA_1_0', tag='CC_BY_SA_1_0')
licenseEnum.CC_BY_SA_2_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_SA_2_0', tag='CC_BY_SA_2_0')
licenseEnum.CC_BY_SA_3_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_SA_3_0', tag='CC_BY_SA_3_0')
licenseEnum.CC_BY_SA_4_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_SA_4_0', tag='CC_BY_SA_4_0')
licenseEnum.CC_BY_ND = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_ND', tag='CC_BY_ND')
licenseEnum.CC_BY_ND_1_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_ND_1_0', tag='CC_BY_ND_1_0')
licenseEnum.CC_BY_ND_2_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_ND_2_0', tag='CC_BY_ND_2_0')
licenseEnum.CC_BY_ND_3_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_ND_3_0', tag='CC_BY_ND_3_0')
licenseEnum.CC_BY_ND_4_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_ND_4_0', tag='CC_BY_ND_4_0')
licenseEnum.CC_BY_NC = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC', tag='CC_BY_NC')
licenseEnum.CC_BY_NC_1_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_1_0', tag='CC_BY_NC_1_0')
licenseEnum.CC_BY_NC_2_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_2_0', tag='CC_BY_NC_2_0')
licenseEnum.CC_BY_NC_3_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_3_0', tag='CC_BY_NC_3_0')
licenseEnum.CC_BY_NC_4_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_4_0', tag='CC_BY_NC_4_0')
licenseEnum.CC_BY_NC_SA = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_SA', tag='CC_BY_NC_SA')
licenseEnum.CC_BY_NC_SA_1_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_SA_1_0', tag='CC_BY_NC_SA_1_0')
licenseEnum.CC_BY_NC_SA_2_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_SA_2_0', tag='CC_BY_NC_SA_2_0')
licenseEnum.CC_BY_NC_SA_3_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_SA_3_0', tag='CC_BY_NC_SA_3_0')
licenseEnum.CC_BY_NC_SA_4_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_SA_4_0', tag='CC_BY_NC_SA_4_0')
licenseEnum.CC_BY_NC_ND = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_ND', tag='CC_BY_NC_ND')
licenseEnum.CC_BY_NC_ND_1_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_ND_1_0', tag='CC_BY_NC_ND_1_0')
licenseEnum.CC_BY_NC_ND_2_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_ND_2_0', tag='CC_BY_NC_ND_2_0')
licenseEnum.CC_BY_NC_ND_3_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_ND_3_0', tag='CC_BY_NC_ND_3_0')
licenseEnum.CC_BY_NC_ND_4_0 = licenseEnum._CF_enumeration.addEnumeration(unicode_value='CC_BY_NC_ND_4_0', tag='CC_BY_NC_ND_4_0')
licenseEnum.USA_GOV = licenseEnum._CF_enumeration.addEnumeration(unicode_value='USA_GOV', tag='USA_GOV')
licenseEnum._InitializeFacetMap(licenseEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'licenseEnum', licenseEnum)
_module_typeBindings.licenseEnum = licenseEnum

# Complex type {urn:vpro:shared:2009}publishableObjectType with content type EMPTY
class publishableObjectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:shared:2009}publishableObjectType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'publishableObjectType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 20, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvproshared2009_publishableObjectType_urn', pyxb.binding.datatypes.anyURI)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 10, 4)
    __urn._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 10, 4)
    
    urn = property(__urn.value, __urn.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvproshared2009_publishableObjectType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 11, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 11, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvproshared2009_publishableObjectType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 12, 4)
    __publishStop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 12, 4)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    
    # Attribute publishDate uses Python identifier publishDate
    __publishDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishDate'), 'publishDate', '__urnvproshared2009_publishableObjectType_publishDate', pyxb.binding.datatypes.dateTime)
    __publishDate._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 13, 4)
    __publishDate._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 13, 4)
    
    publishDate = property(__publishDate.value, __publishDate.set, None, None)

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__urnvproshared2009_publishableObjectType_creationDate', pyxb.binding.datatypes.dateTime)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 14, 4)
    __creationDate._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 14, 4)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Attribute lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastModified'), 'lastModified', '__urnvproshared2009_publishableObjectType_lastModified', pyxb.binding.datatypes.dateTime)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 15, 4)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 15, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute workflow uses Python identifier workflow
    __workflow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'workflow'), 'workflow', '__urnvproshared2009_publishableObjectType_workflow', _module_typeBindings.workflowEnumType)
    __workflow._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 16, 4)
    __workflow._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 16, 4)
    
    workflow = property(__workflow.value, __workflow.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __urn.name() : __urn,
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop,
        __publishDate.name() : __publishDate,
        __creationDate.name() : __creationDate,
        __lastModified.name() : __lastModified,
        __workflow.name() : __workflow
    })
_module_typeBindings.publishableObjectType = publishableObjectType
Namespace.addCategoryObject('typeBinding', 'publishableObjectType', publishableObjectType)


# Complex type {urn:vpro:shared:2009}imageType with content type ELEMENT_ONLY
class imageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:shared:2009}imageType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageType')
    _XSDLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 40, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:shared:2009}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvproshared2009_imageType_urnvproshared2009title', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 42, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:shared:2009}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvproshared2009_imageType_urnvproshared2009description', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 43, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:shared:2009}imageUri uses Python identifier imageUri
    __imageUri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'imageUri'), 'imageUri', '__urnvproshared2009_imageType_urnvproshared2009imageUri', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 44, 6), )

    
    imageUri = property(__imageUri.value, __imageUri.set, None, None)

    
    # Element {urn:vpro:shared:2009}offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'offset'), 'offset', '__urnvproshared2009_imageType_urnvproshared2009offset', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 45, 6), )

    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Element {urn:vpro:shared:2009}height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'height'), 'height', '__urnvproshared2009_imageType_urnvproshared2009height', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 46, 6), )

    
    height = property(__height.value, __height.set, None, None)

    
    # Element {urn:vpro:shared:2009}width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'width'), 'width', '__urnvproshared2009_imageType_urnvproshared2009width', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 47, 6), )

    
    width = property(__width.value, __width.set, None, None)

    
    # Element {urn:vpro:shared:2009}credits uses Python identifier credits
    __credits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'credits'), 'credits', '__urnvproshared2009_imageType_urnvproshared2009credits', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 48, 6), )

    
    credits = property(__credits.value, __credits.set, None, None)

    
    # Element {urn:vpro:shared:2009}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__urnvproshared2009_imageType_urnvproshared2009source', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 49, 6), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {urn:vpro:shared:2009}sourceName uses Python identifier sourceName
    __sourceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sourceName'), 'sourceName', '__urnvproshared2009_imageType_urnvproshared2009sourceName', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 50, 6), )

    
    sourceName = property(__sourceName.value, __sourceName.set, None, None)

    
    # Element {urn:vpro:shared:2009}license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'license'), 'license', '__urnvproshared2009_imageType_urnvproshared2009license', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 51, 6), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element {urn:vpro:shared:2009}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'date'), 'date', '__urnvproshared2009_imageType_urnvproshared2009date', False, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 52, 6), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvproshared2009_imageType_urn', pyxb.binding.datatypes.anyURI)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 10, 4)
    __urn._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 10, 4)
    
    urn = property(__urn.value, __urn.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvproshared2009_imageType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 11, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 11, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvproshared2009_imageType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 12, 4)
    __publishStop._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 12, 4)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    
    # Attribute publishDate uses Python identifier publishDate
    __publishDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishDate'), 'publishDate', '__urnvproshared2009_imageType_publishDate', pyxb.binding.datatypes.dateTime)
    __publishDate._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 13, 4)
    __publishDate._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 13, 4)
    
    publishDate = property(__publishDate.value, __publishDate.set, None, None)

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__urnvproshared2009_imageType_creationDate', pyxb.binding.datatypes.dateTime)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 14, 4)
    __creationDate._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 14, 4)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Attribute lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastModified'), 'lastModified', '__urnvproshared2009_imageType_lastModified', pyxb.binding.datatypes.dateTime)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 15, 4)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 15, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute workflow uses Python identifier workflow
    __workflow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'workflow'), 'workflow', '__urnvproshared2009_imageType_workflow', _module_typeBindings.workflowEnumType)
    __workflow._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 16, 4)
    __workflow._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 16, 4)
    
    workflow = property(__workflow.value, __workflow.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvproshared2009_imageType_type', _module_typeBindings.imageTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 54, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 54, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner'), 'owner', '__urnvproshared2009_imageType_owner', _module_typeBindings.ownerTypeEnum, required=True)
    __owner._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 55, 4)
    __owner._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 55, 4)
    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Attribute highlighted uses Python identifier highlighted
    __highlighted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'highlighted'), 'highlighted', '__urnvproshared2009_imageType_highlighted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __highlighted._DeclarationLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 56, 4)
    __highlighted._UseLocation = pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 56, 4)
    
    highlighted = property(__highlighted.value, __highlighted.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __imageUri.name() : __imageUri,
        __offset.name() : __offset,
        __height.name() : __height,
        __width.name() : __width,
        __credits.name() : __credits,
        __source.name() : __source,
        __sourceName.name() : __sourceName,
        __license.name() : __license,
        __date.name() : __date
    })
    _AttributeMap.update({
        __urn.name() : __urn,
        __publishStart.name() : __publishStart,
        __publishStop.name() : __publishStop,
        __publishDate.name() : __publishDate,
        __creationDate.name() : __creationDate,
        __lastModified.name() : __lastModified,
        __workflow.name() : __workflow,
        __type.name() : __type,
        __owner.name() : __owner,
        __highlighted.name() : __highlighted
    })
_module_typeBindings.imageType = imageType
Namespace.addCategoryObject('typeBinding', 'imageType', imageType)


image = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'image'), imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 7, 2))
Namespace.addCategoryObject('elementBinding', image.name().localName(), image)



imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 42, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 43, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'imageUri'), pyxb.binding.datatypes.anyURI, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 44, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offset'), pyxb.binding.datatypes.duration, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 45, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height'), pyxb.binding.datatypes.positiveInteger, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 46, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'width'), pyxb.binding.datatypes.positiveInteger, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 47, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'credits'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 48, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 49, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sourceName'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 50, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'license'), licenseEnum, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 51, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'date'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 52, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 43, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 44, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 45, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 46, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 47, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 48, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 49, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 50, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 51, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 52, 6))
    counters.add(cc_9)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 42, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 43, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'imageUri')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 44, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'offset')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 45, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'height')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 46, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'width')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 47, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 48, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 49, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sourceName')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 50, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'license')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 51, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'date')), pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 52, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
imageType._Automaton = _BuildAutomaton()

