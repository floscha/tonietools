# :package: TonieTools

## Usage

First, build the provided Docker image:
```bash
docker build . -t tonietools
```

Then, run the following command to see how the CLI works:

```bash
docker run --rm --env-file .env --name tonietools tonietools --help
```

This assumes that you use an *.env* file containing the environmental variables as listed in the provided [template](.env) (make sure to remove the trailing *#* characters).