

npoapi/xml/__init__.py:
	pyxbgen --schema-location=http://poms.omroep.nl/schema/update/vproMediaUpdate.xsd --module=mediaupdate   \
                --schema-location=http://poms.omroep.nl/schema/vproMedia.xsd --module media \
                --schema-location=http://poms.omroep.nl/schema/vproShared.xsd --module=shared \
		--module-prefix=npoapi.xml

clean:
	rm npoapi/xml/*
