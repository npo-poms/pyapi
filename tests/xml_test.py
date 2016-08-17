#!/usr/bin/env python3
import unittest

import pyxb

from npoapi import base
from npoapi.xml import media
from npoapi.xml import poms

base.declare_namespaces()


class Tests(unittest.TestCase):


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
        self.assertEquals(update.type, media.programTypeEnum.CLIP)
        self.assertEquals(update.title[0].value(), "Main title")
        update.duration = "PT5M"
        print(update.toxml())
        self.assertEquals(update.toxml(), """<?xml version="1.0" ?><program avType="VIDEO" embeddable="true" publishStart="2012-01-11T15:16:01.287Z" publishStop="2012-01-11T17:16:01.287Z" type="CLIP" xmlns="urn:vpro:media:update:2009"><broadcaster>VPRO</broadcaster><title type="MAIN">Main title</title><duration>PT5M</duration><memberOf position="34">urn:vpro:media:group:2981744</memberOf><memberOf>POMS_S_VPRO_159096</memberOf><images><image highlighted="false" type="PICTURE"><title>bla</title><urn>urn:vpro:image:496158</urn></image></images></program>""")
        print(len(update.images.image))

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
        self.assertEquals(len(update.images.image), 1)


    def test_image2(self):
        xml = """<?xml version="1.0" ?><image highlighted="false" type="PORTRAIT" xmlns="urn:vpro:media:update:2009"><title>sdf</title><description>asdfasdf</description><urn>urn:vpro:image:274460</urn></image>"""
        image = poms.CreateFromDocument(xml)
        self.assertEquals(image.title, "sdf")

    def test_images_collection(self):
        xml = """<collection xmlns:update="urn:vpro:media:update:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009">
<update:image type="PORTRAIT" highlighted="false">
<update:title>sdf</update:title>
<update:description>asdfasdf</update:description>
<update:urn>urn:vpro:image:274460</update:urn>
</update:image>
</collection>"""
        images = poms.CreateFromDocument(xml)
        self.assertEquals(images.wildcardElements()[0].title, "sdf")


    def test_media_form(self):
        from npoapi.xml import api
        form = api.mediaForm()
        form.searches = pyxb.BIND()
        form.searches.mediaIds = "crid://pyapi/clip/1"
        self.assertEquals('<?xml version="1.0" ?><api:mediaForm xmlns="urn:vpro:media:update:2009" xmlns:api="urn:vpro:api:2013"><api:searches><api:mediaIds><api:matcher>crid://pyapi/clip/1</api:matcher></api:mediaIds></api:searches></api:mediaForm>', form.toxml())

    def test_add_person(self):
        from npoapi.xml import mediaupdate
        program = mediaupdate.program(type="CLIP", avType="MIXED")
        program.title.append(mediaupdate.titleUpdateType("hoi ", type="MAIN"))
        program.broadcaster.append("VPRO")

        program.credits = pyxb.BIND()
        person = mediaupdate.personUpdateType()
        person.role = media.roleType.ACTOR
        person.givenName = "pietje"
        person.familyName = "puk"
        program.credits.append(person)
        print(program.toxml())

    def test_list(self):
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><list xmlns="urn:vpro:media:update:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009" offset="0" totalCount="5" max="200" order="ASC" size="5"><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="1" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422840" urn="urn:vpro:media:program:31357971"><broadcaster>VPRO</broadcaster><title type="MAIN">Sweaty Fingers</title><duration>P0DT0H11M53.000S</duration><memberOf position="1" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357975"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track01.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H11M53.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357976">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="2" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422839" urn="urn:vpro:media:program:31357951"><broadcaster>VPRO</broadcaster><title type="MAIN">Silver Headband</title><duration>P0DT0H8M53.000S</duration><memberOf position="2" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357955"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track02.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H8M53.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357956">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="3" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422842" urn="urn:vpro:media:program:31357990"><broadcaster>VPRO</broadcaster><title type="MAIN">Arrow\'s Myth</title><duration>P0DT0H8M49.000S</duration><memberOf position="3" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357994"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track03.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H8M49.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357995">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="4" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422843" urn="urn:vpro:media:program:31357998"><broadcaster>VPRO</broadcaster><title type="MAIN">Shikaakwa</title><duration>P0DT0H5M2.000S</duration><memberOf position="4" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31358002"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track04.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H5M2.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31358003">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="5" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422841" urn="urn:vpro:media:program:31357982"><broadcaster>VPRO</broadcaster><title type="MAIN">Slow Bern</title><duration>P0DT0H7M14.000S</duration><memberOf position="5" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357986"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track05.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H7M14.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357987">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item></list>"""
        poms.CreateFromDocument(xml)
