import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_SelectList():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
    select_list = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[3]/div[1]/select")))
    select = Select(select_list)
    options_list = select.options
    for option in options_list:
        option.click()
        print(option.text)

    for option in options_list:
        if option.text == "Nissan":
            option.click()
            time.sleep(2)

    driver.quit()

