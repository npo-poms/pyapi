#!/usr/bin/env python3

import unittest
from xmldiff import main

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from npoapi.data.api import PagesForm, PagesSearchType, TextMatcherListType, TextMatcherType


class DataTests(unittest.TestCase):
    def test_xml(self):

        form = PagesForm()
        form.searches = PagesSearchType()
        form.searches.types = TextMatcherListType()
        form.searches.types.matcher = []
        matcher = TextMatcherType()
        matcher.value = "PORTAL"
        form.searches.types.matcher.append(matcher)
        serializer = XmlSerializer(config=SerializerConfig(pretty_print = True))
        xml = serializer.render(form, ns_map={"api": 'urn:vpro:api:2013'})
        print(xml)
        self.assertEquals([],main.diff_texts("""<?xml version="1.0"?>
<api:pagesForm xmlns:api="urn:vpro:api:2013">
  <api:searches>
    <api:types>
      <api:matcher>PORTAL</api:matcher>
    </api:types>
  </api:searches>
</api:pagesForm>
        """, xml.encode("UTF-8")))






