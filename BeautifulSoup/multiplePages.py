from bs4 import BeautifulSoup
import requests
import time

website = 'https://subslikescript.com/movies'

try:
    response = requests.get(website)
    content = response.text

    soup = BeautifulSoup(content, 'lxml')

    article = soup.find('article', class_='main-article')

    links = []

    for link in article.find_all('a', href=True):
        links.append(link['href'])
        time.sleep(1)

    print(links)


    """ for link in links:
        time.sleep(1) """
except requests.exceptions.RequestException as e:
    print(f'Erro ao fazer a request: {e}')
except AttributeError as e:
    print(f'Erro de atribuição: {e}')
except Exception as e:
    print(f'Exceção: {e}')