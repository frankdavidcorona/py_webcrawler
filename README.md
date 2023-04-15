# Simple Web Crawler

A basic web crawler that retrieves and extracts links from web pages, starting with a specified URL.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

To install the required libraries, run:

```bash
pip install requests beautifulsoup4
```

## Usage

```python
from web_crawler import web_crawler

start_url = "https://example.com"
crawled_pages = web_crawler(start_url, max_pages=10)
```

## Example

```python
from web_crawler import web_crawler

start_url = "https://as.com"
crawled_pages = web_crawler(start_url)

print("Crawled pages:")
for page in crawled_pages:
    print(page)
```
