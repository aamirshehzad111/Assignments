from bs4 import BeautifulSoup
from pandas import DataFrame
from urllib.request import urlopen
import re

def Scrapper(url):
    url_client = urlopen(url)
    page_html = url_client.read()
    url_client.close()

    page_soup = BeautifulSoup(page_html, "html.parser")
    containers = page_soup.findAll('div', {"class": "col-md-3 col-sm-4"})
    # print(len(containers))
    # container=containers[0]
    # print(container.div.img["alt"])
    # price=container.findAll("div", {"class":"pro-content text_ac"})
    # p=price[0].text
    title = []
    price = []

    for container in containers:
        title.append(container.div.img["alt"])
        price_of_prouct = container.findAll("div", {"class": "pro-content text_ac"})
        price.append(re.findall('\d+', price_of_prouct[0].text))

    Orginal_price = []
    Discounted_price = []
    for p in price:
        Orginal_price.append(p[0])
        Discounted_price.append(p[1])

    d = {'Product Name': title,
         'Original Price': Orginal_price,
         'Discounted Price': Discounted_price
         }

    df = DataFrame(d)
    df.to_csv('pakstyle1.csv', index=True, encoding='utf-8')
    print(df.iloc[:, 1:])


Scrapper(url="https://www.pakstyle.pk/cat/womens")