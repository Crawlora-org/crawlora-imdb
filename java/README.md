# Crawlora IMDb API client for Java

The official Java client for Crawlora's hosted IMDb API. It exposes 30 endpoints covering title and name search, charts, ratings, credits, awards, episodes, reviews, images, and title metadata. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-imdb</artifactId>
  <version>0.1.2</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-java-console) to get an API key.

```java
import net.crawlora.imdb.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.search(Map.ofEntries(Map.entry("query", "Inception")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported IMDb API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-imdb/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-imdb)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-java-api-docs)
