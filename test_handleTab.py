import time

from selenium import webdriver

def test_handleTab():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.youtube.com/")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    driver.quit()

