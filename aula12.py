from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)

responseJSON = response.content

soup = BeautifulSoup(responseJSON, 'lxml')
print(soup.prettify())