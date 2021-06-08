# :package: TonieTools
![python package](https://github.com/floscha/tonietools/actions/workflows/github-actions.yml/badge.svg)
![push to dockerhub](https://github.com/floscha/tonietools/actions/workflows/push-to-dockerhub.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
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
