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
docker run --rm --env-file .env --name tonietools tonietools --help
```

This assumes that you use a *.env* file containing the environmental variables as listed in the following template:
```
TONIE_MAIL=<your-mail-adress>
TONIE_PASSWORD=<your-tonies-password>
TONIE_HOUSEHOLD=<tonies-household-id>
TONIE_ID=<creative-tonie-id>
```
