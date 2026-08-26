import requests
from bs4 import BeautifulSoup
req= requests.get("https://www.wf-energy.com/politica-de-privacidad")
soup=BeautifulSoup(req.text)


for meta in soup.select("meta"):
    for atributo, valor in meta.attrs.items():
        print(f"{atributo}:{valor}")
