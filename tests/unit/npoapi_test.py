#!/usr/bin/env python3
import os
import unittest

from npoapi.npoapi import NpoApi
from npoapi.npoapi import NpoApiBase

ENV = "test"
CONFIG_DIR=os.path.dirname(os.path.dirname(__file__))
DEBUG=False


class Tests(unittest.TestCase):
    def test_authentication(self):
        client = NpoApi(origin="http://www.vpro.nl") \
            .login(key="a", secret="b")
        self.assertEqual("NPO a:CtHYR9a+nr17OIn5rYml6a+A9ujqe0IywWqr93/DAOk=",
                         client.authenticate(uri="/media", now="Fri, 30 Oct 2015 08:43:31 -0000")[0])

    def test_env(self):
        properties={'a': 'A', 'a.prod': 'Aprod', 'b': 'B', 'b.test': 'Btest'}
        client = NpoApiBase().env('test')
        settings = client._read_settings_from_properties(properties)
        self.assertEqual(settings['a'], "A")
        self.assertEqual(settings['b'], "Btest")




