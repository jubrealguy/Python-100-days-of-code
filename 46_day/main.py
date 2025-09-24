from bs4 import BeautifulSoup
import requests

date = input("what year you would like to travel to in YYY-MM-DD format. e.g. 2000-08-12 ?\n")
res = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
web_page = res.text

soup = BeautifulSoup(web_page, "html.parser")
print(soup)