from components.config import BASE_URL, STYLES
from components.utils import fetch_page, save_to_excel, process_team_cells
from components.scraper import BrasileiraoScraper

class ScrapingService:
    @staticmethod
    def generate_html_page(league_title: str, table_html: str, round_title: str, rounds_html: str) -> str:
        """Gera a página HTML completa"""
        full_page = f"""
        <div>
        <h1>{league_title}</h1>
        {table_html}
        <div>
        <h2>{round_title}</h2>
        """

        for round_ in rounds_html:
            full_page += round_

        full_page += "</div></div>"

        return full_page
    
    @classmethod
    def generate_rounds(cls, roundstitle, rounds) -> str:
        page = f"""
    <div>
    <h2>{roundstitle}</h2>
    """
        
        for round_ in rounds:
            page += round_

        page += "</div>"

        return page

    @classmethod
    def scrape_and_save(cls, url: str, league_title: str):
        """Executa todo o processo de scraping e salva os resultados"""
        # 1. Obter a página
        selector = fetch_page(url)
        
        # 2. Inicializar o scraper
        scraper = BrasileiraoScraper(selector)
        
        # 3. Extrair dados
        table_html = scraper.get_table()
        round_title, rounds_html = scraper.get_current_round()
        
        # 4. Processar dados
        # processed_table = process_team_cells(table_html)
        # save_to_excel(table_html)
        
        # 5. Gerar página final
        full_page = cls.generate_html_page(league_title, table_html, round_title, rounds_html)
        
        print("Processo de scraping concluído! Verifique o arquivo index.html")
        return table_html, cls.generate_rounds(round_title, rounds_html)