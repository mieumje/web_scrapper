import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=%ED%8C%8C%EC%9D%B4%EC%8D%AC&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch')

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div", {"class": "pagination"})

# pagination 변수에 찾은 결과를 넣어줌
# 그 결과를 list로 만들어 pages 변수에 넣어줌


# pages를 가져온 다음
# 빈 array를 만들고
# pages에 있는 각 page마다 span을 찾아서
# 빈 array에 넣어준다.
links = pagination.find_all('a')
pages = []

for link in links[:-1]:
    pages.append(int(link.string))


max_page = pages[-1]
# 페이지 숫자 중 가장 큰 수, 배열의 마지막 요소
