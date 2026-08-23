
.PHONY: docker docker-push
.DEFAULT_GOAL:=xsdata
POMS=https://poms-test.omroep.nl/
#POMS=http://michiel.omroep.nl:8071/
RS=https://rs-test.poms.omroep.nl/v1/
#RS=http://localhost:8070/v1/
PAGESPUB=https://publish-test.pages.omroep.nl/
#PAGESPUB=http://localhost:8069/

VENV_BIN=$(shell pwd)/venv/bin
XSDATA=PATH="$(VENV_BIN):$$PATH" $(VENV_BIN)/xsdata generate




help:     ## Show this help.
	@sed -n 's/^##//p' $(MAKEFILE_LIST)
	@grep -E '^[/%a-zA-Z._-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: xsdata

xsdata: src/npoapi/data/__init__.py   ## generated xsdata files
src/npoapi/data/__init__.py: pyproject.toml Makefile src/.xsdata.xml
	(cd src ; $(XSDATA) $(RS)schema/combined.xsd)
	#hackery, but I think something's not right with the empty namespace
	git checkout  src/npoapi/__init__.py
	echo "from npoapi.data.empty import (Collection,CollectionType)" >> src/npoapi/data/__init__.py
	mv src/npoapi/data.py src/npoapi/data/empty.py

docker:   ## locally build docker image
	docker build -t mihxil/npo-pyapi:latest  -f docker/Dockerfile .

docker-make:  ## locally build docker 'make' image
	docker build -t mihxil/npo-pyapi-make:latest  docker/make

docker-flask:  ## locally build docker flask image
	docker build -t mihxil/npo-pyapi-flask:latest  flask

docker-push:  ## push image
	docker push mihxil/npo-pyapi:latest

docker-flask-push: docker-flask
	docker image push mihxil/npo-pyapi-flask:latest


clean:  # clean target
	rm -rf build

clean.data: clean  # also clean generated xsdata files
	find npoapi/data -type f -not -name 'poms.py' -delete

clean.xml: clean.model clean
	rm -rf npoapi/xml/*
