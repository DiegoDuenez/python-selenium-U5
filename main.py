from app.Interface import Interface
from selenium.webdriver.common.keys import Keys

interface = Interface('chrome', 'http://localhost/selenium-toro/')

interface.open()

# interface.wait(15).css().click('input#correo')

interface.wait(5).css().keys('input#correo', "Hola" + Keys.TAB)
