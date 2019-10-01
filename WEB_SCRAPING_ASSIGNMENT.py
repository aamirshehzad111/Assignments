from bs4 import BeautifulSoup, Comment
from urllib.request import urlopen


def webPageScraping(url, file_name):
    u_client = urlopen(url)
    page_html = u_client.read()
    u_client.close()

    page_soup = BeautifulSoup(page_html, "html.parser")

    while len(page_soup.find_all('style')) > 0:
        page_soup.style.extract()

    # body = page_soup.find('body')
    # for element in body(text=lambda text: isinstance(text, Comment)):
    #     element.extract()

    main_container = page_soup.findAll("body")

    text_of_page = []
    for container in main_container:
        # p=container.findAll("p")
        text_of_page.append(container.text)

    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(text_of_page)
        # [(f.write(text)) for text in textwrap.fill(dedented_text, width=100)
    f.close()


url = "https://techcommunity.microsoft.com/t5/Azure-Service-Fabric/Service-Fabric-Customer-Profile-Societe-Generale-Geysir/ba-p/844918"
str_token = url.split(".")
file_name = str_token[1] + ".txt"
webPageScraping(url, file_name)
