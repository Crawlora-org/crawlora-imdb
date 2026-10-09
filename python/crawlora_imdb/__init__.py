"""Typed IMDb client for the Crawlora hosted API."""

from .platform import IMDbClient, AsyncIMDbClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = IMDbClient
AsyncClient = AsyncIMDbClient
__version__ = '0.1.1'
DISPLAY_NAME = 'IMDb'
PLATFORM = 'imdb'
CONTRACT_REVISION = 'sha256:2f96f0b8f5094ee2366e03038a2840bce6fbe2c09fb7d0ea464de89f1f42f013'

__all__ = [
    "IMDbClient", "AsyncIMDbClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
