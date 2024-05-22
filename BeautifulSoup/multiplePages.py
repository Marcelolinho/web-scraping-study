from bs4 import BeautifulSoup
import requests
import time

root = 'https://subslikescript.com' # Basicamente cria um escopo maior para a raspagem
website = f'{root}/movies'

try:
    response = requests.get(website)
    content = response.text

    soup = BeautifulSoup(content, 'lxml')

    article = soup.find('article', class_='main-article')

    links = []

    for link in article.find_all('a', href=True):
        links.append(link['href'])
        time.sleep(1)

    #print(links)
    
    for link in links:
        website = f'{root}/{link}'
        
        response = requests.get(website)
        content = response.text
        soup = BeautifulSoup(content, 'lxml')

        article = soup.find('article', class_='main-article')

        title = article.find('h1').get_text()
        text = article.find('div', class_='full-script').get_text(strip=True, separator=' \n')

        with open (f'./BeautifulSoup/Roteiros/{title}.txt', 'w') as file:
            file.write(text)

except requests.exceptions.RequestException as e:
    print(f'Erro ao fazer a request: {e}')
except AttributeError as e:
    print(f'Erro de atribuição: {e}')
except Exception as e:
    print(f'Exceção: {e}')