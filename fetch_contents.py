import requests
import urllib.parse
from time import sleep

from config import SCRAPBOX_PROJECT_NAME


def page_list_api(limit):
    return f'https://scrapbox.io/api/pages/{SCRAPBOX_PROJECT_NAME}?limit={limit}'


def page_contents_api(page_title):
    return f'https://scrapbox.io/api/pages/{SCRAPBOX_PROJECT_NAME}/{urllib.parse.quote(page_title)}/text'


def fetch_from_scrapbox():

    if not SCRAPBOX_PROJECT_NAME:
        raise ValueError('SCRAPBOX_PROJECT_NAME is not set.')

    response = requests.get(page_list_api(1000)).json()
    pages = response.get('pages')

    page_contents = []
    page_count = len(pages)

    for i, page in enumerate(pages):
        page_title = page.get('title')
        sleep(0.3)
        print(f'({i: 4}/{page_count}) Fetching {page_title}...')
        response = requests.get(page_contents_api(page_title))
        page_contents.append(response.text)

    return ' '.join(page_contents)
