# ./npoapi/xml/page.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:bae47b8c8a50fe304e6e9de618201baa8dfd97c5
# Generated 2016-05-25 16:19:22.676357 by PyXB version 1.2.4 using Python 3.5.0.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ac7d4c80-2283-11e6-88a5-3c075445667b')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import npoapi.xml.shared as _ImportedBinding_npoapi_xml_shared
import pyxb.binding.datatypes
import npoapi.xml.media as _ImportedBinding_npoapi_xml_media

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:pages:2013', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_media = _ImportedBinding_npoapi_xml_media.Namespace
_Namespace_media.configureCategories(['typeBinding', 'elementBinding'])

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
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 50, 2)
    _Documentation = None
pridType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'pridType', pridType)

# Atomic simple type: {urn:vpro:pages:2013}pageTermType
class pageTermType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageTermType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 79, 2)
    _Documentation = None
pageTermType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'pageTermType', pageTermType)

# Atomic simple type: {urn:vpro:pages:2013}linkTypeEnum
class linkTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'linkTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 139, 2)
    _Documentation = None
linkTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=linkTypeEnum, enum_prefix=None)
linkTypeEnum.TOP_STORY = linkTypeEnum._CF_enumeration.addEnumeration(unicode_value='TOP_STORY', tag='TOP_STORY')
linkTypeEnum._InitializeFacetMap(linkTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'linkTypeEnum', linkTypeEnum)

# Atomic simple type: {urn:vpro:pages:2013}pageTypeEnum
class pageTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 145, 2)
    _Documentation = None
pageTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=pageTypeEnum, enum_prefix=None)
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

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 21, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:pages:2013}paragraph uses Python identifier paragraph
    __paragraph = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paragraph'), 'paragraph', '__urnvpropages2013_CTD_ANON_urnvpropages2013paragraph', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 23, 12), )

    
    paragraph = property(__paragraph.value, __paragraph.set, None, None)

    _ElementMap.update({
        __paragraph.name() : __paragraph
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 32, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:pages:2013}image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'image'), 'image', '__urnvpropages2013_CTD_ANON__urnvpropages2013image', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 34, 12), )

    
    image = property(__image.value, __image.set, None, None)

    _ElementMap.update({
        __image.name() : __image
    })
    _AttributeMap.update({
        
    })



# Complex type {urn:vpro:pages:2013}portalType with content type ELEMENT_ONLY
class portalType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}portalType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'portalType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:pages:2013}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvpropages2013_portalType_urnvpropages2013name', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 56, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:pages:2013}section uses Python identifier section
    __section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'section'), 'section', '__urnvpropages2013_portalType_urnvpropages2013section', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 57, 6), )

    
    section = property(__section.value, __section.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__urnvpropages2013_portalType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 59, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 59, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__urnvpropages2013_portalType_url', pyxb.binding.datatypes.string, required=True)
    __url._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 60, 4)
    __url._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 60, 4)
    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __section.name() : __section
    })
    _AttributeMap.update({
        __id.name() : __id,
        __url.name() : __url
    })
Namespace.addCategoryObject('typeBinding', 'portalType', portalType)


# Complex type {urn:vpro:pages:2013}sectionType with content type SIMPLE
class sectionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}sectionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sectionType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 63, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'path'), 'path', '__urnvpropages2013_sectionType_path', pyxb.binding.datatypes.string)
    __path._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 66, 8)
    __path._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 66, 8)
    
    path = property(__path.value, __path.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __path.name() : __path
    })
Namespace.addCategoryObject('typeBinding', 'sectionType', sectionType)


