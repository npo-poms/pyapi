FROM alpine:3.14
# don't upgrade alpine, we need python <= 3.9

RUN apk add --no-cache --upgrade --virtual .build-deps build-base git python3-dev cargo libffi-dev openssl-dev   && \
    apk add --no-cache  python3  py3-pip && \
    pip3 install cryptography && \
    apk del .build-deps && \
    mkdir /work

# chevron is mustache engine, used by python/vpro 
ADD "." /checkout
RUN   pip3 install --upgrade  '/checkout' && \
      pip3 install chevron && \
      cp /checkout/docker/entrypoint.sh / && \
      rm -rf /checkout

WORKDIR /work

ENTRYPOINT ["/entrypoint.sh"]
