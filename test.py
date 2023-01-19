from bs4 import BeautifulSoup
import requests
from requests import get
import time
import random

url = 'https://v2.vost.pw/page/1/'

cars = []
count = 1
while count < 10:
    url = 'https://v2.vost.pw/page/1/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    car_data = html_soup.findAll('div', id='dle-content')
    if car_data != []:
        cars.extend(car_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break

    count += 1


print(len(cars))
print(cars[1])
print()
n = int(len(cars)) - 1
count = 0
while count <= 5:
    info = cars[int(count)]
    name = info.find('div', {'class':"shortstoryContent"}).text
    title = info.find('div', {'class':'shortstoryHead'}).find('a').text
    print(title, "", name)


    count += 1
