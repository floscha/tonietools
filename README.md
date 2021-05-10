# :package: TonieTools

## Setup

Best use the Python 3.8 Docker, based on Ubuntu:
```bash
docker run -it -v (pwd):/tt -p 8000:8000 -e TONIE_MAIL="<your-mail-adress>" -e TONIE_PASSWORD="<your-tonies-password>" -e TONIE_HOUSEHOLD="<tonies-household-id>" -e TONIE_ID="<creative-tonie-id>" -name tonietools python:3.8 /bin/bash
```

Then,
```bash
apt update
apt install -y ffmpeg

cd /tt
pip install -e .
```

## Usage

After running the setup described above, run `tonietools --help` to see how the CLI works.
