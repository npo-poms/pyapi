
POMS=http://poms-dev.omroep.nl/
RS=https://rs-dev.poms.omroep.nl/v1/

npoapi/xml/__init__.py:
	pyxbgen \
	   --schema-location=$(POMS)schema/vproMedia.xsd --module media \
	   --schema-location=$(POMS)schema/vproShared.xsd --module=shared \
	   --schema-location=$(POMS)schema/update/vproMediaUpdate.xsd --module=mediaupdate   \
	   --schema-location=$(RS)schema/urn:vpro:api:constraint:page:2013 --module api_constraint_page \
	   --schema-location=$(RS)schema/urn:vpro:pages:2013 --module page \
	   --schema-location=$(RS)schema/urn:vpro:api:constraint:2014 --module api_constraint \
	   --schema-location=$(RS)schema/urn:vpro:api:constraint:media:2013 --module api_constraint_media \
	   --schema-location=$(RS)schema/urn:vpro:secondscreen:2015 --module secondscreen \
	   --schema-location=$(RS)schema/urn:vpro:pages:update:2013 --module pageupdate \
	   --schema-location=$(RS)schema/urn:vpro:api:2013 --module api \
	   --schema-location=$(RS)schema/urn:vpro:api:profile:2013 --module profile \
	   --schema-location=$(RS)schema/combined.xsd --module poms \
	   --module-prefix=npoapi.xml



clean:
	rm -rf npoapi/xml/*
