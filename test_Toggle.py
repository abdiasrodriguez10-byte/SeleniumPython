from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Toogle():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
    toggle = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/label[3]/div")))
    driver.save_screenshot("C:\\Users\\abdia\\PycharmProjects\\new\\selenium_test\\images\\toggleOff.png")
    toggle.click()
    driver.save_screenshot("C:\\Users\\abdia\\PycharmProjects\\new\\selenium_test\\images\\toggleOn.png")
    driver.implicitly_wait(5)

    driver.quit()
