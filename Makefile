.PHONY: docker docker-push
POMS=https://poms-test.omroep.nl/
#POMS=http://michiel.omroep.nl:8071/
RS=https://rs-test.poms.omroep.nl/v1/
#RS=http://localhost:8070/v1/
PAGESPUB=https://publish-test.pages.omroep.nl/
#PAGESPUB=http://localhost:8069/

XSDATA=xsdata generate


.PHONY: xsdata

xsdata: src/npoapi/data/__init__.py
src/npoapi/data/__init__.py: pyproject.toml Makefile src/.xsdata.xml
	(cd src ; $(XSDATA) $(RS)schema/combined.xsd)
	#hackery, but I think something's not right with the empty namespace
	git checkout  src/npoapi/__init__.py
	echo "from npoapi.data.empty import (Collection,CollectionType)" >> src/npoapi/data/__init__.py
	mv src/npoapi/data.py src/npoapi/data/empty.py

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


clean:
	rm -rf build


clean.data: clean
	find npoapi/data -type f -not -name 'poms.py' -delete
