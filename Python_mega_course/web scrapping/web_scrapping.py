import requests
from bs4 import BeautifulSoup

r = requests.get("http://pythonhow.com/example.html")
c = r.content

soup = BeautifulSoup(c, "html.parser")

# print(soup.prettify())

all = soup.find_all("div", {"class": "cities"})

for item in all:
    print(item.find_all("h2")[0].text)

