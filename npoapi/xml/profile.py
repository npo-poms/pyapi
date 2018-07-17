# ./npoapi/xml/profile.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:84b11206e77e35c14fdc92e4365d89906a1f1817
# Generated 2018-07-17 13:48:07.106670 by PyXB version 1.2.6 using Python 3.5.2.final.0
# Namespace urn:vpro:api:profile:2013

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4038a9c8-89b7-11e8-87b9-9801a7ae4ad1')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import npoapi.xml.api_constraint_media as _ImportedBinding_npoapi_xml_api_constraint_media
import pyxb.binding.datatypes
import npoapi.xml.api_constraint_page as _ImportedBinding_npoapi_xml_api_constraint_page

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:api:profile:2013', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_media = _ImportedBinding_npoapi_xml_api_constraint_media.Namespace
_Namespace_media.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_page = _ImportedBinding_npoapi_xml_api_constraint_page.Namespace
_Namespace_page.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {urn:vpro:api:profile:2013}profileType with content type ELEMENT_ONLY
class profileType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:profile:2013}profileType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'profileType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 9, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:profile:2013}pageProfile uses Python identifier pageProfile
    __pageProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pageProfile'), 'pageProfile', '__urnvproapiprofile2013_profileType_urnvproapiprofile2013pageProfile', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 11, 6), )

    
    pageProfile = property(__pageProfile.value, __pageProfile.set, None, None)

    
    # Element {urn:vpro:api:profile:2013}mediaProfile uses Python identifier mediaProfile
    __mediaProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediaProfile'), 'mediaProfile', '__urnvproapiprofile2013_profileType_urnvproapiprofile2013mediaProfile', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 12, 6), )

    
    mediaProfile = property(__mediaProfile.value, __mediaProfile.set, None, None)

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__urnvproapiprofile2013_profileType_timestamp', pyxb.binding.datatypes.dateTime)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 14, 4)
    __timestamp._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 14, 4)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__urnvproapiprofile2013_profileType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 15, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 15, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __pageProfile.name() : __pageProfile,
        __mediaProfile.name() : __mediaProfile
    })
    _AttributeMap.update({
        __timestamp.name() : __timestamp,
        __name.name() : __name
    })
_module_typeBindings.profileType = profileType
Namespace.addCategoryObject('typeBinding', 'profileType', profileType)


# Complex type {urn:vpro:api:profile:2013}profileDefinitionType with content type ELEMENT_ONLY
class profileDefinitionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:profile:2013}profileDefinitionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'profileDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:constraint:media:2013}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_media, 'filter'), 'filter', '__urnvproapiprofile2013_profileDefinitionType_urnvproapiconstraintmedia2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 7, 2), )

    
    filter = property(__filter.value, __filter.set, None, None)

    
    # Element {urn:vpro:api:constraint:page:2013}filter uses Python identifier filter_
    __filter_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_page, 'filter'), 'filter_', '__urnvproapiprofile2013_profileDefinitionType_urnvproapiconstraintpage2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:page:2013', 3, 2), )

    
    filter_ = property(__filter_.value, __filter_.set, None, None)

    
    # Attribute since uses Python identifier since
    __since = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'since'), 'since', '__urnvproapiprofile2013_profileDefinitionType_since', pyxb.binding.datatypes.dateTime)
    __since._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 25, 4)
    __since._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 25, 4)
    
    since = property(__since.value, __since.set, None, None)

    _ElementMap.update({
        __filter.name() : __filter,
        __filter_.name() : __filter_
    })
    _AttributeMap.update({
        __since.name() : __since
    })
_module_typeBindings.profileDefinitionType = profileDefinitionType
Namespace.addCategoryObject('typeBinding', 'profileDefinitionType', profileDefinitionType)


profile = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'profile'), profileType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 7, 2))
Namespace.addCategoryObject('elementBinding', profile.name().localName(), profile)



profileType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pageProfile'), profileDefinitionType, scope=profileType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 11, 6)))

profileType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaProfile'), profileDefinitionType, scope=profileType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 12, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 11, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 12, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(profileType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pageProfile')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 11, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(profileType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediaProfile')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 12, 6))
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
profileType._Automaton = _BuildAutomaton()




profileDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_media, 'filter'), _ImportedBinding_npoapi_xml_api_constraint_media.filter_, scope=profileDefinitionType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:media:2013', 7, 2)))

profileDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_page, 'filter'), _ImportedBinding_npoapi_xml_api_constraint_page.filter_, scope=profileDefinitionType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:page:2013', 3, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 20, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(profileDefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 21, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(profileDefinitionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_page, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:profile:2013', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
profileDefinitionType._Automaton = _BuildAutomaton_()

