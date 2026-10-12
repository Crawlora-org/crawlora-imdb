require_relative "lib/crawlora/imdb/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-imdb"
  spec.version = Crawlora::Imdb::VERSION
  spec.summary = "IMDb API client for Crawlora (30 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted IMDb API. Covers title and name search, charts, ratings, credits, awards, episodes, reviews, images, and title metadata across 30 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=imdb-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-imdb", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-imdb/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
