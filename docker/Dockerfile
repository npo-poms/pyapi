FROM debian:bullseye-slim
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y git python3 python3-pip && apt-get clean && apt-get auto-remove

SHELL ["/bin/bash", "-c"]
RUN pip3 install --upgrade  'git+https://github.com/npo-poms/pyapi.git'
