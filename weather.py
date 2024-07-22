from bs4 import BeautifulSoup
import requests

search = "weather in vettaikaranpudur"

url=f"http://www.google.com/search?&q={search}"

r = requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
update=soup.find("div",class_="BNeawe").text                
print(update)
