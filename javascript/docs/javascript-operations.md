# Crawlora IMDb JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `30`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| imdb | `imdb.charts` | `imdb-charts` | `GET /imdb/charts` | `chart` (query "top_rated_movies" \| "top_rated_tv_shows" \| "most_popular_movies" \| "most_popular_tv_shows" \| "top_rated_english_movies" \| "lowest_rated_movies")<br>`limit` (query number) | `ApiKeyAuth` | `ImdbChartsResponse` |  |
| imdb | `imdb.imageTypes` | `imdb-image-types` | `GET /imdb/image-types` | none | `ApiKeyAuth` | `ImdbImageTypesResponse` |  |
| imdb | `imdb.name` | `imdb-name` | `GET /imdb/name` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbNameResponse` |  |
| imdb | `imdb.nameAwards` | `imdb-name-awards` | `GET /imdb/name/awards` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbNameAwardsResponse` |  |
| imdb | `imdb.nameCredits` | `imdb-name-credits` | `GET /imdb/name/credits` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbNameCreditsResponse` |  |
| imdb | `imdb.nameImages` | `imdb-name-images` | `GET /imdb/name/images` | `id` (query string)<br>`url` (query string)<br>`type` (query "behind_the_scenes" \| "event" \| "poster" \| "product" \| "production_art" \| "publicity" \| "still_frame" \| "unknown")<br>`limit` (query number) | `ApiKeyAuth` | `ImdbNameImagesResponse` |  |
| imdb | `imdb.nameVideos` | `imdb-name-videos` | `GET /imdb/name/videos` | `id` (query string)<br>`url` (query string)<br>`limit` (query number) | `ApiKeyAuth` | `ImdbNameVideosResponse` |  |
| imdb | `imdb.search` | `imdb-search` | `GET /imdb/search` | `query` (query string required)<br>`limit` (query number) | `ApiKeyAuth` | `ImdbSearchResponse` |  |
| imdb | `imdb.searchTitle` | `imdb-search-title` | `GET /imdb/search/title` | `title` (query string)<br>`title_type` (query string)<br>`genres` (query string)<br>`release_date_from` (query string)<br>`release_date_to` (query string)<br>`min_user_rating` (query number)<br>`max_user_rating` (query number)<br>`min_votes` (query number)<br>`max_votes` (query number)<br>`min_popularity` (query number)<br>`max_popularity` (query number)<br>`min_runtime` (query number)<br>`max_runtime` (query number)<br>`groups` (query string)<br>`keywords` (query string)<br>`companies` (query string)<br>`certificates` (query string)<br>`colors` (query string)<br>`countries` (query string)<br>`languages` (query string)<br>`sound_mixes` (query string)<br>`role` (query string)<br>`characters` (query string)<br>`plot` (query string)<br>`include_adult` (query boolean)<br>`sort` (query string)<br>`sort_order` (query string)<br>`limit` (query number) | `ApiKeyAuth` | `ImdbSearchTitleResponse` |  |
| imdb | `imdb.title` | `imdb-title` | `GET /imdb/title` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleResponse` |  |
| imdb | `imdb.titleAwards` | `imdb-title-awards` | `GET /imdb/title/awards` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleAwardsResponse` |  |
| imdb | `imdb.titleBoxOffice` | `imdb-title-box-office` | `GET /imdb/title/box-office` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleBoxOfficeResponse` |  |
| imdb | `imdb.titleCompanyCredits` | `imdb-title-company-credits` | `GET /imdb/title/company-credits` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleCompanyCreditsResponse` |  |
| imdb | `imdb.titleConnections` | `imdb-title-connections` | `GET /imdb/title/connections` | `id` (query string)<br>`url` (query string)<br>`limit` (query number) | `ApiKeyAuth` | `ImdbTitleConnectionsResponse` |  |
| imdb | `imdb.titleCredits` | `imdb-title-credits` | `GET /imdb/title/credits` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleCreditsResponse` |  |
| imdb | `imdb.titleEpisodes` | `imdb-title-episodes` | `GET /imdb/title/episodes` | `id` (query string)<br>`url` (query string)<br>`season` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `ImdbTitleEpisodesResponse` |  |
| imdb | `imdb.titleFilmingLocations` | `imdb-title-filming-locations` | `GET /imdb/title/filming-locations` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleFilmingLocationsResponse` |  |
| imdb | `imdb.titleGoofs` | `imdb-title-goofs` | `GET /imdb/title/goofs` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleGoofsResponse` |  |
| imdb | `imdb.titleImages` | `imdb-title-images` | `GET /imdb/title/images` | `id` (query string)<br>`url` (query string)<br>`type` (query "behind_the_scenes" \| "event" \| "poster" \| "product" \| "production_art" \| "publicity" \| "still_frame" \| "unknown")<br>`limit` (query number) | `ApiKeyAuth` | `ImdbTitleImagesResponse` |  |
| imdb | `imdb.titleKeywords` | `imdb-title-keywords` | `GET /imdb/title/keywords` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleKeywordsResponse` |  |
| imdb | `imdb.titleParentalGuide` | `imdb-title-parental-guide` | `GET /imdb/title/parental-guide` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleParentalGuideResponse` |  |
| imdb | `imdb.titlePublicFactsAnalysis` | `imdb-title-public-facts-analysis` | `GET /imdb/title/public-facts-analysis` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitlePublicFactsAnalysisResponse` |  |
| imdb | `imdb.titleQuotes` | `imdb-title-quotes` | `GET /imdb/title/quotes` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleQuotesResponse` |  |
| imdb | `imdb.titleRatings` | `imdb-title-ratings` | `GET /imdb/title/ratings` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleRatingsResponse` |  |
| imdb | `imdb.titleReleaseInfo` | `imdb-title-release-info` | `GET /imdb/title/release-info` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleReleaseInfoResponse` |  |
| imdb | `imdb.titleReviews` | `imdb-title-reviews` | `GET /imdb/title/reviews` | `id` (query string)<br>`url` (query string)<br>`limit` (query number) | `ApiKeyAuth` | `ImdbTitleReviewsResponse` |  |
| imdb | `imdb.titleSimilar` | `imdb-title-similar` | `GET /imdb/title/similar` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleSimilarResponse` |  |
| imdb | `imdb.titleTechnicalSpecs` | `imdb-title-technical-specs` | `GET /imdb/title/technical-specs` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleTechnicalSpecsResponse` |  |
| imdb | `imdb.titleTrivia` | `imdb-title-trivia` | `GET /imdb/title/trivia` | `id` (query string)<br>`url` (query string) | `ApiKeyAuth` | `ImdbTitleTriviaResponse` |  |
| imdb | `imdb.titleVideos` | `imdb-title-videos` | `GET /imdb/title/videos` | `id` (query string)<br>`url` (query string)<br>`limit` (query number) | `ApiKeyAuth` | `ImdbTitleVideosResponse` |  |
