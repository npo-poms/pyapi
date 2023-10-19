#!/usr/bin/env python3
import dataclasses
import unittest

import dateutil.parser
from xmldiff import main
from xsdata.models.datatype import XmlDateTime

from npoapi.data import media, AgeRatingType
from npoapi.data import poms


class Tests(unittest.TestCase):

    def xml_assert(self, expected: str, real: object):
       if not isinstance(real, str):
          real = poms.to_xml(real)

       self.assertEqual([],main.diff_texts(expected.strip().encode("UTF-8"), real.encode("UTF-8")))


    def setUp(self):
        self.maxDiff = None
        
        
    def test_location_xml_datetime(self):
        location = poms.LocationType()
        location.publishStart = XmlDateTime.from_string("2012-01-11T16:16:01.287+01:00")
        self.xml_assert(
            """
            <?xml version="1.0" encoding="UTF-8"?>
<locationType xmlns:update="urn:vpro:media:update:2009" xmlns:pageupdate="urn:vpro:pages:update:2013" xmlns:media="urn:vpro:media:2009" xmlns:pages="urn:vpro:pages:2013" xmlns:api="urn:vpro:api:2013" publishStart="2012-01-11T16:16:01.287+01:00"/>
            """, location)
        
    def test_location_native_datetime(self):
        location = poms.LocationType()
        location.publishStart = XmlDateTime.from_datetime(dateutil.parser.isoparse("2012-01-11T16:16:01.287+01:00"))
        self.xml_assert(
            """
            <?xml version="1.0" encoding="UTF-8"?>
<locationType xmlns:update="urn:vpro:media:update:2009" xmlns:pageupdate="urn:vpro:pages:update:2013" xmlns:media="urn:vpro:media:2009" xmlns:pages="urn:vpro:pages:2013" xmlns:api="urn:vpro:api:2013" publishStart="2012-01-11T16:16:01.287+01:00"/>
            """, location)
        
    def test_locations(self):
        pass

    def test_parse_page_update(self):
        example = """
        <page type="AUDIO" url="http://test.vpro.nl/article/1234"  xmlns="urn:vpro:pages:update:2013">
  <crid>crid://bla/1234</crid>
  <broadcaster>VPRO</broadcaster>
  <title>Hoi &amp; Hallo foobar</title>
  <paragraphs>
    <paragraph>
      <title>Title of &amp; paragraph</title>
      <body>Foo &amp; Bar</body>
    </paragraph>
  </paragraphs>
</page>
        """
        pageupdate = poms.from_string(example)
        self.assertTrue(dataclasses.is_dataclass(pageupdate))

    def test_set_duration(self):
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<program type="CLIP" avType="VIDEO" publishStop="2012-01-11T18:16:01.287+01:00" publishStart="2012-01-11T16:16:01.287+01:00" embeddable="true"
    xmlns="urn:vpro:media:update:2009">
  <broadcaster>VPRO</broadcaster>
  <title type="MAIN">Main title</title>
  <memberOf position="34">urn:vpro:media:group:2981744</memberOf>
  <memberOf>POMS_S_VPRO_159096</memberOf>
  <images>
    <image type="PICTURE" highlighted="false">
      <title>bla</title>
      <urn>urn:vpro:image:496158</urn>
    </image>
  </images>
</program>
"""
        update = poms.from_string(xml)
        self.assertEqual(update.typeValue, media.ProgramTypeEnum.CLIP)
        self.assertEqual(update.title[0].value, "Main title")
        update.duration = "PT5M"
        self.xml_assert("""<?xml version="1.0" encoding="UTF-8"?>
<update:program xmlns:update="urn:vpro:media:update:2009" xmlns:pageupdate="urn:vpro:pages:update:2013" xmlns:media="urn:vpro:media:2009" xmlns:pages="urn:vpro:pages:2013" xmlns:api="urn:vpro:api:2013" avType="VIDEO" embeddable="true" publishStart="2012-01-11T16:16:01.287+01:00" publishStop="2012-01-11T18:16:01.287+01:00" type="CLIP"><update:broadcaster>VPRO</update:broadcaster><update:title type="MAIN">Main title</update:title><update:duration>PT5M</update:duration><update:memberOf position="34" highlighted="false">urn:vpro:media:group:2981744</update:memberOf><update:memberOf highlighted="false">POMS_S_VPRO_159096</update:memberOf><update:images><update:image type="PICTURE" highlighted="false"><update:title>bla</update:title><update:urn>urn:vpro:image:496158</update:urn></update:image></update:images></update:program>""", update)

        
    def test_images_collection(self):
        xml = """<collection xmlns:update="urn:vpro:media:update:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009">
