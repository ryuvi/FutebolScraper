# webdriver_manager.py
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverManager:
    def __init__(self, headless=False):
        self.options = Options()
        if headless:
            self.options.add_argument('--headless')
        self.service = Service(ChromeDriverManager().install())
        
    def create_driver(self):
        return Chrome(service=self.service, options=self.options)