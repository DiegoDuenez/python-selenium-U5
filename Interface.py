from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
                
    
    def wait(self, time):
        self.wait = WebDriverWait(self.driver, time)
        return self

    '''def until(self, method):
        self.wait = self.wait.until(method)
        return self'''

    def element(self, method, type, html):
        if type == 'CSS':
            type = By.CSS_SELECTOR
        if type == 'ID':
            type = By.ID 
        if type == 'ID':
            type = By.TAG_NAME 
        self.wait = self.wait.until(method(type, html))


    def css(self):
        self.CSS = True
        return self

    def id(self):
        self.ID = True
        return self
    
    def keys(self, html, keys):
        if self.CSS:
            self.wait = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, html))).send_keys(keys)

        return self.wait

    def click(self, html):
        if self.CSS:
            self.wait = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, html))).click()

        return self.wait

    def text(self, html):
        if self.CSS:
            self.wait = self.wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, html)).text
            return self.wait
         
    
    #def until
    
    def open(self):
        self.driver.get(self.site)