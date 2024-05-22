from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)

responseText = response.text

soup = BeautifulSoup(responseText, 'lxml')

#print(soup.prettify())
article = soup.find('article', class_='main-article').get_text(strip=True, separator=' ')


# .get_text() deixa os dados desorganizados no excel
# para contornar este problema, usar .get_text(strip=True, separator=' ')
# isso basicamente deleta os espaços das palavras

# para escrever em um arquivo .txt

with open ('teste.txt', 'w') as file:
    # basicamente significa "com o arquivo 'aqruivo.txt' aberto no 'write' mode como file"
    file.write(article)