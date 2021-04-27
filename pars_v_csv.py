#   импорт библиотек
import requests
from bs4 import BeautifulSoup
import csv

user_a = {
    'User-Agent': 'Mozilla / 5.0(iPad; CPU OS 11_0 like Mac OS X) AppleWebKit / 604.1 .34(KHTML, like Gecko) Version / 11.0 Mobile / 15 A5341f Safari / 604.1',
    'Accept-Language': 'ru, en; q = 0.9',
}


def get_html(url):
    response = requests.get(url, user_a)
    return response.text


def pars_one(html):
    links_str = []
    soup = BeautifulSoup(html, 'lxml')
    all_block = soup.find('div', class_="index-root-2c0gs")
    one_block = all_block.find_all('div',
                                   class_="iva-item-root-G3n7v photo-slider-slider-3tEix iva-item-list-2_PpT iva-item-redesign-1OBTh items-item-1Hoqq items-listItem-11orH js-catalog-item-enum")
    for i in one_block:
        links = i.find('a',
                       class_="link-link-39EVK link-design-default-2sPEv title-root-395AQ iva-item-title-1Rmmj title-listRedesign-3RaU2 title-root_maxHeight-3obWc").get(
            'href')
        link = f'https://www.avito.ru{links}'
        links_str.append(link.split(','))  # запись в список и удаление запятых
        print(link)
    return links_str


#   ЗАПИСЬ СПИСКА В CSV ФАЙЛ
def writer(date):
    with open("avito.csv", 'a', newline='', encoding='utf=16') as file:
        writer = csv.writer(file)
        writer.writerows(
            date
        )


def main():
    url = 'https://www.avito.ru/novodvinsk/vakansii?cd=1'
    html = get_html(url)
    link = pars_one(html)
    writer(link)


if __name__ == '__main__':
    main()
