from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_Tables():
    driver = webdriver.Chrome()
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    wait = WebDriverWait(driver, 20)
    table = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='customers']/tbody/tr")))
    for element in table:
        print(element.text)
    driver.quit()
