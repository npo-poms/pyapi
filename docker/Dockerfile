FROM alpine:3.14

RUN apk add --no-cache --upgrade --virtual .build-deps build-base git python3-dev cargo libffi-dev openssl-dev  && \
    apk add --no-cache  python3  py3-pip git && \
    pip3 install cryptography && \
    apk del .build-deps && \
    mkdir /work

ADD "." /checkout
RUN   pip3 install --upgrade  '/checkout' && \
      cp /checkout/docker/entrypoint.sh / && \
      rm -rf /checkout


WORKDIR /work

ENTRYPOINT ["/entrypoint.sh"]
