#!/usr/bin/env python3
import unittest


from npoapi.data import media
from npoapi.data import poms
from xmldiff import main

class Tests(unittest.TestCase):

    def xmlAssert(self, expected: str, real: object):
       if not isinstance(real, str):
          real = poms.to_xml(real)

       self.assertEquals([],main.diff_texts(expected.strip().encode("UTF-8"), real.encode("UTF-8")))


    def setUp(self):
        self.maxDiff = None

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
        update = poms.from_string(xml)
        self.assertEqual(update.type, media.ProgramTypeEnum.CLIP)
        self.assertEqual(update.title[0].value, "Main title")
        update.duration = "PT5M"
        self.xmlAssert("""<?xml version="1.0" encoding="UTF-8"?>
<update:program xmlns:api="urn:vpro:api:2013" xmlns:update="urn:vpro:media:update:2009" avType="VIDEO" embeddable="true" publishStart="2012-01-11T16:16:01.287+01:00" publishStop="2012-01-11T18:16:01.287+01:00" type="CLIP"><update:broadcaster>VPRO</update:broadcaster><update:title type="MAIN">Main title</update:title><update:duration>PT5M</update:duration><update:memberOf position="34" highlighted="false">urn:vpro:media:group:2981744</update:memberOf><update:memberOf highlighted="false">POMS_S_VPRO_159096</update:memberOf><update:images><update:image type="PICTURE" highlighted="false"><update:title>bla</update:title><update:urn>urn:vpro:image:496158</update:urn></update:image></update:images></update:program>""", update)

