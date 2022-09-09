import requests
from bs4 import BeautifulSoup
import json
import random
BASE_URL = 'http://web.chal.csaw.io:5010'
directory = "/piece"
cookie = 'stuff%20threw%20label%20explain%20chapter%20canal%20piece'

while True:
    url = BASE_URL + directory
    print(url)
    print(cookie)
    content = requests.get(url, cookies= {'solChain' : cookie}).text
    soup = BeautifulSoup(content, "html.parser")
    try:
        directory = str(soup.find("a", href=True).get('href'))
        cookie += '%20'
        cookie += directory[1:]
    except Exception as e:
        print(soup)