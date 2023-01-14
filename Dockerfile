FROM python:3.11.1-slim-bullseye

ADD . /plumber

RUN pip3 install -r /plumber/requirements.txt

WORKDIR /plumber/plumber

ENTRYPOINT ["python3"]