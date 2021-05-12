FROM python:3.8

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/tonietools
COPY . .

RUN pip install -e .

ENTRYPOINT [ "tonietools" ]