# ./npoapi/xml/shared.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:aa73b2ec19d0d50df44ac76274274e111838473b
# Generated 2016-05-11 21:43:21.088954 by PyXB version 1.2.4 using Python 3.5.0.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9a8a2b34-17b0-11e6-92db-60fb42f0af34')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

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
    _XSDLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 17, 2)
    _Documentation = None
workflowEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=workflowEnumType)
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

# Atomic simple type: {urn:vpro:shared:2009}imageTypeEnum
class imageTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 52, 2)
    _Documentation = None
imageTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=imageTypeEnum)
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

# Atomic simple type: {urn:vpro:shared:2009}ownerTypeEnum
class ownerTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ownerTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 65, 2)
    _Documentation = None
ownerTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=ownerTypeEnum)
ownerTypeEnum.BROADCASTER = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='BROADCASTER', tag='BROADCASTER')
ownerTypeEnum.RADIOBOX = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='RADIOBOX', tag='RADIOBOX')
ownerTypeEnum.NEBO = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='NEBO', tag='NEBO')
ownerTypeEnum.MIS = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='MIS', tag='MIS')
ownerTypeEnum.CERES = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='CERES', tag='CERES')
ownerTypeEnum.PLUTO = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='PLUTO', tag='PLUTO')
ownerTypeEnum.PROJECTM = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='PROJECTM', tag='PROJECTM')
ownerTypeEnum.WHATS_ON = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='WHATS_ON', tag='WHATS_ON')
ownerTypeEnum.IMMIX = ownerTypeEnum._CF_enumeration.addEnumeration(unicode_value='IMMIX', tag='IMMIX')
ownerTypeEnum._InitializeFacetMap(ownerTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ownerTypeEnum', ownerTypeEnum)

# Atomic simple type: {urn:vpro:shared:2009}countriesEnum
class countriesEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'countriesEnum')
    _XSDLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 79, 2)
    _Documentation = None
countriesEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=countriesEnum)
countriesEnum.AD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AD', tag='AD')
countriesEnum.AE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AE', tag='AE')
countriesEnum.AF = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AF', tag='AF')
countriesEnum.AG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AG', tag='AG')
countriesEnum.AI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AI', tag='AI')
countriesEnum.AL = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
countriesEnum.AM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AM', tag='AM')
countriesEnum.AN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AN', tag='AN')
countriesEnum.AO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AO', tag='AO')
countriesEnum.AQ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AQ', tag='AQ')
countriesEnum.AR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AR', tag='AR')
countriesEnum.AS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AS', tag='AS')
countriesEnum.AT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AT', tag='AT')
countriesEnum.AU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AU', tag='AU')
countriesEnum.AW = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AW', tag='AW')
countriesEnum.AX = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AX', tag='AX')
countriesEnum.AZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AZ', tag='AZ')
countriesEnum.BA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BA', tag='BA')
countriesEnum.BB = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BB', tag='BB')
countriesEnum.BD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BD', tag='BD')
countriesEnum.BE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BE', tag='BE')
countriesEnum.BF = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BF', tag='BF')
countriesEnum.BG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BG', tag='BG')
countriesEnum.BH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BH', tag='BH')
countriesEnum.BI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BI', tag='BI')
countriesEnum.BJ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BJ', tag='BJ')
countriesEnum.BL = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BL', tag='BL')
countriesEnum.BM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BM', tag='BM')
countriesEnum.BN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BN', tag='BN')
countriesEnum.BO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BO', tag='BO')
countriesEnum.BR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BR', tag='BR')
countriesEnum.BS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BS', tag='BS')
countriesEnum.BT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BT', tag='BT')
countriesEnum.BV = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BV', tag='BV')
countriesEnum.BW = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BW', tag='BW')
countriesEnum.BY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BY', tag='BY')
countriesEnum.BZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BZ', tag='BZ')
countriesEnum.CA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CA', tag='CA')
countriesEnum.CC = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
countriesEnum.CD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CD', tag='CD')
countriesEnum.CF = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CF', tag='CF')
countriesEnum.CG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CG', tag='CG')
countriesEnum.CH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CH', tag='CH')
countriesEnum.CI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CI', tag='CI')
countriesEnum.CK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CK', tag='CK')
countriesEnum.CL = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CL', tag='CL')
countriesEnum.CM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CM', tag='CM')
countriesEnum.CN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CN', tag='CN')
countriesEnum.CO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CO', tag='CO')
countriesEnum.CR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CR', tag='CR')
countriesEnum.CU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CU', tag='CU')
countriesEnum.CV = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
countriesEnum.CX = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CX', tag='CX')
countriesEnum.CY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CY', tag='CY')
countriesEnum.CZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CZ', tag='CZ')
countriesEnum.DE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
countriesEnum.DJ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='DJ', tag='DJ')
countriesEnum.DK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='DK', tag='DK')
countriesEnum.DM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='DM', tag='DM')
countriesEnum.DO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='DO', tag='DO')
countriesEnum.DZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='DZ', tag='DZ')
countriesEnum.EC = countriesEnum._CF_enumeration.addEnumeration(unicode_value='EC', tag='EC')
countriesEnum.EE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='EE', tag='EE')
countriesEnum.EG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='EG', tag='EG')
countriesEnum.EH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='EH', tag='EH')
countriesEnum.ER = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
countriesEnum.ES = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ES', tag='ES')
countriesEnum.ET = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ET', tag='ET')
countriesEnum.FI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='FI', tag='FI')
countriesEnum.FJ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='FJ', tag='FJ')
countriesEnum.FK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='FK', tag='FK')
countriesEnum.FM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='FM', tag='FM')
countriesEnum.FO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='FO', tag='FO')
countriesEnum.FR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='FR', tag='FR')
countriesEnum.GA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GA', tag='GA')
countriesEnum.GB = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GB', tag='GB')
countriesEnum.GD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GD', tag='GD')
countriesEnum.GE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GE', tag='GE')
countriesEnum.GF = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GF', tag='GF')
countriesEnum.GG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GG', tag='GG')
countriesEnum.GH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GH', tag='GH')
countriesEnum.GI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GI', tag='GI')
countriesEnum.GL = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GL', tag='GL')
countriesEnum.GM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GM', tag='GM')
countriesEnum.GN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GN', tag='GN')
countriesEnum.GP = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GP', tag='GP')
countriesEnum.GQ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GQ', tag='GQ')
countriesEnum.GR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GR', tag='GR')
countriesEnum.GS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GS', tag='GS')
countriesEnum.GT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
countriesEnum.GU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GU', tag='GU')
countriesEnum.GW = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
countriesEnum.GY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GY', tag='GY')
countriesEnum.HK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='HK', tag='HK')
countriesEnum.HM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='HM', tag='HM')
countriesEnum.HN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='HN', tag='HN')
countriesEnum.HR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='HR', tag='HR')
countriesEnum.HT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='HT', tag='HT')
countriesEnum.HU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='HU', tag='HU')
countriesEnum.ID = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ID', tag='ID')
countriesEnum.IE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='IE', tag='IE')
countriesEnum.IL = countriesEnum._CF_enumeration.addEnumeration(unicode_value='IL', tag='IL')
countriesEnum.IM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='IM', tag='IM')
countriesEnum.IN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='IN', tag='IN')
countriesEnum.IO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='IO', tag='IO')
countriesEnum.IQ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='IQ', tag='IQ')
countriesEnum.IR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='IR', tag='IR')
countriesEnum.IS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='IS', tag='IS')
countriesEnum.IT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='IT', tag='IT')
countriesEnum.JE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='JE', tag='JE')
countriesEnum.JM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='JM', tag='JM')
countriesEnum.JO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='JO', tag='JO')
countriesEnum.JP = countriesEnum._CF_enumeration.addEnumeration(unicode_value='JP', tag='JP')
countriesEnum.KE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KE', tag='KE')
countriesEnum.KG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KG', tag='KG')
countriesEnum.KH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KH', tag='KH')
countriesEnum.KI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KI', tag='KI')
countriesEnum.KM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KM', tag='KM')
countriesEnum.KN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KN', tag='KN')
countriesEnum.KP = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KP', tag='KP')
countriesEnum.KR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KR', tag='KR')
countriesEnum.KW = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KW', tag='KW')
countriesEnum.KY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KY', tag='KY')
countriesEnum.KZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='KZ', tag='KZ')
countriesEnum.LA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LA', tag='LA')
countriesEnum.LB = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LB', tag='LB')
countriesEnum.LC = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LC', tag='LC')
countriesEnum.LI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LI', tag='LI')
countriesEnum.LK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LK', tag='LK')
countriesEnum.LR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LR', tag='LR')
countriesEnum.LS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LS', tag='LS')
countriesEnum.LT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
countriesEnum.LU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LU', tag='LU')
countriesEnum.LV = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LV', tag='LV')
countriesEnum.LY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='LY', tag='LY')
countriesEnum.MA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
countriesEnum.MC = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MC', tag='MC')
countriesEnum.MD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MD', tag='MD')
countriesEnum.ME = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ME', tag='ME')
countriesEnum.MF = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MF', tag='MF')
countriesEnum.MG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MG', tag='MG')
countriesEnum.MH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MH', tag='MH')
countriesEnum.MK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MK', tag='MK')
countriesEnum.ML = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ML', tag='ML')
countriesEnum.MM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MM', tag='MM')
countriesEnum.MN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
countriesEnum.MO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MO', tag='MO')
countriesEnum.MP = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MP', tag='MP')
countriesEnum.MQ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MQ', tag='MQ')
countriesEnum.MR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MR', tag='MR')
countriesEnum.MS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
countriesEnum.MT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MT', tag='MT')
countriesEnum.MU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MU', tag='MU')
countriesEnum.MV = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
countriesEnum.MW = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
countriesEnum.MX = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MX', tag='MX')
countriesEnum.MY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MY', tag='MY')
countriesEnum.MZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MZ', tag='MZ')
countriesEnum.NA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NA', tag='NA')
countriesEnum.NC = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NC', tag='NC')
countriesEnum.NE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NE', tag='NE')
countriesEnum.NF = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NF', tag='NF')
countriesEnum.NG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NG', tag='NG')
countriesEnum.NI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NI', tag='NI')
countriesEnum.NL = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NL', tag='NL')
countriesEnum.NO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NO', tag='NO')
countriesEnum.NP = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NP', tag='NP')
countriesEnum.NR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NR', tag='NR')
countriesEnum.NU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NU', tag='NU')
countriesEnum.NZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NZ', tag='NZ')
countriesEnum.OM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='OM', tag='OM')
countriesEnum.PA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PA', tag='PA')
countriesEnum.PE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PE', tag='PE')
countriesEnum.PF = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PF', tag='PF')
countriesEnum.PG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PG', tag='PG')
countriesEnum.PH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PH', tag='PH')
countriesEnum.PK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PK', tag='PK')
countriesEnum.PL = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PL', tag='PL')
countriesEnum.PM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PM', tag='PM')
countriesEnum.PN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PN', tag='PN')
countriesEnum.PR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
countriesEnum.PS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PS', tag='PS')
countriesEnum.PT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PT', tag='PT')
countriesEnum.PW = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PW', tag='PW')
countriesEnum.PY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PY', tag='PY')
countriesEnum.QA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='QA', tag='QA')
countriesEnum.RE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='RE', tag='RE')
countriesEnum.RO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='RO', tag='RO')
countriesEnum.RS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='RS', tag='RS')
countriesEnum.RU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='RU', tag='RU')
countriesEnum.RW = countriesEnum._CF_enumeration.addEnumeration(unicode_value='RW', tag='RW')
countriesEnum.SA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SA', tag='SA')
countriesEnum.SB = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SB', tag='SB')
countriesEnum.SC = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SC', tag='SC')
countriesEnum.SD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SD', tag='SD')
countriesEnum.SE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SE', tag='SE')
countriesEnum.SG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SG', tag='SG')
countriesEnum.SH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SH', tag='SH')
countriesEnum.SI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
countriesEnum.SJ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SJ', tag='SJ')
countriesEnum.SK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SK', tag='SK')
countriesEnum.SL = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SL', tag='SL')
countriesEnum.SM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SM', tag='SM')
countriesEnum.SN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SN', tag='SN')
countriesEnum.SO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SO', tag='SO')
countriesEnum.SR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SR', tag='SR')
countriesEnum.ST = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ST', tag='ST')
countriesEnum.SV = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SV', tag='SV')
countriesEnum.SY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SY', tag='SY')
countriesEnum.SZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SZ', tag='SZ')
countriesEnum.TC = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TC', tag='TC')
countriesEnum.TD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TD', tag='TD')
countriesEnum.TF = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TF', tag='TF')
countriesEnum.TG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TG', tag='TG')
countriesEnum.TH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TH', tag='TH')
countriesEnum.TJ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TJ', tag='TJ')
countriesEnum.TK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TK', tag='TK')
countriesEnum.TL = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TL', tag='TL')
countriesEnum.TM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TM', tag='TM')
countriesEnum.TN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TN', tag='TN')
countriesEnum.TO = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TO', tag='TO')
countriesEnum.TR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TR', tag='TR')
countriesEnum.TT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TT', tag='TT')
countriesEnum.TV = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TV', tag='TV')
countriesEnum.TW = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
countriesEnum.TZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TZ', tag='TZ')
countriesEnum.UA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='UA', tag='UA')
countriesEnum.UG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='UG', tag='UG')
countriesEnum.UM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='UM', tag='UM')
countriesEnum.US = countriesEnum._CF_enumeration.addEnumeration(unicode_value='US', tag='US')
countriesEnum.UY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='UY', tag='UY')
countriesEnum.UZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='UZ', tag='UZ')
countriesEnum.VA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
countriesEnum.VC = countriesEnum._CF_enumeration.addEnumeration(unicode_value='VC', tag='VC')
countriesEnum.VE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='VE', tag='VE')
countriesEnum.VG = countriesEnum._CF_enumeration.addEnumeration(unicode_value='VG', tag='VG')
countriesEnum.VI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='VI', tag='VI')
countriesEnum.VN = countriesEnum._CF_enumeration.addEnumeration(unicode_value='VN', tag='VN')
countriesEnum.VU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='VU', tag='VU')
countriesEnum.WF = countriesEnum._CF_enumeration.addEnumeration(unicode_value='WF', tag='WF')
countriesEnum.WS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='WS', tag='WS')
countriesEnum.YE = countriesEnum._CF_enumeration.addEnumeration(unicode_value='YE', tag='YE')
countriesEnum.YT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='YT', tag='YT')
countriesEnum.ZA = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ZA', tag='ZA')
countriesEnum.ZM = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ZM', tag='ZM')
countriesEnum.ZW = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ZW', tag='ZW')
countriesEnum.AI_ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='AI', tag='AI_')
countriesEnum.BQ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BQ', tag='BQ')
countriesEnum.BU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='BU', tag='BU')
countriesEnum.CS = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CS', tag='CS')
countriesEnum.CS_ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CS', tag='CS_')
countriesEnum.CT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='CT', tag='CT')
countriesEnum.DD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='DD', tag='DD')
countriesEnum.DY = countriesEnum._CF_enumeration.addEnumeration(unicode_value='DY', tag='DY')
countriesEnum.FQ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='FQ', tag='FQ')
countriesEnum.FX = countriesEnum._CF_enumeration.addEnumeration(unicode_value='FX', tag='FX')
countriesEnum.GE_ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='GE', tag='GE_')
countriesEnum.HV = countriesEnum._CF_enumeration.addEnumeration(unicode_value='HV', tag='HV')
countriesEnum.JT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='JT', tag='JT')
countriesEnum.MI = countriesEnum._CF_enumeration.addEnumeration(unicode_value='MI', tag='MI')
countriesEnum.NH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NH', tag='NH')
countriesEnum.NQ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NQ', tag='NQ')
countriesEnum.NT = countriesEnum._CF_enumeration.addEnumeration(unicode_value='NT', tag='NT')
countriesEnum.PC = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PC', tag='PC')
countriesEnum.PU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PU', tag='PU')
countriesEnum.PZ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='PZ', tag='PZ')
countriesEnum.RH = countriesEnum._CF_enumeration.addEnumeration(unicode_value='RH', tag='RH')
countriesEnum.SK_ = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SK', tag='SK_')
countriesEnum.SU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='SU', tag='SU')
countriesEnum.TP = countriesEnum._CF_enumeration.addEnumeration(unicode_value='TP', tag='TP')
countriesEnum.VD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='VD', tag='VD')
countriesEnum.WK = countriesEnum._CF_enumeration.addEnumeration(unicode_value='WK', tag='WK')
countriesEnum.YD = countriesEnum._CF_enumeration.addEnumeration(unicode_value='YD', tag='YD')
countriesEnum.YU = countriesEnum._CF_enumeration.addEnumeration(unicode_value='YU', tag='YU')
countriesEnum.ZR = countriesEnum._CF_enumeration.addEnumeration(unicode_value='ZR', tag='ZR')
countriesEnum._InitializeFacetMap(countriesEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'countriesEnum', countriesEnum)

