# :package: TonieTools

A handy tool to import songs from Spotify and YouTube to your Creative Tonie using a web UI or CLI.

![python package](https://github.com/floscha/tonietools/actions/workflows/github-actions.yml/badge.svg)
![push to dockerhub](https://github.com/floscha/tonietools/actions/workflows/push-to-dockerhub.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
![License](https://img.shields.io/github/license/mashape/apistatus.svg)

## Usage

### Docker

Then, run the following command to see how the CLI works:
```bash
docker run --rm --name tonietools --env-file .env tonietools --help
```

To start the web server, run
```bash
docker run --rm --name tonietools -p 8000:8000 --env-file .env tonietools
```
The web UI can then be accessed under [localhost:8000](localhost:8000).

This assumes that you use a *.env* file containing the environmental variables as listed in the following template:
```
TONIE_MAIL=<your-mail-adress>
TONIE_PASSWORD=<your-tonies-password>
TONIE_HOUSEHOLD=<tonies-household-id>
TONIE_ID=<creative-tonie-id>
```

Alternatively, you can add environmental variables to the `docker run` command individually as `-e TONIE_MAIL=<your-mail-adress>`.

### CLI

#### Spotify

`tonietools spotify <song-album-or-playlist-id>`


## Development

### Docker

Build the provided Docker image like so:
```bash
docker build . -t tonietools
```

Start a bash session in the Docker container:
```bash
docker run --rm -it --entrypoint /bin/bash --env-file .env --name tonietools tonietools
```

### No Docker

Install FFmpeg:
- OSX: `brew install ffmpeg`
- Ubuntu: `apt-get install ffmpeg`

Setup a new virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pip install -e .
```

When planning to commit to GitHub, activate pre-commit with `pre-commit install`.

To run the pre-commit hooks, use `pre-commit run --all-files`.
