# ./npoapi/xml/api_constraint.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:16fe21f7d82c570c380b0c8dc2a83f6f2249d3d1
# Generated 2021-07-12 12:48:19.442504 by PyXB version 1.2.6 using Python 3.7.2.final.0
# Namespace urn:vpro:api:constraint:2014 [xmlns:constraint]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:aaab0bf2-e2fe-11eb-95b4-a860b637463b')

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
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:api:constraint:2014', create_if_missing=True)
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


# Atomic simple type: {urn:vpro:api:constraint:2014}operatorType
class operatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'operatorType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 61, 2)
    _Documentation = None
operatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=operatorType, enum_prefix=None)
operatorType.LT = operatorType._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
operatorType.GT = operatorType._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
operatorType.EQ = operatorType._CF_enumeration.addEnumeration(unicode_value='EQ', tag='EQ')
operatorType.LTE = operatorType._CF_enumeration.addEnumeration(unicode_value='LTE', tag='LTE')
operatorType.GTE = operatorType._CF_enumeration.addEnumeration(unicode_value='GTE', tag='GTE')
operatorType._InitializeFacetMap(operatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'operatorType', operatorType)
_module_typeBindings.operatorType = operatorType

# Complex type {urn:vpro:api:constraint:2014}booleanPredicateTestResult with content type ELEMENT_ONLY
class booleanPredicateTestResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:2014}booleanPredicateTestResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'booleanPredicateTestResult')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 13, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:constraint:2014}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvproapiconstraint2014_booleanPredicateTestResult_urnvproapiconstraint2014description', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 15, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:api:constraint:2014}clauses uses Python identifier clauses
    __clauses = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'clauses'), 'clauses', '__urnvproapiconstraint2014_booleanPredicateTestResult_urnvproapiconstraint2014clauses', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 16, 6), )

    
    clauses = property(__clauses.value, __clauses.set, None, None)

    
    # Attribute applies uses Python identifier applies
    __applies = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applies'), 'applies', '__urnvproapiconstraint2014_booleanPredicateTestResult_applies', pyxb.binding.datatypes.boolean, required=True)
    __applies._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 24, 4)
    __applies._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 24, 4)
    
    applies = property(__applies.value, __applies.set, None, None)

    
    # Attribute reason uses Python identifier reason
    __reason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reason'), 'reason', '__urnvproapiconstraint2014_booleanPredicateTestResult_reason', pyxb.binding.datatypes.string)
    __reason._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 25, 4)
    __reason._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 25, 4)
    
    reason = property(__reason.value, __reason.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __clauses.name() : __clauses
    })
    _AttributeMap.update({
        __applies.name() : __applies,
        __reason.name() : __reason
    })
_module_typeBindings.booleanPredicateTestResult = booleanPredicateTestResult
Namespace.addCategoryObject('typeBinding', 'booleanPredicateTestResult', booleanPredicateTestResult)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 17, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:constraint:2014}clause uses Python identifier clause
    __clause = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'clause'), 'clause', '__urnvproapiconstraint2014_CTD_ANON_urnvproapiconstraint2014clause', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 19, 12), )

    
    clause = property(__clause.value, __clause.set, None, None)

    _ElementMap.update({
        __clause.name() : __clause
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {urn:vpro:api:constraint:2014}localizedString with content type SIMPLE
class localizedString (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:2014}localizedString with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'localizedString')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__urnvproapiconstraint2014_localizedString_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 31, 8)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.localizedString = localizedString
Namespace.addCategoryObject('typeBinding', 'localizedString', localizedString)


# Complex type {urn:vpro:api:constraint:2014}notPredicateTestResult with content type ELEMENT_ONLY
class notPredicateTestResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:2014}notPredicateTestResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'notPredicateTestResult')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 44, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:constraint:2014}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvproapiconstraint2014_notPredicateTestResult_urnvproapiconstraint2014description', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 46, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:api:constraint:2014}clause uses Python identifier clause
    __clause = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'clause'), 'clause', '__urnvproapiconstraint2014_notPredicateTestResult_urnvproapiconstraint2014clause', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 47, 6), )

    
    clause = property(__clause.value, __clause.set, None, None)

    
    # Attribute applies uses Python identifier applies
    __applies = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applies'), 'applies', '__urnvproapiconstraint2014_notPredicateTestResult_applies', pyxb.binding.datatypes.boolean, required=True)
    __applies._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 49, 4)
    __applies._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 49, 4)
    
    applies = property(__applies.value, __applies.set, None, None)

    
    # Attribute reason uses Python identifier reason
    __reason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reason'), 'reason', '__urnvproapiconstraint2014_notPredicateTestResult_reason', pyxb.binding.datatypes.string)
    __reason._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 50, 4)
    __reason._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 50, 4)
    
    reason = property(__reason.value, __reason.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __clause.name() : __clause
    })
    _AttributeMap.update({
        __applies.name() : __applies,
        __reason.name() : __reason
    })
_module_typeBindings.notPredicateTestResult = notPredicateTestResult
Namespace.addCategoryObject('typeBinding', 'notPredicateTestResult', notPredicateTestResult)


