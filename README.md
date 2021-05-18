# :package: TonieTools
![python package](https://github.com/floscha/tonietools/actions/workflows/github-actions.yml/badge.svg)
![push to dockerhub](https://github.com/floscha/tonietools/actions/workflows/push-to-dockerhub.yml/badge.svg)

## Usage

First, build the provided Docker image:
```bash
docker build . -t tonietools
```

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
