# ./npoapi/xml/poms.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2022-10-21 17:21:06.958022 by PyXB version 1.2.6 using Python 3.9.6.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals

import io
import sys

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import pyxb.utils.domutils
import pyxb.utils.six as _six
import pyxb.utils.utility

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier("urn:uuid:fa5187de-5153-11ed-9cc8-3e22fb45f01a")

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.6"
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(["typeBinding", "elementBinding"])


def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
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


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location("https://poms-test.omroep.nl/schema/absentnamespace.xsd", 12, 6)
    _Documentation = None


STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern="[0-9]+(\\.[0-9]+(\\.[0-9]+)?)?")
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)
_module_typeBindings.STD_ANON = STD_ANON


# Complex type collectionType with content type ELEMENT_ONLY
class collectionType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type collectionType with content type ELEMENT_ONLY"""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "collectionType")
    _XSDLocation = pyxb.utils.utility.Location("https://poms-test.omroep.nl/schema/absentnamespace.xsd", 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "version"),
        "version",
        "__AbsentNamespace0_collectionType_version",
        _module_typeBindings.STD_ANON,
    )
    __version._DeclarationLocation = pyxb.utils.utility.Location(
        "https://poms-test.omroep.nl/schema/absentnamespace.xsd", 11, 4
    )
    __version._UseLocation = pyxb.utils.utility.Location(
        "https://poms-test.omroep.nl/schema/absentnamespace.xsd", 11, 4
    )

    version = property(__version.value, __version.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({})
    _AttributeMap.update({__version.name(): __version})


_module_typeBindings.collectionType = collectionType
Namespace.addCategoryObject("typeBinding", "collectionType", collectionType)


collection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "collection"),
    collectionType,
    location=pyxb.utils.utility.Location("https://poms-test.omroep.nl/schema/absentnamespace.xsd", 5, 2),
)
Namespace.addCategoryObject("elementBinding", collection.name().localName(), collection)


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location("https://poms-test.omroep.nl/schema/absentnamespace.xsd", 9, 6),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(
        pyxb.binding.content.Wildcard(
            process_contents=pyxb.binding.content.Wildcard.PC_lax,
            namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None),
        ),
        pyxb.utils.utility.Location("https://poms-test.omroep.nl/schema/absentnamespace.xsd", 9, 6),
    )
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


collectionType._Automaton = _BuildAutomaton()
