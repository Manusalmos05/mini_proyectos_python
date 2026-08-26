import requests
from bs4 import BeautifulSoup

"""
req= requests.get("https://quotes.toscrape.com/")

soup=BeautifulSoup(req.text)

quotes_tags=soup.select("div.quote")
for quote_tag in quotes_tags:
    print (quote_tag.select("span.text")[0].getText())
    print (quote_tag.select("small.author")[0].getText())
    for tag in quote_tag.select("div.tags a.tag"):
        print(tag.getText(), end=" ")
    print("\n")
"""
def scrap_quotes(url="/page/3"):
    dominian="https://quotes.toscrape.com/"
    reqs= requests.get(f"{dominian}{url}")
    soups=BeautifulSoup(reqs.text)
    quotes=[]

    quotes_t=soups.select("div.quote")
    for quote_t in quotes_t:
        quote={}
        quote['text']=quote_t.select("span.text")[0].getText()
        quote['author']=quote_t.select("small.author")[0].getText()
        quote['tags']=[]

        for tag in quote_t.select("div.tags a.tag"):
            quote['tags'].append(tag.getText())
        quotes.append(quote)

    return quotes

quotes=scrap_quotes()

for quote in quotes:
    print(quote['text'])
    print(quote['author'])
    for tag in quote['tags']:
        print(tag, end=" ")
    print("\n")
