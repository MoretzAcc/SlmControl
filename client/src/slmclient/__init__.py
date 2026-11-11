"""Client API for SLM Control HEROS endpoints."""

from slmclient.client import SlmHeroApi, SlmHeroNotFoundError
from slmclient.file_util import importNpyHologram, importBmpHologram
from slmclient.bit_map_util import byteToPhase, phaseToByte
from slmclient.notebook_helpers import plotHologram
from slmclient.types import SessionStats, SlmHeroConnector
from slmclient.discover_heros import discover_slm_heros

__all__ = [
    "SessionStats",
    "SlmHeroApi",
    "SlmHeroConnector",
    "SlmHeroNotFoundError",
    "byteToPhase",
    "discover_slm_heros",
    "importBmpHologram",
    "importNpyHologram",
    "phaseToByte",
    "plotHologram",
]
