package net.crawlora.imdb;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the IMDb endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 30;
    public static final List<String> OPERATION_IDS = List.of(
            "imdb-charts",
            "imdb-image-types",
            "imdb-name",
            "imdb-name-awards",
            "imdb-name-credits",
            "imdb-name-images",
            "imdb-name-videos",
            "imdb-search",
            "imdb-search-title",
            "imdb-title",
            "imdb-title-awards",
            "imdb-title-box-office",
            "imdb-title-company-credits",
            "imdb-title-connections",
            "imdb-title-credits",
            "imdb-title-episodes",
            "imdb-title-filming-locations",
            "imdb-title-goofs",
            "imdb-title-images",
            "imdb-title-keywords",
            "imdb-title-parental-guide",
            "imdb-title-public-facts-analysis",
            "imdb-title-quotes",
            "imdb-title-ratings",
            "imdb-title-release-info",
            "imdb-title-reviews",
            "imdb-title-similar",
            "imdb-title-technical-specs",
            "imdb-title-trivia",
            "imdb-title-videos"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("imdb-charts", new Operation("imdb-charts", "GET", "/imdb/charts", Map.ofEntries(Map.entry("chart", new Param("chart", "query", false, "string", List.of("top_rated_movies", "top_rated_tv_shows", "most_popular_movies", "most_popular_tv_shows", "top_rated_english_movies", "lowest_rated_movies"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-image-types", new Operation("imdb-image-types", "GET", "/imdb/image-types", Map.of(), List.of("application/json")));
        operations.put("imdb-name", new Operation("imdb-name", "GET", "/imdb/name", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-name-awards", new Operation("imdb-name-awards", "GET", "/imdb/name/awards", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-name-credits", new Operation("imdb-name-credits", "GET", "/imdb/name/credits", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-name-images", new Operation("imdb-name-images", "GET", "/imdb/name/images", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("behind_the_scenes", "event", "poster", "product", "production_art", "publicity", "still_frame", "unknown"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-name-videos", new Operation("imdb-name-videos", "GET", "/imdb/name/videos", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-search", new Operation("imdb-search", "GET", "/imdb/search", Map.ofEntries(Map.entry("query", new Param("query", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-search-title", new Operation("imdb-search-title", "GET", "/imdb/search/title", Map.ofEntries(Map.entry("title", new Param("title", "query", false, "string", List.of(), "csv")), Map.entry("title_type", new Param("title_type", "query", false, "string", List.of(), "csv")), Map.entry("genres", new Param("genres", "query", false, "string", List.of(), "csv")), Map.entry("release_date_from", new Param("release_date_from", "query", false, "string", List.of(), "csv")), Map.entry("release_date_to", new Param("release_date_to", "query", false, "string", List.of(), "csv")), Map.entry("min_user_rating", new Param("min_user_rating", "query", false, "number", List.of(), "csv")), Map.entry("max_user_rating", new Param("max_user_rating", "query", false, "number", List.of(), "csv")), Map.entry("min_votes", new Param("min_votes", "query", false, "integer", List.of(), "csv")), Map.entry("max_votes", new Param("max_votes", "query", false, "integer", List.of(), "csv")), Map.entry("min_popularity", new Param("min_popularity", "query", false, "integer", List.of(), "csv")), Map.entry("max_popularity", new Param("max_popularity", "query", false, "integer", List.of(), "csv")), Map.entry("min_runtime", new Param("min_runtime", "query", false, "integer", List.of(), "csv")), Map.entry("max_runtime", new Param("max_runtime", "query", false, "integer", List.of(), "csv")), Map.entry("groups", new Param("groups", "query", false, "string", List.of(), "csv")), Map.entry("keywords", new Param("keywords", "query", false, "string", List.of(), "csv")), Map.entry("companies", new Param("companies", "query", false, "string", List.of(), "csv")), Map.entry("certificates", new Param("certificates", "query", false, "string", List.of(), "csv")), Map.entry("colors", new Param("colors", "query", false, "string", List.of(), "csv")), Map.entry("countries", new Param("countries", "query", false, "string", List.of(), "csv")), Map.entry("languages", new Param("languages", "query", false, "string", List.of(), "csv")), Map.entry("sound_mixes", new Param("sound_mixes", "query", false, "string", List.of(), "csv")), Map.entry("role", new Param("role", "query", false, "string", List.of(), "csv")), Map.entry("characters", new Param("characters", "query", false, "string", List.of(), "csv")), Map.entry("plot", new Param("plot", "query", false, "string", List.of(), "csv")), Map.entry("include_adult", new Param("include_adult", "query", false, "boolean", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of(), "csv")), Map.entry("sort_order", new Param("sort_order", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title", new Operation("imdb-title", "GET", "/imdb/title", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-awards", new Operation("imdb-title-awards", "GET", "/imdb/title/awards", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-box-office", new Operation("imdb-title-box-office", "GET", "/imdb/title/box-office", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-company-credits", new Operation("imdb-title-company-credits", "GET", "/imdb/title/company-credits", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-connections", new Operation("imdb-title-connections", "GET", "/imdb/title/connections", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-credits", new Operation("imdb-title-credits", "GET", "/imdb/title/credits", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-episodes", new Operation("imdb-title-episodes", "GET", "/imdb/title/episodes", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-filming-locations", new Operation("imdb-title-filming-locations", "GET", "/imdb/title/filming-locations", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-goofs", new Operation("imdb-title-goofs", "GET", "/imdb/title/goofs", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-images", new Operation("imdb-title-images", "GET", "/imdb/title/images", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("behind_the_scenes", "event", "poster", "product", "production_art", "publicity", "still_frame", "unknown"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-keywords", new Operation("imdb-title-keywords", "GET", "/imdb/title/keywords", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-parental-guide", new Operation("imdb-title-parental-guide", "GET", "/imdb/title/parental-guide", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-public-facts-analysis", new Operation("imdb-title-public-facts-analysis", "GET", "/imdb/title/public-facts-analysis", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-quotes", new Operation("imdb-title-quotes", "GET", "/imdb/title/quotes", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-ratings", new Operation("imdb-title-ratings", "GET", "/imdb/title/ratings", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-release-info", new Operation("imdb-title-release-info", "GET", "/imdb/title/release-info", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-reviews", new Operation("imdb-title-reviews", "GET", "/imdb/title/reviews", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-similar", new Operation("imdb-title-similar", "GET", "/imdb/title/similar", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-technical-specs", new Operation("imdb-title-technical-specs", "GET", "/imdb/title/technical-specs", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-trivia", new Operation("imdb-title-trivia", "GET", "/imdb/title/trivia", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("imdb-title-videos", new Operation("imdb-title-videos", "GET", "/imdb/title/videos", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown IMDb operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest request = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation))
                .GET().build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object charts(Map<String, ?> params) { return request("imdb-charts", params); }
    public Object imageTypes(Map<String, ?> params) { return request("imdb-image-types", params); }
    public Object name(Map<String, ?> params) { return request("imdb-name", params); }
    public Object nameAwards(Map<String, ?> params) { return request("imdb-name-awards", params); }
    public Object nameCredits(Map<String, ?> params) { return request("imdb-name-credits", params); }
    public Object nameImages(Map<String, ?> params) { return request("imdb-name-images", params); }
    public Object nameVideos(Map<String, ?> params) { return request("imdb-name-videos", params); }
    public Object search(Map<String, ?> params) { return request("imdb-search", params); }
    public Object searchTitle(Map<String, ?> params) { return request("imdb-search-title", params); }
    public Object title(Map<String, ?> params) { return request("imdb-title", params); }
    public Object titleAwards(Map<String, ?> params) { return request("imdb-title-awards", params); }
    public Object titleBoxOffice(Map<String, ?> params) { return request("imdb-title-box-office", params); }
    public Object titleCompanyCredits(Map<String, ?> params) { return request("imdb-title-company-credits", params); }
    public Object titleConnections(Map<String, ?> params) { return request("imdb-title-connections", params); }
    public Object titleCredits(Map<String, ?> params) { return request("imdb-title-credits", params); }
    public Object titleEpisodes(Map<String, ?> params) { return request("imdb-title-episodes", params); }
    public Object titleFilmingLocations(Map<String, ?> params) { return request("imdb-title-filming-locations", params); }
    public Object titleGoofs(Map<String, ?> params) { return request("imdb-title-goofs", params); }
    public Object titleImages(Map<String, ?> params) { return request("imdb-title-images", params); }
    public Object titleKeywords(Map<String, ?> params) { return request("imdb-title-keywords", params); }
    public Object titleParentalGuide(Map<String, ?> params) { return request("imdb-title-parental-guide", params); }
    public Object titlePublicFactsAnalysis(Map<String, ?> params) { return request("imdb-title-public-facts-analysis", params); }
    public Object titleQuotes(Map<String, ?> params) { return request("imdb-title-quotes", params); }
    public Object titleRatings(Map<String, ?> params) { return request("imdb-title-ratings", params); }
    public Object titleReleaseInfo(Map<String, ?> params) { return request("imdb-title-release-info", params); }
    public Object titleReviews(Map<String, ?> params) { return request("imdb-title-reviews", params); }
    public Object titleSimilar(Map<String, ?> params) { return request("imdb-title-similar", params); }
    public Object titleTechnicalSpecs(Map<String, ?> params) { return request("imdb-title-technical-specs", params); }
    public Object titleTrivia(Map<String, ?> params) { return request("imdb-title-trivia", params); }
    public Object titleVideos(Map<String, ?> params) { return request("imdb-title-videos", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
