# publisher.py
from selenium.webdriver.remote.webdriver import WebDriver
from components.config import ELEMENT_SELECTORS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from json import dumps

class ContentPublisher:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_and_edit_event(self, event_name: str):
        """Encontra e edita um evento específico"""
        id = event_name.replace(' ', '-')
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, f'//a[@id="{id}"]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        sleep(5)
        element.click()
        sleep(5)
        return True
    
    def update_content(self, table: str, rounds: str):
        """Atualiza o conteúdo do editor"""
        self.driver.execute_script(f"$('#league_content_table').summernote('code', {dumps(table)});")
        self.driver.execute_script(f"$('#league_content_rounds').summernote('code', {dumps(rounds)});")
    
    def save_changes(self):
        """Salva as alterações (implementação depende do site)"""
        # Implemente conforme a necessidade do site
        element = self.driver.find_element(By.XPATH, f'//button[@id="submit"]')
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        sleep(5)
        element.click()
        pass
    
    def keep_session_active(self):
        """Mantém a sessão ativa (para debug)"""
        while True:
            sleep(1)