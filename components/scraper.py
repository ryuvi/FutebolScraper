# scraper.py
from typing import Tuple
from parsel import Selector

class BrasileiraoScraper:
    def __init__(self, selector: Selector):
        self.selector = selector
    
    def get_table(self) -> str:
        """Extrai a tabela de classificação"""
        table_html = self.selector.css('section#classificacao-geral').css('table.table-classification--expansive').get()
        return table_html

    def get_current_round(self) -> Tuple[str, str]:
        """Extrai informações da rodada atual"""
        rounds_title = self.selector.css("div.rounds").css('h3.rounds__title::text').get().strip()
        
        rounds = self.selector.xpath('.//article[contains(@class, "card-match")]').getall()

        return rounds_title, rounds
    

