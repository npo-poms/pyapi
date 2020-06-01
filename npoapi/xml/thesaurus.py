# ./npoapi/xml/thesaurus.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ac54f34c9ade42f40dbd05d90aa328ecf2f4878b
# Generated 2020-06-01 22:15:17.907375 by PyXB version 1.2.6 using Python 3.7.2.final.0
# Namespace urn:vpro:gtaa:2017

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:83e765dc-a444-11ea-b7e3-9801a7ae4ad1')

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
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:gtaa:2017', create_if_missing=True)
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


# Atomic simple type: {urn:vpro:gtaa:2017}status
class status (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'status')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 117, 2)
    _Documentation = None
status._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=status, enum_prefix=None)
status.candidate = status._CF_enumeration.addEnumeration(unicode_value='candidate', tag='candidate')
status.approved = status._CF_enumeration.addEnumeration(unicode_value='approved', tag='approved')
status.redirected = status._CF_enumeration.addEnumeration(unicode_value='redirected', tag='redirected')
status.not_compliant = status._CF_enumeration.addEnumeration(unicode_value='not_compliant', tag='not_compliant')
status.rejected = status._CF_enumeration.addEnumeration(unicode_value='rejected', tag='rejected')
status.obsolete = status._CF_enumeration.addEnumeration(unicode_value='obsolete', tag='obsolete')
status.deleted = status._CF_enumeration.addEnumeration(unicode_value='deleted', tag='deleted')
status._InitializeFacetMap(status._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'status', status)
_module_typeBindings.status = status

# Complex type {urn:vpro:gtaa:2017}personType with content type ELEMENT_ONLY
class personType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}personType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'personType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 19, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvprogtaa2017_personType_urnvprogtaa2017name', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 21, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}givenName uses Python identifier givenName
    __givenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'givenName'), 'givenName', '__urnvprogtaa2017_personType_urnvprogtaa2017givenName', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 22, 6), )

    
    givenName = property(__givenName.value, __givenName.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}familyName uses Python identifier familyName
    __familyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'familyName'), 'familyName', '__urnvprogtaa2017_personType_urnvprogtaa2017familyName', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 23, 6), )

    
    familyName = property(__familyName.value, __familyName.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}scopeNote uses Python identifier scopeNote
    __scopeNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), 'scopeNote', '__urnvprogtaa2017_personType_urnvprogtaa2017scopeNote', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 24, 6), )

    
    scopeNote = property(__scopeNote.value, __scopeNote.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}knownAs uses Python identifier knownAs
    __knownAs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'knownAs'), 'knownAs', '__urnvprogtaa2017_personType_urnvprogtaa2017knownAs', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 25, 6), )

    
    knownAs = property(__knownAs.value, __knownAs.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}redirectedFrom uses Python identifier redirectedFrom
    __redirectedFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), 'redirectedFrom', '__urnvprogtaa2017_personType_urnvprogtaa2017redirectedFrom', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 26, 6), )

    
    redirectedFrom = property(__redirectedFrom.value, __redirectedFrom.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__urnvprogtaa2017_personType_urnvprogtaa2017id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 129, 2)
    __id._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 28, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), 'lastModified', '__urnvprogtaa2017_personType_urnvprogtaa2017lastModified', pyxb.binding.datatypes.string)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 131, 2)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 30, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnvprogtaa2017_personType_urnvprogtaa2017status', pyxb.binding.datatypes.string)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 133, 2)
    __status._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 29, 4)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __givenName.name() : __givenName,
        __familyName.name() : __familyName,
        __scopeNote.name() : __scopeNote,
        __knownAs.name() : __knownAs,
        __redirectedFrom.name() : __redirectedFrom
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lastModified.name() : __lastModified,
        __status.name() : __status
    })
_module_typeBindings.personType = personType
Namespace.addCategoryObject('typeBinding', 'personType', personType)


