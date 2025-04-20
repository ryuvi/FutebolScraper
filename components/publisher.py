# publisher.py
from selenium.webdriver.remote.webdriver import WebDriver
from components.config import ELEMENT_SELECTORS
from selenium.webdriver.common.by import By
from time import sleep

class ContentPublisher:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def find_and_edit_event(self, event_name: str):
        """Encontra e edita um evento específico"""
        tabela = self.driver.find_element(By.XPATH, ELEMENT_SELECTORS['tabela_relacao'])
        
        for row in tabela.find_elements(By.XPATH, ELEMENT_SELECTORS['evento_row']):
            name = row.find_element(By.XPATH, ELEMENT_SELECTORS['evento_name']).text
            if name.strip() == event_name:
                row.find_element(By.XPATH, ELEMENT_SELECTORS['edit_button']).click()
                sleep(2)  # Esperar a página carregar
                return True
        return False
    
    def update_content(self, content: str):
        """Atualiza o conteúdo do editor"""
        textarea = self.driver.find_element(By.XPATH, ELEMENT_SELECTORS['textarea'])
        textarea.click()
        self.driver.execute_script("arguments[0].innerHTML = arguments[1];", textarea, content)
    
    def save_changes(self):
        """Salva as alterações (implementação depende do site)"""
        # Implemente conforme a necessidade do site
        save_button = self.driver.find_element(By.XPATH, ELEMENT_SELECTORS['save_button'])
        save_button.click()
        pass
    
    def keep_session_active(self):
        """Mantém a sessão ativa (para debug)"""
        while True:
            sleep(1)