<update:image type="PORTRAIT" highlighted="false">
<update:title>sdf</update:title>
<update:description>asdfasdf</update:description>
<update:urn>urn:vpro:image:274460</update:urn>
</update:image>
</collection>"""
        images = poms.from_string(xml)
        first_image = images.otherElement[0]
        self.assertEqual(first_image.title, "sdf")
        
    def test_locations_collection(self):
        xml = """
<collection xmlns:update="urn:vpro:media:update:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009" version="7.6.2">
  <update:location publishStop="2012-01-11T18:16:01.287+01:00" urn="urn:vpro:media:location:126275555">
    <update:programUrl>http://www.vpro.nl/123</update:programUrl>
    <update:avAttributes>
      <update:avFileFormat>UNKNOWN</update:avFileFormat>
    </update:avAttributes>
  </update:location>
  <update:location publishStop="2012-01-11T18:16:01.287+01:00" urn="urn:vpro:media:location:126275547">
    <update:programUrl>http://www.vpro.nl/1681974873.mp3</update:programUrl>
    <update:avAttributes>
      <update:avFileFormat>MP3</update:avFileFormat>
    </update:avAttributes>
  </update:location>
  <update:location urn="urn:vpro:media:location:99591948">
    <update:programUrl>npo://internetvod.omroep.nl/WO_VPRO_783763</update:programUrl>
    <update:avAttributes>
      <update:bitrate>3500000</update:bitrate>
      <update:avFileFormat>HASP</update:avFileFormat>
    </update:avAttributes>
  </update:location>
</collection>"""
        locations = poms.from_string(xml)
        first_location = locations.otherElement[0]
        self.assertEqual(first_location.urn, "urn:vpro:media:location:126275555")

    def test_page_domain(self):
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<api:pageSearchResult xmlns:api="urn:vpro:api:2013" xmlns="urn:vpro:media:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009" xmlns:pages="urn:vpro:pages:2013" total="432" totalQualifier="EQUAL_TO" offset="0" max="0">
  <api:items>
    <api:item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="api:searchResultItem" score="0.3099519">
      <api:result xsi:type="pages:pageType" url="https://www.vprobroadcast.com/play~WO_VPRO_2297327~antibiotics~.html" type="VIDEO" creationDate="2019-11-22T14:15:09.443+01:00" lastModified="2019-11-22T14:15:09.443+01:00" lastPublished="2019-11-22T14:15:24.341+01:00" publishStart="2015-10-16T14:23:14.729+02:00" refCount="0" sortDate="2015-10-16T14:23:14.729+02:00">
        <pages:crid>crid://vpro/media/vprobroadcast/WO_VPRO_2297327</pages:crid>
        <pages:broadcaster id="VPRO"></pages:broadcaster>
        <pages:portal id="VPROBROADCAST" url="https://www.vprobroadcast.com">
          <pages:name>www.vprobroadcast.com</pages:name>
        </pages:portal>
        <pages:title>Antibiotics</pages:title>
        <pages:images>
          <pages:image type="PICTURE" url="https://images.poms.omroep.nl/image/s360/665086.jpg">
            <pages:title>Antibiotica</pages:title>
            <pages:description>Labyrint</pages:description>
          </pages:image>
        </pages:images>
      </api:result>
    </api:item>
  </api:items>
  <api:facets/>
  <api:selectedFacets/>
</api:pageSearchResult>
"""

        object = poms.from_string(xml)
        print(str(object))
        print(object.to_xml())
        
    def test_tolerate_xsi(self):
       xml =  """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!-- This clip does not have a mid. So it will be a new clip when you post this -->
<program xmlns="urn:vpro:media:update:2009"
         type="CLIP" avType="VIDEO"
         publishStart="2012-01-11T16:16:01.287+01:00" embeddable="true"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="urn:vpro:media:update:2009 https://poms.omroep.nl/schema/update/vproMediaUpdate.xsd"        
         >
  <broadcaster>VPRO</broadcaster>
  <title type="MAIN">TEST TEST</title>
  <tag>Kabouters</tag>
  <ageRating>ALL</ageRating>
  <email>programma@avro.nl</email>  
</program>         
         """
       program_update =  poms.from_string(xml) # FAILS: https://github.com/tefra/xsdata/issues/845
       self.assertEqual(program_update.ageRating, AgeRatingType.ALL)