# Complex type {urn:vpro:gtaa:2017}names with content type ELEMENT_ONLY
class names (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}names with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'names')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}familyName uses Python identifier familyName
    __familyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'familyName'), 'familyName', '__urnvprogtaa2017_names_urnvprogtaa2017familyName', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 35, 6), )

    
    familyName = property(__familyName.value, __familyName.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}givenName uses Python identifier givenName
    __givenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'givenName'), 'givenName', '__urnvprogtaa2017_names_urnvprogtaa2017givenName', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 36, 6), )

    
    givenName = property(__givenName.value, __givenName.set, None, None)

    _ElementMap.update({
        __familyName.name() : __familyName,
        __givenName.name() : __givenName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.names = names
Namespace.addCategoryObject('typeBinding', 'names', names)


# Complex type {urn:vpro:gtaa:2017}geographicNameType with content type ELEMENT_ONLY
class geographicNameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}geographicNameType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geographicNameType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 40, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvprogtaa2017_geographicNameType_urnvprogtaa2017name', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 42, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}scopeNote uses Python identifier scopeNote
    __scopeNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), 'scopeNote', '__urnvprogtaa2017_geographicNameType_urnvprogtaa2017scopeNote', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 43, 6), )

    
    scopeNote = property(__scopeNote.value, __scopeNote.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}redirectedFrom uses Python identifier redirectedFrom
    __redirectedFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), 'redirectedFrom', '__urnvprogtaa2017_geographicNameType_urnvprogtaa2017redirectedFrom', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 44, 6), )

    
    redirectedFrom = property(__redirectedFrom.value, __redirectedFrom.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__urnvprogtaa2017_geographicNameType_urnvprogtaa2017id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 129, 2)
    __id._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 46, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), 'lastModified', '__urnvprogtaa2017_geographicNameType_urnvprogtaa2017lastModified', pyxb.binding.datatypes.string)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 131, 2)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 48, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnvprogtaa2017_geographicNameType_urnvprogtaa2017status', pyxb.binding.datatypes.string)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 133, 2)
    __status._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 47, 4)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __scopeNote.name() : __scopeNote,
        __redirectedFrom.name() : __redirectedFrom
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lastModified.name() : __lastModified,
        __status.name() : __status
    })
_module_typeBindings.geographicNameType = geographicNameType
Namespace.addCategoryObject('typeBinding', 'geographicNameType', geographicNameType)


# Complex type {urn:vpro:gtaa:2017}topicType with content type ELEMENT_ONLY
class topicType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}topicType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'topicType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 51, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvprogtaa2017_topicType_urnvprogtaa2017name', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 53, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}scopeNote uses Python identifier scopeNote
    __scopeNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), 'scopeNote', '__urnvprogtaa2017_topicType_urnvprogtaa2017scopeNote', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 54, 6), )

    
    scopeNote = property(__scopeNote.value, __scopeNote.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}redirectedFrom uses Python identifier redirectedFrom
    __redirectedFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), 'redirectedFrom', '__urnvprogtaa2017_topicType_urnvprogtaa2017redirectedFrom', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 55, 6), )

    
    redirectedFrom = property(__redirectedFrom.value, __redirectedFrom.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__urnvprogtaa2017_topicType_urnvprogtaa2017id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 129, 2)
    __id._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 57, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), 'lastModified', '__urnvprogtaa2017_topicType_urnvprogtaa2017lastModified', pyxb.binding.datatypes.string)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 131, 2)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 59, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnvprogtaa2017_topicType_urnvprogtaa2017status', pyxb.binding.datatypes.string)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 133, 2)
    __status._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 58, 4)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __scopeNote.name() : __scopeNote,
        __redirectedFrom.name() : __redirectedFrom
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lastModified.name() : __lastModified,
        __status.name() : __status
    })
_module_typeBindings.topicType = topicType
Namespace.addCategoryObject('typeBinding', 'topicType', topicType)


