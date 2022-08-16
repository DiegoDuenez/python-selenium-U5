from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://localhost/selenium-toro/")



WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'input.imdb-header-search__input searchTypeahead__input react-autosuggest__input'.replace(' ','.'))))\
    .send_keys('Harry potter')

WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'button#suggestion-search-button')))\
                                        .click()

WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.LINK_TEXT,
                                    'Names')))\
                                        .click()

name = WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[3]/table/tbody/tr[1]/td[2]')))\
                                        .text

name2 = WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[3]/table/tbody/tr[2]/td[2]')))\
                                        .text


print(name)
print(name2)