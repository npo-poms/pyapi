FROM mihxil/npo-pyapi:latest

RUN apk add --no-cache curl
RUN  pip3 install flask
ADD . /flask
WORKDIR /flask
ENV FLASK_ENV=development
ENV configdir=/flask

# look out on osx: https://developer.apple.com/forums/thread/682332 (disable sharing -> airport receiver)
EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0"]

