FROM python:3.8-alpine

RUN apk update \
    apk add ffmpeg

WORKDIR /opt/tonietools
COPY . .

RUN pip install -e .

ENTRYPOINT [ "tonietools" ]