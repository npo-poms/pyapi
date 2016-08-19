#!/usr/bin/env python3
import unittest

import pyxb

from npoapi import MediaBackendUtil as MU
from npoapi.xml import media
from npoapi.xml import poms


class Tests(unittest.TestCase):


    def test_create_image(self):
        image = MU.create_image("http://www.vpro.nl/1.jpg")
        print(image.toxml())
