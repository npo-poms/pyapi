FROM alpine:3.18

RUN apk add --no-cache --upgrade --virtual .build-deps gcc build-base python3-dev cargo libffi-dev openssl-dev   && \
    apk add --no-cache git python3 py3-pip gcc && \
    pip3 install cffi && \
    apk del .build-deps && \
    mkdir /work
     
ADD "." /checkout
RUN   pip3 install --upgrade  '/checkout' && \
      cp /checkout/docker/entrypoint.sh / && \
      rm -rf /checkout

WORKDIR /work

ENTRYPOINT ["/entrypoint.sh"]
