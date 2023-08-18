import requests
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
import time
import random
import time

url = 'https://www.avito.ru/rostov-na-donu/avtomobili/nissan/qashqai/mehanika-ASgCAQICA0Dgtg0U~pgo4rYNFNqtKPC2DRTstyg?cd=1&radius=200&s=1&searchRadius=200'


driver = webdriver.Chrome()

try:
    driver.get(url=url)
    html = driver.page_source
    response = BeautifulSoup(html, "lxml")
    find_p = response.text
    print(find_p)
    time.sleep(3)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

# cars =[]
# response = get(url)
# print(response.text)
# html = BeautifulSoup(response.text, "lxml")
# title = html.title
# t1 =title.text
# find_p = html.find('a')
#
# print(find_p.get('href'))