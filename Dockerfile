FROM python:3.8

# Install FFmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/tonietools

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install TonieTools
COPY tonietools tonietools
COPY setup.py .
RUN pip install -e .

# Add static web content
COPY static static
 
# Set "tonietools server" as default command
ENTRYPOINT [ "tonietools" ]
CMD [ "server" ]