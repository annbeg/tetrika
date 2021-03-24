from bs4 import BeautifulSoup
import requests

response = requests.request("GET", 'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from=А')
soup = BeautifulSoup(response.text, 'html.parser')
allLinksAs = soup.findAll('span', style="white-space:nowrap")[0].findAll('a', class_ = 'external text')
letter = soup.findAll('div', class_='mw-category-group')[0].find('h3').text
countOfAnimals = len(soup.findAll('div', class_='mw-category-group')[0].find('ul').findAll('li'))

listOfCounts = [(letter, countOfAnimals)]
print(f'{letter}: {countOfAnimals}')

for i in range(1, len(allLinksAs)):
    link = allLinksAs[i]['href']
    response = requests.request("GET", link)
    soup = BeautifulSoup(response.text, 'html.parser')
    letter = soup.findAll('div', class_='mw-category-group')[0].find('h3').text
    countOfAnimals = len(soup.findAll('div', class_='mw-category-group')[0].find('ul').findAll('li'))
    listOfCounts.append((letter, countOfAnimals))
    print(f'{letter}: {countOfAnimals}')
