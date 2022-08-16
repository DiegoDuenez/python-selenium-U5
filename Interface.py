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

    '''def util(self, method):
        self.wait = self.wait.util(method)
        return self'''

    def element(self, method, type, html):
        if type == 'CSS':
            type = By.CSS_SELECTOR
        if type == 'ID':
            type = By.ID 
        if type == 'ID':
            type = By.TAG_NAME 
        self.wait = self.wait.util(method(type, html))


    def css(self):
        self.CSS = True
        return self
    
    def clickable(self, html):
        if self.CSS:
             self.wait = self.wait.util(EC.element_to_be_clickable(By.CSS_SELECTOR, html))
        
        return self
    
    #def util
    
    def open(self):
        self.driver.get(self.site)