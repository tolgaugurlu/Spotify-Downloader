"""
Lyrics providers for spotdl.
"""

from spotdl.providers.lyrics.azlyrics import AzLyrics
from spotdl.providers.lyrics.base import LyricsProvider
from spotdl.providers.lyrics.genius import Genius
from spotdl.providers.lyrics.musixmatch import MusixMatch
from spotdl.providers.lyrics.synced import Synced

__all__ = ["AzLyrics", "Genius", "MusixMatch", "Synced", "LyricsProvider"]
