.PHONY: docker docker-push
POMS=https://poms-test.omroep.nl/
RS=https://rs-test.poms.omroep.nl/v1/
PAGESPUB=https://publish-test.pages.omroep.nl/
#PAGESPUB=http://localhost:8069/

npoapi/xml/__init__.py: setup.py
	pyxbgen \
	   --schema-location=$(POMS)schema/vproMedia.xsd --module media \
	   --schema-location=$(POMS)schema/vproShared.xsd --module shared \
	   --schema-location=$(POMS)schema/update/vproMediaUpdate.xsd --module mediaupdate   \
	   --schema-location=$(POMS)schema/search/vproMediaSearch.xsd --module media_search \
	   --schema-location=$(RS)schema/urn:vpro:api:constraint:page:2013 --module api_constraint_page \
	   --schema-location=$(RS)schema/urn:vpro:pages:2013 --module page \
	   --schema-location=$(RS)schema/urn:vpro:api:constraint:2014 --module api_constraint \
	   --schema-location=$(RS)schema/urn:vpro:api:constraint:media:2013 --module api_constraint_media \
	   --schema-location=$(RS)schema/urn:vpro:pages:update:2013 --module pageupdate \
	   --schema-location=$(RS)schema/urn:vpro:api:2013 --module api \
	   --schema-location=$(RS)schema/urn:vpro:api:profile:2013 --module profile \
	   --schema-location=$(RS)schema/urn:vpro:media:subtitles:2009 --module subtitles \
	   --schema-location=$(RS)schema/urn:vpro:gtaa:2017 --module thesaurus \
	   --schema-location=$(RS)schema/combined.xsd --module poms \
	   --module-prefix=npoapi.xml

docker:
	docker build -t mihxil/npo-pyapi:alpine-latest  docker

docker-push:
	docker push mihxil/npo-pyapi:alpine-latest

clean:
	rm -rf npoapi/xml/*
