from bs4 import BeautifulSoup
#lxml


with open("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_28/website.html", encoding="utf8") as data:
    content = data.read()

soup = BeautifulSoup(content, "html.parser")
title = soup.title

all = soup.find_all(name = "a")
for tag in all:
    print(tag.getText())
    print(tag.get("href"))