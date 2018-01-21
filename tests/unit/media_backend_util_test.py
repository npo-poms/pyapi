#!/usr/bin/env python3
import unittest
import os

from npoapi import MediaBackendUtil as MU


class Tests(unittest.TestCase):


    def test_create_image(self):
        image = MU.create_image("http://www.vpro.nl/1.jpg", title="hoi")
        print(image.toxml())
        self.assertEqual("""
       <?xml version="1.0" ?><image highlighted="false" type="PICTURE" xmlns="urn:vpro:media:update:2009"><title>hoi</title><license>COPYRIGHTED</license><imageLocation><url>http://www.vpro.nl/1.jpg</url></imageLocation></image>
        """.strip(), image.toxml())

    def test_create_image_from_file(self):
        file = os.path.join(os.path.dirname(__file__), "1.gif")
        image = MU.create_image_from_file(file, title="hoi")
        self.assertEqual("""
        <?xml version="1.0" ?><image highlighted="false" type="PICTURE" xmlns="urn:vpro:media:update:2009"><title>hoi</title><license>COPYRIGHTED</license><imageData><data>R0lGODdhGAAQAKEAAP8AAP///wAA/wAAACwAAAAAGAAQAAACIISPqcvtD6OclIWLs968+w+G4kgK5omm6sq27gvH8lwAADs=</data></imageData></image>
        """.strip(), image.toxml())

    def test_format_duration(self):
        duration = 1222000
        self.assertEqual("P0DT0H20M22.000S", MU.format_duration(duration))

    def test_parse_list(self):

        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><list xmlns="urn:vpro:media:update:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009" offset="0" totalCount="5" max="200" order="ASC" size="5"><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="1" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422840" urn="urn:vpro:media:program:31357971"><broadcaster>VPRO</broadcaster><title type="MAIN">Sweaty Fingers</title><duration>P0DT0H11M53.000S</duration><memberOf position="1" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357975"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track01.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H11M53.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357976">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="2" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422839" urn="urn:vpro:media:program:31357951"><broadcaster>VPRO</broadcaster><title type="MAIN">Silver Headband</title><duration>P0DT0H8M53.000S</duration><memberOf position="2" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357955"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track02.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H8M53.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357956">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="3" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422842" urn="urn:vpro:media:program:31357990"><broadcaster>VPRO</broadcaster><title type="MAIN">Arrow\'s Myth</title><duration>P0DT0H8M49.000S</duration><memberOf position="3" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357994"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track03.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H8M49.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357995">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="4" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422843" urn="urn:vpro:media:program:31357998"><broadcaster>VPRO</broadcaster><title type="MAIN">Shikaakwa</title><duration>P0DT0H5M2.000S</duration><memberOf position="4" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31358002"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track04.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H5M2.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31358003">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="5" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422841" urn="urn:vpro:media:program:31357982"><broadcaster>VPRO</broadcaster><title type="MAIN">Slow Bern</title><duration>P0DT0H7M14.000S</duration><memberOf position="5" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357986"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track05.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H7M14.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357987">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item></list>"""
        mapped = list(MU.iterate_objects(xml))
        self.assertEqual("""
        <?xml version="1.0" ?><program avType="AUDIO" embeddable="true" mid="WO_VPRO_422840" type="TRACK" urn="urn:vpro:media:program:31357971" xmlns="urn:vpro:media:update:2009"><broadcaster>VPRO</broadcaster><title type="MAIN">Sweaty Fingers</title><duration>PT11M53S</duration><memberOf highlighted="false" position="1">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357975"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track01.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>PT11M53S</duration></location></locations><scheduleEvents/><relation broadcaster="VPRO" type="ARTIST" urn="urn:vpro:media:relation:31357976">Cave</relation><images><image highlighted="false" type="PICTURE"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></program>
        """.strip(), mapped[0].toxml(element_name="program"))


    def testStripHtml(self):
        self.assertEqual("bla", MU.strip_tags("<a>bla</a>"))
        self.assertEqual("bl&a", MU.strip_tags("<a>bl&amp;a</a>"))
        self.assertEqual("Trailer: Pather Panchali van Satyajit Ray", MU.strip_tags("Trailer: Pather Panchali van Satyajit Ray"))

    def test_segments_as_members(self):
        xml = """
        <program xmlns="urn:vpro:media:update:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009" type="BROADCAST" avType="AUDIO" embeddable="true" mid="RBX_NOS_703622" urn="urn:vpro:media:program:47853525">
<crid>crid://broadcast.radiobox2/309347</crid>
<broadcaster>NOS</broadcaster>
<title type="MAIN">NOS-Radio 1-Journaal</title>
<description type="MAIN">Nieuws en actualiteiten.</description>
<locations/>
<scheduleEvents>
<scheduleEvent channel="RAD1">
<start>2015-04-22T06:00:00.000+02:00</start>
<duration>P0DT3H0M0.000S</duration>
</scheduleEvent>
</scheduleEvents>
<images/>
<episodeOf position="1" highlighted="false">RBX_S_NOS_553954</episodeOf>
<segments>
<segment midRef="RBX_NOS_703622" avType="AUDIO" embeddable="true" mid="RBX_NOS_839624" urn="urn:vpro:media:segment:54408153">
<crid>crid://audiofragment.radiobox2/182587</crid>
<broadcaster>NOS</broadcaster>
<title type="MAIN">Actievoerende agenten rijden langzaam op snelweg</title>
<description type="MAIN">
In Groningen is de landelijke politieactie op de snelwegen begonnen. Politiewagens rijden met 60 kilometer per uur over de volle breedte van snelwegen naar het zuiden. De actie eindigt vanavond in Maastricht. Onderweg sluiten andere agenten zich vanuit het hele land bij de actie aan.De politie houdt de langzaamaanacties om aandacht te vragen voor het cao-conflict met minister Van der Steur. De agenten willen onder meer een hoger salaris. Vorige maand hielden ze al een sireneprotest.VertragingDe estafetteactie van vandaag gaat tot ongeveer 20.00 uur duren. Dan komen de laatste politiewagens in Maastricht aan.Rijkswaterstaat verwacht dat de langzaam rijdende wagens veel vertraging veroorzaken, vooral in de middag bij Rotterdam en tijdens de avondspits in Noord-Brabant.
</description>
<duration>P0DT0H3M14.000S</duration>
<locations/>
<scheduleEvents/>
<images/>
<start>P0DT0H12M44.000S</start>
</segment>
<segment midRef="RBX_NOS_703622" avType="AUDIO" embeddable="true" mid="RBX_NOS_839600" urn="urn:vpro:media:segment:54407864">
<crid>crid://audiofragment.radiobox2/182585</crid>
<broadcaster>NOS</broadcaster>
<title type="MAIN">Saudi-Arabië begint 'nieuwe fase' in Jemen</title>
<description type="MAIN">
Saudi-Arabië heeft de bombardementscampagne 'Vastbesloten Storm' in Jemen voor beëindigd verklaard. De militaire doelen van die campagne zijn bereikt, zegt de regering in Riyad. Tegelijkertijd begint een nieuwe operatie in Jemen, die de naam 'Herstel van Hoop' krijgt.Daarbij gaat het volgens het Saudische ministerie van Defensie om het regelen van evacuaties in Jemen, het voorkomen van terreinwinst van de Houthi's en de bescherming van burgers.Koning SalmanEerder vandaag maakte de Saudische koning Salman bekend dat hij de Nationale Garde in zijn land opdracht heeft gegeven deel te nemen aan de strijd in het buurland Jemen. De nationale garde staat onder rechtstreeks bevel van het Saudische koningshuis. De gardisten staan al aan de grens opgesteld. Een invasie wordt echter onwaarschijnlijk geacht.Bijna een maand heeft de Saudische luchtmacht doelen in Jemen gebombardeerd. De Saudi's kwamen in actie naar aanleiding van de opmars van Houthi-rebellen in Jemen. Die hadden de macht in de hoofdstad Sanaa al maanden geleden overgenomen en stonden op het punt ook de zuidelijke havenstad Aden in te nemen.Bij de bombardementen zijn honderden doden gevallen. Vandaag melden artsen in Jemen veertig doden bij twee aanvallen. Gisteren vielen zeker twintig doden bij Saudische luchtaanvallen.
</description>
<tag>Jemen</tag>
<duration>P0DT0H4M13.000S</duration>
<locations/>
<scheduleEvents/>
<images/>
<start>P0DT1H8M1.000S</start>
</segment>
<segment midRef="RBX_NOS_703622" avType="AUDIO" embeddable="true" mid="RBX_NOS_839602" urn="urn:vpro:media:segment:54408053">
<crid>crid://audiofragment.radiobox2/182586</crid>
<broadcaster>NOS</broadcaster>
<title type="MAIN">Nationale Ik Stap Over Van Bank week</title>
<description type="MAIN">
Het rommelt in banken-land. Na de flinke salarisverhogingen voor de top van ING en ABN Amro, blijkt dat steeds meer mensen een andere bank zoeken. En dan is het ook nog de: 'Ik stap over van Bank week'. Bijna 4.000 mensen hebben deze week gezegd over te stappen. Bert van Slooten dook in de wereld van de overstappers
</description>
<duration>P0DT0H2M49.000S</duration>
<locations/>
<scheduleEvents/>
<images/>
<start>P0DT1H20M40.000S</start>
</segment>
</segments>
</program>
        """
        print(list((MU.iterate_objects(MU.segments_as_members(xml)))))
