import requests
from bs4 import BeautifulSoup
import re

def scrape_magnet_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all 'a' tags with 'href' attribute
        links = soup.find_all('a', href=True)
        
        # Regular expression pattern for magnet links
        magnet_pattern = re.compile(r'magnet:\?xt=urn:btih:[a-zA-Z0-9]*')
        
        # Extract magnet links
        magnet_links = []
        for link in links:
            href = link['href']
            if magnet_pattern.match(href):
                magnet_links.append(href)
        
        return magnet_links
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

# Example usage
url = input("Enter the URL of the torrent page: ")
magnet_links = scrape_magnet_links(url)

if magnet_links:
    print("Found magnet links:")
    for link in magnet_links:
        print(link)
else:
    print("No magnet links found on the page.")