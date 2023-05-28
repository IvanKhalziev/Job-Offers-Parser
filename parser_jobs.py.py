import requests
import pandas as pd
from bs4 import BeautifulSoup

PATH = 'Job_offers.xlsx'
HOST = 'https://www.azubiyo.de/'
URL = 'https://www.azubiyo.de/ausbildung/fachinformatiker-anwendungsentwicklung/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r.text


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(
        'div', class_='col-lg-12 col-md-6 mb-3 mb-md-30px mb-lg-3')
    vacancies_info_array = []

    for item in items:
        location_element = item.find('span', class_='')
        date_element = item.find_all(
            'li', class_='d-flex align-items-center mr-md-3 font-size-12')[1]

        vacancies_info_array.append(
            {
                'Name of job': item.find('h3', class_='az-hyphenate break-word mb-1 font-size-16').get_text(),
                'Company': item.find('p', class_='az-hyphenate break-word mb-1 font-size-16').get_text(),
                'Location': location_element.get_text() if location_element else '',
                'Date of start': date_element.get_text(strip=True) if date_element else ''
            }
        )

    return vacancies_info_array


def save_doc(items, path):
    df = pd.DataFrame(items)
    df.to_excel(path, index=False)


def parser():
    PAGINATION = input("How many pages do you want to parse: ")
    PAGINATION = int(PAGINATION.strip())
    vacansies_info_array = []

    if requests.get(URL, headers=HEADERS).status_code == 200:
        for page in range(1, PAGINATION + 1):
            print(f"Parsing page: {page}")
            page_url = f"{URL}{page}/"
            html = get_html(page_url)
            page_data = get_content(html)
            vacansies_info_array.extend(page_data)
    else:
        print('Error')

    save_doc(vacansies_info_array, PATH)


parser()
