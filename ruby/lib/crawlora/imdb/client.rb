require "json"
require "net/http"
require "uri"

module Crawlora
  module Imdb
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"imdb-charts": {"id": "imdb-charts", "method": "GET", "params": [{"default": "top_rated_movies", "description": "IMDb chart", "enum": ["top_rated_movies", "top_rated_tv_shows", "most_popular_movies", "most_popular_tv_shows", "top_rated_english_movies", "lowest_rated_movies"], "in": "query", "name": "chart", "type": "string"}, {"default": 25, "description": "Rows to return, default 25, max 250", "in": "query", "name": "limit", "type": "integer"}], "path": "/imdb/charts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["top_rated_movies", "top_rated_tv_shows", "most_popular_movies", "most_popular_tv_shows", "top_rated_english_movies", "lowest_rated_movies"], "in": "query", "name": "chart", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "imdb-image-types": {"id": "imdb-image-types", "method": "GET", "params": [], "path": "/imdb/image-types", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "imdb-name": {"id": "imdb-name", "method": "GET", "params": [{"description": "IMDb name id", "in": "query", "name": "id", "type": "string", "x-example": "nm0634240"}, {"description": "Absolute https://www.imdb.com/name/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/name/nm0634240/"}], "path": "/imdb/name", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-name-awards": {"id": "imdb-name-awards", "method": "GET", "params": [{"description": "IMDb name id", "in": "query", "name": "id", "type": "string", "x-example": "nm0634240"}, {"description": "Absolute https://www.imdb.com/name/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/name/nm0634240/"}], "path": "/imdb/name/awards", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-name-credits": {"id": "imdb-name-credits", "method": "GET", "params": [{"description": "IMDb name id", "in": "query", "name": "id", "type": "string", "x-example": "nm0634240"}, {"description": "Absolute https://www.imdb.com/name/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/name/nm0634240/"}], "path": "/imdb/name/credits", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-name-images": {"id": "imdb-name-images", "method": "GET", "params": [{"description": "IMDb name id", "in": "query", "name": "id", "type": "string", "x-example": "nm0000151"}, {"description": "Absolute https://www.imdb.com/name/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/name/nm0000151/"}, {"description": "Image type filter, single value or comma-separated list", "enum": ["behind_the_scenes", "event", "poster", "product", "production_art", "publicity", "still_frame", "unknown"], "in": "query", "name": "type", "type": "string", "x-example": "still_frame"}, {"description": "Rows to return, default 50, max 1000", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/imdb/name/images", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"enum": ["behind_the_scenes", "event", "poster", "product", "production_art", "publicity", "still_frame", "unknown"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "imdb-name-videos": {"id": "imdb-name-videos", "method": "GET", "params": [{"description": "IMDb name id", "in": "query", "name": "id", "type": "string", "x-example": "nm0000151"}, {"description": "Absolute https://www.imdb.com/name/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/name/nm0000151/"}, {"description": "Rows to return, default 50, max 100", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/imdb/name/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "imdb-search": {"id": "imdb-search", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "query", "required": true, "type": "string", "x-example": "inception"}, {"description": "Rows to return, default 10, max 20", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/imdb/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "imdb-search-title": {"id": "imdb-search-title", "method": "GET", "params": [{"description": "Title-name substring match", "in": "query", "name": "title", "type": "string", "x-example": "matrix"}, {"description": "Comma-separated title types: `feature`, `tvSeries`, `short`, `tvEpisode`, `tvMiniSeries`, `tvMovie`, `tvSpecial`, `tvShort`, `videoGame`, `video`, `musicVideo`, `podcastSeries`, `podcastEpisode`", "in": "query", "name": "title_type", "type": "string", "x-example": "feature"}, {"description": "Comma-separated genres (include-only): `Action`, `Adventure`, `Animation`, `Biography`, `Comedy`, `Crime`, `Documentary`, `Drama`, `Family`, `Fantasy`, `Film-Noir`, `Game-Show`, `History`, `Horror`, `Music`, `Musical`, `Mystery`, `News`, `Reality-TV`, `Romance`, `Sci-Fi`, `Short`, `Sport`, `Talk-Show`, `Thriller`, `War`, `Western`", "in": "query", "name": "genres", "type": "string", "x-example": "Action,Adventure"}, {"description": "Release date lower bound: YYYY, YYYY-MM, or YYYY-MM-DD", "in": "query", "name": "release_date_from", "type": "string", "x-example": "2020-01-01"}, {"description": "Release date upper bound: YYYY, YYYY-MM, or YYYY-MM-DD", "in": "query", "name": "release_date_to", "type": "string", "x-example": "2021-12-31"}, {"description": "Minimum IMDb user rating, 0-10", "in": "query", "name": "min_user_rating", "type": "number", "x-example": 7}, {"description": "Maximum IMDb user rating, 0-10", "in": "query", "name": "max_user_rating", "type": "number", "x-example": 9.5}, {"description": "Minimum number of user rating votes", "in": "query", "name": "min_votes", "type": "integer", "x-example": 25000}, {"description": "Maximum number of user rating votes", "in": "query", "name": "max_votes", "type": "integer"}, {"description": "Minimum IMDb popularity rank (1 is most popular)", "in": "query", "name": "min_popularity", "type": "integer"}, {"description": "Maximum IMDb popularity rank", "in": "query", "name": "max_popularity", "type": "integer"}, {"description": "Minimum runtime in minutes", "in": "query", "name": "min_runtime", "type": "integer"}, {"description": "Maximum runtime in minutes", "in": "query", "name": "max_runtime", "type": "integer"}, {"description": "Comma-separated awards/curated-list groups: `oscar_winner`, `oscar_nominee`, `emmy_winner`, `emmy_nominee`, `golden_globe_winner`, `golden_globe_nominee`, `best_picture_winner`, `best_director_winner`, `razzie_winner`, `razzie_nominee`, `top_100`, `top_250`, `top_1000`, `bottom_100`, `bottom_250`, `bottom_1000`", "in": "query", "name": "groups", "type": "string"}, {"description": "Comma-separated plot keywords", "in": "query", "name": "keywords", "type": "string", "x-example": "superhero"}, {"description": "Comma-separated IMDb company ids, format `co########`", "in": "query", "name": "companies", "type": "string", "x-example": "co0000756"}, {"description": "Comma-separated `COUNTRY:RATING` certificate pairs, e.g. `US:PG-13`", "in": "query", "name": "certificates", "type": "string", "x-example": "US:PG-13"}, {"description": "Comma-separated color info: `color`, `black_and_white`, `colorized`, `aces`", "in": "query", "name": "colors", "type": "string"}, {"description": "Comma-separated ISO country codes", "in": "query", "name": "countries", "type": "string", "x-example": "US"}, {"description": "Comma-separated ISO language codes", "in": "query", "name": "languages", "type": "string", "x-example": "en"}, {"description": "Comma-separated sound mix names: `12-Track Digital Sound`, `3 Channel Stereo`, `4-Track Stereo`, `6-Track Stereo`, `70 mm 6-Track`, `AGA Sound System`, `Auro 11.1`, `CDS`, `Chronophone`, `Cinematophone`, `Cinephone`, `Cinerama 7-Track`, `Cinesound`, `D-Cinema 48kHz 5.1`, `Datasat`, `De Forest Phonofilm`, `Digitrac Digital Audio System`, `Dolby`, `Dolby Atmos`, `Dolby Digital`, `Dolby Digital EX`, `Dolby SR`, `Dolby Stereo`, `Dolby Surround 7.1`, `DTS`, `DTS 70 mm`, `DTS Stereo`, `DTS-ES`, `IMAX 6-Track`, `Kinoplasticon`, `LC-Concept Digital Sound`, `Matrix Surround`, `Mono`, `Perspecta Stereo`, `Phono-Kinema`, `SDDS`, `Sensurround`, `Silent`, `Sonics-DDP`, `Sonix`, `Stereo`, `Ultra Stereo`, `Vitaphone`", "in": "query", "name": "sound_mixes", "type": "string"}, {"description": "Comma-separated cast/crew IMDb name ids, format `nm########`", "in": "query", "name": "role", "type": "string", "x-example": "nm0634240"}, {"description": "Comma-separated character names", "in": "query", "name": "characters", "type": "string", "x-example": "Neo"}, {"description": "Plot text search term", "in": "query", "name": "plot", "type": "string", "x-example": "hacker"}, {"default": false, "description": "Include adult titles. Defaults to excluded", "in": "query", "name": "include_adult", "type": "boolean"}, {"description": "One of `moviemeter`, `alpha`, `user_rating`, `num_votes`, `boxoffice_gross_us`, `runtime`, `year`, `release_date`", "in": "query", "name": "sort", "type": "string", "x-example": "user_rating"}, {"description": "`asc` or `desc`. Defaults to `asc` when sort is set", "in": "query", "name": "sort_order", "type": "string", "x-example": "desc"}, {"description": "Rows to return, default 25, max 50", "in": "query", "name": "limit", "type": "integer", "x-example": 25}], "path": "/imdb/search/title", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "title", "type": "string"}, {"in": "query", "name": "title_type", "type": "string"}, {"in": "query", "name": "genres", "type": "string"}, {"in": "query", "name": "release_date_from", "type": "string"}, {"in": "query", "name": "release_date_to", "type": "string"}, {"in": "query", "name": "min_user_rating", "type": "number"}, {"in": "query", "name": "max_user_rating", "type": "number"}, {"in": "query", "name": "min_votes", "type": "integer"}, {"in": "query", "name": "max_votes", "type": "integer"}, {"in": "query", "name": "min_popularity", "type": "integer"}, {"in": "query", "name": "max_popularity", "type": "integer"}, {"in": "query", "name": "min_runtime", "type": "integer"}, {"in": "query", "name": "max_runtime", "type": "integer"}, {"in": "query", "name": "groups", "type": "string"}, {"in": "query", "name": "keywords", "type": "string"}, {"in": "query", "name": "companies", "type": "string"}, {"in": "query", "name": "certificates", "type": "string"}, {"in": "query", "name": "colors", "type": "string"}, {"in": "query", "name": "countries", "type": "string"}, {"in": "query", "name": "languages", "type": "string"}, {"in": "query", "name": "sound_mixes", "type": "string"}, {"in": "query", "name": "role", "type": "string"}, {"in": "query", "name": "characters", "type": "string"}, {"in": "query", "name": "plot", "type": "string"}, {"in": "query", "name": "include_adult", "type": "boolean"}, {"in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "sort_order", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "imdb-title": {"id": "imdb-title", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-awards": {"id": "imdb-title-awards", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/awards", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-box-office": {"id": "imdb-title-box-office", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt0111161"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt0111161/"}], "path": "/imdb/title/box-office", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-company-credits": {"id": "imdb-title-company-credits", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/company-credits", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-connections": {"id": "imdb-title-connections", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt0111161"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt0111161/"}, {"description": "Rows to return, default 50, max 250", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/imdb/title/connections", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "imdb-title-credits": {"id": "imdb-title-credits", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/credits", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-episodes": {"id": "imdb-title-episodes", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt0944947"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt0944947/"}, {"description": "Season number to request", "in": "query", "name": "season", "type": "integer", "x-example": 1}, {"description": "Rows to return, default 10, max 20", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/imdb/title/episodes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "season", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "imdb-title-filming-locations": {"id": "imdb-title-filming-locations", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/filming-locations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-goofs": {"id": "imdb-title-goofs", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/goofs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-images": {"id": "imdb-title-images", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt0089753"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt0089753/"}, {"description": "Image type filter, single value or comma-separated list", "enum": ["behind_the_scenes", "event", "poster", "product", "production_art", "publicity", "still_frame", "unknown"], "in": "query", "name": "type", "type": "string", "x-example": "still_frame"}, {"description": "Rows to return, default 50, max 1000", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/imdb/title/images", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"enum": ["behind_the_scenes", "event", "poster", "product", "production_art", "publicity", "still_frame", "unknown"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "imdb-title-keywords": {"id": "imdb-title-keywords", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/keywords", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-parental-guide": {"id": "imdb-title-parental-guide", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/parental-guide", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-public-facts-analysis": {"id": "imdb-title-public-facts-analysis", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/public-facts-analysis", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-quotes": {"id": "imdb-title-quotes", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/quotes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-ratings": {"id": "imdb-title-ratings", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt0111161"}, {"description": "Absolute IMDb title URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt0111161/"}], "path": "/imdb/title/ratings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-release-info": {"id": "imdb-title-release-info", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/release-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-reviews": {"id": "imdb-title-reviews", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}, {"description": "Rows to return, default 10, max 20", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/imdb/title/reviews", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "imdb-title-similar": {"id": "imdb-title-similar", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt0111161"}, {"description": "Absolute IMDb title URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt0111161/"}], "path": "/imdb/title/similar", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-technical-specs": {"id": "imdb-title-technical-specs", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/technical-specs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-trivia": {"id": "imdb-title-trivia", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}], "path": "/imdb/title/trivia", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}], "security": ["ApiKeyAuth"]}, "imdb-title-videos": {"id": "imdb-title-videos", "method": "GET", "params": [{"description": "IMDb title id", "in": "query", "name": "id", "type": "string", "x-example": "tt1375666"}, {"description": "Absolute https://www.imdb.com/title/<id>/ URL", "in": "query", "name": "url", "type": "string", "x-example": "https://www.imdb.com/title/tt1375666/"}, {"description": "Rows to return, default 50, max 100", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/imdb/title/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["imdb-charts", "imdb-image-types", "imdb-name", "imdb-name-awards", "imdb-name-credits", "imdb-name-images", "imdb-name-videos", "imdb-search", "imdb-search-title", "imdb-title", "imdb-title-awards", "imdb-title-box-office", "imdb-title-company-credits", "imdb-title-connections", "imdb-title-credits", "imdb-title-episodes", "imdb-title-filming-locations", "imdb-title-goofs", "imdb-title-images", "imdb-title-keywords", "imdb-title-parental-guide", "imdb-title-public-facts-analysis", "imdb-title-quotes", "imdb-title-ratings", "imdb-title-release-info", "imdb-title-reviews", "imdb-title-similar", "imdb-title-technical-specs", "imdb-title-trivia", "imdb-title-videos"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-imdb-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = Net::HTTP::Get.new(uri)
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = @transport.call(url, request.to_hash, @timeout)
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('charts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-charts', params, response_type: response_type)
      end
      define_method('image_types') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-image-types', params, response_type: response_type)
      end
      define_method('name') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-name', params, response_type: response_type)
      end
      define_method('name_awards') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-name-awards', params, response_type: response_type)
      end
      define_method('name_credits') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-name-credits', params, response_type: response_type)
      end
      define_method('name_images') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-name-images', params, response_type: response_type)
      end
      define_method('name_videos') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-name-videos', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-search', params, response_type: response_type)
      end
      define_method('search_title') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-search-title', params, response_type: response_type)
      end
      define_method('title') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title', params, response_type: response_type)
      end
      define_method('title_awards') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-awards', params, response_type: response_type)
      end
      define_method('title_box_office') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-box-office', params, response_type: response_type)
      end
      define_method('title_company_credits') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-company-credits', params, response_type: response_type)
      end
      define_method('title_connections') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-connections', params, response_type: response_type)
      end
      define_method('title_credits') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-credits', params, response_type: response_type)
      end
      define_method('title_episodes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-episodes', params, response_type: response_type)
      end
      define_method('title_filming_locations') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-filming-locations', params, response_type: response_type)
      end
      define_method('title_goofs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-goofs', params, response_type: response_type)
      end
      define_method('title_images') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-images', params, response_type: response_type)
      end
      define_method('title_keywords') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-keywords', params, response_type: response_type)
      end
      define_method('title_parental_guide') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-parental-guide', params, response_type: response_type)
      end
      define_method('title_public_facts_analysis') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-public-facts-analysis', params, response_type: response_type)
      end
      define_method('title_quotes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-quotes', params, response_type: response_type)
      end
      define_method('title_ratings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-ratings', params, response_type: response_type)
      end
      define_method('title_release_info') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-release-info', params, response_type: response_type)
      end
      define_method('title_reviews') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-reviews', params, response_type: response_type)
      end
      define_method('title_similar') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-similar', params, response_type: response_type)
      end
      define_method('title_technical_specs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-technical-specs', params, response_type: response_type)
      end
      define_method('title_trivia') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-trivia', params, response_type: response_type)
      end
      define_method('title_videos') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('imdb-title-videos', params, response_type: response_type)
      end

      private

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
