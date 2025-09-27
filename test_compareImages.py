import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from visual_comparison.utils import ImageComparisonUtil

def test_compareImages():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    driver.save_screenshot("C:\\Users\\abdia\\PycharmProjects\\new\\selenium_test\\images\\img2.png")

    expected_image = cv2.imread("C:\\Users\\abdia\\PycharmProjects\\new\\selenium_test\\images\\img1.png")
    actual_image = cv2.imread("C:\\Users\\abdia\\PycharmProjects\\new\\selenium_test\\images\\img2.png")

    if expected_image.shape[:2] != actual_image.shape[:2]:
        actual_image = cv2.resize(actual_image, (expected_image.shape[1], expected_image.shape[0]))

    result = cv2.absdiff(expected_image, actual_image)
    gray_image = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    contours,_ = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for count in contours:
        if cv2.contourArea(count) >= 20:
            x, y, widht, height = cv2.boundingRect(count)
            cv2.rectangle(expected_image,(x,y),(x+widht,y+height),(0,0,255),2)

    while(1):
        cv2.imshow('Image 1', expected_image)
        cv2.imshow('Image 2', actual_image)
        cv2.imshow('Diff: ', result)
        keyboard = cv2.waitKey(5) & 0xFF
        if keyboard == 27:
            break
    cv2.destroyAllWindows()
    driver.quit()
