import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_page_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_links(page_content, base_url):
    soup = BeautifulSoup(page_content, "html.parser")
    links = []
    for link in soup.find_all("a", href=True):
        full_url = urljoin(base_url, link["href"])
        links.append(full_url)
    return links

def web_crawler(start_url, max_pages=10):
    visited_pages = set()
    pages_to_visit = [start_url]

    while pages_to_visit and len(visited_pages) < max_pages:
        current_url = pages_to_visit.pop(0)
        if current_url not in visited_pages:
            try:
                print(f"Crawling: {current_url}")
                page_content = get_page_content(current_url)
                links = extract_links(page_content, current_url)
                pages_to_visit.extend(links)
                visited_pages.add(current_url)
            except requests.HTTPError as e:
                print(f"Failed to crawl {current_url}: {e}")

    return visited_pages

if __name__ == "__main__":
    start_url = "https://as.com"
    crawled_pages = web_crawler(start_url)
    print("Crawled pages:")
    for page in crawled_pages:
        print(page)
