import time
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class SmokeTest:

    def __init__(self):
        self.driver = self._init_driver()

    def _init_driver(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def fetch_title(self, url):
        self.driver.get(url)
        return self.driver.title
    
    def fetch_document_data(self, url, document_id='94913204'):
        veraz_information = {}
        veraz_information=requests.post(url+document_id)
        document_data = veraz_information
        print(document_data)
        return document_data

    def quit(self):
        if self.driver:
            self.driver.quit()


def fetch_document_data(url, document_id):
    try:
        response = requests.get(url + document_id, timeout=10)  # set a timeout
        response.raise_for_status()  # raises HTTPError for bad status codes

        # Assuming the API returns JSON; adjust if it returns plain text
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        # Log the error (replace with proper logging in real code)
        print(f"Error fetching document data from {url + document_id}: {e}")
        return None