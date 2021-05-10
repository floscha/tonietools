from typing import Optional

import typer

from tonietools.youtube_importer import import_youtube_video


app = typer.Typer()


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
