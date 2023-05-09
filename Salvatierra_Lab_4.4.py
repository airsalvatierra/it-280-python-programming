import requests
import validators
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

print('Welcome to checking website links')
print(
    'If you want to test unsecured sites, you should explicity write the '
    'full http url'
)
url: str = input('Enter a url or a website: ').strip()
while not url:
    url = input('Enter a url or a website: ').strip()

# The request package needs schema or protocol
if not url.startswith('http') or not url.startswith('https'):
    url = f'https://{url}'

try:
    print(f'{url} website will be tested')
    response = requests.get(url)
    website_content = BeautifulSoup(response.content, 'html.parser')
    # get all ling tags
    all_links = website_content.find_all('a')

    for link in all_links:
        link_url = link.get('href')

        # only tests valid urls sites
        if not link_url or not validators.url(link_url):
            continue

        message = f'Link {link_url} is: '
        try:
            response = requests.get(link_url, timeout=(None, 20))
            print(message + 'Good')
        except RequestException:
            # If the exception occur, it means that the link is broken
            print(message + 'Broken')

except RequestException as e:
    print(f'It was not possible to access the given url. The error is: {e}')
