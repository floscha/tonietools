import os
from typing import List, Union

import eyed3
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

    def download(self, urls: Union[str, List[str]]):
        downloaded_tracks = {}

        for url in urls:
            with DownloadManager() as downloader:
                if "open.spotify.com" in url and "track" in url:
                    song = song_gatherer.from_spotify_url(url)
                    downloader.download_single_song(song)

                    # Set title in mp3 tags
                    new_title = f"{song.contributing_artists[0]} - {song.song_name}"
                    track_file_name = f"{new_title}.mp3"
                    track = eyed3.load(track_file_name)
                    track.tag.title = new_title
                    track.tag.save()

                    downloaded_tracks[new_title] = track_file_name

                elif "open.spotify.com" in url and "album" in url:
                    raise NotImplementedError("Albums are not supported at the moment")
                    # songObjList = song_gatherer.from_album(url)
                    # downloader.download_multiple_songs(songObjList)
                elif "open.spotify.com" in url and "playlist" in url:
                    raise NotImplementedError(
                        "Playlists are not supported at the moment"
                    )
                    # songObjList = song_gatherer.from_playlist(url)
                    # downloader.download_multiple_songs(songObjList)

        return downloaded_tracks
