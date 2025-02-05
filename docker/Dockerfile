FROM alpine:3.20

LABEL org.opencontainers.image.description="A alpine image containing python 3 with the pyapi library installed"

RUN apk add --no-cache --upgrade --virtual .build-deps   && \
    apk add --no-cache python3 py3-pip  && \
    apk del .build-deps && \
    ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime && \
    mkdir /work

ADD "." /checkout

ENV ENV="/root/.ashrc"

RUN   cp /checkout/docker/entrypoint.sh / && \
      cp /checkout/docker/ashrc /root/.ashrc


RUN  python3 -m venv /pyapi

RUN  source /pyapi/bin/activate && \
     pip install --upgrade pip && \
     pip install --upgrade  '/checkout' && \
     rm -rf /checkout




WORKDIR /work

ENTRYPOINT ["/entrypoint.sh"]
