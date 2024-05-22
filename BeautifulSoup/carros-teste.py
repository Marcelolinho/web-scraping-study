from bs4 import BeautifulSoup
import requests
import time

root = 'https://vehicles-website.netlify.app/'
suvs = f'{root}/#/suvs'

try:
    response = requests.get(root)
    content = response.text
    

except requests.exceptions.RequestException as e:
    print(f'Erro de request: {e}')
except AttributeError as e:
    print(f'Erro de atribuição: {e}')
except Exception as e:
    print(f'Erro: {e}')