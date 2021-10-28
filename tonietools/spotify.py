import os
from typing import List

from spotdl.download.downloader import DownloadManager
from spotdl.search import song_gatherer
from spotdl.search.spotify_client import SpotifyClient

DEFAULT_SPOTIFY_ID = "5f573c9620494bae87890c0f08a60293"
DEFAULT_SPOTIFY_SECRET = "212476d9b0f3472eaa762d90b19b0ba8"


def _marshal_search_result(result: dict) -> dict:
    return {
        "title": f'{result["artists"][0]["name"]} - {result["name"]}',
        "url": result["external_urls"]["spotify"],
        "duration_seconds": result["duration_ms"] // 1000,
        "thumbnail": result["album"]["images"][0]["url"],
    }


class Spotify:
    def __init__(self):
        # From https://github.com/spotDL/spotify-downloader/blob/master/spotdl/__main__.py
        self.client = SpotifyClient.init(
            client_id=os.environ.get("SPOTIFY_ID", DEFAULT_SPOTIFY_ID),
            client_secret=os.environ.get("SPOTIFY_SECRET", DEFAULT_SPOTIFY_SECRET),
            user_auth={},
        )

    def search(self, query: str, limit: int = 5) -> List[dict]:
        results = self.client.search(query, limit=limit, type="track")["tracks"][
            "items"
        ]
        return [_marshal_search_result(r) for r in results]

    def download(self, request: str):
        with DownloadManager() as downloader:
            if "open.spotify.com" in request and "track" in request:
                song = song_gatherer.from_spotify_url(request)
                downloader.download_single_song(song)

            elif "open.spotify.com" in request and "album" in request:
                songObjList = song_gatherer.from_album(request)
                downloader.download_multiple_songs(songObjList)

            elif "open.spotify.com" in request and "playlist" in request:
                songObjList = song_gatherer.from_playlist(request)
                downloader.download_multiple_songs(songObjList)
