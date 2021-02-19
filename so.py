import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=python&pg=2"


def get_last_page():
    resulst = requests.get(URL)
    soup = BeautifulSoup(resulst.text, "html.parser")
    pagination = soup.find("div", {"class": "s-pagination"})
    print(pagination)


def get_jobs():
    last_page = get_last_page()
    return []
