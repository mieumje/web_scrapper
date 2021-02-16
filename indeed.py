import requests
from bs4 import BeautifulSoup

LIMIT = 20
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div", {"class": "pagination"})

    # pagination 변수에 찾은 결과를 넣어줌
    # 그 결과를 list로 만들어 pages 변수에 넣어줌

    # pages를 가져온 다음
    # 빈 array를 만들고
    # pages에 있는 각 page마다 span을 찾아서
    # 빈 array에 넣어준다.
    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]:  # '다음'버튼은 무시
        pages.append(int(link.string))

    max_page = pages[-1]
    # 페이지 숫자 중 가장 큰 수, 배열의 마지막 요소
    return max_page


def extract_jobs(html):  # 인자로 soup을 준다.
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("div", {"class": "sjcl"}).find("span")
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = company_anchor.string
    else:
        company = company.string
    return {'title': title, 'company': company}


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
        job = extract_jobs(result)
        print(job)
    return jobs
