import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def test_hoverAction():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)

    hover_element = driver.find_element(By.LINK_TEXT, "Privacidad")
    hover_action = ActionChains(driver).move_to_element(hover_element)
    hover_action.perform()
    driver.implicitly_wait(10)

    driver.quit()

