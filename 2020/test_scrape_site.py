import requests
from bs4 import BeautifulSoup

YEAR = 2020
DAY = 6
SESSION_ID = "53616c7465645f5fec0de59dcb22942549edaa80deb4498cf25b1fb94b7ad561b377e004e238d17e029fa98ded4ccfa0"

aoc_day_url = f"https://adventofcode.com/{YEAR}/day/{DAY}"
cookies = dict(session=SESSION_ID)
response = requests.get(url=aoc_day_url, cookies=cookies)
txt = response.text

soup = BeautifulSoup(txt, "html.parser")
# print(soup.prettify())
codes = soup.find_all("pre")
for code in codes:
    print("-----------------------")
    print(code.getText())