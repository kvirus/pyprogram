import requests
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
import pandas as pd
import openpyxl
from openpyxl.drawing.image import Image
from selenium.webdriver.common.by import By
import io
from io import BytesIO
from PIL import Image

url = 'https://www.avito.ru/rostov-na-donu/avtomobili/nissan/qashqai/mehanika-ASgCAQICA0Dgtg0U~pgo4rYNFNqtKPC2DRTstyg?cd=1&radius=200&s=1&searchRadius=200'


driver = webdriver.Chrome()

try:
    driver.get(url=url)
    html = driver.page_source
    response = BeautifulSoup(html, "lxml")
    find_p = response.find_all('div', {'data-marker':'item'})
    #find_p = response.find_all("a",href = True)

    # Создаем новый файл Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = '1'
    sheet['B1'] = '2'
    xx=len(find_p)
    i=1
    name = f'Товар {i}'


    for d in find_p:
        #img_element = driver.find_element(By.TAG_NAME, 'img')
        #print(img_element)
        #img_url = img_element.get_attribute('src')
        #response1 = requests.get(img_url)
        #img_data = response1.content
        #img1 = Image.open(BytesIO(response1.content))
        #img1 = Image.open(requests.get(img_url, stream=True).raw)
        #img1.show()
        #sheet.add_image(img1, 'С1')
        price = d.text
        sheet[f'A{i + 1}'] = name
        sheet[f'B{i + 1}'] = price
        i=i+1
    workbook.save('c:\\12.xlsx')
        # print(d.text)
        # df = pd.DataFrame({
        #     'Opisanie' : [d.text]
        # })
        # df.append(pd.DataFrame([d.text]))
        # df.to_excel('c:\\test.xlsx')

    # for a in find_p:
    #      print(a['content'])

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