"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class IMDbClient(CrawloraClient):
    """Synchronous IMDb API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-imdb-python/0.1.0')
        super().__init__(*args, **kwargs)

    def charts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-charts', params, response_type=response_type, timeout=timeout, headers=headers)

    def image_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-image-types', params, response_type=response_type, timeout=timeout, headers=headers)

    def name(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-name', params, response_type=response_type, timeout=timeout, headers=headers)

    def name_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-name-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    def name_credits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-name-credits', params, response_type=response_type, timeout=timeout, headers=headers)

    def name_images(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-name-images', params, response_type=response_type, timeout=timeout, headers=headers)

    def name_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-name-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_title(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-search-title', params, response_type=response_type, timeout=timeout, headers=headers)

    def title(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_box_office(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-box-office', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_company_credits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-company-credits', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_connections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-connections', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_credits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-credits', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_episodes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-episodes', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_filming_locations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-filming-locations', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_goofs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-goofs', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_images(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-images', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_keywords(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-keywords', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_parental_guide(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-parental-guide', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_public_facts_analysis(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-public-facts-analysis', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_quotes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-quotes', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_ratings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-ratings', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_release_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-release-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_similar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-similar', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_technical_specs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-technical-specs', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_trivia(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-trivia', params, response_type=response_type, timeout=timeout, headers=headers)

    def title_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('imdb-title-videos', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncIMDbClient(AsyncCrawloraClient):
    """Asynchronous IMDb API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-imdb-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def charts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-charts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def image_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-image-types', params, response_type=response_type, timeout=timeout, headers=headers)

    async def name(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-name', params, response_type=response_type, timeout=timeout, headers=headers)

    async def name_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-name-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    async def name_credits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-name-credits', params, response_type=response_type, timeout=timeout, headers=headers)

    async def name_images(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-name-images', params, response_type=response_type, timeout=timeout, headers=headers)

    async def name_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-name-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_title(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-search-title', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_box_office(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-box-office', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_company_credits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-company-credits', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_connections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-connections', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_credits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-credits', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_episodes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-episodes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_filming_locations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-filming-locations', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_goofs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-goofs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_images(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-images', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_keywords(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-keywords', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_parental_guide(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-parental-guide', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_public_facts_analysis(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-public-facts-analysis', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_quotes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-quotes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_ratings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-ratings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_release_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-release-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_similar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-similar', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_technical_specs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-technical-specs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_trivia(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-trivia', params, response_type=response_type, timeout=timeout, headers=headers)

    async def title_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('imdb-title-videos', params, response_type=response_type, timeout=timeout, headers=headers)
