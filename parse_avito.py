import requests
from bs4 import BeautifulSoup
from requests import get
import time
import random

url = 'https://www.avito.ru/rostov-na-donu/avtomobili/nissan/qashqai/mehanika-ASgBAQICAkTgtg36mCjitg3arSgBQPC2DRTstyg?radius=200&searchRadius=200'
cars =[]
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
print(html_soup)