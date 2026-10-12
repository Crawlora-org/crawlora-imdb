# crawlora-imdb — IMDb API client for Python

Python client for Crawlora's hosted IMDb API. It exposes 30 API endpoints covering title and name search, charts, ratings, credits, awards, episodes, reviews, images, and title metadata. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-python-homepage); the package does not run a browser or scrape
IMDb locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
IMDb or its owners.

## Install

```sh
python -m pip install crawlora-imdb
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_imdb import IMDbClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with IMDbClient(api_key=api_key) as client:
    result_1 = client.search(query='Inception')
    print(result_1)
    result_2 = client.charts()
    print(result_2)
```

The package also exports `Client` as an alias for `IMDbClient`. Operation
methods are available directly in snake_case and through the `imdb`
group. The async package client is `AsyncIMDbClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-imdb/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-imdb/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_imdb import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.search(query='Inception')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-imdb/blob/main/examples/python.py) for a complete usage example.

## Supported IMDb API endpoints

This package exposes every route below through direct snake_case methods and the `imdb` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-imdb/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
