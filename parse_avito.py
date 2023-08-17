import requests
from bs4 import BeautifulSoup
from requests import get
import time
import random

url = 'https://www.avito.ru/rostov-na-donu/avtomobili/nissan/qashqai/mehanika-ASgBAQICAkTgtg36mCjitg3arSgBQPC2DRTstyg?radius=200&searchRadius=200'
cars =[]
response = get(url)

html = BeautifulSoup(response.text, "lxml")
title = html.title
t1 =title.text
find_p = html.find('a')

print(find_p.get('href'))