from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com")

soup = BeautifulSoup(resp.text, "lxml")
for link in soup.find_all("a"):
    href = link['href']
    if href != '#':
      print(href)
