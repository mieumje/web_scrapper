import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=python&pg=2"


def get_last_page():
    resulst = requests.get(URL)
    soup = BeautifulSoup(resulst.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)
    return int(last_pages)  # for 문의 in range에 사용하기 위해 integer로 형변환


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        print(result.status_code)


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
