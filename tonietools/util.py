from typing import Optional

from pydub import AudioSegment


def _to_milliseconds(_str) -> int:
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


def cut_mp3(
    file_path: str, start: Optional[str] = None, end: Optional[str] = None
) -> None:
    if start is None and end is None:
        return

    start_time = _to_milliseconds(start) if start else 0
    end_time = _to_milliseconds(end) if end else None

    audio = AudioSegment.from_mp3(file_path)
    cut_audio = audio[start_time:end_time]
    cut_audio.export(file_path, format="mp3")
