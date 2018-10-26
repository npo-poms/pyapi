# ./npoapi/xml/secondscreen.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:fe46ea2052bee47af12417922dca9d6562e4d308
# Generated 2018-10-26 15:05:03.367825 by PyXB version 1.2.6 using Python 3.5.2.final.0
# Namespace urn:vpro:secondscreen:2015

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:bd5bfb38-d91f-11e8-90fe-6a0002581300')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import npoapi.xml.media as _ImportedBinding_npoapi_xml_media
import pyxb.binding.datatypes
import npoapi.xml.shared as _ImportedBinding_npoapi_xml_shared

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:secondscreen:2015', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 18, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:shared:2009}image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_shared, 'image'), 'image', '__urnvprosecondscreen2015_CTD_ANON_urnvproshared2009image', True, pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 7, 2), )

    
    image = property(__image.value, __image.set, None, None)

    _ElementMap.update({
        __image.name() : __image
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {urn:vpro:secondscreen:2015}mediaRefType with content type EMPTY
class mediaRefType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:secondscreen:2015}mediaRefType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaRefType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 30, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute midRef uses Python identifier midRef
    __midRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'midRef'), 'midRef', '__urnvprosecondscreen2015_mediaRefType_midRef', pyxb.binding.datatypes.string)
    __midRef._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 32, 4)
    __midRef._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 32, 4)
    
    midRef = property(__midRef.value, __midRef.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvprosecondscreen2015_mediaRefType_type', _ImportedBinding_npoapi_xml_media.mediaTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 33, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 33, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __midRef.name() : __midRef,
        __type.name() : __type
    })
_module_typeBindings.mediaRefType = mediaRefType
Namespace.addCategoryObject('typeBinding', 'mediaRefType', mediaRefType)


# Complex type {urn:vpro:secondscreen:2015}screenType with content type ELEMENT_ONLY
class screenType (_ImportedBinding_npoapi_xml_shared.publishableObjectType):
    """Complex type {urn:vpro:secondscreen:2015}screenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'screenType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 9, 2)
    _ElementMap = _ImportedBinding_npoapi_xml_shared.publishableObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_npoapi_xml_shared.publishableObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_npoapi_xml_shared.publishableObjectType
    
    # Element {urn:vpro:secondscreen:2015}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvprosecondscreen2015_screenType_urnvprosecondscreen2015title', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 13, 10), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:secondscreen:2015}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvprosecondscreen2015_screenType_urnvprosecondscreen2015description', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 14, 10), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:secondscreen:2015}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'url'), 'url', '__urnvprosecondscreen2015_screenType_urnvprosecondscreen2015url', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 15, 10), )

    
    url = property(__url.value, __url.set, None, None)

    
    # Element {urn:vpro:secondscreen:2015}screenOf uses Python identifier screenOf
    __screenOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'screenOf'), 'screenOf', '__urnvprosecondscreen2015_screenType_urnvprosecondscreen2015screenOf', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 16, 10), )

    
    screenOf = property(__screenOf.value, __screenOf.set, None, None)

    
    # Element {urn:vpro:secondscreen:2015}images uses Python identifier images
    __images = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'images'), 'images', '__urnvprosecondscreen2015_screenType_urnvprosecondscreen2015images', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 17, 10), )

    
    images = property(__images.value, __images.set, None, None)

    
    # Attribute sid uses Python identifier sid
    __sid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sid'), 'sid', '__urnvprosecondscreen2015_screenType_sid', pyxb.binding.datatypes.string)
    __sid._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 25, 8)
    __sid._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 25, 8)
    
    sid = property(__sid.value, __sid.set, None, None)

    
    # Attribute urn inherited from {urn:vpro:shared:2009}publishableObjectType
    
    # Attribute publishStart inherited from {urn:vpro:shared:2009}publishableObjectType
    
    # Attribute publishStop inherited from {urn:vpro:shared:2009}publishableObjectType
    
    # Attribute publishDate inherited from {urn:vpro:shared:2009}publishableObjectType
    
    # Attribute creationDate inherited from {urn:vpro:shared:2009}publishableObjectType
    
    # Attribute lastModified inherited from {urn:vpro:shared:2009}publishableObjectType
    
    # Attribute workflow inherited from {urn:vpro:shared:2009}publishableObjectType
    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __url.name() : __url,
        __screenOf.name() : __screenOf,
        __images.name() : __images
    })
    _AttributeMap.update({
        __sid.name() : __sid
    })
_module_typeBindings.screenType = screenType
Namespace.addCategoryObject('typeBinding', 'screenType', screenType)


screen = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'screen'), screenType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 7, 2))
Namespace.addCategoryObject('elementBinding', screen.name().localName(), screen)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_shared, 'image'), _ImportedBinding_npoapi_xml_shared.imageType, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://poms-dev.omroep.nl/schema/vproShared.xsd', 7, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 20, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_shared, 'image')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 20, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




screenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), pyxb.binding.datatypes.string, scope=screenType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 13, 10)))

screenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=screenType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 14, 10)))

screenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'url'), pyxb.binding.datatypes.anyURI, scope=screenType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 15, 10)))

screenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'screenOf'), mediaRefType, scope=screenType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 16, 10)))

screenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'images'), CTD_ANON, scope=screenType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 17, 10)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 13, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 14, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 15, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 16, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 17, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(screenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 13, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(screenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 14, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(screenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'url')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 15, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(screenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'screenOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 16, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(screenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'images')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:secondscreen:2015', 17, 10))
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
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
screenType._Automaton = _BuildAutomaton_()

