from pathlib import Path
from typing import Optional

import youtube_dl
from pydub import AudioSegment

from tonietools.tonies_helper import get_tonies_api, upload


def download_youtube_audio(url: str, name: str = None):
    ydl_opts = {
        "outtmpl": "%(id)s.%(ext)s",
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)
        title, file_name = result["title"], f"{result['id']}.mp3"
        ydl.download([url])

    return title, file_name


def _to_milliseconds(_str):
    _tuple = _str.split(":")
    if len(_tuple) == 1:
        hour, min, sec = 0, 0, int(_tuple[0])
    elif len(_tuple) == 2:
        hour, min, sec = 0, int(_tuple[0]), int(_tuple[1])
    elif len(_tuple) == 3:
        hour, min, sec = int(_tuple[0]), int(_tuple[1]), int(_tuple[2])
    else:
        raise ValueError("Invalid value for _tuple parameter")

    total_seconds = hour * 3600 + min * 60 + sec
    total_milliseconds = total_seconds * 1000
    return total_milliseconds


def cut_mp3(file_path: str, start: Optional[str] = None, end: Optional[str] = None):
    if start is None and end is None:
        return

    start_time = _to_milliseconds(start) if start else 0
    end_time = _to_milliseconds(end) if end else None

    audio = AudioSegment.from_mp3(file_path)
    cut_audio = audio[start_time:end_time]
    cut_audio.export(file_path, format="mp3")


def import_youtube_video(
    video_url: str, name: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None
):
    title, file_name = download_youtube_audio(video_url)
    cut_mp3(file_name, start, end)
    api = get_tonies_api()
    upload(api, file_name, name or title)
    Path(file_name).unlink()


def import_youtube_playlist():
    raise NotImplementedError()
