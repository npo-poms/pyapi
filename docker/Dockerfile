FROM alpine:3.14

RUN apk add --no-cache --upgrade --virtual .build-deps build-base git python3-dev cargo libffi-dev openssl-dev  && \
    apk add --no-cache  python3  py3-pip && \
    pip3 install --upgrade  'git+https://github.com/npo-poms/pyapi.git' && \
    apk del .build-deps && \
    mkdir /work

COPY entrypoint.sh /
WORKDIR /work

ENTRYPOINT ["/entrypoint.sh"]
