FROM debian:bullseye-slim

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y git python3 python3-pip && \
    mkdir /work

COPY inputrc /etc
RUN echo "dash dash/sh boolean false" | debconf-set-selections &&  DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash ; exit 0
RUN pip3 install --upgrade  'git+https://github.com/npo-poms/pyapi.git'

COPY entrypoint.sh /
WORKDIR /work

ENTRYPOINT ["/entrypoint.sh"]
