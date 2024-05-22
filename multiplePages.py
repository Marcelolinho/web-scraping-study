from bs4 import BeautifulSoup
import requests
import time

website = 'https://subslikescript.com/movies'
response = requests.get(website)
