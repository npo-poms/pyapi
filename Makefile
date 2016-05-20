
POMS=http://poms-dev.omroep.nl/
PAGES=http://publish.pages.omroep.nl/

npoapi/xml/__init__.py:  
	pyxbgen \
	   --schema-location=$(POMS)schema/update/vproMediaUpdate.xsd --module=mediaupdate   \
       --schema-location=$(POMS)schema/vproMedia.xsd --module media \
       --schema-location=$(POMS)schema/vproShared.xsd --module=shared \
	   --schema-location=$(POMS)schema/combined.xsd --module poms  \
	   --schema-location=$(PAGES)schema/pages_2013.xsd --module pages \
	   --schema-location=$(PAGES)schema/urn%3Avpro%3Apages%3Aupdate%3A2013 --module pagesupdate \
	   --module-prefix=npoapi.xml

clean:
	rm npoapi/xml/*