# Complex type {urn:vpro:gtaa:2017}topicbandgType with content type ELEMENT_ONLY
class topicbandgType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}topicbandgType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'topicbandgType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 62, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvprogtaa2017_topicbandgType_urnvprogtaa2017name', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 64, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}scopeNote uses Python identifier scopeNote
    __scopeNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), 'scopeNote', '__urnvprogtaa2017_topicbandgType_urnvprogtaa2017scopeNote', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 65, 6), )

    
    scopeNote = property(__scopeNote.value, __scopeNote.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}redirectedFrom uses Python identifier redirectedFrom
    __redirectedFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), 'redirectedFrom', '__urnvprogtaa2017_topicbandgType_urnvprogtaa2017redirectedFrom', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 66, 6), )

    
    redirectedFrom = property(__redirectedFrom.value, __redirectedFrom.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__urnvprogtaa2017_topicbandgType_urnvprogtaa2017id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 129, 2)
    __id._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 68, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), 'lastModified', '__urnvprogtaa2017_topicbandgType_urnvprogtaa2017lastModified', pyxb.binding.datatypes.string)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 131, 2)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 70, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnvprogtaa2017_topicbandgType_urnvprogtaa2017status', pyxb.binding.datatypes.string)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 133, 2)
    __status._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 69, 4)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __scopeNote.name() : __scopeNote,
        __redirectedFrom.name() : __redirectedFrom
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lastModified.name() : __lastModified,
        __status.name() : __status
    })
_module_typeBindings.topicbandgType = topicbandgType
Namespace.addCategoryObject('typeBinding', 'topicbandgType', topicbandgType)


# Complex type {urn:vpro:gtaa:2017}classificationType with content type ELEMENT_ONLY
class classificationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}classificationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'classificationType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 73, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvprogtaa2017_classificationType_urnvprogtaa2017name', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 75, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}scopeNote uses Python identifier scopeNote
    __scopeNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), 'scopeNote', '__urnvprogtaa2017_classificationType_urnvprogtaa2017scopeNote', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 76, 6), )

    
    scopeNote = property(__scopeNote.value, __scopeNote.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}redirectedFrom uses Python identifier redirectedFrom
    __redirectedFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), 'redirectedFrom', '__urnvprogtaa2017_classificationType_urnvprogtaa2017redirectedFrom', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 77, 6), )

    
    redirectedFrom = property(__redirectedFrom.value, __redirectedFrom.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__urnvprogtaa2017_classificationType_urnvprogtaa2017id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 129, 2)
    __id._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 79, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), 'lastModified', '__urnvprogtaa2017_classificationType_urnvprogtaa2017lastModified', pyxb.binding.datatypes.string)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 131, 2)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 81, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnvprogtaa2017_classificationType_urnvprogtaa2017status', pyxb.binding.datatypes.string)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 133, 2)
    __status._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 80, 4)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __scopeNote.name() : __scopeNote,
        __redirectedFrom.name() : __redirectedFrom
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lastModified.name() : __lastModified,
        __status.name() : __status
    })
_module_typeBindings.classificationType = classificationType
Namespace.addCategoryObject('typeBinding', 'classificationType', classificationType)


# Complex type {urn:vpro:gtaa:2017}makerType with content type ELEMENT_ONLY
class makerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}makerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'makerType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 84, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvprogtaa2017_makerType_urnvprogtaa2017name', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 86, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}scopeNote uses Python identifier scopeNote
    __scopeNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), 'scopeNote', '__urnvprogtaa2017_makerType_urnvprogtaa2017scopeNote', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 87, 6), )

    
    scopeNote = property(__scopeNote.value, __scopeNote.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}redirectedFrom uses Python identifier redirectedFrom
    __redirectedFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), 'redirectedFrom', '__urnvprogtaa2017_makerType_urnvprogtaa2017redirectedFrom', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 88, 6), )

    
    redirectedFrom = property(__redirectedFrom.value, __redirectedFrom.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__urnvprogtaa2017_makerType_urnvprogtaa2017id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 129, 2)
    __id._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 90, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), 'lastModified', '__urnvprogtaa2017_makerType_urnvprogtaa2017lastModified', pyxb.binding.datatypes.string)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 131, 2)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 92, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnvprogtaa2017_makerType_urnvprogtaa2017status', pyxb.binding.datatypes.string)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 133, 2)
    __status._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 91, 4)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __scopeNote.name() : __scopeNote,
        __redirectedFrom.name() : __redirectedFrom
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lastModified.name() : __lastModified,
        __status.name() : __status
    })
