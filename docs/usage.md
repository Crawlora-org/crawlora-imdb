# IMDb client usage

The `@crawlora-org/imdb` and `crawlora-imdb` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape IMDb locally; Crawlora is independent from and not endorsed by IMDb or its owners.

The package tracks the public API contract revision `sha256:2f96f0b8f5094ee2366e03038a2840bce6fbe2c09fb7d0ea464de89f1f42f013` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 30 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `imdb` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `charts` / `charts` | `GET /imdb/charts` | `chart` (query, optional; values: `top_rated_movies`, `top_rated_tv_shows`, `most_popular_movies`, `most_popular_tv_shows`, `top_rated_english_movies`, `lowest_rated_movies`), `limit` (query, optional) | IMDb title charts |
| `imageTypes` / `image_types` | `GET /imdb/image-types` | — | IMDb image types |
| `name` / `name` | `GET /imdb/name` | `id` (query, optional), `url` (query, optional) | IMDb name detail |
| `nameAwards` / `name_awards` | `GET /imdb/name/awards` | `id` (query, optional), `url` (query, optional) | IMDb name awards |
| `nameCredits` / `name_credits` | `GET /imdb/name/credits` | `id` (query, optional), `url` (query, optional) | IMDb name credits |
| `nameImages` / `name_images` | `GET /imdb/name/images` | `id` (query, optional), `url` (query, optional), `type` (query, optional; values: `behind_the_scenes`, `event`, `poster`, `product`, `production_art`, `publicity`, `still_frame`, `unknown`), `limit` (query, optional) | IMDb name images |
| `nameVideos` / `name_videos` | `GET /imdb/name/videos` | `id` (query, optional), `url` (query, optional), `limit` (query, optional) | IMDb name video metadata |
| `search` / `search` | `GET /imdb/search` | `query` (query, required), `limit` (query, optional) | IMDb title search |
| `searchTitle` / `search_title` | `GET /imdb/search/title` | `title` (query, optional), `title_type` (query, optional), `genres` (query, optional), `release_date_from` (query, optional), `release_date_to` (query, optional), `min_user_rating` (query, optional), `max_user_rating` (query, optional), `min_votes` (query, optional), `max_votes` (query, optional), `min_popularity` (query, optional), `max_popularity` (query, optional), `min_runtime` (query, optional), `max_runtime` (query, optional), `groups` (query, optional), `keywords` (query, optional), `companies` (query, optional), `certificates` (query, optional), `colors` (query, optional), `countries` (query, optional), `languages` (query, optional), `sound_mixes` (query, optional), `role` (query, optional), `characters` (query, optional), `plot` (query, optional), `include_adult` (query, optional), `sort` (query, optional), `sort_order` (query, optional), `limit` (query, optional) | IMDb advanced title search |
| `title` / `title` | `GET /imdb/title` | `id` (query, optional), `url` (query, optional) | IMDb title detail |
| `titleAwards` / `title_awards` | `GET /imdb/title/awards` | `id` (query, optional), `url` (query, optional) | IMDb title awards |
| `titleBoxOffice` / `title_box_office` | `GET /imdb/title/box-office` | `id` (query, optional), `url` (query, optional) | IMDb title box office summary |
| `titleCompanyCredits` / `title_company_credits` | `GET /imdb/title/company-credits` | `id` (query, optional), `url` (query, optional) | IMDb title company credits |
| `titleConnections` / `title_connections` | `GET /imdb/title/connections` | `id` (query, optional), `url` (query, optional), `limit` (query, optional) | IMDb title connections |
| `titleCredits` / `title_credits` | `GET /imdb/title/credits` | `id` (query, optional), `url` (query, optional) | IMDb title credits |
| `titleEpisodes` / `title_episodes` | `GET /imdb/title/episodes` | `id` (query, optional), `url` (query, optional), `season` (query, optional), `limit` (query, optional) | IMDb title episodes |
| `titleFilmingLocations` / `title_filming_locations` | `GET /imdb/title/filming-locations` | `id` (query, optional), `url` (query, optional) | IMDb title filming locations |
| `titleGoofs` / `title_goofs` | `GET /imdb/title/goofs` | `id` (query, optional), `url` (query, optional) | IMDb title goofs |
| `titleImages` / `title_images` | `GET /imdb/title/images` | `id` (query, optional), `url` (query, optional), `type` (query, optional; values: `behind_the_scenes`, `event`, `poster`, `product`, `production_art`, `publicity`, `still_frame`, `unknown`), `limit` (query, optional) | IMDb title images |
| `titleKeywords` / `title_keywords` | `GET /imdb/title/keywords` | `id` (query, optional), `url` (query, optional) | IMDb title keywords |
| `titleParentalGuide` / `title_parental_guide` | `GET /imdb/title/parental-guide` | `id` (query, optional), `url` (query, optional) | IMDb title parental guide |
| `titlePublicFactsAnalysis` / `title_public_facts_analysis` | `GET /imdb/title/public-facts-analysis` | `id` (query, optional), `url` (query, optional) | IMDb title public facts analysis |
| `titleQuotes` / `title_quotes` | `GET /imdb/title/quotes` | `id` (query, optional), `url` (query, optional) | IMDb title quotes |
| `titleRatings` / `title_ratings` | `GET /imdb/title/ratings` | `id` (query, optional), `url` (query, optional) | IMDb title ratings breakdown |
| `titleReleaseInfo` / `title_release_info` | `GET /imdb/title/release-info` | `id` (query, optional), `url` (query, optional) | IMDb title release info |
| `titleReviews` / `title_reviews` | `GET /imdb/title/reviews` | `id` (query, optional), `url` (query, optional), `limit` (query, optional) | IMDb title user reviews |
| `titleSimilar` / `title_similar` | `GET /imdb/title/similar` | `id` (query, optional), `url` (query, optional) | IMDb similar titles |
| `titleTechnicalSpecs` / `title_technical_specs` | `GET /imdb/title/technical-specs` | `id` (query, optional), `url` (query, optional) | IMDb title technical specs |
| `titleTrivia` / `title_trivia` | `GET /imdb/title/trivia` | `id` (query, optional), `url` (query, optional) | IMDb title trivia |
| `titleVideos` / `title_videos` | `GET /imdb/title/videos` | `id` (query, optional), `url` (query, optional), `limit` (query, optional) | IMDb title video metadata |

## Client forms

- JavaScript: import `IMDbClient` (also exported as `Client`) from `@crawlora-org/imdb`; use `new IMDbClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `IMDbClient` (also exported as `Client`) from `crawlora_imdb`; use `with IMDbClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncIMDbClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
