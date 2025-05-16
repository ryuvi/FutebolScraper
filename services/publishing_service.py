from components.webdriver_manager import WebDriverManager
from components.auth import SiteAuthenticator
from components.publisher import ContentPublisher

class PublishingService:
    @staticmethod
    def publish_content(event_name: str, content: str, rounds: str, headless=False, debug=False):
        """
        Publica conteúdo no site
        
        :param event_name: Nome do evento a ser editado
        :param content: Conteúdo HTML a ser publicado
        :param headless: Executar em modo headless
        :param debug: Manter sessão aberta para debug
        """
        # 1. Inicializar WebDriver
        driver_manager = WebDriverManager(headless=headless)
        driver = driver_manager.create_driver()
        
        try:
            # 2. Autenticar
            authenticator = SiteAuthenticator(driver)
            authenticator.login()
            authenticator.navigate_to_events()
            
            # 3. Publicar conteúdo
            publisher = ContentPublisher(driver)
            if publisher.find_and_edit_event(event_name):
                publisher.update_content(content, rounds)
                
                # Descomente para salvar automaticamente
                if debug:
                    publisher.keep_session_active()
                else:
                    publisher.save_changes()
                    
            else:
                print(f"Evento '{event_name}' não encontrado!")
        
        except Exception as e:
            print(f"Erro durante a publicação: {str(e)}")
            raise
        
        finally:
            if not debug:
                driver.quit()