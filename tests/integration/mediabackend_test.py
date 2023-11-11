#!/usr/bin/env python3
import os
import time
import unittest
from xml.dom import minidom

from npoapi import MediaBackend, data


ENV = "acc"
MID = "WO_VPRO_783763"
CONFIG_DIR=os.path.dirname(os.path.dirname(__file__))
DEBUG=False


class MediaBackendTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = MediaBackend().configured_login(config_dir=CONFIG_DIR).env(ENV).debug(DEBUG)

    def test_xml_to_bytes_string(self):
        self.assertEqual("<a xmlns='urn:vpro:media:update:2009' />",
                          self.client.xml_to_bytes("<a xmlns='urn:vpro:media:update:2009' />").decode("utf-8"))

    def test_xml_to_bytes_minidom(self):
        self.assertEqual('<a xmlns="urn:vpro:media:update:2009"/>',
                          self.client.xml_to_bytes(
                              minidom.parseString("<a xmlns='urn:vpro:media:update:2009' />").documentElement).decode(
                              "utf-8"))

    def test_append_params(self):
        self.assertEqual("http://vpro.nl?a=a&x=y", self.client.append_params("http://vpro.nl", include_errors=False,  a="a", x="y"))

    def test_set_duration(self):
        existing = self.client.get_object(MID)
        existing.duration = "PT30M"
        self.client.post(existing)

    def test_get_locations(self):
        bs = self.client.get_locations(MID)
        locations_pyxb=poms.CreateFromDocument(bs)
        print(str(locations_pyxb))
        locations_xsdata=data.poms.from_bytes(bs)
        print(str(locations_xsdata))


    def test_get_segments(self):
        bytes = self.client.get("RBX_AT_2145721")
        existing = mediaupdate.CreateFromDocument(bytes)
        self.assertTrue(type(existing) == mediaupdate.segmentUpdateType)

    def test_get_images(self):
        media = poms.CreateFromDocument(self.client.get(MID))
        print(len(media.images.image))
        image = media.images.image[0] if len(media.images.image) > 0 else None
        bytes = self.client.get_images(MID)
        images = poms.CreateFromDocument(bytes)
        image2 = images.wildcardElements()[0] if len(images.wildcardElements()) > 0 else None
        self.assertEqual(image.title, image2.title)
        #self.assertEquals(image2.title, "testte")
        print(image2.toxml())

    def test_set_location(self):
        self.client.set_location(MID, "http://www.vpro.nl/123", publishStop="2012-01-11T17:16:01.287Z")

    def test_set_location_by_id(self):
        #id  = 14728807
        self.client.set_location(MID, 14728813, publishStop="2012-01-11T17:16:01.287Z")

    def test_set_location_by_id_as_string(self):
        self.client.set_location(MID, "58758190", publishStop="2013-01-11T17:16:01.287Z")

    def test_set_location_by_urn(self):
        self.client.set_location(MID, "urn:vpro:media:location:58758190", publishStop="2014-01-11T17:16:01.287Z")

    def test_create_location(self):
        self.client.set_location(MID, "http://www.vpro.nl/" + str(round(time.time())) + ".mp3", publishStop="2012-01-11T17:16:01.287Z")


