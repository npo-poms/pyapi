#!/usr/bin/env python3
import unittest

from npoapi.xml import poms
from npoapi.xml import media
from npoapi import base
import pyxb

import npoapi.basic_backend

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
