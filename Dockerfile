FROM python:3.8

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/tonietools

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY static static
COPY tonietools tonietools
COPY setup.py .

RUN pip install -e .

ENTRYPOINT [ "tonietools" ]
CMD [ "server" ]