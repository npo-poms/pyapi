# ./npoapi/xml/thesaurus.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ac54f34c9ade42f40dbd05d90aa328ecf2f4878b
# Generated 2018-04-30 09:29:51.127386 by PyXB version 1.2.6 using Python 3.5.0.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:404ec5fa-4c48-11e8-9f84-a860b637463b')

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


# Complex type {urn:vpro:gtaa:2017}newPersonRequest with content type ELEMENT_ONLY
class newPersonRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}newPersonRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'newPersonRequest')
    _XSDLocation = pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}jws uses Python identifier jws
    __jws = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'jws'), 'jws', '__urnvprogtaa2017_newPersonRequest__urnvprogtaa2017jws', False, pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 10, 6), )

    
    jws = property(__jws.value, __jws.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__urnvprogtaa2017_newPersonRequest__urnvprogtaa2017person', False, pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 11, 6), )

    
    person = property(__person.value, __person.set, None, None)

    _ElementMap.update({
        __jws.name() : __jws,
        __person.name() : __person
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.newPersonRequest_ = newPersonRequest_
Namespace.addCategoryObject('typeBinding', 'newPersonRequest', newPersonRequest_)


# Complex type {urn:vpro:gtaa:2017}newPerson with content type ELEMENT_ONLY
class newPerson_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}newPerson with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'newPerson')
    _XSDLocation = pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}familyName uses Python identifier familyName
    __familyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'familyName'), 'familyName', '__urnvprogtaa2017_newPerson__urnvprogtaa2017familyName', False, pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 17, 6), )

    
    familyName = property(__familyName.value, __familyName.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}givenName uses Python identifier givenName
    __givenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'givenName'), 'givenName', '__urnvprogtaa2017_newPerson__urnvprogtaa2017givenName', False, pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 18, 6), )

    
    givenName = property(__givenName.value, __givenName.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'note'), 'note', '__urnvprogtaa2017_newPerson__urnvprogtaa2017note', False, pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 19, 6), )

    
    note = property(__note.value, __note.set, None, None)

    _ElementMap.update({
        __familyName.name() : __familyName,
        __givenName.name() : __givenName,
        __note.name() : __note
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.newPerson_ = newPerson_
Namespace.addCategoryObject('typeBinding', 'newPerson', newPerson_)


newPerson = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'newPerson'), newPerson_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 4, 2))
Namespace.addCategoryObject('elementBinding', newPerson.name().localName(), newPerson)

newPersonRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'newPersonRequest'), newPersonRequest_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 6, 2))
Namespace.addCategoryObject('elementBinding', newPersonRequest.name().localName(), newPersonRequest)



newPersonRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'jws'), pyxb.binding.datatypes.string, scope=newPersonRequest_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 10, 6)))

newPersonRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), newPerson_, scope=newPersonRequest_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 11, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 10, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 11, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(newPersonRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'jws')), pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 10, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(newPersonRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 11, 6))
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
newPersonRequest_._Automaton = _BuildAutomaton()




newPerson_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'familyName'), pyxb.binding.datatypes.string, scope=newPerson_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 17, 6)))

newPerson_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'givenName'), pyxb.binding.datatypes.string, scope=newPerson_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 18, 6)))

newPerson_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'note'), pyxb.binding.datatypes.string, scope=newPerson_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 19, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 17, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 18, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 19, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(newPerson_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'familyName')), pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 17, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(newPerson_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'givenName')), pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 18, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(newPerson_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'note')), pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 19, 6))
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
newPerson_._Automaton = _BuildAutomaton_()

