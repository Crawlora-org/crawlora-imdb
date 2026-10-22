# Crawlora IMDb Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `30`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| imdb | `imdb.charts` | `imdb-charts` | `GET /imdb/charts` | `chart` (query String enum{top_rated_movies, top_rated_tv_shows, most_popular_movies, most_popular_tv_shows, top_rated_english_movies, lowest_rated_movies})<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbChartsResponse` |  |
| imdb | `imdb.image_types` | `imdb-image-types` | `GET /imdb/image-types` | none | `ApiKeyAuth` | `ImdbImageTypesResponse` |  |
| imdb | `imdb.name` | `imdb-name` | `GET /imdb/name` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbNameResponse` |  |
| imdb | `imdb.name_awards` | `imdb-name-awards` | `GET /imdb/name/awards` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbNameAwardsResponse` |  |
| imdb | `imdb.name_credits` | `imdb-name-credits` | `GET /imdb/name/credits` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbNameCreditsResponse` |  |
| imdb | `imdb.name_images` | `imdb-name-images` | `GET /imdb/name/images` | `id` (query String)<br>`url` (query String)<br>`type` (query String enum{behind_the_scenes, event, poster, product, production_art, publicity, still_frame, unknown})<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbNameImagesResponse` |  |
| imdb | `imdb.name_videos` | `imdb-name-videos` | `GET /imdb/name/videos` | `id` (query String)<br>`url` (query String)<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbNameVideosResponse` |  |
| imdb | `imdb.search` | `imdb-search` | `GET /imdb/search` | `query` (query String required)<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbSearchResponse` |  |
| imdb | `imdb.search_title` | `imdb-search-title` | `GET /imdb/search/title` | `title` (query String)<br>`title_type` (query String)<br>`genres` (query String)<br>`release_date_from` (query String)<br>`release_date_to` (query String)<br>`min_user_rating` (query f64)<br>`max_user_rating` (query f64)<br>`min_votes` (query i64)<br>`max_votes` (query i64)<br>`min_popularity` (query i64)<br>`max_popularity` (query i64)<br>`min_runtime` (query i64)<br>`max_runtime` (query i64)<br>`groups` (query String)<br>`keywords` (query String)<br>`companies` (query String)<br>`certificates` (query String)<br>`colors` (query String)<br>`countries` (query String)<br>`languages` (query String)<br>`sound_mixes` (query String)<br>`role` (query String)<br>`characters` (query String)<br>`plot` (query String)<br>`include_adult` (query bool)<br>`sort` (query String)<br>`sort_order` (query String)<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbSearchTitleResponse` |  |
| imdb | `imdb.title` | `imdb-title` | `GET /imdb/title` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleResponse` |  |
| imdb | `imdb.title_awards` | `imdb-title-awards` | `GET /imdb/title/awards` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleAwardsResponse` |  |
| imdb | `imdb.title_box_office` | `imdb-title-box-office` | `GET /imdb/title/box-office` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleBoxOfficeResponse` |  |
| imdb | `imdb.title_company_credits` | `imdb-title-company-credits` | `GET /imdb/title/company-credits` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleCompanyCreditsResponse` |  |
| imdb | `imdb.title_connections` | `imdb-title-connections` | `GET /imdb/title/connections` | `id` (query String)<br>`url` (query String)<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbTitleConnectionsResponse` |  |
| imdb | `imdb.title_credits` | `imdb-title-credits` | `GET /imdb/title/credits` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleCreditsResponse` |  |
| imdb | `imdb.title_episodes` | `imdb-title-episodes` | `GET /imdb/title/episodes` | `id` (query String)<br>`url` (query String)<br>`season` (query i64)<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbTitleEpisodesResponse` |  |
| imdb | `imdb.title_filming_locations` | `imdb-title-filming-locations` | `GET /imdb/title/filming-locations` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleFilmingLocationsResponse` |  |
| imdb | `imdb.title_goofs` | `imdb-title-goofs` | `GET /imdb/title/goofs` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleGoofsResponse` |  |
| imdb | `imdb.title_images` | `imdb-title-images` | `GET /imdb/title/images` | `id` (query String)<br>`url` (query String)<br>`type` (query String enum{behind_the_scenes, event, poster, product, production_art, publicity, still_frame, unknown})<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbTitleImagesResponse` |  |
| imdb | `imdb.title_keywords` | `imdb-title-keywords` | `GET /imdb/title/keywords` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleKeywordsResponse` |  |
| imdb | `imdb.title_parental_guide` | `imdb-title-parental-guide` | `GET /imdb/title/parental-guide` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleParentalGuideResponse` |  |
| imdb | `imdb.title_public_facts_analysis` | `imdb-title-public-facts-analysis` | `GET /imdb/title/public-facts-analysis` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitlePublicFactsAnalysisResponse` |  |
| imdb | `imdb.title_quotes` | `imdb-title-quotes` | `GET /imdb/title/quotes` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleQuotesResponse` |  |
| imdb | `imdb.title_ratings` | `imdb-title-ratings` | `GET /imdb/title/ratings` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleRatingsResponse` |  |
| imdb | `imdb.title_release_info` | `imdb-title-release-info` | `GET /imdb/title/release-info` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleReleaseInfoResponse` |  |
| imdb | `imdb.title_reviews` | `imdb-title-reviews` | `GET /imdb/title/reviews` | `id` (query String)<br>`url` (query String)<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbTitleReviewsResponse` |  |
| imdb | `imdb.title_similar` | `imdb-title-similar` | `GET /imdb/title/similar` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleSimilarResponse` |  |
| imdb | `imdb.title_technical_specs` | `imdb-title-technical-specs` | `GET /imdb/title/technical-specs` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleTechnicalSpecsResponse` |  |
| imdb | `imdb.title_trivia` | `imdb-title-trivia` | `GET /imdb/title/trivia` | `id` (query String)<br>`url` (query String) | `ApiKeyAuth` | `ImdbTitleTriviaResponse` |  |
| imdb | `imdb.title_videos` | `imdb-title-videos` | `GET /imdb/title/videos` | `id` (query String)<br>`url` (query String)<br>`limit` (query i64) | `ApiKeyAuth` | `ImdbTitleVideosResponse` |  |
