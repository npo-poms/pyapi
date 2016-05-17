
POMS=http://poms-dev.omroep.nl/

npoapi/xml/__init__.py:  
	pyxbgen \
	   --schema-location=$(POMS)schema/update/vproMediaUpdate.xsd --module=mediaupdate   \
       --schema-location=$(POMS)schema/vproMedia.xsd --module media \
       --schema-location=$(POMS)schema/vproShared.xsd --module=shared \
	   --schema-location=$(POMS)schema/combined.xsd --module poms  \
	   --module-prefix=npoapi.xml

clean:
	rm npoapi/xml/*
