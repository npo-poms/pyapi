FROM mihxil/npo-pyapi:latest

RUN  pip3 install flask
ADD . /flask
WORKDIR /flask
ENV FLASK_ENV=development
EXPOSE 5000
ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0"]

