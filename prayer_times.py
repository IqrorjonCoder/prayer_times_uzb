from bs4 import BeautifulSoup
import requests


def sana(soup):
    sana_div = soup.find('div', class_="button")
    sana = sana_div.find("h5", class_='vil')
    print("")
    print(sana.text.replace("\n", "").replace("                ", ""))


def table(soup):
    divs = soup.find('div', class_='ad__container')

    nomi = divs.find_all('h2')
    vaqti = divs.find_all('p')

    nom_list = []
    vaqt_list = []

    for i in nomi:   nom_list.append(str(i.text))

    for i in vaqti:
        if len(i.text) == 5:    vaqt_list.append(str(i.text))

    print(f"{'-' * 25}".center(40))
    for i in range(6):
        print(f"| {nom_list[i].center(10)} |  {vaqt_list[i]}   |".center(40))
    print(f"{'-' * 25}".center(40))


def get_time(soup):
    c_time = soup.find('div', class_="current_time")
    spans = c_time.find_all('span')
    c_time_result = ""
    for i in spans:
        c_time_result += i.text

    print(f"\n{c_time_result}\n")


def _main():
    req = requests.get("https://namozvaqti.uz/")
    soup = BeautifulSoup(req.text, "html.parser")
    sana(soup)
    get_time(soup)
    table(soup)


_main()