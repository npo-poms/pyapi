FROM alpine:3.20

LABEL org.opencontainers.image.description="A alpine image containing python 3 with the pyapi library installed"

RUN apk add --no-cache --upgrade --virtual .build-deps gcc build-base python3-dev cargo libffi-dev openssl-dev   && \
    apk add --no-cache git python3 py3-pip gcc tzdata ffmpeg mediainfo && \
    pip3 install cffi && \
    apk del .build-deps && \
    ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime && \
    mkdir /work

ADD "." /checkout
RUN   pip3 install --upgrade  '/checkout' && \
      cp /checkout/docker/entrypoint.sh / && \
      rm -rf /checkout

WORKDIR /work

ENTRYPOINT ["/entrypoint.sh"]
