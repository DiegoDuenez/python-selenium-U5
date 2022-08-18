from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Interface:

    ID = False
    XPATH = False
    LINK_TEXT = False
    PARTIAL_LINK_TEXT = False
    NAME = False
    TAG = False
    CLASS_NAME = False
    CSS = False

    def __init__(self, driver, site):

        self.site = site
        if driver == 'chrome':
            self.driver = webdriver.Chrome()
        if driver == 'firefox':
            self.driver = webdriver.Firefox()
        if driver == 'edge':
            self.driver = webdriver.Edge()
                
    def sleep(self, time):
        self.time = time
        return self

    def web(self):
        time.sleep(self.time)
        self.wait = WebDriverWait(self.driver, self.time)
        return self

    def element(self, event, by, selector, value = ""):
        if by == 'css':
            by = By.CSS_SELECTOR
        elif by == 'xpath':
            by = By.XPATH 
        if event == 'keys':
            return self.wait.until(EC.element_to_be_clickable((by, selector))).send_keys(value)
        elif event == 'click':
            return self.wait.until(EC.element_to_be_clickable((by, selector))).click()
        elif event == "select":
            s = Select(self.driver.find_element(by, selector))
            return s.select_by_value(value)
        elif event == "text":
            return self.wait.until(EC.element_to_be_clickable((by, selector))).text

    def open(self):
        self.driver.get(self.site)