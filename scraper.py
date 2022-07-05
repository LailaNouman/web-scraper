import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    paragraph_cards = soup.find_all("p")
    counter = 0
    for paragraph in paragraph_cards:
        span = paragraph.find_all('span')
        counter += len(span)
    return counter


def get_citations_needed_report(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    paragraph_cards = soup.find_all("p")
    need_citation = ""
    for paragraph in paragraph_cards:
        span = paragraph.find_all('span')
        # print(span)
        if span:
            need_citation += "-" + paragraph.contents[0].strip() + '\n'
    return need_citation


report = get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
print(report)
print(f'the number of citations needed is {get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")}')