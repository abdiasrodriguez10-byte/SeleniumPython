from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_radioButton():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
    radio_button1 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[3]/div[1]/input[3]")))
    radio_button2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[3]/div[1]/input[4]")))
    assert radio_button1.is_selected()

    radio_button2.click()
    assert radio_button2.is_selected()

    driver.quit()

