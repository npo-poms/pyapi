#!/usr/bin/env python3
import unittest

from npoapi import MediaBackendUtil as MU


class Tests(unittest.TestCase):


    def test_create_image(self):
        image = MU.create_image("http://www.vpro.nl/1.jpg")
        print(image.toxml())
