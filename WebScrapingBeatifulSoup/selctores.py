import requests
from bs4 import BeautifulSoup

import re

url = "https://es.wikipedia.org/wiki/Python"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


try:
    req = requests.get(url, headers=headers, timeout=10)
    req.raise_for_status()
    soup=BeautifulSoup(req.text)
    title = soup.select("title")[0].getText()
    print(title)
except requests.exceptions.Timeout:
    print("El servidor de Archive.org tardó demasiado en responder.")
except requests.exceptions.RequestException as e:
    print(f"Error en la petición: {e}")


resumen=soup.select("p")[0].getText()
print(resumen)


toc=soup.select("#vector-toc")[0]

for a in toc.select("a"):
    print(a.getText())


for a in toc.select("a"):
    text = a.getText()
    if re.match(r"\d+ ", text):
        print(text)
    elif re.match(r"\d+.\d+ ", text):
        print(" ", text)
    elif re.match(r"\d+.\d+.\d+ ", text):
        print("   ", text)