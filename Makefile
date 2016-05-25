
POMS=http://poms-dev.omroep.nl/
PAGES=http://publish.pages.omroep.nl/
RS=https://rs.poms.omroep.nl/v1/


npoapi/xml/__init__.py:
	pyxbgen \
	   --schema-location=$(POMS)schema/update/vproMediaUpdate.xsd --module=mediaupdate   \
	   --schema-location=$(POMS)schema/vproMedia.xsd --module media \
	   --schema-location=$(POMS)schema/vproShared.xsd --module=shared \
	   --schema-location=$(PAGES)schema/pages_2013.xsd --module pages \
	   --schema-location=$(PAGES)schema/urn%3Avpro%3Apages%3Aupdate%3A2013 --module pagesupdate \
	   --schema-location=$(RS)schema/urn%3Avpro%3Aapi%3A2013 --module=api \
 	   --schema-location=$(RS)schema/urn%3Avpro%3Aapi%3Aprofile%3A2013 --module=profile \
	   --schema-location=combined.xsd --module poms \
	   --module-prefix=npoapi.xml



clean:
	rm -rf npoapi/xml/*
