from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)

responseText = response.text

soup = BeautifulSoup(responseText, 'lxml')

#print(soup.prettify())

box = soup.find('article', class_='main-article')

h1 = soup.find('h1').get_text()
titulo = box.find('h1').get_text()

print(h1)
print(titulo)

# .get_text() deixa os dados desorganizados no excel
# para contornar este problema, usar .get_text(strip=True, separator=' ')
# isso basicamente deleta os espaços das palavras

