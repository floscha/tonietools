from typing import List, Union

import youtube_dl
from youtubesearchpython import VideosSearch


def _marshal_search_result(result: dict) -> dict:
    return {
        "title": result["title"],
        "url": result["link"],
        "duration": result["duration"],
        "thumbnail": result["thumbnails"][0]["url"],
    }


class YouTube:
    def search(self, query: str, limit: int = 5) -> List[dict]:
        results = VideosSearch(query, limit=limit).result()["result"]
        return [_marshal_search_result(r) for r in results]

    def download(self, urls: Union[str, List[str]]):
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

        downloaded_tracks = {}
        for url in urls:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(url, download=False)
                title, file_name = result["title"], f"{result['id']}.mp3"
                downloaded_tracks[title] = file_name
                ydl.download([url])

        return downloaded_tracks
