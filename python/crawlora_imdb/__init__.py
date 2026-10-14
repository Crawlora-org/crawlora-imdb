"""Typed IMDb client for the Crawlora hosted API."""

from .platform import IMDbClient, AsyncIMDbClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = IMDbClient
AsyncClient = AsyncIMDbClient
__version__ = '0.2.0'
DISPLAY_NAME = 'IMDb'
PLATFORM = 'imdb'
CONTRACT_REVISION = 'sha256:3377b774bff0bdc3a1939c8a81b9d62c3a2e846a741435145586f6cc3885396c'

__all__ = [
    "IMDbClient", "AsyncIMDbClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
