import os
from typing import List

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


def search(query: str, limit: int = 5) -> List[dict]:
    # From https://github.com/spotDL/spotify-downloader/blob/master/spotdl/__main__.py
    client = SpotifyClient.init(
        client_id=os.environ.get("SPOTIFY_ID", DEFAULT_SPOTIFY_ID),
        client_secret=os.environ.get("SPOTIFY_SECRET", DEFAULT_SPOTIFY_SECRET),
        user_auth={},
    )
    results = client.search(query, limit=limit, type="track")["tracks"]["items"]
    return [_marshal_search_result(r) for r in results]


if __name__ == "__main__":
    import sys
    from pprint import pprint

    pprint(search(sys.argv[1]))