# Complex type {urn:vpro:pages:2013}genreType with content type ELEMENT_ONLY
class genreType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}genreType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genreType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 71, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:pages:2013}term uses Python identifier term
    __term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'term'), 'term', '__urnvpropages2013_genreType_urnvpropages2013term', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 73, 6), )

    
    term = property(__term.value, __term.set, None, None)

    
    # Attribute displayName uses Python identifier displayName
    __displayName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'displayName'), 'displayName', '__urnvpropages2013_genreType_displayName', pyxb.binding.datatypes.string)
    __displayName._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 75, 4)
    __displayName._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 75, 4)
    
    displayName = property(__displayName.value, __displayName.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__urnvpropages2013_genreType_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 76, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 76, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __term.name() : __term
    })
    _AttributeMap.update({
        __displayName.name() : __displayName,
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'genreType', genreType)


# Complex type {urn:vpro:pages:2013}paragraphType with content type ELEMENT_ONLY
class paragraphType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}paragraphType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'paragraphType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 83, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:pages:2013}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpropages2013_paragraphType_urnvpropages2013title', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 85, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:pages:2013}body uses Python identifier body
    __body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'body'), 'body', '__urnvpropages2013_paragraphType_urnvpropages2013body', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 86, 6), )

    
    body = property(__body.value, __body.set, None, None)

    
    # Element {urn:vpro:pages:2013}image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'image'), 'image', '__urnvpropages2013_paragraphType_urnvpropages2013image', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 87, 6), )

    
    image = property(__image.value, __image.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __body.name() : __body,
        __image.name() : __image
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'paragraphType', paragraphType)


# Complex type {urn:vpro:pages:2013}embedType with content type ELEMENT_ONLY
class embedType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}embedType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'embedType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 117, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:pages:2013}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpropages2013_embedType_urnvpropages2013title', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 119, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:pages:2013}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvpropages2013_embedType_urnvpropages2013description', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 120, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:media:2009}program uses Python identifier program
    __program = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_media, 'program'), 'program', '__urnvpropages2013_embedType_urnvpromedia2009program', False, pyxb.utils.utility.Location('http://localhost:8071/schema/vproMedia.xsd', 19, 2), )

    
    program = property(__program.value, __program.set, None, ' Meest gebruikte basiselement uit POMS wordt gebruikt voor indiv\n      ')

    
    # Element {urn:vpro:media:2009}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_media, 'group'), 'group', '__urnvpropages2013_embedType_urnvpromedia2009group', False, pyxb.utils.utility.Location('http://localhost:8071/schema/vproMedia.xsd', 25, 2), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {urn:vpro:media:2009}segment uses Python identifier segment
    __segment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_media, 'segment'), 'segment', '__urnvpropages2013_embedType_urnvpromedia2009segment', False, pyxb.utils.utility.Location('http://localhost:8071/schema/vproMedia.xsd', 26, 2), )

    
    segment = property(__segment.value, __segment.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __program.name() : __program,
        __group.name() : __group,
        __segment.name() : __segment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'embedType', embedType)


# Complex type {urn:vpro:pages:2013}relationType with content type SIMPLE
class relationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}relationType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relationType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 129, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute uriRef uses Python identifier uriRef
    __uriRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uriRef'), 'uriRef', '__urnvpropages2013_relationType_uriRef', pyxb.binding.datatypes.string)
    __uriRef._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 132, 8)
    __uriRef._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 132, 8)
    
    uriRef = property(__uriRef.value, __uriRef.set, None, None)

    
    # Attribute broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'broadcaster'), 'broadcaster', '__urnvpropages2013_relationType_broadcaster', pyxb.binding.datatypes.string, required=True)
    __broadcaster._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 133, 8)
    __broadcaster._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 133, 8)
    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpropages2013_relationType_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 134, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 134, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uriRef.name() : __uriRef,
        __broadcaster.name() : __broadcaster,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'relationType', relationType)


