#!/usr/bin/env python3
import unittest

from npoapi.xml import mediaupdate as U
from npoapi.xml import media

import npoapi.media_backend  

npoapi.media_backend.declare_namespaces()


class Tests(unittest.TestCase):
    def test_create(self):
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<program type="CLIP" avType="VIDEO" publishStop="2012-01-11T18:16:01.287+01:00" publishStart="2012-01-11T16:16:01.287+01:00" embeddable="true"
    xmlns="urn:vpro:media:update:2009">
  <broadcaster>VPRO</broadcaster>
  <title type="MAIN">Main title</title>
    <memberOf position="34">urn:vpro:media:group:2981744</memberOf>
    <memberOf>POMS_S_VPRO_159096</memberOf>
</program>
"""
        update = U.CreateFromDocument(xml)
        self.assertEquals(update.type, media.programTypeEnum.CLIP)
        self.assertEquals(update.title[0].value(), "Main title")
        update.duration = "PT5M"
        print(update.toxml())
        self.assertEquals(update.toxml(), """<?xml version="1.0" ?><program avType="VIDEO" embeddable="true" publishStart="2012-01-11T15:16:01.287Z" publishStop="2012-01-11T17:16:01.287Z" type="CLIP" xmlns="urn:vpro:media:update:2009"><broadcaster>VPRO</broadcaster><title type="MAIN">Main title</title><duration>PT5M</duration><memberOf position="34">urn:vpro:media:group:2981744</memberOf><memberOf>POMS_S_VPRO_159096</memberOf></program>""")

    