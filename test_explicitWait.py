from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_explicitWait():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
    finally:
        driver.quit()