# Complex type {urn:vpro:pages:2013}pageType with content type ELEMENT_ONLY
class pageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}pageType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:pages:2013}genre uses Python identifier genre
    __genre = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genre'), 'genre', '__urnvpropages2013_pageType_urnvpropages2013genre', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 8, 2), )

    
    genre = property(__genre.value, __genre.set, None, None)

    
    # Element {urn:vpro:pages:2013}crid uses Python identifier crid
    __crid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'crid'), 'crid', '__urnvpropages2013_pageType_urnvpropages2013crid', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 12, 6), )

    
    crid = property(__crid.value, __crid.set, None, None)

    
    # Element {urn:vpro:pages:2013}broadcaster uses Python identifier broadcaster
    __broadcaster = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), 'broadcaster', '__urnvpropages2013_pageType_urnvpropages2013broadcaster', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 13, 6), )

    
    broadcaster = property(__broadcaster.value, __broadcaster.set, None, None)

    
    # Element {urn:vpro:pages:2013}portal uses Python identifier portal
    __portal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portal'), 'portal', '__urnvpropages2013_pageType_urnvpropages2013portal', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 14, 6), )

    
    portal = property(__portal.value, __portal.set, None, None)

    
    # Element {urn:vpro:pages:2013}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpropages2013_pageType_urnvpropages2013title', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 15, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:pages:2013}subTitle uses Python identifier subTitle
    __subTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subTitle'), 'subTitle', '__urnvpropages2013_pageType_urnvpropages2013subTitle', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 16, 6), )

    
    subTitle = property(__subTitle.value, __subTitle.set, None, None)

    
    # Element {urn:vpro:pages:2013}keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'keyword'), 'keyword', '__urnvpropages2013_pageType_urnvpropages2013keyword', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 17, 6), )

    
    keyword = property(__keyword.value, __keyword.set, None, None)

    
    # Element {urn:vpro:pages:2013}summary uses Python identifier summary
    __summary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'summary'), 'summary', '__urnvpropages2013_pageType_urnvpropages2013summary', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 19, 6), )

    
    summary = property(__summary.value, __summary.set, None, None)

    
    # Element {urn:vpro:pages:2013}paragraphs uses Python identifier paragraphs
    __paragraphs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paragraphs'), 'paragraphs', '__urnvpropages2013_pageType_urnvpropages2013paragraphs', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 20, 6), )

    
    paragraphs = property(__paragraphs.value, __paragraphs.set, None, None)

    
    # Element {urn:vpro:pages:2013}tag uses Python identifier tag
    __tag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tag'), 'tag', '__urnvpropages2013_pageType_urnvpropages2013tag', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 27, 6), )

    
    tag = property(__tag.value, __tag.set, None, None)

    
    # Element {urn:vpro:pages:2013}referral uses Python identifier referral
    __referral = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'referral'), 'referral', '__urnvpropages2013_pageType_urnvpropages2013referral', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 28, 6), )

    
    referral = property(__referral.value, __referral.set, None, None)

    
    # Element {urn:vpro:pages:2013}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'link'), 'link', '__urnvpropages2013_pageType_urnvpropages2013link', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 29, 6), )

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {urn:vpro:pages:2013}embed uses Python identifier embed
    __embed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'embed'), 'embed', '__urnvpropages2013_pageType_urnvpropages2013embed', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 30, 6), )

    
    embed = property(__embed.value, __embed.set, None, None)

    
    # Element {urn:vpro:pages:2013}images uses Python identifier images
    __images = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'images'), 'images', '__urnvpropages2013_pageType_urnvpropages2013images', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 31, 6), )

    
    images = property(__images.value, __images.set, None, None)

    
    # Element {urn:vpro:pages:2013}relation uses Python identifier relation
    __relation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relation'), 'relation', '__urnvpropages2013_pageType_urnvpropages2013relation', True, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 38, 6), )

    
    relation = property(__relation.value, __relation.set, None, None)

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__urnvpropages2013_pageType_url', pyxb.binding.datatypes.string, required=True)
    __url._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 40, 4)
    __url._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 40, 4)
    
    url = property(__url.value, __url.set, None, None)

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__urnvpropages2013_pageType_creationDate', pyxb.binding.datatypes.dateTime)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 41, 4)
    __creationDate._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 41, 4)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Attribute lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastModified'), 'lastModified', '__urnvpropages2013_pageType_lastModified', pyxb.binding.datatypes.dateTime)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 42, 4)
    __lastModified._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 42, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute lastPublished uses Python identifier lastPublished
    __lastPublished = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastPublished'), 'lastPublished', '__urnvpropages2013_pageType_lastPublished', pyxb.binding.datatypes.dateTime)
    __lastPublished._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 43, 4)
    __lastPublished._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 43, 4)
    
    lastPublished = property(__lastPublished.value, __lastPublished.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvpropages2013_pageType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 44, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 44, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute refCount uses Python identifier refCount
    __refCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'refCount'), 'refCount', '__urnvpropages2013_pageType_refCount', pyxb.binding.datatypes.int)
    __refCount._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 45, 4)
    __refCount._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 45, 4)
    
    refCount = property(__refCount.value, __refCount.set, None, None)

    
    # Attribute sortDate uses Python identifier sortDate
    __sortDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sortDate'), 'sortDate', '__urnvpropages2013_pageType_sortDate', pyxb.binding.datatypes.dateTime)
    __sortDate._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 46, 4)
    __sortDate._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 46, 4)
    
    sortDate = property(__sortDate.value, __sortDate.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpropages2013_pageType_type', pageTypeEnum, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 47, 4)
    __type._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 47, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __genre.name() : __genre,
        __crid.name() : __crid,
        __broadcaster.name() : __broadcaster,
        __portal.name() : __portal,
        __title.name() : __title,
        __subTitle.name() : __subTitle,
        __keyword.name() : __keyword,
        __summary.name() : __summary,
        __paragraphs.name() : __paragraphs,
        __tag.name() : __tag,
        __referral.name() : __referral,
        __link.name() : __link,
        __embed.name() : __embed,
        __images.name() : __images,
        __relation.name() : __relation
    })
    _AttributeMap.update({
        __url.name() : __url,
        __creationDate.name() : __creationDate,
        __lastModified.name() : __lastModified,
        __lastPublished.name() : __lastPublished,
        __publishStart.name() : __publishStart,
        __refCount.name() : __refCount,
        __sortDate.name() : __sortDate,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'pageType', pageType)


# Complex type {urn:vpro:pages:2013}imageType with content type ELEMENT_ONLY
class imageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}imageType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 91, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:pages:2013}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvpropages2013_imageType_urnvpropages2013title', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 93, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:pages:2013}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvpropages2013_imageType_urnvpropages2013description', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 94, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpropages2013_imageType_type', _ImportedBinding_npoapi_xml_shared.imageTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 96, 4)
    __type._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 96, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__urnvpropages2013_imageType_url', pyxb.binding.datatypes.string)
    __url._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 97, 4)
    __url._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 97, 4)
    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description
    })
    _AttributeMap.update({
        __type.name() : __type,
        __url.name() : __url
    })
