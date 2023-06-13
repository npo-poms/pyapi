#!/usr/bin/env python3
import unittest

import pyxb

from npoapi import base
from npoapi.xml import media
from npoapi.xml import poms
from npoapi.xml import mediaupdate
from xmldiff import main


base.declare_namespaces()


class Tests(unittest.TestCase):

    def xmlAssert(self, expected: str, real: object):
       if not isinstance(real, str):
          real = real.toxml()

       self.assertEqual([],main.diff_texts(expected.strip(), real))


    def setUp(self):
        pyxb.RequireValidWhenGenerating(True)
        self.maxDiff = None

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
        update = poms.CreateFromDocument(xml)
        self.assertEqual(update.type, media.programTypeEnum.CLIP)
        self.assertEqual(update.title[0].value(), "Main title")
        update.duration = "PT5M"
        print(update.toxml())
        self.xmlAssert("""<?xml version="1.0" ?><program avType="VIDEO" embeddable="true" publishStart="2012-01-11T15:16:01.287Z" publishStop="2012-01-11T17:16:01.287Z" type="CLIP" xmlns="urn:vpro:media:update:2009"><broadcaster>VPRO</broadcaster><title type="MAIN">Main title</title><duration>PT5M</duration><memberOf position="34">urn:vpro:media:group:2981744</memberOf><memberOf>POMS_S_VPRO_159096</memberOf><images><image highlighted="false" type="PICTURE"><title>bla</title><urn>urn:vpro:image:496158</urn></image></images></program>""", update)
        print(len(update.images.image))

    def test_segment(self):
        pyxb.RequireValidWhenGenerating(False)
        segment = mediaupdate.segmentUpdateType(midRef="program_mid")
        segment.start = "PT0S"
        print(segment.toxml(encoding='UTF-8', element_name="segment")),

    def test_image(self):
        xml = """<program xmlns="urn:vpro:media:update:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009" type="CLIP" avType="AUDIO" embeddable="true" mid="POMS_VPRO_1421796" urn="urn:vpro:media:program:58516847">
<broadcaster>EO</broadcaster>
<title type="MAIN">Test 2016-04-22T09:38:43.304Z</title>
<locations/>
<scheduleEvents/>
<images>
<image type="PORTRAIT" highlighted="false">
<title>sdf</title>
<description>asdfasdf</description>
<urn>urn:vpro:image:274460</urn>
</image>
</images>
<segments/>
</program>"""
        update = poms.CreateFromDocument(xml)
        self.assertEqual(len(update.images.image), 1)


    def test_image2(self):
        xml = """<?xml version="1.0" ?><image highlighted="false" type="PORTRAIT" xmlns="urn:vpro:media:update:2009"><title>sdf</title><description>asdfasdf</description><urn>urn:vpro:image:274460</urn></image>"""
        image = poms.CreateFromDocument(xml)
        self.assertEqual(image.title, "sdf")

    def test_images_collection(self):
        xml = """<collection xmlns:update="urn:vpro:media:update:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009">
<update:image type="PORTRAIT" highlighted="false">
<update:title>sdf</update:title>
<update:description>asdfasdf</update:description>
<update:urn>urn:vpro:image:274460</update:urn>
</update:image>
</collection>"""
        images = poms.CreateFromDocument(xml)
        self.assertEqual(images.wildcardElements()[0].title, "sdf")

    def test_media_form(self):
        from npoapi.xml import api
        form = api.mediaForm()
        form.searches = pyxb.BIND()
        form.searches.mediaIds = "crid://pyapi/clip/1"
        self.assertEqual('<?xml version="1.0" ?><api:mediaForm xmlns="urn:vpro:media:update:2009" xmlns:api="urn:vpro:api:2013"><api:searches><api:mediaIds><api:matcher>crid://pyapi/clip/1</api:matcher></api:mediaIds></api:searches></api:mediaForm>', form.toxml())

    def test_add_person(self):
        from npoapi.xml import mediaupdate
        program = mediaupdate.program(type="CLIP", avType="MIXED")
        program.title.append(mediaupdate.titleUpdateType("hoi ", type="MAIN"))
        program.broadcaster.append("VPRO")

        program.credits = pyxb.BIND()
        person = mediaupdate.personUpdateType(role=media.roleType.ACTOR, givenName = "Pietje", familyName = "Puk")
        program.credits.append(person)
        print(program.toxml())

    def test_memberRefUpdate(self):
        from npoapi.xml import mediaupdate
        memberOf = mediaupdate.memberRef("owner_mid")
        memberOf.position = 4
        memberOf.highlighted = False
        print(memberOf.toxml())


    def test_page_form(self):
        from npoapi.xml import api
        import datetime
        form = api.pagesForm()
        form.sortFields = pyxb.BIND()
        form.sortFields.append(api.pageSortTypeEnum.lastModified)
        form.searches = pyxb.BIND()
        form.searches.lastModifiedDates = pyxb.BIND()
        end = datetime.datetime(2017, 6, 19, 0, 0)
        #now = datetime.datetime.now()
        #today = now.replace(hour = 6, minute=0, second=0, microsecond=0)
        dateRange = api.dateRangeMatcherType(end = end)
        form.searches.lastModifiedDates.append(dateRange)
        self.assertEqual('<?xml version="1.0" ?><api:pagesForm xmlns="urn:vpro:media:update:2009" xmlns:api="urn:vpro:api:2013"><api:searches><api:lastModifiedDates><api:matcher><api:end>2017-06-19T00:00:00</api:end></api:matcher></api:lastModifiedDates></api:searches><api:sortFields><api:sort>lastModified</api:sort></api:sortFields></api:pagesForm>',
        form.toxml())

    def test_page_update(self):
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
        page_update = poms.CreateFromDocument(example.encode("UTF-8"))
        self.assertEqual(page_update.title, "Hoi & Hallo foobar")


    def test_media_domain(self):
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<program type="CLIP" avType="VIDEO" publishStop="2012-01-11T18:16:01.287+01:00" publishStart="2012-01-11T16:16:01.287+01:00" embeddable="true"   xmlns="urn:vpro:media:2009">
  <broadcaster id='VPRO'>VPRO</broadcaster>
  <title type="MAIN" owner='BROADCASTER'>Main title</title>
</program>
"""
        object = poms.CreateFromDocument(xml)

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

        object = poms.CreateFromDocument(xml)

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
        locations = poms.CreateFromDocument(xml)
        self.assertEqual(locations.wildcardElements()[0].urn, "urn:vpro:media:location:126275555")