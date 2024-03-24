import requests
from bs4 import BeautifulSoup

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if 'track' in href or 'release' in href:
            full_link = f'https://beatport.com{href}'
            links.append(full_link)

    return links

def save_links_to_file(links, filename):
    with open(filename, 'w') as file:
        for link in links:
            file.write(f'{link}\n')

def main():
    url = input("Enter the URL: ")
    links = get_links(url)

    print("\nFound links:")
    for link in links:
        print(link)

    filename = 'links.txt'
    save_links_to_file(links, filename)
    print(f"\nLinks saved to {filename}")

if __name__ == "__main__":
    main()
