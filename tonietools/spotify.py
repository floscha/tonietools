import os
from pathlib import Path
from typing import List

from spotdl.download.downloader import DownloadManager
from spotdl.search.spotify_client import SpotifyClient

from tonietools.tonies_helper import get_tonies_api, upload

# from spotdl.search.song_obj import SongObj
# from spotdl.search.spotifyClient import SpotifyClient
# from spotdl.search.utils import (
#     get_playlist_tracks,
#     get_album_tracks,
# )


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
                song = SongObj.from_url(request)

                if song is not None:
                    if song.get_youtube_link() is not None:
                        downloader.download_single_song(song)
                    else:
                        print(
                            "Skipping %s (%s) as no match could be found on youtube"
                            % (song.get_song_name(), request)
                        )

            elif "open.spotify.com" in request and "album" in request:
                songObjList = get_album_tracks(request)
                downloader.download_multiple_songs(songObjList)

            elif "open.spotify.com" in request and "playlist" in request:
                songObjList = get_playlist_tracks(request)
                downloader.download_multiple_songs(songObjList)


# def sync(request: str):
#     download(request)

#     downloaded_files = Path().glob("*.mp3")
#     api = get_tonies_api()

#     for f in downloaded_files:
#         upload(api, str(f), str(f).split("- ")[1].split(".mp3")[0])
#         f.unlink()
