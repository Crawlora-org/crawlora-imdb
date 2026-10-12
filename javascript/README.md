# @crawlora-org/imdb — IMDb API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted IMDb API.
It exposes 30 API endpoints for title and name search, charts, ratings, credits, awards, episodes, reviews, images, and title metadata through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-javascript-homepage). It does not run a browser or scrape IMDb locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by IMDb or its owners.

## Install

```sh
npm install @crawlora-org/imdb
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { IMDbClient } from "@crawlora-org/imdb";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new IMDbClient({ apiKey });
const result1 = await client.search({ query: "Inception" });
console.log(result1);
const result2 = await client.charts({});
console.log(result2);
```

The client also exports `Client` as an alias for `IMDbClient`. Operation
methods are available directly in camelCase and through the `imdb`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-imdb/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-imdb/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported IMDb API endpoints

This package exposes each route below as a direct method and through the `imdb` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-imdb/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
