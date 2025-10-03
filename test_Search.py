from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_Search():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    word = "Iphone"

    driver.get("https://www.mercadolibre.com.mx/")
    search_bar = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='cb1-edit']")))
    search_bar.send_keys(word)
    search_bar.send_keys(Keys.ENTER)

    elements_titles = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ol[@class='ui-search-layout ui-search-layout--stack']//li//h3")))
    print(f"The total result is: ", len(elements_titles))
    item_texts = []
    for item in elements_titles:
        item_texts.append(item)
        print(f"The title is: ", {item.text})

    driver.quit()