_module_typeBindings.makerType = makerType
Namespace.addCategoryObject('typeBinding', 'makerType', makerType)


# Complex type {urn:vpro:gtaa:2017}genreType with content type ELEMENT_ONLY
class genreType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}genreType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genreType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 95, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvprogtaa2017_genreType_urnvprogtaa2017name', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 97, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}scopeNote uses Python identifier scopeNote
    __scopeNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), 'scopeNote', '__urnvprogtaa2017_genreType_urnvprogtaa2017scopeNote', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 98, 6), )

    
    scopeNote = property(__scopeNote.value, __scopeNote.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}redirectedFrom uses Python identifier redirectedFrom
    __redirectedFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), 'redirectedFrom', '__urnvprogtaa2017_genreType_urnvprogtaa2017redirectedFrom', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 99, 6), )

    
    redirectedFrom = property(__redirectedFrom.value, __redirectedFrom.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__urnvprogtaa2017_genreType_urnvprogtaa2017id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 129, 2)
    __id._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 101, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), 'lastModified', '__urnvprogtaa2017_genreType_urnvprogtaa2017lastModified', pyxb.binding.datatypes.string)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 131, 2)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 103, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnvprogtaa2017_genreType_urnvprogtaa2017status', pyxb.binding.datatypes.string)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 133, 2)
    __status._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 102, 4)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __scopeNote.name() : __scopeNote,
        __redirectedFrom.name() : __redirectedFrom
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lastModified.name() : __lastModified,
        __status.name() : __status
    })
_module_typeBindings.genreType = genreType
Namespace.addCategoryObject('typeBinding', 'genreType', genreType)


# Complex type {urn:vpro:gtaa:2017}nameType with content type ELEMENT_ONLY
class nameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}nameType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 106, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvprogtaa2017_nameType_urnvprogtaa2017name', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 108, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}scopeNote uses Python identifier scopeNote
    __scopeNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), 'scopeNote', '__urnvprogtaa2017_nameType_urnvprogtaa2017scopeNote', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 109, 6), )

    
    scopeNote = property(__scopeNote.value, __scopeNote.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}redirectedFrom uses Python identifier redirectedFrom
    __redirectedFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), 'redirectedFrom', '__urnvprogtaa2017_nameType_urnvprogtaa2017redirectedFrom', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 110, 6), )

    
    redirectedFrom = property(__redirectedFrom.value, __redirectedFrom.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__urnvprogtaa2017_nameType_urnvprogtaa2017id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 129, 2)
    __id._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 112, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'lastModified'), 'lastModified', '__urnvprogtaa2017_nameType_urnvprogtaa2017lastModified', pyxb.binding.datatypes.string)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 131, 2)
    __lastModified._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 114, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute {urn:vpro:gtaa:2017}status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnvprogtaa2017_nameType_urnvprogtaa2017status', pyxb.binding.datatypes.string)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 133, 2)
    __status._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 113, 4)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __scopeNote.name() : __scopeNote,
        __redirectedFrom.name() : __redirectedFrom
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lastModified.name() : __lastModified,
        __status.name() : __status
    })
_module_typeBindings.nameType = nameType
Namespace.addCategoryObject('typeBinding', 'nameType', nameType)


classification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'classification'), classificationType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 3, 2))
Namespace.addCategoryObject('elementBinding', classification.name().localName(), classification)

genre = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genre'), genreType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 5, 2))
Namespace.addCategoryObject('elementBinding', genre.name().localName(), genre)

geographicName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geographicName'), geographicNameType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 7, 2))
Namespace.addCategoryObject('elementBinding', geographicName.name().localName(), geographicName)

maker = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maker'), makerType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 9, 2))
Namespace.addCategoryObject('elementBinding', maker.name().localName(), maker)

name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), nameType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 11, 2))
Namespace.addCategoryObject('elementBinding', name.name().localName(), name)

person = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), personType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 13, 2))
Namespace.addCategoryObject('elementBinding', person.name().localName(), person)

topic = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'topic'), topicType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 15, 2))
Namespace.addCategoryObject('elementBinding', topic.name().localName(), topic)

