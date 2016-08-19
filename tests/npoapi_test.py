#!/usr/bin/env python3
import json
import unittest
from xml.dom import minidom
import os

from npoapi import Media
from npoapi import Screens
from npoapi import MediaBackend
from npoapi.npoapi import NpoApi
from npoapi.npoapi import NpoApiBase

from npoapi.xml import poms
from npoapi.xml import mediaupdate

import time

ENV = "dev"


class Tests(unittest.TestCase):
    def test_authentication(self):
        client = NpoApi(origin="http://www.vpro.nl") \
            .login(key="a", secret="b")
        self.assertEqual("NPO a:CtHYR9a+nr17OIn5rYml6a+A9ujqe0IywWqr93/DAOk=",
                         client.authenticate(uri="/media", now="Fri, 30 Oct 2015 08:43:31 -0000")[0])

    def test_env(self):
        properties={'a': 'A', 'a.prod': 'Aprod', 'b': 'B', 'b.test': 'Btest'}
        client = NpoApiBase().env('test')
        settings = client.read_settings_from_properties(properties)
        self.assertEquals(settings['a'], "A")
        self.assertEquals(settings['b'], "Btest")

class MediaTests(unittest.TestCase):
    def test_get(self):
        client = self.get_client()
        result = json.JSONDecoder().decode(client.get("AVRO_1656037"))
        self.assertEqual(result["mid"], "AVRO_1656037")

    def test_get_quote(self):
        client = self.get_client()
        result = client.get(" Avro_1260864")
        self.assertEqual("", result)
        self.assertEqual(404, client.code)

    def test_get_space(self):
        client = self.get_client()
        result = json.JSONDecoder().decode(client.get("BNN 240466"))
        self.assertEqual(result["mid"], "BNN 240466")

    def test_list(self):
        client = self.get_client()
        result = json.JSONDecoder().decode(client.list())
        ""

    def test_search(self):
        client = self.get_client()
        result = json.JSONDecoder().decode(client.search("{}"))
        ""

    def test_stream(self):
        import ijson
        from datetime import datetime
        client = self.get_client()
        objects = ijson.items(client.changes(stream=True), 'changes.item')
        for o in objects:
            media = o["media"]
            sortDate = datetime.fromtimestamp(media["sortDate"] / 1e3)
            print(media["broadcasters"], sortDate)

    def test(self):
        import datetime
        dates = [datetime.date(2016, 1, 31), datetime.date(2016, 1, 30), datetime.date(2016, 2, 1)]
        sorted(dates)
        print(dates)

    def get_client(self):
        print(os.path.dirname(__file__))
        return Media().configured_login(config_dir=os.path.dirname(__file__)).env(ENV).debug()


class ScreenTests(unittest.TestCase):
    def test_screens(self):
        client = self.get_client()
        result = json.JSONDecoder().decode(client.list(offset=3))
        self.assertEqual(result["offset"], 3)

    def get_client(self):
        print(os.path.dirname(__file__))
        return Screens().configured_login(config_dir=os.path.dirname(__file__)).env(ENV).debug()


class MediaBackendTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = MediaBackend().configured_login(config_dir=os.path.dirname(__file__)).env(ENV).debug()

    def test_xml_to_bytes_string(self):
        self.assertEquals("<a xmlns='urn:vpro:media:update:2009' />",
                          self.client.xml_to_bytes("<a xmlns='urn:vpro:media:update:2009' />").decode("utf-8"))

    def test_xml_to_bytes_minidom(self):
        self.assertEquals('<a xmlns="urn:vpro:media:update:2009"/>',
                          self.client.xml_to_bytes(
                              minidom.parseString("<a xmlns='urn:vpro:media:update:2009' />").documentElement).decode(
                              "utf-8"))

    def test_append_params(self):
        self.assertEquals("http://vpro.nl?a=a&x=y", self.client.append_params("http://vpro.nl", include_errors=False,  a="a", x="y"))



    def test_set_duration(self):
        existing = poms.CreateFromDocument(self.client.get("WO_VPRO_1422026"))
        existing.duration = "PT30M"
        self.client.post(existing)

    def test_get_locations(self):
        bytes=self.client.get_locations("POMS_VPRO_1421796")
        locations=poms.CreateFromDocument(bytes)
        print(str(locations))

    def test_get_segments(self):
        bytes = self.client.get("RBX_AT_2145721")
        existing = mediaupdate.CreateFromDocument(bytes)
        self.assertTrue(type(existing) == mediaupdate.segmentUpdateType)


    def test_get_images(self):
        mid="POMS_VPRO_1421796"
        media=poms.CreateFromDocument(self.client.get(mid))
        print(len(media.images.image))
        image=media.images.image[0]
        bytes = self.client.get_images("POMS_VPRO_1421796")
        images= poms.CreateFromDocument(bytes)
        image2=images.wildcardElements()[0]
        self.assertEquals(image.title, image2.title)
        self.assertEquals(image2.title, "sdf")
        print(image2.toxml())


    def test_set_location(self):
        mid = "POMS_VPRO_1421796"
        self.client.set_location(mid, "http://www.vpro.nl/123", publishStop="2012-01-11T17:16:01.287Z")


    def test_set_location_by_id(self):
        mid = "POMS_VPRO_1421796"
        self.client.set_location(mid, 58758190, publishStop="2012-01-11T17:16:01.287Z")

    def test_set_location_by_id_as_string(self):
        mid = "POMS_VPRO_1421796"
        self.client.set_location(mid, "58758190", publishStop="2013-01-11T17:16:01.287Z")

    def test_set_location_by_urn(self):
        mid = "POMS_VPRO_1421796"
        self.client.set_location(mid, "urn:vpro:media:location:58758190", publishStop="2014-01-11T17:16:01.287Z")


    def test_create_location(self):
        mid = "POMS_VPRO_1421796"
        self.client.set_location(mid, "http://www.vpro.nl/" + str(round(time.time())) + ".mp3", publishStop="2012-01-11T17:16:01.287Z")




