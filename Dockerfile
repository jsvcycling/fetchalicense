FROM python:alpine

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENV FLASK_APP=fetchalicense

ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0"]
