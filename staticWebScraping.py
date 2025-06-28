from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.newegg.com/p/pl?d=gtx")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.find_all("a", class_="item-title")


for item in items:
    print(item.text)

driver.quit()
