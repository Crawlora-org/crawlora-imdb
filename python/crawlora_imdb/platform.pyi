from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelImdbTitleVideosResponseDoc = TypedDict('ModelImdbTitleVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbTitleVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbTitleVideosResponse = TypedDict('ModelImdbTitleVideosResponse', {
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'title': NotRequired[str],
    'total': NotRequired[int],
    'url': NotRequired[str],
    'videos': NotRequired[list[ModelImdbVideoItem]],
}, total=False)

ModelImdbVideoItem = TypedDict('ModelImdbVideoItem', {
    'content_type': NotRequired[str],
    'duration_seconds': NotRequired[int],
    'id': NotRequired[str],
    'position': NotRequired[int],
    'primary_title': NotRequired[ModelImdbVideoPrimaryTitle],
    'thumbnail': NotRequired[ModelImdbVideoThumbnail],
    'title': NotRequired[str],
}, total=False)

ModelImdbVideoThumbnail = TypedDict('ModelImdbVideoThumbnail', {
    'height': NotRequired[int],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelImdbVideoPrimaryTitle = TypedDict('ModelImdbVideoPrimaryTitle', {
    'id': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbTitlePublicFactsResponseDoc = TypedDict('ModelImdbTitlePublicFactsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbTitlePublicFactsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbTitlePublicFactsResponse = TypedDict('ModelImdbTitlePublicFactsResponse', {
    'company_credits': NotRequired[list[ModelImdbCompanySection]],
    'facts': NotRequired[list[ModelImdbPublicFactItem]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'keywords': NotRequired[list[ModelImdbKeywordItem]],
    'locations': NotRequired[list[ModelImdbLocationItem]],
    'public_page_derived': NotRequired[bool],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbLocationItem = TypedDict('ModelImdbLocationItem', {
    'location': NotRequired[str],
    'note': NotRequired[str],
    'public_signals': NotRequired[int],
}, total=False)

ModelImdbKeywordItem = TypedDict('ModelImdbKeywordItem', {
    'keyword': NotRequired[str],
    'public_signals': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelImdbPublicFactItem = TypedDict('ModelImdbPublicFactItem', {
    'category': NotRequired[str],
    'public_signals': NotRequired[int],
    'spoiler': NotRequired[bool],
    'text': NotRequired[str],
}, total=False)

ModelImdbCompanySection = TypedDict('ModelImdbCompanySection', {
    'companies': NotRequired[list[ModelImdbCompanyItem]],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelImdbCompanyItem = TypedDict('ModelImdbCompanyItem', {
    'name': NotRequired[str],
    'note': NotRequired[str],
    'public_signals': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelImdbTechnicalSpecsResponseDoc = TypedDict('ModelImdbTechnicalSpecsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbTechnicalSpecsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbTechnicalSpecsResponse = TypedDict('ModelImdbTechnicalSpecsResponse', {
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'public_page_derived': NotRequired[bool],
    'source_url': NotRequired[str],
    'specs': NotRequired[list[ModelImdbTechnicalSpecItem]],
    'url': NotRequired[str],
}, total=False)

ModelImdbTechnicalSpecItem = TypedDict('ModelImdbTechnicalSpecItem', {
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'values': NotRequired[list[str]],
}, total=False)

ModelImdbSimilarResponseDoc = TypedDict('ModelImdbSimilarResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbSimilarResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbSimilarResponse = TypedDict('ModelImdbSimilarResponse', {
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'source_url': NotRequired[str],
    'titles': NotRequired[list[ModelImdbSimilarTitle]],
    'url': NotRequired[str],
}, total=False)

ModelImdbSimilarTitle = TypedDict('ModelImdbSimilarTitle', {
    'content_rating': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'rating_count': NotRequired[int],
    'rating_value': NotRequired[float],
    'runtime_minutes': NotRequired[int],
    'title': NotRequired[str],
    'title_type': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelImdbReviewsResponseDoc = TypedDict('ModelImdbReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbReviewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbReviewsResponse = TypedDict('ModelImdbReviewsResponse', {
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'public_page_derived': NotRequired[bool],
    'reviews': NotRequired[list[ModelImdbReviewItem]],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelImdbReviewItem = TypedDict('ModelImdbReviewItem', {
    'author': NotRequired[str],
    'date': NotRequired[str],
    'helpful_votes': NotRequired[int],
    'helpfulness': NotRequired[str],
    'id': NotRequired[str],
    'public_signals': NotRequired[int],
    'rating': NotRequired[int],
    'spoiler': NotRequired[bool],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'total_votes': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelImdbReleaseInfoResponseDoc = TypedDict('ModelImdbReleaseInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbReleaseInfoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbReleaseInfoResponse = TypedDict('ModelImdbReleaseInfoResponse', {
    'alternate_titles': NotRequired[list[ModelImdbAlternateTitle]],
    'alternate_titles_total': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'public_page_derived': NotRequired[bool],
    'releases': NotRequired[list[ModelImdbReleaseInfoItem]],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelImdbReleaseInfoItem = TypedDict('ModelImdbReleaseInfoItem', {
    'country': NotRequired[str],
    'date': NotRequired[str],
    'note': NotRequired[str],
}, total=False)

ModelImdbAlternateTitle = TypedDict('ModelImdbAlternateTitle', {
    'country': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelImdbRatingsResponseDoc = TypedDict('ModelImdbRatingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbRatingsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbRatingsResponse = TypedDict('ModelImdbRatingsResponse', {
    'countries': NotRequired[list[ModelImdbRatingCountrySummary]],
    'fetched_at': NotRequired[str],
    'histogram': NotRequired[list[ModelImdbRatingHistogramBucket]],
    'id': NotRequired[str],
    'rating_count': NotRequired[int],
    'rating_value': NotRequired[float],
    'source_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbRatingHistogramBucket = TypedDict('ModelImdbRatingHistogramBucket', {
    'rating': NotRequired[int],
    'vote_count': NotRequired[int],
}, total=False)

ModelImdbRatingCountrySummary = TypedDict('ModelImdbRatingCountrySummary', {
    'aggregate': NotRequired[float],
    'country': NotRequired[str],
    'vote_count': NotRequired[int],
}, total=False)

ModelImdbTitlePublicFactsAnalysisResponseDoc = TypedDict('ModelImdbTitlePublicFactsAnalysisResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbTitlePublicFactsAnalysisResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbTitlePublicFactsAnalysisResponse = TypedDict('ModelImdbTitlePublicFactsAnalysisResponse', {
    'company_credits': NotRequired[ModelImdbTitlePublicFactsResponse],
    'filming_locations': NotRequired[ModelImdbTitlePublicFactsResponse],
    'goofs': NotRequired[ModelImdbTitlePublicFactsResponse],
    'keywords': NotRequired[ModelImdbTitlePublicFactsResponse],
    'missing_sections': NotRequired[list[str]],
    'not_viewing_advice': NotRequired[bool],
    'partial': NotRequired[bool],
    'public_page_derived': NotRequired[bool],
    'quotes': NotRequired[ModelImdbTitlePublicFactsResponse],
    'summary': NotRequired[ModelImdbPublicFactsAnalysisSummary],
    'trivia': NotRequired[ModelImdbTitlePublicFactsResponse],
}, total=False)

ModelImdbPublicFactsAnalysisSummary = TypedDict('ModelImdbPublicFactsAnalysisSummary', {
    'company_count': NotRequired[int],
    'company_section_count': NotRequired[int],
    'filming_location_count': NotRequired[int],
    'goof_count': NotRequired[int],
    'keyword_count': NotRequired[int],
    'public_fact_coverage_pages': NotRequired[int],
    'public_page_signals': NotRequired[int],
    'quote_count': NotRequired[int],
    'spoiler_fact_count': NotRequired[int],
    'trivia_count': NotRequired[int],
}, total=False)

ModelImdbParentalGuideResponseDoc = TypedDict('ModelImdbParentalGuideResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbParentalGuideResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbParentalGuideResponse = TypedDict('ModelImdbParentalGuideResponse', {
    'categories': NotRequired[list[ModelImdbParentalGuideCategory]],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'public_page_derived': NotRequired[bool],
    'source_url': NotRequired[str],
    'summary': NotRequired[ModelImdbParentalGuideSummary],
    'url': NotRequired[str],
}, total=False)

ModelImdbParentalGuideSummary = TypedDict('ModelImdbParentalGuideSummary', {
    'categories_count': NotRequired[int],
    'highest_severity': NotRequired[str],
    'item_count': NotRequired[int],
    'present_categories': NotRequired[list[str]],
    'public_page_signals': NotRequired[int],
    'severity_counts': NotRequired[dict[str, int]],
}, total=False)

ModelImdbParentalGuideCategory = TypedDict('ModelImdbParentalGuideCategory', {
    'items': NotRequired[list[str]],
    'name': NotRequired[str],
    'severity': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelImdbTitleImagesResponseDoc = TypedDict('ModelImdbTitleImagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbTitleImagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbTitleImagesResponse = TypedDict('ModelImdbTitleImagesResponse', {
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'images': NotRequired[list[ModelImdbImageItem]],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'title': NotRequired[str],
    'total': NotRequired[int],
    'type_counts': NotRequired[list[ModelImdbImageTypeCount]],
    'types': NotRequired[list[str]],
    'url': NotRequired[str],
}, total=False)

ModelImdbImageTypeCount = TypedDict('ModelImdbImageTypeCount', {
    'label': NotRequired[str],
    'total': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelImdbImageItem = TypedDict('ModelImdbImageItem', {
    'caption': NotRequired[str],
    'copyright': NotRequired[str],
    'countries': NotRequired[list[ModelImdbImageLocale]],
    'created_by': NotRequired[str],
    'created_on': NotRequired[str],
    'height': NotRequired[int],
    'id': NotRequired[str],
    'languages': NotRequired[list[ModelImdbImageLocale]],
    'names': NotRequired[list[ModelImdbImageName]],
    'position': NotRequired[int],
    'source': NotRequired[str],
    'titles': NotRequired[list[ModelImdbImageTitle]],
    'type': NotRequired[str],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelImdbImageTitle = TypedDict('ModelImdbImageTitle', {
    'id': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelImdbImageName = TypedDict('ModelImdbImageName', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbImageLocale = TypedDict('ModelImdbImageLocale', {
    'code': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelImdbEpisodesResponseDoc = TypedDict('ModelImdbEpisodesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbEpisodesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbEpisodesResponse = TypedDict('ModelImdbEpisodesResponse', {
    'episodes': NotRequired[list[ModelImdbEpisodeItem]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'public_page_derived': NotRequired[bool],
    'season': NotRequired[int],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelImdbEpisodeItem = TypedDict('ModelImdbEpisodeItem', {
    'air_date': NotRequired[str],
    'episode': NotRequired[int],
    'id': NotRequired[str],
    'plot': NotRequired[str],
    'public_signals': NotRequired[int],
    'rating_count': NotRequired[int],
    'rating_value': NotRequired[float],
    'season': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbCreditsResponseDoc = TypedDict('ModelImdbCreditsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbCreditsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbCreditsResponse = TypedDict('ModelImdbCreditsResponse', {
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'public_page_derived': NotRequired[bool],
    'sections': NotRequired[list[ModelImdbCreditSection]],
    'source_url': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbCreditSection = TypedDict('ModelImdbCreditSection', {
    'credits': NotRequired[list[ModelImdbCreditItem]],
    'has_more': NotRequired[bool],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelImdbCreditItem = TypedDict('ModelImdbCreditItem', {
    'character': NotRequired[str],
    'name': NotRequired[str],
    'role': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbTitleConnectionsResponseDoc = TypedDict('ModelImdbTitleConnectionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbTitleConnectionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbTitleConnectionsResponse = TypedDict('ModelImdbTitleConnectionsResponse', {
    'connections': NotRequired[list[ModelImdbConnectionItem]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'title': NotRequired[str],
    'total': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelImdbConnectionItem = TypedDict('ModelImdbConnectionItem', {
    'associated_title': NotRequired[ModelImdbConnectionAssociatedTitle],
    'category': NotRequired[str],
    'note': NotRequired[str],
}, total=False)

ModelImdbConnectionAssociatedTitle = TypedDict('ModelImdbConnectionAssociatedTitle', {
    'id': NotRequired[str],
    'title': NotRequired[str],
    'title_type': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelImdbTitleBoxOfficeResponseDoc = TypedDict('ModelImdbTitleBoxOfficeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbTitleBoxOfficeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbTitleBoxOfficeResponse = TypedDict('ModelImdbTitleBoxOfficeResponse', {
    'fetched_at': NotRequired[str],
    'has_box_office': NotRequired[bool],
    'id': NotRequired[str],
    'lifetime_gross': NotRequired[ModelImdbLifetimeGross],
    'opening_weekend': NotRequired[ModelImdbOpeningWeekend],
    'production_budget': NotRequired[ModelImdbMoney],
    'source_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbMoney = TypedDict('ModelImdbMoney', {
    'amount': NotRequired[int],
    'currency': NotRequired[str],
}, total=False)

ModelImdbOpeningWeekend = TypedDict('ModelImdbOpeningWeekend', {
    'gross': NotRequired[ModelImdbMoney],
    'theater_count': NotRequired[int],
    'weekend_end_date': NotRequired[str],
    'weekend_start_date': NotRequired[str],
}, total=False)

ModelImdbLifetimeGross = TypedDict('ModelImdbLifetimeGross', {
    'domestic': NotRequired[ModelImdbMoney],
    'international': NotRequired[ModelImdbMoney],
    'worldwide': NotRequired[ModelImdbMoney],
}, total=False)

ModelImdbTitleAwardsResponseDoc = TypedDict('ModelImdbTitleAwardsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbTitleAwardsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbTitleAwardsResponse = TypedDict('ModelImdbTitleAwardsResponse', {
    'awards': NotRequired[list[ModelImdbAwardItem]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'public_page_derived': NotRequired[bool],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelImdbAwardItem = TypedDict('ModelImdbAwardItem', {
    'award': NotRequired[str],
    'category': NotRequired[str],
    'event': NotRequired[str],
    'notes': NotRequired[str],
    'public_signals': NotRequired[int],
    'recipients': NotRequired[list[ModelImdbPerson]],
    'result': NotRequired[str],
    'titles': NotRequired[list[ModelImdbAwardTitle]],
    'year': NotRequired[str],
}, total=False)

ModelImdbAwardTitle = TypedDict('ModelImdbAwardTitle', {
    'id': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbPerson = TypedDict('ModelImdbPerson', {
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbTitleResponseDoc = TypedDict('ModelImdbTitleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbTitleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbTitleResponse = TypedDict('ModelImdbTitleResponse', {
    'cast': NotRequired[list[ModelImdbPerson]],
    'content_rating': NotRequired[str],
    'directors': NotRequired[list[ModelImdbPerson]],
    'fetched_at': NotRequired[str],
    'genres': NotRequired[list[str]],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'plot': NotRequired[str],
    'popularity_rank': NotRequired[int],
    'public_page_derived': NotRequired[bool],
    'rating_count': NotRequired[int],
    'rating_value': NotRequired[float],
    'release_date': NotRequired[str],
    'runtime_minutes': NotRequired[int],
    'source_url': NotRequired[str],
    'title': NotRequired[str],
    'title_type': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelImdbSearchTitleResponseDoc = TypedDict('ModelImdbSearchTitleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbSearchTitleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbSearchTitleResponse = TypedDict('ModelImdbSearchTitleResponse', {
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'results': NotRequired[list[ModelImdbSearchTitleItem]],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelImdbSearchTitleItem = TypedDict('ModelImdbSearchTitleItem', {
    'certificate': NotRequired[str],
    'genres': NotRequired[list[str]],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'metascore': NotRequired[int],
    'plot': NotRequired[str],
    'rating_count': NotRequired[int],
    'rating_value': NotRequired[float],
    'release_date': NotRequired[str],
    'runtime_minutes': NotRequired[int],
    'title': NotRequired[str],
    'title_type': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelImdbSearchResponseDoc = TypedDict('ModelImdbSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbSearchResponse = TypedDict('ModelImdbSearchResponse', {
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelImdbSearchItem]],
    'source_url': NotRequired[str],
}, total=False)

ModelImdbSearchItem = TypedDict('ModelImdbSearchItem', {
    'description': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'title': NotRequired[str],
    'title_type': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelImdbNameVideosResponseDoc = TypedDict('ModelImdbNameVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbNameVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbNameVideosResponse = TypedDict('ModelImdbNameVideosResponse', {
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'name': NotRequired[str],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'url': NotRequired[str],
    'videos': NotRequired[list[ModelImdbVideoItem]],
}, total=False)

ModelImdbNameImagesResponseDoc = TypedDict('ModelImdbNameImagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbNameImagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbNameImagesResponse = TypedDict('ModelImdbNameImagesResponse', {
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'images': NotRequired[list[ModelImdbImageItem]],
    'limit': NotRequired[int],
    'name': NotRequired[str],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'type_counts': NotRequired[list[ModelImdbImageTypeCount]],
    'types': NotRequired[list[str]],
    'url': NotRequired[str],
}, total=False)

ModelImdbNameCreditsResponseDoc = TypedDict('ModelImdbNameCreditsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbNameCreditsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbNameCreditsResponse = TypedDict('ModelImdbNameCreditsResponse', {
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'public_page_derived': NotRequired[bool],
    'sections': NotRequired[list[ModelImdbNameCreditSection]],
    'source_url': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbNameCreditSection = TypedDict('ModelImdbNameCreditSection', {
    'credits': NotRequired[list[ModelImdbNameCreditItem]],
    'has_more': NotRequired[bool],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelImdbNameCreditItem = TypedDict('ModelImdbNameCreditItem', {
    'episodes': NotRequired[str],
    'id': NotRequired[str],
    'role': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelImdbNameAwardsResponseDoc = TypedDict('ModelImdbNameAwardsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbNameAwardsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbNameAwardsResponse = TypedDict('ModelImdbNameAwardsResponse', {
    'awards': NotRequired[list[ModelImdbAwardItem]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'public_page_derived': NotRequired[bool],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelImdbNameResponseDoc = TypedDict('ModelImdbNameResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbNameResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbNameResponse = TypedDict('ModelImdbNameResponse', {
    'bio': NotRequired[str],
    'birth_date': NotRequired[str],
    'birth_place': NotRequired[str],
    'death_date': NotRequired[str],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'known_for': NotRequired[list[ModelImdbNameKnownForItem]],
    'name': NotRequired[str],
    'professions': NotRequired[list[str]],
    'public_page_derived': NotRequired[bool],
    'source_url': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelImdbNameKnownForItem = TypedDict('ModelImdbNameKnownForItem', {
    'category': NotRequired[str],
    'id': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelImdbImageTypesResponseDoc = TypedDict('ModelImdbImageTypesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbImageTypesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbImageTypesResponse = TypedDict('ModelImdbImageTypesResponse', {
    'fetched_at': NotRequired[str],
    'total': NotRequired[int],
    'types': NotRequired[list[ModelImdbImageType]],
}, total=False)

ModelImdbImageType = TypedDict('ModelImdbImageType', {
    'description': NotRequired[str],
    'label': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelImdbChartsResponseDoc = TypedDict('ModelImdbChartsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelImdbChartResponse],
    'msg': NotRequired[str],
}, total=False)

ModelImdbChartResponse = TypedDict('ModelImdbChartResponse', {
    'chart': NotRequired[str],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'titles': NotRequired[list[ModelImdbChartTitle]],
}, total=False)

ModelImdbChartTitle = TypedDict('ModelImdbChartTitle', {
    'cast': NotRequired[list[ModelImdbPerson]],
    'directors': NotRequired[list[ModelImdbPerson]],
    'id': NotRequired[str],
    'rank': NotRequired[int],
    'rating_count': NotRequired[int],
    'rating_value': NotRequired[float],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'writers': NotRequired[list[ModelImdbPerson]],
    'year': NotRequired[int],
}, total=False)

ImdbChartsResponse = ModelImdbChartsResponseDoc
ImdbChartsParams = TypedDict('ImdbChartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'chart': NotRequired[Literal['top_rated_movies', 'top_rated_tv_shows', 'most_popular_movies', 'most_popular_tv_shows', 'top_rated_english_movies', 'lowest_rated_movies']],
    'limit': NotRequired[int],
}, total=False)

ImdbImageTypesResponse = ModelImdbImageTypesResponseDoc
ImdbImageTypesParams = TypedDict('ImdbImageTypesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ImdbNameResponse = ModelImdbNameResponseDoc
ImdbNameParams = TypedDict('ImdbNameParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameAwardsResponse = ModelImdbNameAwardsResponseDoc
ImdbNameAwardsParams = TypedDict('ImdbNameAwardsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameCreditsResponse = ModelImdbNameCreditsResponseDoc
ImdbNameCreditsParams = TypedDict('ImdbNameCreditsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameImagesResponse = ModelImdbNameImagesResponseDoc
ImdbNameImagesParams = TypedDict('ImdbNameImagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'type': NotRequired[Literal['behind_the_scenes', 'event', 'poster', 'product', 'production_art', 'publicity', 'still_frame', 'unknown']],
    'limit': NotRequired[int],
}, total=False)

ImdbNameVideosResponse = ModelImdbNameVideosResponseDoc
ImdbNameVideosParams = TypedDict('ImdbNameVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbSearchResponse = ModelImdbSearchResponseDoc
ImdbSearchParams = TypedDict('ImdbSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

ImdbSearchTitleResponse = ModelImdbSearchTitleResponseDoc
ImdbSearchTitleParams = TypedDict('ImdbSearchTitleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'title': NotRequired[str],
    'title_type': NotRequired[str],
    'genres': NotRequired[str],
    'release_date_from': NotRequired[str],
    'release_date_to': NotRequired[str],
    'min_user_rating': NotRequired[float],
    'max_user_rating': NotRequired[float],
    'min_votes': NotRequired[int],
    'max_votes': NotRequired[int],
    'min_popularity': NotRequired[int],
    'max_popularity': NotRequired[int],
    'min_runtime': NotRequired[int],
    'max_runtime': NotRequired[int],
    'groups': NotRequired[str],
    'keywords': NotRequired[str],
    'companies': NotRequired[str],
    'certificates': NotRequired[str],
    'colors': NotRequired[str],
    'countries': NotRequired[str],
    'languages': NotRequired[str],
    'sound_mixes': NotRequired[str],
    'role': NotRequired[str],
    'characters': NotRequired[str],
    'plot': NotRequired[str],
    'include_adult': NotRequired[bool],
    'sort': NotRequired[str],
    'sort_order': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleResponse = ModelImdbTitleResponseDoc
ImdbTitleParams = TypedDict('ImdbTitleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleAwardsResponse = ModelImdbTitleAwardsResponseDoc
ImdbTitleAwardsParams = TypedDict('ImdbTitleAwardsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleBoxOfficeResponse = ModelImdbTitleBoxOfficeResponseDoc
ImdbTitleBoxOfficeParams = TypedDict('ImdbTitleBoxOfficeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleCompanyCreditsResponse = ModelImdbTitlePublicFactsResponseDoc
ImdbTitleCompanyCreditsParams = TypedDict('ImdbTitleCompanyCreditsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleConnectionsResponse = ModelImdbTitleConnectionsResponseDoc
ImdbTitleConnectionsParams = TypedDict('ImdbTitleConnectionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleCreditsResponse = ModelImdbCreditsResponseDoc
ImdbTitleCreditsParams = TypedDict('ImdbTitleCreditsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleEpisodesResponse = ModelImdbEpisodesResponseDoc
ImdbTitleEpisodesParams = TypedDict('ImdbTitleEpisodesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'season': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleFilmingLocationsResponse = ModelImdbTitlePublicFactsResponseDoc
ImdbTitleFilmingLocationsParams = TypedDict('ImdbTitleFilmingLocationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleGoofsResponse = ModelImdbTitlePublicFactsResponseDoc
ImdbTitleGoofsParams = TypedDict('ImdbTitleGoofsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleImagesResponse = ModelImdbTitleImagesResponseDoc
ImdbTitleImagesParams = TypedDict('ImdbTitleImagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'type': NotRequired[Literal['behind_the_scenes', 'event', 'poster', 'product', 'production_art', 'publicity', 'still_frame', 'unknown']],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleKeywordsResponse = ModelImdbTitlePublicFactsResponseDoc
ImdbTitleKeywordsParams = TypedDict('ImdbTitleKeywordsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleParentalGuideResponse = ModelImdbParentalGuideResponseDoc
ImdbTitleParentalGuideParams = TypedDict('ImdbTitleParentalGuideParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitlePublicFactsAnalysisResponse = ModelImdbTitlePublicFactsAnalysisResponseDoc
ImdbTitlePublicFactsAnalysisParams = TypedDict('ImdbTitlePublicFactsAnalysisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleQuotesResponse = ModelImdbTitlePublicFactsResponseDoc
ImdbTitleQuotesParams = TypedDict('ImdbTitleQuotesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleRatingsResponse = ModelImdbRatingsResponseDoc
ImdbTitleRatingsParams = TypedDict('ImdbTitleRatingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleReleaseInfoResponse = ModelImdbReleaseInfoResponseDoc
ImdbTitleReleaseInfoParams = TypedDict('ImdbTitleReleaseInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleReviewsResponse = ModelImdbReviewsResponseDoc
ImdbTitleReviewsParams = TypedDict('ImdbTitleReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleSimilarResponse = ModelImdbSimilarResponseDoc
ImdbTitleSimilarParams = TypedDict('ImdbTitleSimilarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleTechnicalSpecsResponse = ModelImdbTechnicalSpecsResponseDoc
ImdbTitleTechnicalSpecsParams = TypedDict('ImdbTitleTechnicalSpecsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleTriviaResponse = ModelImdbTitlePublicFactsResponseDoc
ImdbTitleTriviaParams = TypedDict('ImdbTitleTriviaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleVideosResponse = ModelImdbTitleVideosResponseDoc
ImdbTitleVideosParams = TypedDict('ImdbTitleVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

class ImdbGroup:
    @overload
    def charts(self, **params: Unpack[ImdbChartsStreamParams]) -> BinaryIO: ...
    @overload
    def charts(self, **params: Unpack[ImdbChartsTextResponseParams]) -> str: ...
    @overload
    def charts(self, **params: Unpack[ImdbChartsDefaultParams]) -> ImdbChartsResponse: ...
    @overload
    def image_types(self, **params: Unpack[ImdbImageTypesStreamParams]) -> BinaryIO: ...
    @overload
    def image_types(self, **params: Unpack[ImdbImageTypesTextResponseParams]) -> str: ...
    @overload
    def image_types(self, **params: Unpack[ImdbImageTypesDefaultParams]) -> ImdbImageTypesResponse: ...
    @overload
    def name(self, **params: Unpack[ImdbNameStreamParams]) -> BinaryIO: ...
    @overload
    def name(self, **params: Unpack[ImdbNameTextResponseParams]) -> str: ...
    @overload
    def name(self, **params: Unpack[ImdbNameDefaultParams]) -> ImdbNameResponse: ...
    @overload
    def name_awards(self, **params: Unpack[ImdbNameAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def name_awards(self, **params: Unpack[ImdbNameAwardsTextResponseParams]) -> str: ...
    @overload
    def name_awards(self, **params: Unpack[ImdbNameAwardsDefaultParams]) -> ImdbNameAwardsResponse: ...
    @overload
    def name_credits(self, **params: Unpack[ImdbNameCreditsStreamParams]) -> BinaryIO: ...
    @overload
    def name_credits(self, **params: Unpack[ImdbNameCreditsTextResponseParams]) -> str: ...
    @overload
    def name_credits(self, **params: Unpack[ImdbNameCreditsDefaultParams]) -> ImdbNameCreditsResponse: ...
    @overload
    def name_images(self, **params: Unpack[ImdbNameImagesStreamParams]) -> BinaryIO: ...
    @overload
    def name_images(self, **params: Unpack[ImdbNameImagesTextResponseParams]) -> str: ...
    @overload
    def name_images(self, **params: Unpack[ImdbNameImagesDefaultParams]) -> ImdbNameImagesResponse: ...
    @overload
    def name_videos(self, **params: Unpack[ImdbNameVideosStreamParams]) -> BinaryIO: ...
    @overload
    def name_videos(self, **params: Unpack[ImdbNameVideosTextResponseParams]) -> str: ...
    @overload
    def name_videos(self, **params: Unpack[ImdbNameVideosDefaultParams]) -> ImdbNameVideosResponse: ...
    @overload
    def search(self, **params: Unpack[ImdbSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[ImdbSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[ImdbSearchDefaultParams]) -> ImdbSearchResponse: ...
    @overload
    def search_title(self, **params: Unpack[ImdbSearchTitleStreamParams]) -> BinaryIO: ...
    @overload
    def search_title(self, **params: Unpack[ImdbSearchTitleTextResponseParams]) -> str: ...
    @overload
    def search_title(self, **params: Unpack[ImdbSearchTitleDefaultParams]) -> ImdbSearchTitleResponse: ...
    @overload
    def title(self, **params: Unpack[ImdbTitleStreamParams]) -> BinaryIO: ...
    @overload
    def title(self, **params: Unpack[ImdbTitleTextResponseParams]) -> str: ...
    @overload
    def title(self, **params: Unpack[ImdbTitleDefaultParams]) -> ImdbTitleResponse: ...
    @overload
    def title_awards(self, **params: Unpack[ImdbTitleAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def title_awards(self, **params: Unpack[ImdbTitleAwardsTextResponseParams]) -> str: ...
    @overload
    def title_awards(self, **params: Unpack[ImdbTitleAwardsDefaultParams]) -> ImdbTitleAwardsResponse: ...
    @overload
    def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeStreamParams]) -> BinaryIO: ...
    @overload
    def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeTextResponseParams]) -> str: ...
    @overload
    def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeDefaultParams]) -> ImdbTitleBoxOfficeResponse: ...
    @overload
    def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsStreamParams]) -> BinaryIO: ...
    @overload
    def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsTextResponseParams]) -> str: ...
    @overload
    def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsDefaultParams]) -> ImdbTitleCompanyCreditsResponse: ...
    @overload
    def title_connections(self, **params: Unpack[ImdbTitleConnectionsStreamParams]) -> BinaryIO: ...
    @overload
    def title_connections(self, **params: Unpack[ImdbTitleConnectionsTextResponseParams]) -> str: ...
    @overload
    def title_connections(self, **params: Unpack[ImdbTitleConnectionsDefaultParams]) -> ImdbTitleConnectionsResponse: ...
    @overload
    def title_credits(self, **params: Unpack[ImdbTitleCreditsStreamParams]) -> BinaryIO: ...
    @overload
    def title_credits(self, **params: Unpack[ImdbTitleCreditsTextResponseParams]) -> str: ...
    @overload
    def title_credits(self, **params: Unpack[ImdbTitleCreditsDefaultParams]) -> ImdbTitleCreditsResponse: ...
    @overload
    def title_episodes(self, **params: Unpack[ImdbTitleEpisodesStreamParams]) -> BinaryIO: ...
    @overload
    def title_episodes(self, **params: Unpack[ImdbTitleEpisodesTextResponseParams]) -> str: ...
    @overload
    def title_episodes(self, **params: Unpack[ImdbTitleEpisodesDefaultParams]) -> ImdbTitleEpisodesResponse: ...
    @overload
    def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsStreamParams]) -> BinaryIO: ...
    @overload
    def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsTextResponseParams]) -> str: ...
    @overload
    def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsDefaultParams]) -> ImdbTitleFilmingLocationsResponse: ...
    @overload
    def title_goofs(self, **params: Unpack[ImdbTitleGoofsStreamParams]) -> BinaryIO: ...
    @overload
    def title_goofs(self, **params: Unpack[ImdbTitleGoofsTextResponseParams]) -> str: ...
    @overload
    def title_goofs(self, **params: Unpack[ImdbTitleGoofsDefaultParams]) -> ImdbTitleGoofsResponse: ...
    @overload
    def title_images(self, **params: Unpack[ImdbTitleImagesStreamParams]) -> BinaryIO: ...
    @overload
    def title_images(self, **params: Unpack[ImdbTitleImagesTextResponseParams]) -> str: ...
    @overload
    def title_images(self, **params: Unpack[ImdbTitleImagesDefaultParams]) -> ImdbTitleImagesResponse: ...
    @overload
    def title_keywords(self, **params: Unpack[ImdbTitleKeywordsStreamParams]) -> BinaryIO: ...
    @overload
    def title_keywords(self, **params: Unpack[ImdbTitleKeywordsTextResponseParams]) -> str: ...
    @overload
    def title_keywords(self, **params: Unpack[ImdbTitleKeywordsDefaultParams]) -> ImdbTitleKeywordsResponse: ...
    @overload
    def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideStreamParams]) -> BinaryIO: ...
    @overload
    def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideTextResponseParams]) -> str: ...
    @overload
    def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideDefaultParams]) -> ImdbTitleParentalGuideResponse: ...
    @overload
    def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisStreamParams]) -> BinaryIO: ...
    @overload
    def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisTextResponseParams]) -> str: ...
    @overload
    def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisDefaultParams]) -> ImdbTitlePublicFactsAnalysisResponse: ...
    @overload
    def title_quotes(self, **params: Unpack[ImdbTitleQuotesStreamParams]) -> BinaryIO: ...
    @overload
    def title_quotes(self, **params: Unpack[ImdbTitleQuotesTextResponseParams]) -> str: ...
    @overload
    def title_quotes(self, **params: Unpack[ImdbTitleQuotesDefaultParams]) -> ImdbTitleQuotesResponse: ...
    @overload
    def title_ratings(self, **params: Unpack[ImdbTitleRatingsStreamParams]) -> BinaryIO: ...
    @overload
    def title_ratings(self, **params: Unpack[ImdbTitleRatingsTextResponseParams]) -> str: ...
    @overload
    def title_ratings(self, **params: Unpack[ImdbTitleRatingsDefaultParams]) -> ImdbTitleRatingsResponse: ...
    @overload
    def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoStreamParams]) -> BinaryIO: ...
    @overload
    def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoTextResponseParams]) -> str: ...
    @overload
    def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoDefaultParams]) -> ImdbTitleReleaseInfoResponse: ...
    @overload
    def title_reviews(self, **params: Unpack[ImdbTitleReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def title_reviews(self, **params: Unpack[ImdbTitleReviewsTextResponseParams]) -> str: ...
    @overload
    def title_reviews(self, **params: Unpack[ImdbTitleReviewsDefaultParams]) -> ImdbTitleReviewsResponse: ...
    @overload
    def title_similar(self, **params: Unpack[ImdbTitleSimilarStreamParams]) -> BinaryIO: ...
    @overload
    def title_similar(self, **params: Unpack[ImdbTitleSimilarTextResponseParams]) -> str: ...
    @overload
    def title_similar(self, **params: Unpack[ImdbTitleSimilarDefaultParams]) -> ImdbTitleSimilarResponse: ...
    @overload
    def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsStreamParams]) -> BinaryIO: ...
    @overload
    def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsTextResponseParams]) -> str: ...
    @overload
    def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsDefaultParams]) -> ImdbTitleTechnicalSpecsResponse: ...
    @overload
    def title_trivia(self, **params: Unpack[ImdbTitleTriviaStreamParams]) -> BinaryIO: ...
    @overload
    def title_trivia(self, **params: Unpack[ImdbTitleTriviaTextResponseParams]) -> str: ...
    @overload
    def title_trivia(self, **params: Unpack[ImdbTitleTriviaDefaultParams]) -> ImdbTitleTriviaResponse: ...
    @overload
    def title_videos(self, **params: Unpack[ImdbTitleVideosStreamParams]) -> BinaryIO: ...
    @overload
    def title_videos(self, **params: Unpack[ImdbTitleVideosTextResponseParams]) -> str: ...
    @overload
    def title_videos(self, **params: Unpack[ImdbTitleVideosDefaultParams]) -> ImdbTitleVideosResponse: ...

OperationId = Literal[
    'imdb-charts',
    'imdb-image-types',
    'imdb-name',
    'imdb-name-awards',
    'imdb-name-credits',
    'imdb-name-images',
    'imdb-name-videos',
    'imdb-search',
    'imdb-search-title',
    'imdb-title',
    'imdb-title-awards',
    'imdb-title-box-office',
    'imdb-title-company-credits',
    'imdb-title-connections',
    'imdb-title-credits',
    'imdb-title-episodes',
    'imdb-title-filming-locations',
    'imdb-title-goofs',
    'imdb-title-images',
    'imdb-title-keywords',
    'imdb-title-parental-guide',
    'imdb-title-public-facts-analysis',
    'imdb-title-quotes',
    'imdb-title-ratings',
    'imdb-title-release-info',
    'imdb-title-reviews',
    'imdb-title-similar',
    'imdb-title-technical-specs',
    'imdb-title-trivia',
    'imdb-title-videos',
]

class CrawloraClient:
    imdb: ImdbGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-charts'],
        params: ImdbChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbChartsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-image-types'],
        params: ImdbImageTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbImageTypesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-name'],
        params: ImdbNameParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-name-awards'],
        params: ImdbNameAwardsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameAwardsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-name-credits'],
        params: ImdbNameCreditsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameCreditsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-name-images'],
        params: ImdbNameImagesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameImagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-name-videos'],
        params: ImdbNameVideosParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-search'],
        params: ImdbSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-search-title'],
        params: ImdbSearchTitleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbSearchTitleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title'],
        params: ImdbTitleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-awards'],
        params: ImdbTitleAwardsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleAwardsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-box-office'],
        params: ImdbTitleBoxOfficeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleBoxOfficeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-company-credits'],
        params: ImdbTitleCompanyCreditsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleCompanyCreditsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-connections'],
        params: ImdbTitleConnectionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleConnectionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-credits'],
        params: ImdbTitleCreditsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleCreditsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-episodes'],
        params: ImdbTitleEpisodesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleEpisodesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-filming-locations'],
        params: ImdbTitleFilmingLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleFilmingLocationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-goofs'],
        params: ImdbTitleGoofsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleGoofsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-images'],
        params: ImdbTitleImagesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleImagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-keywords'],
        params: ImdbTitleKeywordsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleKeywordsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-parental-guide'],
        params: ImdbTitleParentalGuideParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleParentalGuideResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-public-facts-analysis'],
        params: ImdbTitlePublicFactsAnalysisParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitlePublicFactsAnalysisResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-quotes'],
        params: ImdbTitleQuotesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleQuotesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-ratings'],
        params: ImdbTitleRatingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleRatingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-release-info'],
        params: ImdbTitleReleaseInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleReleaseInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-reviews'],
        params: ImdbTitleReviewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-similar'],
        params: ImdbTitleSimilarParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleSimilarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-technical-specs'],
        params: ImdbTitleTechnicalSpecsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleTechnicalSpecsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-trivia'],
        params: ImdbTitleTriviaParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleTriviaResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['imdb-title-videos'],
        params: ImdbTitleVideosParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-charts'],
        params: ImdbChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbChartsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-image-types'],
        params: ImdbImageTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbImageTypesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-name'],
        params: ImdbNameParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-name-awards'],
        params: ImdbNameAwardsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameAwardsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-name-credits'],
        params: ImdbNameCreditsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameCreditsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-name-images'],
        params: ImdbNameImagesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameImagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-name-videos'],
        params: ImdbNameVideosParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbNameVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-search'],
        params: ImdbSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-search-title'],
        params: ImdbSearchTitleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbSearchTitleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title'],
        params: ImdbTitleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-awards'],
        params: ImdbTitleAwardsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleAwardsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-box-office'],
        params: ImdbTitleBoxOfficeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleBoxOfficeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-company-credits'],
        params: ImdbTitleCompanyCreditsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleCompanyCreditsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-connections'],
        params: ImdbTitleConnectionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleConnectionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-credits'],
        params: ImdbTitleCreditsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleCreditsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-episodes'],
        params: ImdbTitleEpisodesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleEpisodesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-filming-locations'],
        params: ImdbTitleFilmingLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleFilmingLocationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-goofs'],
        params: ImdbTitleGoofsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleGoofsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-images'],
        params: ImdbTitleImagesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleImagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-keywords'],
        params: ImdbTitleKeywordsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleKeywordsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-parental-guide'],
        params: ImdbTitleParentalGuideParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleParentalGuideResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-public-facts-analysis'],
        params: ImdbTitlePublicFactsAnalysisParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitlePublicFactsAnalysisResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-quotes'],
        params: ImdbTitleQuotesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleQuotesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-ratings'],
        params: ImdbTitleRatingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleRatingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-release-info'],
        params: ImdbTitleReleaseInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleReleaseInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-reviews'],
        params: ImdbTitleReviewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-similar'],
        params: ImdbTitleSimilarParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleSimilarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-technical-specs'],
        params: ImdbTitleTechnicalSpecsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleTechnicalSpecsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-trivia'],
        params: ImdbTitleTriviaParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleTriviaResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['imdb-title-videos'],
        params: ImdbTitleVideosParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ImdbTitleVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class IMDbClient(CrawloraClient):
    def __enter__(self) -> IMDbClient: ...
    @overload
    def charts(self, **params: Unpack[ImdbChartsStreamParams]) -> BinaryIO: ...
    @overload
    def charts(self, **params: Unpack[ImdbChartsTextResponseParams]) -> str: ...
    @overload
    def charts(self, **params: Unpack[ImdbChartsDefaultParams]) -> ImdbChartsResponse: ...
    @overload
    def image_types(self, **params: Unpack[ImdbImageTypesStreamParams]) -> BinaryIO: ...
    @overload
    def image_types(self, **params: Unpack[ImdbImageTypesTextResponseParams]) -> str: ...
    @overload
    def image_types(self, **params: Unpack[ImdbImageTypesDefaultParams]) -> ImdbImageTypesResponse: ...
    @overload
    def name(self, **params: Unpack[ImdbNameStreamParams]) -> BinaryIO: ...
    @overload
    def name(self, **params: Unpack[ImdbNameTextResponseParams]) -> str: ...
    @overload
    def name(self, **params: Unpack[ImdbNameDefaultParams]) -> ImdbNameResponse: ...
    @overload
    def name_awards(self, **params: Unpack[ImdbNameAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def name_awards(self, **params: Unpack[ImdbNameAwardsTextResponseParams]) -> str: ...
    @overload
    def name_awards(self, **params: Unpack[ImdbNameAwardsDefaultParams]) -> ImdbNameAwardsResponse: ...
    @overload
    def name_credits(self, **params: Unpack[ImdbNameCreditsStreamParams]) -> BinaryIO: ...
    @overload
    def name_credits(self, **params: Unpack[ImdbNameCreditsTextResponseParams]) -> str: ...
    @overload
    def name_credits(self, **params: Unpack[ImdbNameCreditsDefaultParams]) -> ImdbNameCreditsResponse: ...
    @overload
    def name_images(self, **params: Unpack[ImdbNameImagesStreamParams]) -> BinaryIO: ...
    @overload
    def name_images(self, **params: Unpack[ImdbNameImagesTextResponseParams]) -> str: ...
    @overload
    def name_images(self, **params: Unpack[ImdbNameImagesDefaultParams]) -> ImdbNameImagesResponse: ...
    @overload
    def name_videos(self, **params: Unpack[ImdbNameVideosStreamParams]) -> BinaryIO: ...
    @overload
    def name_videos(self, **params: Unpack[ImdbNameVideosTextResponseParams]) -> str: ...
    @overload
    def name_videos(self, **params: Unpack[ImdbNameVideosDefaultParams]) -> ImdbNameVideosResponse: ...
    @overload
    def search(self, **params: Unpack[ImdbSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[ImdbSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[ImdbSearchDefaultParams]) -> ImdbSearchResponse: ...
    @overload
    def search_title(self, **params: Unpack[ImdbSearchTitleStreamParams]) -> BinaryIO: ...
    @overload
    def search_title(self, **params: Unpack[ImdbSearchTitleTextResponseParams]) -> str: ...
    @overload
    def search_title(self, **params: Unpack[ImdbSearchTitleDefaultParams]) -> ImdbSearchTitleResponse: ...
    @overload
    def title(self, **params: Unpack[ImdbTitleStreamParams]) -> BinaryIO: ...
    @overload
    def title(self, **params: Unpack[ImdbTitleTextResponseParams]) -> str: ...
    @overload
    def title(self, **params: Unpack[ImdbTitleDefaultParams]) -> ImdbTitleResponse: ...
    @overload
    def title_awards(self, **params: Unpack[ImdbTitleAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def title_awards(self, **params: Unpack[ImdbTitleAwardsTextResponseParams]) -> str: ...
    @overload
    def title_awards(self, **params: Unpack[ImdbTitleAwardsDefaultParams]) -> ImdbTitleAwardsResponse: ...
    @overload
    def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeStreamParams]) -> BinaryIO: ...
    @overload
    def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeTextResponseParams]) -> str: ...
    @overload
    def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeDefaultParams]) -> ImdbTitleBoxOfficeResponse: ...
    @overload
    def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsStreamParams]) -> BinaryIO: ...
    @overload
    def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsTextResponseParams]) -> str: ...
    @overload
    def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsDefaultParams]) -> ImdbTitleCompanyCreditsResponse: ...
    @overload
    def title_connections(self, **params: Unpack[ImdbTitleConnectionsStreamParams]) -> BinaryIO: ...
    @overload
    def title_connections(self, **params: Unpack[ImdbTitleConnectionsTextResponseParams]) -> str: ...
    @overload
    def title_connections(self, **params: Unpack[ImdbTitleConnectionsDefaultParams]) -> ImdbTitleConnectionsResponse: ...
    @overload
    def title_credits(self, **params: Unpack[ImdbTitleCreditsStreamParams]) -> BinaryIO: ...
    @overload
    def title_credits(self, **params: Unpack[ImdbTitleCreditsTextResponseParams]) -> str: ...
    @overload
    def title_credits(self, **params: Unpack[ImdbTitleCreditsDefaultParams]) -> ImdbTitleCreditsResponse: ...
    @overload
    def title_episodes(self, **params: Unpack[ImdbTitleEpisodesStreamParams]) -> BinaryIO: ...
    @overload
    def title_episodes(self, **params: Unpack[ImdbTitleEpisodesTextResponseParams]) -> str: ...
    @overload
    def title_episodes(self, **params: Unpack[ImdbTitleEpisodesDefaultParams]) -> ImdbTitleEpisodesResponse: ...
    @overload
    def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsStreamParams]) -> BinaryIO: ...
    @overload
    def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsTextResponseParams]) -> str: ...
    @overload
    def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsDefaultParams]) -> ImdbTitleFilmingLocationsResponse: ...
    @overload
    def title_goofs(self, **params: Unpack[ImdbTitleGoofsStreamParams]) -> BinaryIO: ...
    @overload
    def title_goofs(self, **params: Unpack[ImdbTitleGoofsTextResponseParams]) -> str: ...
    @overload
    def title_goofs(self, **params: Unpack[ImdbTitleGoofsDefaultParams]) -> ImdbTitleGoofsResponse: ...
    @overload
    def title_images(self, **params: Unpack[ImdbTitleImagesStreamParams]) -> BinaryIO: ...
    @overload
    def title_images(self, **params: Unpack[ImdbTitleImagesTextResponseParams]) -> str: ...
    @overload
    def title_images(self, **params: Unpack[ImdbTitleImagesDefaultParams]) -> ImdbTitleImagesResponse: ...
    @overload
    def title_keywords(self, **params: Unpack[ImdbTitleKeywordsStreamParams]) -> BinaryIO: ...
    @overload
    def title_keywords(self, **params: Unpack[ImdbTitleKeywordsTextResponseParams]) -> str: ...
    @overload
    def title_keywords(self, **params: Unpack[ImdbTitleKeywordsDefaultParams]) -> ImdbTitleKeywordsResponse: ...
    @overload
    def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideStreamParams]) -> BinaryIO: ...
    @overload
    def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideTextResponseParams]) -> str: ...
    @overload
    def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideDefaultParams]) -> ImdbTitleParentalGuideResponse: ...
    @overload
    def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisStreamParams]) -> BinaryIO: ...
    @overload
    def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisTextResponseParams]) -> str: ...
    @overload
    def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisDefaultParams]) -> ImdbTitlePublicFactsAnalysisResponse: ...
    @overload
    def title_quotes(self, **params: Unpack[ImdbTitleQuotesStreamParams]) -> BinaryIO: ...
    @overload
    def title_quotes(self, **params: Unpack[ImdbTitleQuotesTextResponseParams]) -> str: ...
    @overload
    def title_quotes(self, **params: Unpack[ImdbTitleQuotesDefaultParams]) -> ImdbTitleQuotesResponse: ...
    @overload
    def title_ratings(self, **params: Unpack[ImdbTitleRatingsStreamParams]) -> BinaryIO: ...
    @overload
    def title_ratings(self, **params: Unpack[ImdbTitleRatingsTextResponseParams]) -> str: ...
    @overload
    def title_ratings(self, **params: Unpack[ImdbTitleRatingsDefaultParams]) -> ImdbTitleRatingsResponse: ...
    @overload
    def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoStreamParams]) -> BinaryIO: ...
    @overload
    def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoTextResponseParams]) -> str: ...
    @overload
    def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoDefaultParams]) -> ImdbTitleReleaseInfoResponse: ...
    @overload
    def title_reviews(self, **params: Unpack[ImdbTitleReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def title_reviews(self, **params: Unpack[ImdbTitleReviewsTextResponseParams]) -> str: ...
    @overload
    def title_reviews(self, **params: Unpack[ImdbTitleReviewsDefaultParams]) -> ImdbTitleReviewsResponse: ...
    @overload
    def title_similar(self, **params: Unpack[ImdbTitleSimilarStreamParams]) -> BinaryIO: ...
    @overload
    def title_similar(self, **params: Unpack[ImdbTitleSimilarTextResponseParams]) -> str: ...
    @overload
    def title_similar(self, **params: Unpack[ImdbTitleSimilarDefaultParams]) -> ImdbTitleSimilarResponse: ...
    @overload
    def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsStreamParams]) -> BinaryIO: ...
    @overload
    def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsTextResponseParams]) -> str: ...
    @overload
    def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsDefaultParams]) -> ImdbTitleTechnicalSpecsResponse: ...
    @overload
    def title_trivia(self, **params: Unpack[ImdbTitleTriviaStreamParams]) -> BinaryIO: ...
    @overload
    def title_trivia(self, **params: Unpack[ImdbTitleTriviaTextResponseParams]) -> str: ...
    @overload
    def title_trivia(self, **params: Unpack[ImdbTitleTriviaDefaultParams]) -> ImdbTitleTriviaResponse: ...
    @overload
    def title_videos(self, **params: Unpack[ImdbTitleVideosStreamParams]) -> BinaryIO: ...
    @overload
    def title_videos(self, **params: Unpack[ImdbTitleVideosTextResponseParams]) -> str: ...
    @overload
    def title_videos(self, **params: Unpack[ImdbTitleVideosDefaultParams]) -> ImdbTitleVideosResponse: ...

class AsyncIMDbClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncIMDbClient: ...
    imdb: _AsyncImdbGroup
    @overload
    async def charts(self, **params: Unpack[ImdbChartsStreamParams]) -> BinaryIO: ...
    @overload
    async def charts(self, **params: Unpack[ImdbChartsTextResponseParams]) -> str: ...
    @overload
    async def charts(self, **params: Unpack[ImdbChartsDefaultParams]) -> ImdbChartsResponse: ...
    @overload
    async def image_types(self, **params: Unpack[ImdbImageTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def image_types(self, **params: Unpack[ImdbImageTypesTextResponseParams]) -> str: ...
    @overload
    async def image_types(self, **params: Unpack[ImdbImageTypesDefaultParams]) -> ImdbImageTypesResponse: ...
    @overload
    async def name(self, **params: Unpack[ImdbNameStreamParams]) -> BinaryIO: ...
    @overload
    async def name(self, **params: Unpack[ImdbNameTextResponseParams]) -> str: ...
    @overload
    async def name(self, **params: Unpack[ImdbNameDefaultParams]) -> ImdbNameResponse: ...
    @overload
    async def name_awards(self, **params: Unpack[ImdbNameAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def name_awards(self, **params: Unpack[ImdbNameAwardsTextResponseParams]) -> str: ...
    @overload
    async def name_awards(self, **params: Unpack[ImdbNameAwardsDefaultParams]) -> ImdbNameAwardsResponse: ...
    @overload
    async def name_credits(self, **params: Unpack[ImdbNameCreditsStreamParams]) -> BinaryIO: ...
    @overload
    async def name_credits(self, **params: Unpack[ImdbNameCreditsTextResponseParams]) -> str: ...
    @overload
    async def name_credits(self, **params: Unpack[ImdbNameCreditsDefaultParams]) -> ImdbNameCreditsResponse: ...
    @overload
    async def name_images(self, **params: Unpack[ImdbNameImagesStreamParams]) -> BinaryIO: ...
    @overload
    async def name_images(self, **params: Unpack[ImdbNameImagesTextResponseParams]) -> str: ...
    @overload
    async def name_images(self, **params: Unpack[ImdbNameImagesDefaultParams]) -> ImdbNameImagesResponse: ...
    @overload
    async def name_videos(self, **params: Unpack[ImdbNameVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def name_videos(self, **params: Unpack[ImdbNameVideosTextResponseParams]) -> str: ...
    @overload
    async def name_videos(self, **params: Unpack[ImdbNameVideosDefaultParams]) -> ImdbNameVideosResponse: ...
    @overload
    async def search(self, **params: Unpack[ImdbSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[ImdbSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[ImdbSearchDefaultParams]) -> ImdbSearchResponse: ...
    @overload
    async def search_title(self, **params: Unpack[ImdbSearchTitleStreamParams]) -> BinaryIO: ...
    @overload
    async def search_title(self, **params: Unpack[ImdbSearchTitleTextResponseParams]) -> str: ...
    @overload
    async def search_title(self, **params: Unpack[ImdbSearchTitleDefaultParams]) -> ImdbSearchTitleResponse: ...
    @overload
    async def title(self, **params: Unpack[ImdbTitleStreamParams]) -> BinaryIO: ...
    @overload
    async def title(self, **params: Unpack[ImdbTitleTextResponseParams]) -> str: ...
    @overload
    async def title(self, **params: Unpack[ImdbTitleDefaultParams]) -> ImdbTitleResponse: ...
    @overload
    async def title_awards(self, **params: Unpack[ImdbTitleAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_awards(self, **params: Unpack[ImdbTitleAwardsTextResponseParams]) -> str: ...
    @overload
    async def title_awards(self, **params: Unpack[ImdbTitleAwardsDefaultParams]) -> ImdbTitleAwardsResponse: ...
    @overload
    async def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeStreamParams]) -> BinaryIO: ...
    @overload
    async def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeTextResponseParams]) -> str: ...
    @overload
    async def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeDefaultParams]) -> ImdbTitleBoxOfficeResponse: ...
    @overload
    async def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsTextResponseParams]) -> str: ...
    @overload
    async def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsDefaultParams]) -> ImdbTitleCompanyCreditsResponse: ...
    @overload
    async def title_connections(self, **params: Unpack[ImdbTitleConnectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_connections(self, **params: Unpack[ImdbTitleConnectionsTextResponseParams]) -> str: ...
    @overload
    async def title_connections(self, **params: Unpack[ImdbTitleConnectionsDefaultParams]) -> ImdbTitleConnectionsResponse: ...
    @overload
    async def title_credits(self, **params: Unpack[ImdbTitleCreditsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_credits(self, **params: Unpack[ImdbTitleCreditsTextResponseParams]) -> str: ...
    @overload
    async def title_credits(self, **params: Unpack[ImdbTitleCreditsDefaultParams]) -> ImdbTitleCreditsResponse: ...
    @overload
    async def title_episodes(self, **params: Unpack[ImdbTitleEpisodesStreamParams]) -> BinaryIO: ...
    @overload
    async def title_episodes(self, **params: Unpack[ImdbTitleEpisodesTextResponseParams]) -> str: ...
    @overload
    async def title_episodes(self, **params: Unpack[ImdbTitleEpisodesDefaultParams]) -> ImdbTitleEpisodesResponse: ...
    @overload
    async def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsTextResponseParams]) -> str: ...
    @overload
    async def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsDefaultParams]) -> ImdbTitleFilmingLocationsResponse: ...
    @overload
    async def title_goofs(self, **params: Unpack[ImdbTitleGoofsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_goofs(self, **params: Unpack[ImdbTitleGoofsTextResponseParams]) -> str: ...
    @overload
    async def title_goofs(self, **params: Unpack[ImdbTitleGoofsDefaultParams]) -> ImdbTitleGoofsResponse: ...
    @overload
    async def title_images(self, **params: Unpack[ImdbTitleImagesStreamParams]) -> BinaryIO: ...
    @overload
    async def title_images(self, **params: Unpack[ImdbTitleImagesTextResponseParams]) -> str: ...
    @overload
    async def title_images(self, **params: Unpack[ImdbTitleImagesDefaultParams]) -> ImdbTitleImagesResponse: ...
    @overload
    async def title_keywords(self, **params: Unpack[ImdbTitleKeywordsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_keywords(self, **params: Unpack[ImdbTitleKeywordsTextResponseParams]) -> str: ...
    @overload
    async def title_keywords(self, **params: Unpack[ImdbTitleKeywordsDefaultParams]) -> ImdbTitleKeywordsResponse: ...
    @overload
    async def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideStreamParams]) -> BinaryIO: ...
    @overload
    async def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideTextResponseParams]) -> str: ...
    @overload
    async def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideDefaultParams]) -> ImdbTitleParentalGuideResponse: ...
    @overload
    async def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisStreamParams]) -> BinaryIO: ...
    @overload
    async def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisTextResponseParams]) -> str: ...
    @overload
    async def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisDefaultParams]) -> ImdbTitlePublicFactsAnalysisResponse: ...
    @overload
    async def title_quotes(self, **params: Unpack[ImdbTitleQuotesStreamParams]) -> BinaryIO: ...
    @overload
    async def title_quotes(self, **params: Unpack[ImdbTitleQuotesTextResponseParams]) -> str: ...
    @overload
    async def title_quotes(self, **params: Unpack[ImdbTitleQuotesDefaultParams]) -> ImdbTitleQuotesResponse: ...
    @overload
    async def title_ratings(self, **params: Unpack[ImdbTitleRatingsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_ratings(self, **params: Unpack[ImdbTitleRatingsTextResponseParams]) -> str: ...
    @overload
    async def title_ratings(self, **params: Unpack[ImdbTitleRatingsDefaultParams]) -> ImdbTitleRatingsResponse: ...
    @overload
    async def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoTextResponseParams]) -> str: ...
    @overload
    async def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoDefaultParams]) -> ImdbTitleReleaseInfoResponse: ...
    @overload
    async def title_reviews(self, **params: Unpack[ImdbTitleReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_reviews(self, **params: Unpack[ImdbTitleReviewsTextResponseParams]) -> str: ...
    @overload
    async def title_reviews(self, **params: Unpack[ImdbTitleReviewsDefaultParams]) -> ImdbTitleReviewsResponse: ...
    @overload
    async def title_similar(self, **params: Unpack[ImdbTitleSimilarStreamParams]) -> BinaryIO: ...
    @overload
    async def title_similar(self, **params: Unpack[ImdbTitleSimilarTextResponseParams]) -> str: ...
    @overload
    async def title_similar(self, **params: Unpack[ImdbTitleSimilarDefaultParams]) -> ImdbTitleSimilarResponse: ...
    @overload
    async def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsTextResponseParams]) -> str: ...
    @overload
    async def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsDefaultParams]) -> ImdbTitleTechnicalSpecsResponse: ...
    @overload
    async def title_trivia(self, **params: Unpack[ImdbTitleTriviaStreamParams]) -> BinaryIO: ...
    @overload
    async def title_trivia(self, **params: Unpack[ImdbTitleTriviaTextResponseParams]) -> str: ...
    @overload
    async def title_trivia(self, **params: Unpack[ImdbTitleTriviaDefaultParams]) -> ImdbTitleTriviaResponse: ...
    @overload
    async def title_videos(self, **params: Unpack[ImdbTitleVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def title_videos(self, **params: Unpack[ImdbTitleVideosTextResponseParams]) -> str: ...
    @overload
    async def title_videos(self, **params: Unpack[ImdbTitleVideosDefaultParams]) -> ImdbTitleVideosResponse: ...

class _AsyncImdbGroup:
    @overload
    async def charts(self, **params: Unpack[ImdbChartsStreamParams]) -> BinaryIO: ...
    @overload
    async def charts(self, **params: Unpack[ImdbChartsTextResponseParams]) -> str: ...
    @overload
    async def charts(self, **params: Unpack[ImdbChartsDefaultParams]) -> ImdbChartsResponse: ...
    @overload
    async def image_types(self, **params: Unpack[ImdbImageTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def image_types(self, **params: Unpack[ImdbImageTypesTextResponseParams]) -> str: ...
    @overload
    async def image_types(self, **params: Unpack[ImdbImageTypesDefaultParams]) -> ImdbImageTypesResponse: ...
    @overload
    async def name(self, **params: Unpack[ImdbNameStreamParams]) -> BinaryIO: ...
    @overload
    async def name(self, **params: Unpack[ImdbNameTextResponseParams]) -> str: ...
    @overload
    async def name(self, **params: Unpack[ImdbNameDefaultParams]) -> ImdbNameResponse: ...
    @overload
    async def name_awards(self, **params: Unpack[ImdbNameAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def name_awards(self, **params: Unpack[ImdbNameAwardsTextResponseParams]) -> str: ...
    @overload
    async def name_awards(self, **params: Unpack[ImdbNameAwardsDefaultParams]) -> ImdbNameAwardsResponse: ...
    @overload
    async def name_credits(self, **params: Unpack[ImdbNameCreditsStreamParams]) -> BinaryIO: ...
    @overload
    async def name_credits(self, **params: Unpack[ImdbNameCreditsTextResponseParams]) -> str: ...
    @overload
    async def name_credits(self, **params: Unpack[ImdbNameCreditsDefaultParams]) -> ImdbNameCreditsResponse: ...
    @overload
    async def name_images(self, **params: Unpack[ImdbNameImagesStreamParams]) -> BinaryIO: ...
    @overload
    async def name_images(self, **params: Unpack[ImdbNameImagesTextResponseParams]) -> str: ...
    @overload
    async def name_images(self, **params: Unpack[ImdbNameImagesDefaultParams]) -> ImdbNameImagesResponse: ...
    @overload
    async def name_videos(self, **params: Unpack[ImdbNameVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def name_videos(self, **params: Unpack[ImdbNameVideosTextResponseParams]) -> str: ...
    @overload
    async def name_videos(self, **params: Unpack[ImdbNameVideosDefaultParams]) -> ImdbNameVideosResponse: ...
    @overload
    async def search(self, **params: Unpack[ImdbSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[ImdbSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[ImdbSearchDefaultParams]) -> ImdbSearchResponse: ...
    @overload
    async def search_title(self, **params: Unpack[ImdbSearchTitleStreamParams]) -> BinaryIO: ...
    @overload
    async def search_title(self, **params: Unpack[ImdbSearchTitleTextResponseParams]) -> str: ...
    @overload
    async def search_title(self, **params: Unpack[ImdbSearchTitleDefaultParams]) -> ImdbSearchTitleResponse: ...
    @overload
    async def title(self, **params: Unpack[ImdbTitleStreamParams]) -> BinaryIO: ...
    @overload
    async def title(self, **params: Unpack[ImdbTitleTextResponseParams]) -> str: ...
    @overload
    async def title(self, **params: Unpack[ImdbTitleDefaultParams]) -> ImdbTitleResponse: ...
    @overload
    async def title_awards(self, **params: Unpack[ImdbTitleAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_awards(self, **params: Unpack[ImdbTitleAwardsTextResponseParams]) -> str: ...
    @overload
    async def title_awards(self, **params: Unpack[ImdbTitleAwardsDefaultParams]) -> ImdbTitleAwardsResponse: ...
    @overload
    async def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeStreamParams]) -> BinaryIO: ...
    @overload
    async def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeTextResponseParams]) -> str: ...
    @overload
    async def title_box_office(self, **params: Unpack[ImdbTitleBoxOfficeDefaultParams]) -> ImdbTitleBoxOfficeResponse: ...
    @overload
    async def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsTextResponseParams]) -> str: ...
    @overload
    async def title_company_credits(self, **params: Unpack[ImdbTitleCompanyCreditsDefaultParams]) -> ImdbTitleCompanyCreditsResponse: ...
    @overload
    async def title_connections(self, **params: Unpack[ImdbTitleConnectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_connections(self, **params: Unpack[ImdbTitleConnectionsTextResponseParams]) -> str: ...
    @overload
    async def title_connections(self, **params: Unpack[ImdbTitleConnectionsDefaultParams]) -> ImdbTitleConnectionsResponse: ...
    @overload
    async def title_credits(self, **params: Unpack[ImdbTitleCreditsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_credits(self, **params: Unpack[ImdbTitleCreditsTextResponseParams]) -> str: ...
    @overload
    async def title_credits(self, **params: Unpack[ImdbTitleCreditsDefaultParams]) -> ImdbTitleCreditsResponse: ...
    @overload
    async def title_episodes(self, **params: Unpack[ImdbTitleEpisodesStreamParams]) -> BinaryIO: ...
    @overload
    async def title_episodes(self, **params: Unpack[ImdbTitleEpisodesTextResponseParams]) -> str: ...
    @overload
    async def title_episodes(self, **params: Unpack[ImdbTitleEpisodesDefaultParams]) -> ImdbTitleEpisodesResponse: ...
    @overload
    async def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsTextResponseParams]) -> str: ...
    @overload
    async def title_filming_locations(self, **params: Unpack[ImdbTitleFilmingLocationsDefaultParams]) -> ImdbTitleFilmingLocationsResponse: ...
    @overload
    async def title_goofs(self, **params: Unpack[ImdbTitleGoofsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_goofs(self, **params: Unpack[ImdbTitleGoofsTextResponseParams]) -> str: ...
    @overload
    async def title_goofs(self, **params: Unpack[ImdbTitleGoofsDefaultParams]) -> ImdbTitleGoofsResponse: ...
    @overload
    async def title_images(self, **params: Unpack[ImdbTitleImagesStreamParams]) -> BinaryIO: ...
    @overload
    async def title_images(self, **params: Unpack[ImdbTitleImagesTextResponseParams]) -> str: ...
    @overload
    async def title_images(self, **params: Unpack[ImdbTitleImagesDefaultParams]) -> ImdbTitleImagesResponse: ...
    @overload
    async def title_keywords(self, **params: Unpack[ImdbTitleKeywordsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_keywords(self, **params: Unpack[ImdbTitleKeywordsTextResponseParams]) -> str: ...
    @overload
    async def title_keywords(self, **params: Unpack[ImdbTitleKeywordsDefaultParams]) -> ImdbTitleKeywordsResponse: ...
    @overload
    async def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideStreamParams]) -> BinaryIO: ...
    @overload
    async def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideTextResponseParams]) -> str: ...
    @overload
    async def title_parental_guide(self, **params: Unpack[ImdbTitleParentalGuideDefaultParams]) -> ImdbTitleParentalGuideResponse: ...
    @overload
    async def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisStreamParams]) -> BinaryIO: ...
    @overload
    async def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisTextResponseParams]) -> str: ...
    @overload
    async def title_public_facts_analysis(self, **params: Unpack[ImdbTitlePublicFactsAnalysisDefaultParams]) -> ImdbTitlePublicFactsAnalysisResponse: ...
    @overload
    async def title_quotes(self, **params: Unpack[ImdbTitleQuotesStreamParams]) -> BinaryIO: ...
    @overload
    async def title_quotes(self, **params: Unpack[ImdbTitleQuotesTextResponseParams]) -> str: ...
    @overload
    async def title_quotes(self, **params: Unpack[ImdbTitleQuotesDefaultParams]) -> ImdbTitleQuotesResponse: ...
    @overload
    async def title_ratings(self, **params: Unpack[ImdbTitleRatingsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_ratings(self, **params: Unpack[ImdbTitleRatingsTextResponseParams]) -> str: ...
    @overload
    async def title_ratings(self, **params: Unpack[ImdbTitleRatingsDefaultParams]) -> ImdbTitleRatingsResponse: ...
    @overload
    async def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoTextResponseParams]) -> str: ...
    @overload
    async def title_release_info(self, **params: Unpack[ImdbTitleReleaseInfoDefaultParams]) -> ImdbTitleReleaseInfoResponse: ...
    @overload
    async def title_reviews(self, **params: Unpack[ImdbTitleReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_reviews(self, **params: Unpack[ImdbTitleReviewsTextResponseParams]) -> str: ...
    @overload
    async def title_reviews(self, **params: Unpack[ImdbTitleReviewsDefaultParams]) -> ImdbTitleReviewsResponse: ...
    @overload
    async def title_similar(self, **params: Unpack[ImdbTitleSimilarStreamParams]) -> BinaryIO: ...
    @overload
    async def title_similar(self, **params: Unpack[ImdbTitleSimilarTextResponseParams]) -> str: ...
    @overload
    async def title_similar(self, **params: Unpack[ImdbTitleSimilarDefaultParams]) -> ImdbTitleSimilarResponse: ...
    @overload
    async def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsStreamParams]) -> BinaryIO: ...
    @overload
    async def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsTextResponseParams]) -> str: ...
    @overload
    async def title_technical_specs(self, **params: Unpack[ImdbTitleTechnicalSpecsDefaultParams]) -> ImdbTitleTechnicalSpecsResponse: ...
    @overload
    async def title_trivia(self, **params: Unpack[ImdbTitleTriviaStreamParams]) -> BinaryIO: ...
    @overload
    async def title_trivia(self, **params: Unpack[ImdbTitleTriviaTextResponseParams]) -> str: ...
    @overload
    async def title_trivia(self, **params: Unpack[ImdbTitleTriviaDefaultParams]) -> ImdbTitleTriviaResponse: ...
    @overload
    async def title_videos(self, **params: Unpack[ImdbTitleVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def title_videos(self, **params: Unpack[ImdbTitleVideosTextResponseParams]) -> str: ...
    @overload
    async def title_videos(self, **params: Unpack[ImdbTitleVideosDefaultParams]) -> ImdbTitleVideosResponse: ...

ImdbChartsDefaultParams = TypedDict('ImdbChartsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'chart': NotRequired[Literal['top_rated_movies', 'top_rated_tv_shows', 'most_popular_movies', 'most_popular_tv_shows', 'top_rated_english_movies', 'lowest_rated_movies']],
    'limit': NotRequired[int],
}, total=False)

ImdbChartsTextResponseParams = TypedDict('ImdbChartsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'chart': NotRequired[Literal['top_rated_movies', 'top_rated_tv_shows', 'most_popular_movies', 'most_popular_tv_shows', 'top_rated_english_movies', 'lowest_rated_movies']],
    'limit': NotRequired[int],
}, total=False)

ImdbChartsStreamParams = TypedDict('ImdbChartsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'chart': NotRequired[Literal['top_rated_movies', 'top_rated_tv_shows', 'most_popular_movies', 'most_popular_tv_shows', 'top_rated_english_movies', 'lowest_rated_movies']],
    'limit': NotRequired[int],
}, total=False)

ImdbImageTypesDefaultParams = TypedDict('ImdbImageTypesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

ImdbImageTypesTextResponseParams = TypedDict('ImdbImageTypesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

ImdbImageTypesStreamParams = TypedDict('ImdbImageTypesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

ImdbNameDefaultParams = TypedDict('ImdbNameDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameTextResponseParams = TypedDict('ImdbNameTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameStreamParams = TypedDict('ImdbNameStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameAwardsDefaultParams = TypedDict('ImdbNameAwardsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameAwardsTextResponseParams = TypedDict('ImdbNameAwardsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameAwardsStreamParams = TypedDict('ImdbNameAwardsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameCreditsDefaultParams = TypedDict('ImdbNameCreditsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameCreditsTextResponseParams = TypedDict('ImdbNameCreditsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameCreditsStreamParams = TypedDict('ImdbNameCreditsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbNameImagesDefaultParams = TypedDict('ImdbNameImagesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'type': NotRequired[Literal['behind_the_scenes', 'event', 'poster', 'product', 'production_art', 'publicity', 'still_frame', 'unknown']],
    'limit': NotRequired[int],
}, total=False)

ImdbNameImagesTextResponseParams = TypedDict('ImdbNameImagesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'type': NotRequired[Literal['behind_the_scenes', 'event', 'poster', 'product', 'production_art', 'publicity', 'still_frame', 'unknown']],
    'limit': NotRequired[int],
}, total=False)

ImdbNameImagesStreamParams = TypedDict('ImdbNameImagesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'type': NotRequired[Literal['behind_the_scenes', 'event', 'poster', 'product', 'production_art', 'publicity', 'still_frame', 'unknown']],
    'limit': NotRequired[int],
}, total=False)

ImdbNameVideosDefaultParams = TypedDict('ImdbNameVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbNameVideosTextResponseParams = TypedDict('ImdbNameVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbNameVideosStreamParams = TypedDict('ImdbNameVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbSearchDefaultParams = TypedDict('ImdbSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

ImdbSearchTextResponseParams = TypedDict('ImdbSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

ImdbSearchStreamParams = TypedDict('ImdbSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

ImdbSearchTitleDefaultParams = TypedDict('ImdbSearchTitleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'title': NotRequired[str],
    'title_type': NotRequired[str],
    'genres': NotRequired[str],
    'release_date_from': NotRequired[str],
    'release_date_to': NotRequired[str],
    'min_user_rating': NotRequired[float],
    'max_user_rating': NotRequired[float],
    'min_votes': NotRequired[int],
    'max_votes': NotRequired[int],
    'min_popularity': NotRequired[int],
    'max_popularity': NotRequired[int],
    'min_runtime': NotRequired[int],
    'max_runtime': NotRequired[int],
    'groups': NotRequired[str],
    'keywords': NotRequired[str],
    'companies': NotRequired[str],
    'certificates': NotRequired[str],
    'colors': NotRequired[str],
    'countries': NotRequired[str],
    'languages': NotRequired[str],
    'sound_mixes': NotRequired[str],
    'role': NotRequired[str],
    'characters': NotRequired[str],
    'plot': NotRequired[str],
    'include_adult': NotRequired[bool],
    'sort': NotRequired[str],
    'sort_order': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbSearchTitleTextResponseParams = TypedDict('ImdbSearchTitleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'title': NotRequired[str],
    'title_type': NotRequired[str],
    'genres': NotRequired[str],
    'release_date_from': NotRequired[str],
    'release_date_to': NotRequired[str],
    'min_user_rating': NotRequired[float],
    'max_user_rating': NotRequired[float],
    'min_votes': NotRequired[int],
    'max_votes': NotRequired[int],
    'min_popularity': NotRequired[int],
    'max_popularity': NotRequired[int],
    'min_runtime': NotRequired[int],
    'max_runtime': NotRequired[int],
    'groups': NotRequired[str],
    'keywords': NotRequired[str],
    'companies': NotRequired[str],
    'certificates': NotRequired[str],
    'colors': NotRequired[str],
    'countries': NotRequired[str],
    'languages': NotRequired[str],
    'sound_mixes': NotRequired[str],
    'role': NotRequired[str],
    'characters': NotRequired[str],
    'plot': NotRequired[str],
    'include_adult': NotRequired[bool],
    'sort': NotRequired[str],
    'sort_order': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbSearchTitleStreamParams = TypedDict('ImdbSearchTitleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'title': NotRequired[str],
    'title_type': NotRequired[str],
    'genres': NotRequired[str],
    'release_date_from': NotRequired[str],
    'release_date_to': NotRequired[str],
    'min_user_rating': NotRequired[float],
    'max_user_rating': NotRequired[float],
    'min_votes': NotRequired[int],
    'max_votes': NotRequired[int],
    'min_popularity': NotRequired[int],
    'max_popularity': NotRequired[int],
    'min_runtime': NotRequired[int],
    'max_runtime': NotRequired[int],
    'groups': NotRequired[str],
    'keywords': NotRequired[str],
    'companies': NotRequired[str],
    'certificates': NotRequired[str],
    'colors': NotRequired[str],
    'countries': NotRequired[str],
    'languages': NotRequired[str],
    'sound_mixes': NotRequired[str],
    'role': NotRequired[str],
    'characters': NotRequired[str],
    'plot': NotRequired[str],
    'include_adult': NotRequired[bool],
    'sort': NotRequired[str],
    'sort_order': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleDefaultParams = TypedDict('ImdbTitleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleTextResponseParams = TypedDict('ImdbTitleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleStreamParams = TypedDict('ImdbTitleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleAwardsDefaultParams = TypedDict('ImdbTitleAwardsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleAwardsTextResponseParams = TypedDict('ImdbTitleAwardsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleAwardsStreamParams = TypedDict('ImdbTitleAwardsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleBoxOfficeDefaultParams = TypedDict('ImdbTitleBoxOfficeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleBoxOfficeTextResponseParams = TypedDict('ImdbTitleBoxOfficeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleBoxOfficeStreamParams = TypedDict('ImdbTitleBoxOfficeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleCompanyCreditsDefaultParams = TypedDict('ImdbTitleCompanyCreditsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleCompanyCreditsTextResponseParams = TypedDict('ImdbTitleCompanyCreditsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleCompanyCreditsStreamParams = TypedDict('ImdbTitleCompanyCreditsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleConnectionsDefaultParams = TypedDict('ImdbTitleConnectionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleConnectionsTextResponseParams = TypedDict('ImdbTitleConnectionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleConnectionsStreamParams = TypedDict('ImdbTitleConnectionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleCreditsDefaultParams = TypedDict('ImdbTitleCreditsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleCreditsTextResponseParams = TypedDict('ImdbTitleCreditsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleCreditsStreamParams = TypedDict('ImdbTitleCreditsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleEpisodesDefaultParams = TypedDict('ImdbTitleEpisodesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'season': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleEpisodesTextResponseParams = TypedDict('ImdbTitleEpisodesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'season': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleEpisodesStreamParams = TypedDict('ImdbTitleEpisodesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'season': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleFilmingLocationsDefaultParams = TypedDict('ImdbTitleFilmingLocationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleFilmingLocationsTextResponseParams = TypedDict('ImdbTitleFilmingLocationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleFilmingLocationsStreamParams = TypedDict('ImdbTitleFilmingLocationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleGoofsDefaultParams = TypedDict('ImdbTitleGoofsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleGoofsTextResponseParams = TypedDict('ImdbTitleGoofsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleGoofsStreamParams = TypedDict('ImdbTitleGoofsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleImagesDefaultParams = TypedDict('ImdbTitleImagesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'type': NotRequired[Literal['behind_the_scenes', 'event', 'poster', 'product', 'production_art', 'publicity', 'still_frame', 'unknown']],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleImagesTextResponseParams = TypedDict('ImdbTitleImagesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'type': NotRequired[Literal['behind_the_scenes', 'event', 'poster', 'product', 'production_art', 'publicity', 'still_frame', 'unknown']],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleImagesStreamParams = TypedDict('ImdbTitleImagesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'type': NotRequired[Literal['behind_the_scenes', 'event', 'poster', 'product', 'production_art', 'publicity', 'still_frame', 'unknown']],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleKeywordsDefaultParams = TypedDict('ImdbTitleKeywordsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleKeywordsTextResponseParams = TypedDict('ImdbTitleKeywordsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleKeywordsStreamParams = TypedDict('ImdbTitleKeywordsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleParentalGuideDefaultParams = TypedDict('ImdbTitleParentalGuideDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleParentalGuideTextResponseParams = TypedDict('ImdbTitleParentalGuideTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleParentalGuideStreamParams = TypedDict('ImdbTitleParentalGuideStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitlePublicFactsAnalysisDefaultParams = TypedDict('ImdbTitlePublicFactsAnalysisDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitlePublicFactsAnalysisTextResponseParams = TypedDict('ImdbTitlePublicFactsAnalysisTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitlePublicFactsAnalysisStreamParams = TypedDict('ImdbTitlePublicFactsAnalysisStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleQuotesDefaultParams = TypedDict('ImdbTitleQuotesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleQuotesTextResponseParams = TypedDict('ImdbTitleQuotesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleQuotesStreamParams = TypedDict('ImdbTitleQuotesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleRatingsDefaultParams = TypedDict('ImdbTitleRatingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleRatingsTextResponseParams = TypedDict('ImdbTitleRatingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleRatingsStreamParams = TypedDict('ImdbTitleRatingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleReleaseInfoDefaultParams = TypedDict('ImdbTitleReleaseInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleReleaseInfoTextResponseParams = TypedDict('ImdbTitleReleaseInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleReleaseInfoStreamParams = TypedDict('ImdbTitleReleaseInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleReviewsDefaultParams = TypedDict('ImdbTitleReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleReviewsTextResponseParams = TypedDict('ImdbTitleReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleReviewsStreamParams = TypedDict('ImdbTitleReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleSimilarDefaultParams = TypedDict('ImdbTitleSimilarDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleSimilarTextResponseParams = TypedDict('ImdbTitleSimilarTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleSimilarStreamParams = TypedDict('ImdbTitleSimilarStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleTechnicalSpecsDefaultParams = TypedDict('ImdbTitleTechnicalSpecsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleTechnicalSpecsTextResponseParams = TypedDict('ImdbTitleTechnicalSpecsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleTechnicalSpecsStreamParams = TypedDict('ImdbTitleTechnicalSpecsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleTriviaDefaultParams = TypedDict('ImdbTitleTriviaDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleTriviaTextResponseParams = TypedDict('ImdbTitleTriviaTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleTriviaStreamParams = TypedDict('ImdbTitleTriviaStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ImdbTitleVideosDefaultParams = TypedDict('ImdbTitleVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleVideosTextResponseParams = TypedDict('ImdbTitleVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ImdbTitleVideosStreamParams = TypedDict('ImdbTitleVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)
