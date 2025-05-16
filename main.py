from services.scraping_service import ScrapingService
from services.publishing_service import PublishingService
from components.config import BASE_URL

import argparse

is_debug = True

def set_debug(value: bool):
    global is_debug
    is_debug = value

def get_debug():
    return is_debug

def get_league_title(url: str):
    league_title = url.rstrip('/').lstrip('https://').split('/')[-1]
    if league_title:
        league_title = ' '.join([word.capitalize() for word in league_title.split('-')])
        return league_title

def main(league: str):
    url = BASE_URL[league]

    print("Agora, Liga: " + league)

    # 1. Executar scraping
    print("Iniciando processo de scraping...")

    # 1. Executar scraping
    title = get_league_title(url)
    table_content, rounds_content = ScrapingService.scrape_and_save(url, title)

    # 2. Publicar conteúdo
    print("\nIniciando processo de publicação...")
    import sqlite3

    conn = sqlite3.connect('../cms/database.sqlite')
    cur = conn.cursor()

    cur.execute(f"UPDATE leagues SET tabela_html=?, rodada_html=? WHERE nome=?;", (table_content, rounds_content, league))

    conn.commit()
    conn.close()

    # PublishingService.publish_content(
    #     event_name=league,
    #     content=table_content,
    #     rounds=rounds_content,
    #     headless=False, #(not get_debug()),  # Altere para True em produção
    #     debug=False #(get_debug())       # Altere para False em produção
    # )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Script para pegar e publicar as tabelas e rodadas de alguns campeonatos de futebol'
    )

    parser.add_argument(
        '--league',
        type=str,
        help='Campeonato para Pegar'
    )

    parser.add_argument(
        '--debug',
        action='store_true',
        help='Modo debug'
    )

    args = parser.parse_args()

    set_debug(args.debug)

    main(args.league)
