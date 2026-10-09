import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class IMDbClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  charts(params?: OperationParamsMap["imdb-charts"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  imageTypes(params?: OperationParamsMap["imdb-image-types"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  name(params?: OperationParamsMap["imdb-name"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  nameAwards(params?: OperationParamsMap["imdb-name-awards"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  nameCredits(params?: OperationParamsMap["imdb-name-credits"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  nameImages(params?: OperationParamsMap["imdb-name-images"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  nameVideos(params?: OperationParamsMap["imdb-name-videos"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["imdb-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchTitle(params?: OperationParamsMap["imdb-search-title"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  title(params?: OperationParamsMap["imdb-title"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleAwards(params?: OperationParamsMap["imdb-title-awards"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleBoxOffice(params?: OperationParamsMap["imdb-title-box-office"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleCompanyCredits(params?: OperationParamsMap["imdb-title-company-credits"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleConnections(params?: OperationParamsMap["imdb-title-connections"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleCredits(params?: OperationParamsMap["imdb-title-credits"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleEpisodes(params?: OperationParamsMap["imdb-title-episodes"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleFilmingLocations(params?: OperationParamsMap["imdb-title-filming-locations"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleGoofs(params?: OperationParamsMap["imdb-title-goofs"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleImages(params?: OperationParamsMap["imdb-title-images"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleKeywords(params?: OperationParamsMap["imdb-title-keywords"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleParentalGuide(params?: OperationParamsMap["imdb-title-parental-guide"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titlePublicFactsAnalysis(params?: OperationParamsMap["imdb-title-public-facts-analysis"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleQuotes(params?: OperationParamsMap["imdb-title-quotes"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleRatings(params?: OperationParamsMap["imdb-title-ratings"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleReleaseInfo(params?: OperationParamsMap["imdb-title-release-info"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleReviews(params?: OperationParamsMap["imdb-title-reviews"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleSimilar(params?: OperationParamsMap["imdb-title-similar"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleTechnicalSpecs(params?: OperationParamsMap["imdb-title-technical-specs"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleTrivia(params?: OperationParamsMap["imdb-title-trivia"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  titleVideos(params?: OperationParamsMap["imdb-title-videos"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  charts(params?: OperationParamsMap["imdb-charts"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  imageTypes(params?: OperationParamsMap["imdb-image-types"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  name(params?: OperationParamsMap["imdb-name"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  nameAwards(params?: OperationParamsMap["imdb-name-awards"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  nameCredits(params?: OperationParamsMap["imdb-name-credits"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  nameImages(params?: OperationParamsMap["imdb-name-images"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  nameVideos(params?: OperationParamsMap["imdb-name-videos"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["imdb-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchTitle(params?: OperationParamsMap["imdb-search-title"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  title(params?: OperationParamsMap["imdb-title"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleAwards(params?: OperationParamsMap["imdb-title-awards"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleBoxOffice(params?: OperationParamsMap["imdb-title-box-office"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleCompanyCredits(params?: OperationParamsMap["imdb-title-company-credits"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleConnections(params?: OperationParamsMap["imdb-title-connections"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleCredits(params?: OperationParamsMap["imdb-title-credits"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleEpisodes(params?: OperationParamsMap["imdb-title-episodes"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleFilmingLocations(params?: OperationParamsMap["imdb-title-filming-locations"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleGoofs(params?: OperationParamsMap["imdb-title-goofs"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleImages(params?: OperationParamsMap["imdb-title-images"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleKeywords(params?: OperationParamsMap["imdb-title-keywords"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleParentalGuide(params?: OperationParamsMap["imdb-title-parental-guide"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titlePublicFactsAnalysis(params?: OperationParamsMap["imdb-title-public-facts-analysis"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleQuotes(params?: OperationParamsMap["imdb-title-quotes"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleRatings(params?: OperationParamsMap["imdb-title-ratings"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleReleaseInfo(params?: OperationParamsMap["imdb-title-release-info"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleReviews(params?: OperationParamsMap["imdb-title-reviews"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleSimilar(params?: OperationParamsMap["imdb-title-similar"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleTechnicalSpecs(params?: OperationParamsMap["imdb-title-technical-specs"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleTrivia(params?: OperationParamsMap["imdb-title-trivia"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  titleVideos(params?: OperationParamsMap["imdb-title-videos"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  charts(...args: OperationRequestArgs<"imdb-charts">): Promise<OperationResponseMap["imdb-charts"]>;
  imageTypes(...args: OperationRequestArgs<"imdb-image-types">): Promise<OperationResponseMap["imdb-image-types"]>;
  name(...args: OperationRequestArgs<"imdb-name">): Promise<OperationResponseMap["imdb-name"]>;
  nameAwards(...args: OperationRequestArgs<"imdb-name-awards">): Promise<OperationResponseMap["imdb-name-awards"]>;
  nameCredits(...args: OperationRequestArgs<"imdb-name-credits">): Promise<OperationResponseMap["imdb-name-credits"]>;
  nameImages(...args: OperationRequestArgs<"imdb-name-images">): Promise<OperationResponseMap["imdb-name-images"]>;
  nameVideos(...args: OperationRequestArgs<"imdb-name-videos">): Promise<OperationResponseMap["imdb-name-videos"]>;
  search(...args: OperationRequestArgs<"imdb-search">): Promise<OperationResponseMap["imdb-search"]>;
  searchTitle(...args: OperationRequestArgs<"imdb-search-title">): Promise<OperationResponseMap["imdb-search-title"]>;
  title(...args: OperationRequestArgs<"imdb-title">): Promise<OperationResponseMap["imdb-title"]>;
  titleAwards(...args: OperationRequestArgs<"imdb-title-awards">): Promise<OperationResponseMap["imdb-title-awards"]>;
  titleBoxOffice(...args: OperationRequestArgs<"imdb-title-box-office">): Promise<OperationResponseMap["imdb-title-box-office"]>;
  titleCompanyCredits(...args: OperationRequestArgs<"imdb-title-company-credits">): Promise<OperationResponseMap["imdb-title-company-credits"]>;
  titleConnections(...args: OperationRequestArgs<"imdb-title-connections">): Promise<OperationResponseMap["imdb-title-connections"]>;
  titleCredits(...args: OperationRequestArgs<"imdb-title-credits">): Promise<OperationResponseMap["imdb-title-credits"]>;
  titleEpisodes(...args: OperationRequestArgs<"imdb-title-episodes">): Promise<OperationResponseMap["imdb-title-episodes"]>;
  titleFilmingLocations(...args: OperationRequestArgs<"imdb-title-filming-locations">): Promise<OperationResponseMap["imdb-title-filming-locations"]>;
  titleGoofs(...args: OperationRequestArgs<"imdb-title-goofs">): Promise<OperationResponseMap["imdb-title-goofs"]>;
  titleImages(...args: OperationRequestArgs<"imdb-title-images">): Promise<OperationResponseMap["imdb-title-images"]>;
  titleKeywords(...args: OperationRequestArgs<"imdb-title-keywords">): Promise<OperationResponseMap["imdb-title-keywords"]>;
  titleParentalGuide(...args: OperationRequestArgs<"imdb-title-parental-guide">): Promise<OperationResponseMap["imdb-title-parental-guide"]>;
  titlePublicFactsAnalysis(...args: OperationRequestArgs<"imdb-title-public-facts-analysis">): Promise<OperationResponseMap["imdb-title-public-facts-analysis"]>;
  titleQuotes(...args: OperationRequestArgs<"imdb-title-quotes">): Promise<OperationResponseMap["imdb-title-quotes"]>;
  titleRatings(...args: OperationRequestArgs<"imdb-title-ratings">): Promise<OperationResponseMap["imdb-title-ratings"]>;
  titleReleaseInfo(...args: OperationRequestArgs<"imdb-title-release-info">): Promise<OperationResponseMap["imdb-title-release-info"]>;
  titleReviews(...args: OperationRequestArgs<"imdb-title-reviews">): Promise<OperationResponseMap["imdb-title-reviews"]>;
  titleSimilar(...args: OperationRequestArgs<"imdb-title-similar">): Promise<OperationResponseMap["imdb-title-similar"]>;
  titleTechnicalSpecs(...args: OperationRequestArgs<"imdb-title-technical-specs">): Promise<OperationResponseMap["imdb-title-technical-specs"]>;
  titleTrivia(...args: OperationRequestArgs<"imdb-title-trivia">): Promise<OperationResponseMap["imdb-title-trivia"]>;
  titleVideos(...args: OperationRequestArgs<"imdb-title-videos">): Promise<OperationResponseMap["imdb-title-videos"]>;
}
export { IMDbClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default IMDbClient;
