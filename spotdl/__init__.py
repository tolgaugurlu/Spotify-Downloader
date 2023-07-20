import asyncio
import concurrent.futures
import logging
from pathlib import Path
from typing import List, Optional, Tuple, Union

from spotdl._version import __version__
from spotdl.console import console_entry_point
from spotdl.download.downloader import Downloader
from spotdl.types.options import DownloaderOptionalOptions, DownloaderOptions
from spotdl.types.song import Song
from spotdl.utils.search import parse_query
from spotdl.utils.spotify import SpotifyClient

__all__ = ["Spotdl", "console_entry_point", "__version__"]

logger = logging.getLogger(__name__)


class Spotdl:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        user_auth: bool = False,
        cache_path: Optional[str] = None,
        no_cache: bool = False,
        headless: bool = False,
        downloader_settings: Optional[
            Union[DownloaderOptionalOptions, DownloaderOptions]
        ] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
       if downloader_settings is None:
            downloader_settings = {}

        # Initialize spotify client
        SpotifyClient.init(
            client_id=client_id,
            client_secret=client_secret,
            user_auth=user_auth,
            cache_path=cache_path,
            no_cache=no_cache,
            headless=headless,
        )

        # Initialize downloader
        self.downloader = Downloader(
            settings=downloader_settings,
            loop=loop,
        )

    def search(self, query: List[str]) -> List[Song]:
        """
        Search for songs.

        ### Arguments
        - query: List of search queries

        ### Returns
        - A list of Song objects

        ### Notes
        - query can be a list of song titles, urls, uris
        """

        return parse_query(query, self.downloader.settings["threads"])

    def get_download_urls(self, songs: List[Song]) -> List[Optional[str]]:
        """
        Get the download urls for a list of songs.

        ### Arguments
        - songs: List of Song objects

        ### Returns
        - A list of urls if successful.

        ### Notes
        - This function is multi-threaded.
        """

        urls: List[Optional[str]] = []
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.downloader.settings["threads"]
        ) as executor:
            future_to_song = {
                executor.submit(self.downloader.search, song): song for song in songs
            }
            for future in concurrent.futures.as_completed(future_to_song):
                song = future_to_song[future]
                try:
                    data = future.result()
                    urls.append(data)
                except Exception as exc:
                    logger.error("%s generated an exception: %s", song, exc)

        return urls

    def download(self, song: Song) -> Tuple[Song, Optional[Path]]:
        """
        Download and convert song to the output format.

        ### Arguments
        - song: Song object

        ### Returns
        - A tuple containing the song and the path to the downloaded file if successful.
        """

        return self.downloader.download_song(song)

    def download_songs(self, songs: List[Song]) -> List[Tuple[Song, Optional[Path]]]:
        """
        Download and convert songs to the output format.

        ### Arguments
        - songs: List of Song objects

        ### Returns
        - A list of tuples containing the song and the path to the downloaded file if successful.
        """

        return self.downloader.download_multiple_songs(songs)
