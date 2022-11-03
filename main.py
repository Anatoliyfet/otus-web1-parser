import requests
from bs4 import BeautifulSoup as bs
import csv

# constants
URL = 'https://javascript.info/'
BASE_URL = 'https://www.avito.ru'
ATTR_HREF = {'class': ['Link', 'ListingItemTitle__link']}
LINK = 'list-sub__link'
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def export_to_csv(it_href):
    with open('href.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(it_href)

def do_parse(iv_url):
    html = requests.get(url=iv_url, headers=HEADERS).text
    soup = bs(html, 'html.parser')
    # print(soup)
    table_href = soup.find_all('a', class_=LINK)
    '''attrs=ATTRS_HREF)'''
    # print(table_href)
    list_href = []
    i = 0
    for href in table_href:
        i += 1
        lv_link = href.get('href')
        lv_url = URL + lv_link
        print(f' Ссылка {i} {lv_url}')
        list_href.append(lv_url)
        do_parse(lv_url)
    return list_href
def main():
    # proxies = {
    #     'htpp': '212.46.230.102:6969'
    # }
    it_list_href = do_parse(URL)
    export_to_csv(it_list_href)

if __name__ == '__main__':
    main()