# Complex type {urn:vpro:shared:2009}imageType with content type ELEMENT_ONLY
class imageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:shared:2009}imageType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageType')
    _XSDLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:shared:2009}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__urnvproshared2009_imageType_urnvproshared2009title', False, pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 35, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {urn:vpro:shared:2009}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__urnvproshared2009_imageType_urnvproshared2009description', False, pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 36, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {urn:vpro:shared:2009}imageUri uses Python identifier imageUri
    __imageUri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'imageUri'), 'imageUri', '__urnvproshared2009_imageType_urnvproshared2009imageUri', False, pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 37, 6), )

    
    imageUri = property(__imageUri.value, __imageUri.set, None, None)

    
    # Element {urn:vpro:shared:2009}offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'offset'), 'offset', '__urnvproshared2009_imageType_urnvproshared2009offset', False, pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 38, 6), )

    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Element {urn:vpro:shared:2009}height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'height'), 'height', '__urnvproshared2009_imageType_urnvproshared2009height', False, pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 39, 6), )

    
    height = property(__height.value, __height.set, None, None)

    
    # Element {urn:vpro:shared:2009}width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'width'), 'width', '__urnvproshared2009_imageType_urnvproshared2009width', False, pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 40, 6), )

    
    width = property(__width.value, __width.set, None, None)

    
    # Element {urn:vpro:shared:2009}credits uses Python identifier credits
    __credits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'credits'), 'credits', '__urnvproshared2009_imageType_urnvproshared2009credits', False, pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 41, 6), )

    
    credits = property(__credits.value, __credits.set, None, None)

    
    # Element {urn:vpro:shared:2009}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__urnvproshared2009_imageType_urnvproshared2009source', False, pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 42, 6), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {urn:vpro:shared:2009}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'date'), 'date', '__urnvproshared2009_imageType_urnvproshared2009date', False, pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 43, 6), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute urn uses Python identifier urn
    __urn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'urn'), 'urn', '__urnvproshared2009_imageType_urn', pyxb.binding.datatypes.anyURI)
    __urn._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 8, 4)
    __urn._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 8, 4)
    
    urn = property(__urn.value, __urn.set, None, None)

    
    # Attribute publishStart uses Python identifier publishStart
    __publishStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStart'), 'publishStart', '__urnvproshared2009_imageType_publishStart', pyxb.binding.datatypes.dateTime)
    __publishStart._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 9, 4)
    __publishStart._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 9, 4)
    
    publishStart = property(__publishStart.value, __publishStart.set, None, None)

    
    # Attribute publishStop uses Python identifier publishStop
    __publishStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishStop'), 'publishStop', '__urnvproshared2009_imageType_publishStop', pyxb.binding.datatypes.dateTime)
    __publishStop._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 10, 4)
    __publishStop._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 10, 4)
    
    publishStop = property(__publishStop.value, __publishStop.set, None, None)

    
    # Attribute publishDate uses Python identifier publishDate
    __publishDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishDate'), 'publishDate', '__urnvproshared2009_imageType_publishDate', pyxb.binding.datatypes.dateTime)
    __publishDate._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 11, 4)
    __publishDate._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 11, 4)
    
    publishDate = property(__publishDate.value, __publishDate.set, None, None)

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__urnvproshared2009_imageType_creationDate', pyxb.binding.datatypes.dateTime)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 12, 4)
    __creationDate._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 12, 4)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Attribute lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastModified'), 'lastModified', '__urnvproshared2009_imageType_lastModified', pyxb.binding.datatypes.dateTime)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 13, 4)
    __lastModified._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 13, 4)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute workflow uses Python identifier workflow
    __workflow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'workflow'), 'workflow', '__urnvproshared2009_imageType_workflow', workflowEnumType)
    __workflow._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 14, 4)
    __workflow._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 14, 4)
    
    workflow = property(__workflow.value, __workflow.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnvproshared2009_imageType_type', imageTypeEnum)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 46, 4)
    __type._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 46, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner'), 'owner', '__urnvproshared2009_imageType_owner', ownerTypeEnum, required=True)
    __owner._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 47, 4)
    __owner._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 47, 4)
    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Attribute highlighted uses Python identifier highlighted
    __highlighted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'highlighted'), 'highlighted', '__urnvproshared2009_imageType_highlighted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __highlighted._DeclarationLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 48, 4)
    __highlighted._UseLocation = pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 48, 4)
    
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
Namespace.addCategoryObject('typeBinding', 'imageType', imageType)


image = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'image'), imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', image.name().localName(), image)



imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 35, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 36, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'imageUri'), pyxb.binding.datatypes.anyURI, scope=imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 37, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offset'), pyxb.binding.datatypes.duration, scope=imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 38, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height'), pyxb.binding.datatypes.positiveInteger, scope=imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 39, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'width'), pyxb.binding.datatypes.positiveInteger, scope=imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 40, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'credits'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 41, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 42, 6)))

imageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'date'), pyxb.binding.datatypes.string, scope=imageType, location=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 43, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 36, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 37, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 38, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 39, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 40, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 41, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 42, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 43, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 36, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'imageUri')), pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 37, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'offset')), pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 38, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'height')), pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 39, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'width')), pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 40, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credits')), pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 41, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 42, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'date')), pyxb.utils.utility.Location('http://poms.omroep.nl/schema/vproShared.xsd', 43, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
imageType._Automaton = _BuildAutomaton()