# Complex type {urn:vpro:api:constraint:2014}simplePredicateTestResult with content type ELEMENT_ONLY
class simplePredicateTestResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:constraint:2014}simplePredicateTestResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'simplePredicateTestResult')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 53, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:constraint:2014}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvproapiconstraint2014_simplePredicateTestResult_urnvproapiconstraint2014description', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 55, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute applies uses Python identifier applies
    __applies = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applies'), 'applies', '__urnvproapiconstraint2014_simplePredicateTestResult_applies', pyxb.binding.datatypes.boolean, required=True)
    __applies._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 57, 4)
    __applies._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 57, 4)
    
    applies = property(__applies.value, __applies.set, None, None)

    
    # Attribute reason uses Python identifier reason
    __reason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reason'), 'reason', '__urnvproapiconstraint2014_simplePredicateTestResult_reason', pyxb.binding.datatypes.string)
    __reason._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 58, 4)
    __reason._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 58, 4)
    
    reason = property(__reason.value, __reason.set, None, None)

    _ElementMap.update({
        __description.name() : __description
    })
    _AttributeMap.update({
        __applies.name() : __applies,
        __reason.name() : __reason
    })
_module_typeBindings.simplePredicateTestResult = simplePredicateTestResult
Namespace.addCategoryObject('typeBinding', 'simplePredicateTestResult', simplePredicateTestResult)


# Complex type {urn:vpro:api:constraint:2014}andPredicateTestResult with content type ELEMENT_ONLY
class andPredicateTestResult (booleanPredicateTestResult):
    """Complex type {urn:vpro:api:constraint:2014}andPredicateTestResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'andPredicateTestResult')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 5, 2)
    _ElementMap = booleanPredicateTestResult._ElementMap.copy()
    _AttributeMap = booleanPredicateTestResult._AttributeMap.copy()
    # Base type is booleanPredicateTestResult
    
    # Element description ({urn:vpro:api:constraint:2014}description) inherited from {urn:vpro:api:constraint:2014}booleanPredicateTestResult
    
    # Element clauses ({urn:vpro:api:constraint:2014}clauses) inherited from {urn:vpro:api:constraint:2014}booleanPredicateTestResult
    
    # Attribute applies inherited from {urn:vpro:api:constraint:2014}booleanPredicateTestResult
    
    # Attribute reason inherited from {urn:vpro:api:constraint:2014}booleanPredicateTestResult
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.andPredicateTestResult = andPredicateTestResult
Namespace.addCategoryObject('typeBinding', 'andPredicateTestResult', andPredicateTestResult)


# Complex type {urn:vpro:api:constraint:2014}orPredicateTestResult with content type ELEMENT_ONLY
class orPredicateTestResult (booleanPredicateTestResult):
    """Complex type {urn:vpro:api:constraint:2014}orPredicateTestResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'orPredicateTestResult')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 36, 2)
    _ElementMap = booleanPredicateTestResult._ElementMap.copy()
    _AttributeMap = booleanPredicateTestResult._AttributeMap.copy()
    # Base type is booleanPredicateTestResult
    
    # Element description ({urn:vpro:api:constraint:2014}description) inherited from {urn:vpro:api:constraint:2014}booleanPredicateTestResult
    
    # Element clauses ({urn:vpro:api:constraint:2014}clauses) inherited from {urn:vpro:api:constraint:2014}booleanPredicateTestResult
    
    # Attribute applies inherited from {urn:vpro:api:constraint:2014}booleanPredicateTestResult
    
    # Attribute reason inherited from {urn:vpro:api:constraint:2014}booleanPredicateTestResult
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.orPredicateTestResult = orPredicateTestResult
Namespace.addCategoryObject('typeBinding', 'orPredicateTestResult', orPredicateTestResult)




booleanPredicateTestResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), localizedString, scope=booleanPredicateTestResult, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 15, 6)))

booleanPredicateTestResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'clauses'), CTD_ANON, scope=booleanPredicateTestResult, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 16, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 15, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 16, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(booleanPredicateTestResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 15, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(booleanPredicateTestResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'clauses')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 16, 6))
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
booleanPredicateTestResult._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'clause'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 19, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 19, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'clause')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




notPredicateTestResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), localizedString, scope=notPredicateTestResult, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 46, 6)))

notPredicateTestResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'clause'), pyxb.binding.datatypes.anyType, scope=notPredicateTestResult, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 47, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 46, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 47, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(notPredicateTestResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 46, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(notPredicateTestResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'clause')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 47, 6))
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
notPredicateTestResult._Automaton = _BuildAutomaton_2()




simplePredicateTestResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), localizedString, scope=simplePredicateTestResult, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 55, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 55, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(simplePredicateTestResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 55, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
simplePredicateTestResult._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 15, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 16, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(andPredicateTestResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 15, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(andPredicateTestResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'clauses')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 16, 6))
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
andPredicateTestResult._Automaton = _BuildAutomaton_4()




def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 15, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 16, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(orPredicateTestResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 15, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(orPredicateTestResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'clauses')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:constraint:2014', 16, 6))
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
orPredicateTestResult._Automaton = _BuildAutomaton_5()

