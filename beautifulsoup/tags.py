import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title) #<title>Document</title>
# print(soup.title.string) # Document
# print(soup.title.string, type(soup.title.string)) #Document <class 'bs4.element.NavigableString'>
# print(soup.div)
# print(soup.find_all("div"))

# find all the link 
for link in soup.find_all("a"):
    print(link.get("href"))

s = soup.find(id="link3")
print(s) #<a href="/data/times.html" id="link3"></a>