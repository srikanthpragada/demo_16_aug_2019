from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")

# must install lxml to use xml
soup = BeautifulSoup(resp.text, "xml")
for item in soup.find_all("item"):
    print(item.find("title").text.strip(" ").strip("\n"))
