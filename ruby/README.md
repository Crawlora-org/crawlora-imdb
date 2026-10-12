# Crawlora IMDb API client for Ruby (`crawlora-imdb`)

This Ruby gem calls Crawlora's hosted IMDb API at `https://api.crawlora.net/api/v1`. It exposes 30 endpoints covering title and name search, charts, ratings, credits, awards, episodes, reviews, images, and title metadata; it does not call or scrape IMDb directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-imdb"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/imdb"

client = Crawlora::Imdb::Client.new
result = client.request("imdb-search", JSON.parse("{\"query\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 30 API operations.

```ruby
client = Crawlora::Imdb::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported IMDb API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-imdb/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/imdb/charts` | `imdb-charts` | IMDb title charts |
| `GET` | `/imdb/image-types` | `imdb-image-types` | IMDb image types |
| `GET` | `/imdb/name` | `imdb-name` | IMDb name detail |
| `GET` | `/imdb/name/awards` | `imdb-name-awards` | IMDb name awards |
| `GET` | `/imdb/name/credits` | `imdb-name-credits` | IMDb name credits |
| `GET` | `/imdb/name/images` | `imdb-name-images` | IMDb name images |
| `GET` | `/imdb/name/videos` | `imdb-name-videos` | IMDb name video metadata |
| `GET` | `/imdb/search` | `imdb-search` | IMDb title search |
| `GET` | `/imdb/search/title` | `imdb-search-title` | IMDb advanced title search |
| `GET` | `/imdb/title` | `imdb-title` | IMDb title detail |
| `GET` | `/imdb/title/awards` | `imdb-title-awards` | IMDb title awards |
| `GET` | `/imdb/title/box-office` | `imdb-title-box-office` | IMDb title box office summary |
| `GET` | `/imdb/title/company-credits` | `imdb-title-company-credits` | IMDb title company credits |
| `GET` | `/imdb/title/connections` | `imdb-title-connections` | IMDb title connections |
| `GET` | `/imdb/title/credits` | `imdb-title-credits` | IMDb title credits |
| `GET` | `/imdb/title/episodes` | `imdb-title-episodes` | IMDb title episodes |
| `GET` | `/imdb/title/filming-locations` | `imdb-title-filming-locations` | IMDb title filming locations |
| `GET` | `/imdb/title/goofs` | `imdb-title-goofs` | IMDb title goofs |
| `GET` | `/imdb/title/images` | `imdb-title-images` | IMDb title images |
| `GET` | `/imdb/title/keywords` | `imdb-title-keywords` | IMDb title keywords |
| `GET` | `/imdb/title/parental-guide` | `imdb-title-parental-guide` | IMDb title parental guide |
| `GET` | `/imdb/title/public-facts-analysis` | `imdb-title-public-facts-analysis` | IMDb title public facts analysis |
| `GET` | `/imdb/title/quotes` | `imdb-title-quotes` | IMDb title quotes |
| `GET` | `/imdb/title/ratings` | `imdb-title-ratings` | IMDb title ratings breakdown |
| `GET` | `/imdb/title/release-info` | `imdb-title-release-info` | IMDb title release info |
| `GET` | `/imdb/title/reviews` | `imdb-title-reviews` | IMDb title user reviews |
| `GET` | `/imdb/title/similar` | `imdb-title-similar` | IMDb similar titles |
| `GET` | `/imdb/title/technical-specs` | `imdb-title-technical-specs` | IMDb title technical specs |
| `GET` | `/imdb/title/trivia` | `imdb-title-trivia` | IMDb title trivia |
| `GET` | `/imdb/title/videos` | `imdb-title-videos` | IMDb title video metadata |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-imdb) for account setup, the API operation reference, and release history.
