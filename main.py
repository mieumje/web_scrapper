import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&limit=50')

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all('a')

print(pages)
