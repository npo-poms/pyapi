#!/usr/bin/env python3
import unittest

from npoapi import MediaBackendUtil as MU


class Tests(unittest.TestCase):


    def test_create_image(self):
        image = MU.create_image("http://www.vpro.nl/1.jpg")
        print(image.toxml())

    def test_create_image_from_file(self):

        image = MU.create_image_from_file("/tmp/still.3.jpg", title="hoi")
        print(image.toxml())

    def format_duration(self):
        duration = 1222000
        self.assertEquals("P0DT0H20M22.000S", MU.format_duration(duration))
