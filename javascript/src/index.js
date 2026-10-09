import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class IMDbClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-imdb-js/0.1.0" });
    this["charts"] = (...args) => this.request("imdb-charts", ...args);
    this["imageTypes"] = (...args) => this.request("imdb-image-types", ...args);
    this["name"] = (...args) => this.request("imdb-name", ...args);
    this["nameAwards"] = (...args) => this.request("imdb-name-awards", ...args);
    this["nameCredits"] = (...args) => this.request("imdb-name-credits", ...args);
    this["nameImages"] = (...args) => this.request("imdb-name-images", ...args);
    this["nameVideos"] = (...args) => this.request("imdb-name-videos", ...args);
    this["search"] = (...args) => this.request("imdb-search", ...args);
    this["searchTitle"] = (...args) => this.request("imdb-search-title", ...args);
    this["title"] = (...args) => this.request("imdb-title", ...args);
    this["titleAwards"] = (...args) => this.request("imdb-title-awards", ...args);
    this["titleBoxOffice"] = (...args) => this.request("imdb-title-box-office", ...args);
    this["titleCompanyCredits"] = (...args) => this.request("imdb-title-company-credits", ...args);
    this["titleConnections"] = (...args) => this.request("imdb-title-connections", ...args);
    this["titleCredits"] = (...args) => this.request("imdb-title-credits", ...args);
    this["titleEpisodes"] = (...args) => this.request("imdb-title-episodes", ...args);
    this["titleFilmingLocations"] = (...args) => this.request("imdb-title-filming-locations", ...args);
    this["titleGoofs"] = (...args) => this.request("imdb-title-goofs", ...args);
    this["titleImages"] = (...args) => this.request("imdb-title-images", ...args);
    this["titleKeywords"] = (...args) => this.request("imdb-title-keywords", ...args);
    this["titleParentalGuide"] = (...args) => this.request("imdb-title-parental-guide", ...args);
    this["titlePublicFactsAnalysis"] = (...args) => this.request("imdb-title-public-facts-analysis", ...args);
    this["titleQuotes"] = (...args) => this.request("imdb-title-quotes", ...args);
    this["titleRatings"] = (...args) => this.request("imdb-title-ratings", ...args);
    this["titleReleaseInfo"] = (...args) => this.request("imdb-title-release-info", ...args);
    this["titleReviews"] = (...args) => this.request("imdb-title-reviews", ...args);
    this["titleSimilar"] = (...args) => this.request("imdb-title-similar", ...args);
    this["titleTechnicalSpecs"] = (...args) => this.request("imdb-title-technical-specs", ...args);
    this["titleTrivia"] = (...args) => this.request("imdb-title-trivia", ...args);
    this["titleVideos"] = (...args) => this.request("imdb-title-videos", ...args);
  }
}

export { IMDbClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default IMDbClient;
