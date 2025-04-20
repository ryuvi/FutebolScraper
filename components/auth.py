# auth.py
from selenium.webdriver.remote.webdriver import WebDriver
from components.config import ELEMENT_SELECTORS
from selenium.webdriver.common.by import By
from time import sleep
from load_dotenv import load_dotenv
import os
load_dotenv()

LOGIN_CREDENTIALS = {
    'url': os.getenv('LOGIN_URL'),
    'email': os.getenv('LOGIN_EMAIL'),
    'password': os.getenv('LOGIN_PASSWORD')
}

class SiteAuthenticator:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def login(self):
        """Realiza o login no site"""
        self.driver.get(LOGIN_CREDENTIALS['url'])
        
        # Preencher credenciais
        self._find_and_send_keys(ELEMENT_SELECTORS['email'], LOGIN_CREDENTIALS['email'])
        self._find_and_send_keys(ELEMENT_SELECTORS['password'], LOGIN_CREDENTIALS['password'])
        
        # Clicar no botão de login
        self._find_and_click(ELEMENT_SELECTORS['login_button'])
        
        # Esperar login ser concluído
        sleep(2)
    
    def navigate_to_events(self):
        """Navega para a página de eventos"""
        self._find_and_click(ELEMENT_SELECTORS['eventos_link'])
        sleep(2)
    
    def _find_and_send_keys(self, xpath: str, text: str):
        element = self.driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(text)
    
    def _find_and_click(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()