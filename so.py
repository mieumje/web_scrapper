import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=python&pg=2"


def get_last_page():
    resulst = requests.get(URL)
    soup = BeautifulSoup(resulst.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)
    return last_pages


def get_jobs():
    last_page = get_last_page()
    print(last_page)
    return []
