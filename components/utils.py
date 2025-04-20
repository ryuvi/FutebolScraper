# utils.py
import requests
from parsel import Selector
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page(url: str) -> Selector:
    """Busca a página e retorna um objeto Selector"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return Selector(response.text)

def save_to_excel(html_table: str, filename: str = 'tabela.xlsx'):
    """Salva uma tabela HTML em arquivo Excel"""
    pd.read_html(html_table)[0].to_excel(filename)

def process_team_cells(html: str) -> str:
    """Processa células de time com BeautifulSoup"""
    soup = BeautifulSoup(html, 'html.parser')
    for td in soup.find_all('td'):
        img = td.find('img')
        if img and td.text.strip():
            span = soup.new_tag('span')
            span.string = td.text.strip()
            td.clear()
            td['class'] = td.get('class', []) + ['team-cell']
            td.append(img)
            td.append(span)
    return str(soup)