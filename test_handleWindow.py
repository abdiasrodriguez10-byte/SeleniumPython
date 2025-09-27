import time

from selenium import webdriver

def test_handleWindow():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    time.sleep(2)
    driver.get("https://www.youtube.com/")
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.quit()
