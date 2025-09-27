from selenium import webdriver

def test_implicitlyWait():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    driver.close()