import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint

WIKI_TEMPLATE = 'https://imslp.org/wiki/{name}'

def get_name(composition):
    try:
        return composition[2][1][0]
    except TypeError:
        return None

def get_difficulty(composition):
    try:
        return composition[1][2]
    except TypeError:
        return None

def find_midi_links(name):
    src = requests.get(WIKI_TEMPLATE.format(name=name)).text
    doc = BeautifulSoup(src, features="lxml")
    mid_file_tags = doc(text='MID file')
    file_blocks = [tag.find_parent('div', {'class','we_file_first'}) for tag in mid_file_tags]
    links = [block.find('div',{'class':'we_file_download'}).find('a', href=True)['href'] for block in file_blocks]
    print(links)
    return links

def get_names_and_difficulties():
    with open('../raw_data/imslp_difficulty.json', encoding='utf-8') as f:
        doc = json.load(f)
        names = [get_name(composition) for composition in doc]
        difficulties = [get_difficulty(composition) for composition in doc]

    return names, difficulties

if __name__ == '__main__':
    names, difficulties = get_names_and_difficulties()
    find_midi_links('120_Handstücke_für_angehende_Klavierspieler_(Türk,_Daniel_Gottlob)')