Namespace.addCategoryObject('typeBinding', 'imageType', imageType)


# Complex type {urn:vpro:pages:2013}referralType with content type SIMPLE
class referralType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}referralType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'referralType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 100, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute referrer uses Python identifier referrer
    __referrer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'referrer'), 'referrer', '__urnvpropages2013_referralType_referrer', pyxb.binding.datatypes.string)
    __referrer._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 103, 8)
    __referrer._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 103, 8)
    
    referrer = property(__referrer.value, __referrer.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpropages2013_referralType_type', linkTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 104, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 104, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __referrer.name() : __referrer,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'referralType', referralType)


# Complex type {urn:vpro:pages:2013}linkType with content type ELEMENT_ONLY
class linkType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:pages:2013}linkType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'linkType')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 109, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:pages:2013}text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'text'), 'text', '__urnvpropages2013_linkType_urnvpropages2013text', False, pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 111, 6), )

    
    text = property(__text.value, __text.set, None, None)

    
    # Attribute pageRef uses Python identifier pageRef
    __pageRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pageRef'), 'pageRef', '__urnvpropages2013_linkType_pageRef', pyxb.binding.datatypes.string)
    __pageRef._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 113, 4)
    __pageRef._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 113, 4)
    
    pageRef = property(__pageRef.value, __pageRef.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvpropages2013_linkType_type', linkTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 114, 4)
    __type._UseLocation = pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 114, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __text.name() : __text
    })
    _AttributeMap.update({
        __pageRef.name() : __pageRef,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'linkType', linkType)


genre = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genre'), genreType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 8, 2))
Namespace.addCategoryObject('elementBinding', genre.name().localName(), genre)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paragraph'), paragraphType, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 23, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 23, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paragraph')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'image'), imageType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 34, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 34, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'image')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 34, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




portalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=portalType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 56, 6)))

portalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'section'), sectionType, scope=portalType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 57, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 57, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(portalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 56, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(portalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'section')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 57, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
portalType._Automaton = _BuildAutomaton_2()




genreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'term'), pageTermType, scope=genreType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 73, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 73, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(genreType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'term')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 73, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
genreType._Automaton = _BuildAutomaton_3()




paragraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), pyxb.binding.datatypes.string, scope=paragraphType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 85, 6)))

paragraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'body'), pyxb.binding.datatypes.string, scope=paragraphType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 86, 6)))

paragraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'image'), imageType, scope=paragraphType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 87, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 85, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 86, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 87, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(paragraphType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 85, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(paragraphType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'body')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 86, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(paragraphType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'image')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 87, 6))
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
paragraphType._Automaton = _BuildAutomaton_4()




embedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), pyxb.binding.datatypes.string, scope=embedType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 119, 6)))

embedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=embedType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 120, 6)))

embedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_media, 'program'), _ImportedBinding_npoapi_xml_media.programType, scope=embedType, documentation=' Meest gebruikte basiselement uit POMS wordt gebruikt voor indiv\n      ', location=pyxb.utils.utility.Location('http://localhost:8071/schema/vproMedia.xsd', 19, 2)))

embedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_media, 'group'), _ImportedBinding_npoapi_xml_media.groupType, scope=embedType, location=pyxb.utils.utility.Location('http://localhost:8071/schema/vproMedia.xsd', 25, 2)))

embedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_media, 'segment'), _ImportedBinding_npoapi_xml_media.segmentType, scope=embedType, location=pyxb.utils.utility.Location('http://localhost:8071/schema/vproMedia.xsd', 26, 2)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 119, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 120, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 121, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(embedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 119, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(embedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 120, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(embedType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'group')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 122, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(embedType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'program')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 123, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(embedType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'segment')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 124, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
embedType._Automaton = _BuildAutomaton_5()




pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genre'), genreType, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 8, 2)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'crid'), pridType, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 12, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcaster'), _ImportedBinding_npoapi_xml_media.broadcasterType, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 13, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portal'), portalType, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 14, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), pyxb.binding.datatypes.string, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 15, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subTitle'), pyxb.binding.datatypes.string, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 16, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'keyword'), pyxb.binding.datatypes.string, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 17, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'summary'), pyxb.binding.datatypes.string, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 19, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paragraphs'), CTD_ANON, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 20, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tag'), pyxb.binding.datatypes.string, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 27, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referral'), referralType, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 28, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'link'), linkType, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 29, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'embed'), embedType, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 30, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'images'), CTD_ANON_, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 31, 6)))

pageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relation'), relationType, scope=pageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 38, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 12, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 14, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 16, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 17, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 18, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 19, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 20, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 27, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 28, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 29, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 30, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 31, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 38, 6))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crid')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 12, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcaster')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 13, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portal')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 14, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 15, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subTitle')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 16, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'keyword')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 17, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 18, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'summary')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 19, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paragraphs')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 20, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tag')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 27, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referral')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 28, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'link')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 29, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'embed')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 30, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 31, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(pageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relation')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 38, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
pageType._Automaton = _BuildAutomaton_6()




imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 93, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 94, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 93, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 94, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 93, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 94, 6))
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
imageType._Automaton = _BuildAutomaton_7()




linkType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'text'), pyxb.binding.datatypes.string, scope=linkType, location=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 111, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 111, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(linkType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'text')), pyxb.utils.utility.Location('http://localhost:8070/v1/schema/urn:vpro:pages:2013', 111, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
linkType._Automaton = _BuildAutomaton_8()

