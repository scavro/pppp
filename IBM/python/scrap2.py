import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error al obtener la página {url}: {e}")
        return None

def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        full_url = urljoin(base_url, href)
        if full_url.startswith(('http://', 'https://')):
            links.append(full_url)
    return links

def find_magnet_links(html):
    magnet_pattern = re.compile(r'magnet:\?xt=urn:btih:[a-zA-Z0-9]*')
    return magnet_pattern.findall(html)

def scrape_magnet_links(url):
    magnet_links = set()
    
    # Obtener contenido de la página inicial
    initial_html = get_page_content(url)
    if initial_html:
        # Buscar enlaces magnéticos en la página inicial
        magnet_links.update(find_magnet_links(initial_html))
        
        # Obtener todos los enlaces de la página inicial
        links = extract_links(initial_html, url)
        
        # Explorar los enlaces de segundo nivel
        for link in links:
            print(f"Explorando: {link}")
            secondary_html = get_page_content(link)
            if secondary_html:
                magnet_links.update(find_magnet_links(secondary_html))
    
    return list(magnet_links)

def save_to_file(links):
    try:
        with open('enlaces.txt', 'a') as file:
            for link in links:
                file.write(link + '\n')
        print(f"Se han guardado {len(links)} enlaces en enlaces.txt")
    except IOError as e:
        print(f"Error al guardar en el archivo: {e}")

def main():
    while True:
        url = input("Introduce la URL de la página de torrents (o escribe 'salir' para terminar): ")
        
        if url.lower() == 'salir':
            print("Saliendo del programa...")
            break
        
        print(f"Buscando enlaces magnéticos en {url} y en las páginas enlazadas...")
        magnet_links = scrape_magnet_links(url)
        
        if magnet_links:
            print(f"Se encontraron {len(magnet_links)} enlaces magnéticos únicos:")
            for link in magnet_links:
                print(link)
            save_to_file(magnet_links)
        else:
            print("No se encontraron enlaces magnéticos en la página ni en las páginas enlazadas.")

if __name__ == "__main__":
    main()