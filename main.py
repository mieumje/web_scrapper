# requests 사용방법
""" import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass')) """


import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&limit=50')


print(indeed_result.text)
