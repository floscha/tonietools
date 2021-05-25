from pathlib import Path

from spotdl.download.downloader import DownloadManager
from spotdl.search.songObj import SongObj
from spotdl.search.spotifyClient import SpotifyClient
from spotdl.search.utils import (
    get_playlist_tracks,
    get_album_tracks,
)

from tonietools.tonies_helper import get_tonies_api, upload


def download(request: str):
    # From https://github.com/spotDL/spotify-downloader/blob/master/spotdl/__main__.py
    SpotifyClient.init(
        client_id='5f573c9620494bae87890c0f08a60293',
        client_secret='212476d9b0f3472eaa762d90b19b0ba8',
        user_auth={}
    )

    with DownloadManager() as downloader:
        if 'open.spotify.com' in request and 'track' in request:
            song = SongObj.from_url(request)

            if song is not None:
                if song.get_youtube_link() is not None:
                    downloader.download_single_song(song)
                else:
                    print('Skipping %s (%s) as no match could be found on youtube' % (
                        song.get_song_name(), request
                    ))

        elif 'open.spotify.com' in request and 'album' in request:
            songObjList = get_album_tracks(request)
            downloader.download_multiple_songs(songObjList)

        elif 'open.spotify.com' in request and 'playlist' in request:
            songObjList = get_playlist_tracks(request)
            downloader.download_multiple_songs(songObjList)


def sync(request: str):
    download(request)

    downloaded_files = Path().glob("*.mp3")
    api = get_tonies_api()

    for f in downloaded_files:
        upload(api, str(f), str(f).split("- ")[1].split(".mp3")[0])
        f.unlink()