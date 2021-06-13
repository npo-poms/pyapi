ARG ARCH=
FROM ${ARG}debian:bullseye
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y git python3 python3-pip && \
    COPY inputrc /etc && \
    RUN echo "dash dash/sh boolean false" | debconf-set-selections &&  DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash ; exit 0

SHELL ["/bin/bash", "-c"]

RUN pip3 install --upgrade  'git+https://github.com/npo-poms/pyapi.git'
