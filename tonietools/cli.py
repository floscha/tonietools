from typing import Optional

import typer

from tonietools.tonies_helper import list_households, list_tonies
from tonietools.youtube_importer import import_youtube_video


app = typer.Typer()


@app.command()
def list(
    what: str,
):
    if what == "households":
        print(list_households())
    elif what == "tonies":
        list_tonies()
    else:
        raise ValueError()


@app.command()
def youtube(
    video_url: str,
    name: Optional[str] = None,
    start: Optional[str] = None,
    end: Optional[str] = None,
):
    import_youtube_video(video_url, name, start, end)


if __name__ == "__main__":
    app()
