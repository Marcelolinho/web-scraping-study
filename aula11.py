from bs4 import BeautifulSoup
import requests

website = 'https://pokes-info.netlify.app/'
response = requests.get(website)
content = response.content

soup = BeautifulSoup(content, 'lxml')

teste = soup.find('h2')
print(teste)
print(soup.find('h1'))