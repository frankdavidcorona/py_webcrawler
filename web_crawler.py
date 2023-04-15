import requests
from bs4 import BeautifulSoup

def get_links(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and not href.startswith('#'):
            links.append(href)
    return links

if __name__ == "__main__":
    url = input("Enter a URL to crawl: ")
    links = get_links(url)
    print("Links:")
    for link in links:
        print(link)