topicbandg = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'topicbandg'), topicbandgType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 17, 2))
Namespace.addCategoryObject('elementBinding', topicbandg.name().localName(), topicbandg)



personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=personType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 21, 6)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'givenName'), pyxb.binding.datatypes.string, scope=personType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 22, 6)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'familyName'), pyxb.binding.datatypes.string, scope=personType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 23, 6)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), pyxb.binding.datatypes.string, scope=personType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 24, 6)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'knownAs'), names, scope=personType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 25, 6)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), pyxb.binding.datatypes.string, scope=personType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 26, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 21, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 22, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 23, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 24, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 25, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 26, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 21, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'givenName')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 22, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'familyName')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 23, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scopeNote')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 24, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'knownAs')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 25, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 26, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
personType._Automaton = _BuildAutomaton()




names._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'familyName'), pyxb.binding.datatypes.string, scope=names, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 35, 6)))

names._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'givenName'), pyxb.binding.datatypes.string, scope=names, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 36, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 35, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 36, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(names._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'familyName')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(names._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'givenName')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 36, 6))
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
names._Automaton = _BuildAutomaton_()




geographicNameType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=geographicNameType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 42, 6)))

geographicNameType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), pyxb.binding.datatypes.string, scope=geographicNameType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 43, 6)))

geographicNameType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), pyxb.binding.datatypes.string, scope=geographicNameType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 44, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 42, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 43, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 44, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(geographicNameType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 42, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(geographicNameType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scopeNote')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 43, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(geographicNameType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 44, 6))
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
geographicNameType._Automaton = _BuildAutomaton_2()




topicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=topicType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 53, 6)))

topicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), pyxb.binding.datatypes.string, scope=topicType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 54, 6)))

topicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), pyxb.binding.datatypes.string, scope=topicType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 55, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 53, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 54, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 55, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(topicType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 53, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(topicType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scopeNote')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 54, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(topicType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 55, 6))
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
topicType._Automaton = _BuildAutomaton_3()




topicbandgType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=topicbandgType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 64, 6)))

topicbandgType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), pyxb.binding.datatypes.string, scope=topicbandgType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 65, 6)))

topicbandgType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), pyxb.binding.datatypes.string, scope=topicbandgType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 66, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 64, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 65, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 66, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(topicbandgType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 64, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(topicbandgType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scopeNote')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 65, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(topicbandgType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 66, 6))
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
topicbandgType._Automaton = _BuildAutomaton_4()




classificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=classificationType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 75, 6)))

classificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), pyxb.binding.datatypes.string, scope=classificationType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 76, 6)))

classificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), pyxb.binding.datatypes.string, scope=classificationType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 77, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 75, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 76, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 77, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(classificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 75, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(classificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scopeNote')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 76, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(classificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 77, 6))
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
classificationType._Automaton = _BuildAutomaton_5()




makerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=makerType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 86, 6)))

makerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), pyxb.binding.datatypes.string, scope=makerType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 87, 6)))

makerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), pyxb.binding.datatypes.string, scope=makerType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 88, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 86, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 87, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 88, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(makerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 86, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(makerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scopeNote')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 87, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(makerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 88, 6))
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
makerType._Automaton = _BuildAutomaton_6()




genreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=genreType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 97, 6)))

genreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), pyxb.binding.datatypes.string, scope=genreType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 98, 6)))

genreType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), pyxb.binding.datatypes.string, scope=genreType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 99, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 97, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 98, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 99, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(genreType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(genreType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scopeNote')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 98, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(genreType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 99, 6))
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
genreType._Automaton = _BuildAutomaton_7()




nameType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=nameType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 108, 6)))

nameType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scopeNote'), pyxb.binding.datatypes.string, scope=nameType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 109, 6)))

nameType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom'), pyxb.binding.datatypes.string, scope=nameType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 110, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 108, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 109, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 110, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(nameType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 108, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(nameType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scopeNote')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 109, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(nameType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'redirectedFrom')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:gtaa:2017', 110, 6))
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
nameType._Automaton = _BuildAutomaton_8()

