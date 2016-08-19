#!/usr/bin/env python3
import unittest
import os

from npoapi import MediaBackendUtil as MU


class Tests(unittest.TestCase):


    def test_create_image(self):
        image = MU.create_image("http://www.vpro.nl/1.jpg", title="hoi")
        print(image.toxml())
        self.assertEquals("""
        <?xml version="1.0" ?><image highlighted="false" type="PICTURE" xmlns="urn:vpro:media:update:2009"><title>hoi</title><imageLocation><url>http://www.vpro.nl/1.jpg</url></imageLocation></image>
        """.strip(), image.toxml())

    def test_create_image_from_file(self):
        file = os.path.join(os.path.dirname(__file__), "1.gif")
        image = MU.create_image_from_file(file, title="hoi")
        self.assertEquals("""
        <?xml version="1.0" ?><image highlighted="false" type="PICTURE" xmlns="urn:vpro:media:update:2009"><title>hoi</title><imageData><data>R0lGODdhGAAQAKEAAP8AAP///wAA/wAAACwAAAAAGAAQAAACIISPqcvtD6OclIWLs968+w+G4kgK5omm6sq27gvH8lwAADs=</data></imageData></image>
        """.strip(), image.toxml())

    def format_duration(self):
        duration = 1222000
        self.assertEquals("P0DT0H20M22.000S", MU.format_duration(duration))
