# auth.py
from selenium.webdriver.remote.webdriver import WebDriver
from components.config import ELEMENT_SELECTORS
from selenium.webdriver.common.by import By
from time import sleep
from load_dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_CREDENTIALS = {
    'url': os.getenv('LOGIN_URL'),
    'email': os.getenv('LOGIN_EMAIL'),
    'password': os.getenv('LOGIN_PASSWORD')
}



class SiteAuthenticator:
    def __init__(self, driver: WebDriver):
        load_dotenv()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60*5)
    
    def login(self):
        """Realiza o login no site"""
        print(LOGIN_CREDENTIALS)
        self.driver.get('http://'+LOGIN_CREDENTIALS['url'])

        sleep(2)
        
        # Preencher credenciais
        self._find_and_send_keys(ELEMENT_SELECTORS['email'], LOGIN_CREDENTIALS['email'])
        self._find_and_send_keys(ELEMENT_SELECTORS['password'], LOGIN_CREDENTIALS['password'])
        
        # Clicar no botão de login
        self._find_and_click(ELEMENT_SELECTORS['login_button'])
        
        # Esperar login ser concluído
        sleep(2)
    
    def navigate_to_events(self):
        """Navega para a página de eventos"""
        self._find_and_click('//a[@id="minhas-ligas"]')
        sleep(2)
    
    def _find_and_send_keys(self, xpath: str, text: str):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        element.clear()
        element.send_keys(text)
    
    def _find_and_click(self, xpath: str):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).click()