.PHONY: docker docker-push
POMS=https://poms-test.omroep.nl/
RS=https://rs-test.poms.omroep.nl/v1/
PAGESPUB=https://publish-test.pages.omroep.nl/
#PAGESPUB=http://localhost:8069/

XSDATA=xsdata generate


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

.PHONY: xsdata

xsdata: npoapi/data/__init__.py
npoapi/data/__init__.py: setup.py Makefile .xsdata.xml
	$(XSDATA) $(RS)schema/combined.xsd
	#hackery, but I think something's not right with the empty namespace
	cat npoapi/__init__.py
	git checkout  npoapi/__init__.py
	echo "from npoapi.data.empty import (Collection,CollectionType)" >> npoapi/data/__init__.py
	mv npoapi/data.py npoapi/data/empty.py

docker:
	docker build -t mihxil/npo-pyapi:latest  -f docker/Dockerfile .

docker-make:
	docker build -t mihxil/npo-pyapi-make:latest  docker/make

docker-flask:
	docker build -t mihxil/npo-pyapi-flask:latest  flask

docker-push:
	docker push mihxil/npo-pyapi:latest

docker-flask-push: docker-flask
	docker image push mihxil/npo-pyapi-flask:latest


clean.data:
	rm -rf npoapi/data/*

clean: clean.model
	rm -rf npoapi/xml/*
