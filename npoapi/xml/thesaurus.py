# ./npoapi/xml/thesaurus.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ac54f34c9ade42f40dbd05d90aa328ecf2f4878b
# Generated 2018-10-26 21:56:37.893238 by PyXB version 1.2.6 using Python 3.5.2.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:3df7c0e4-d959-11e8-8a82-6a0002581300')

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


# Complex type {urn:vpro:gtaa:2017}gtaaNewPerson with content type ELEMENT_ONLY
class gtaaNewPerson_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:gtaa:2017}gtaaNewPerson with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gtaaNewPerson')
    _XSDLocation = pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:gtaa:2017}familyName uses Python identifier familyName
    __familyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'familyName'), 'familyName', '__urnvprogtaa2017_gtaaNewPerson__urnvprogtaa2017familyName', False, pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 8, 6), )

    
    familyName = property(__familyName.value, __familyName.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}givenName uses Python identifier givenName
    __givenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'givenName'), 'givenName', '__urnvprogtaa2017_gtaaNewPerson__urnvprogtaa2017givenName', False, pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 9, 6), )

    
    givenName = property(__givenName.value, __givenName.set, None, None)

    
    # Element {urn:vpro:gtaa:2017}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'note'), 'note', '__urnvprogtaa2017_gtaaNewPerson__urnvprogtaa2017note', False, pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 10, 6), )

    
    note = property(__note.value, __note.set, None, None)

    _ElementMap.update({
        __familyName.name() : __familyName,
        __givenName.name() : __givenName,
        __note.name() : __note
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.gtaaNewPerson_ = gtaaNewPerson_
Namespace.addCategoryObject('typeBinding', 'gtaaNewPerson', gtaaNewPerson_)


gtaaNewPerson = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gtaaNewPerson'), gtaaNewPerson_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 4, 2))
Namespace.addCategoryObject('elementBinding', gtaaNewPerson.name().localName(), gtaaNewPerson)



gtaaNewPerson_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'familyName'), pyxb.binding.datatypes.string, scope=gtaaNewPerson_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 8, 6)))

gtaaNewPerson_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'givenName'), pyxb.binding.datatypes.string, scope=gtaaNewPerson_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 9, 6)))

gtaaNewPerson_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'note'), pyxb.binding.datatypes.string, scope=gtaaNewPerson_, location=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 10, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 8, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 9, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 10, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gtaaNewPerson_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'familyName')), pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 8, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(gtaaNewPerson_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'givenName')), pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 9, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(gtaaNewPerson_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'note')), pyxb.utils.utility.Location('https://publish-dev.pages.omroep.nl/schema/urn:vpro:gtaa:2017', 10, 6))
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
gtaaNewPerson_._Automaton = _BuildAutomaton()

