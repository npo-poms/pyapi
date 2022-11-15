FROM mihxil/npo-pyapi:latest

RUN   apk add --no-cache git make bash gnuplot && \
      pip3 install chevron
# chevron is mustache engine, used by python/vpro \

ENTRYPOINT ["/bin/bash"]
