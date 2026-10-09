import os

from crawlora_imdb import IMDbClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with IMDbClient(api_key=api_key) as client:
    search = client.search(query='Inception')
    print('search', search)
    charts = client.charts()
    print('charts', charts)
