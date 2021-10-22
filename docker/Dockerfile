FROM alpine:3.14

RUN apk add --no-cache --upgrade --virtual .build-deps build-base git python3-dev cargo libffi-dev openssl-dev py3-pip  && \
    apk add --no-cache  python3  && \
    pip3 install --upgrade  'git+https://github.com/npo-poms/pyapi.git' && \
    apk del .build-deps

